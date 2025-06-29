from django.contrib.auth.models import BaseUserManager


class MsUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user_type = extra_fields.pop("user_type", "client")
        is_staff = extra_fields.pop("is_staff", False)
        if user_type == "client":
            is_staff = False

        user = self.model(
            email=email, user_type=user_type, is_staff=is_staff, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("user_type", "manager")

        return self.create_user(email, password, **extra_fields)
