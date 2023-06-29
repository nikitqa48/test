from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, AbstractUser
from src.department.models import Department
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password, check_password


def user_directory_path(instance: 'FatUser', filename: str) -> str:
    """Generate path to file in upload"""
    return f'users/avatar/user_{instance.id}/{str(uuid.uuid4())}.{filename.split(".")[-1]}'


class CustomUser(AbstractBaseUser, PermissionsMixin):
    avatar = models.ImageField(
        upload_to=user_directory_path,
        default='default/default.jpg',
        null=True,
        blank=True,
    )
    objects = UserManager()
    job_title = models.CharField('Должность', max_length=100)
    first_name = models.CharField('Имя', max_length=500, null=True)
    last_name = models.CharField('Фамилия', max_length=500, null=True)
    middle_name = models.CharField('Отчество', max_length=500, null=True)
    salary = models.IntegerField('Оклад', default=0)
    age = models.IntegerField('Возраст', default=18)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='personal', null=True, blank=True)
    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    USERNAME_FIELD = "username"
    email = models.EmailField("email address", blank=True)
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        "active",
        default=True
    )
    date_joined = models.DateTimeField("date joined", default=timezone.now)
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name", "middle_name"]

    class Meta:
        unique_together = ('id', 'department')
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
        ]

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)
