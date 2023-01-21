from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """ User manager """

    def _create_user(self, username, password=None, **extra_fields):
        """Creates and returns a new user using an email address"""
        if not username:
            raise ValueError('Users must have a Username')

        # create user
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # hashes/encrypts password
        user.save(using=self._db)  # safe for multiple databases
        return user

    def create_user(self, username, password=None, **extra_fields):
        """Creates and returns a new user using an email address"""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_staffuser(self, username, password=None, **extra_fields):
        """Creates and returns a new staffuser using an email address"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        """Creates and returns a new superuser using an email address"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(username, password, **extra_fields)

# class UserManager(BaseUserManager):
#     def create_user(self, username, password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not username:
#             raise ValueError('Users must have a Username')
#
#         user = self.model(
#             username=self.normalize_username(username),
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_staffuser(self, username, password):
#         """
#         Creates and saves a staff user with the given email and password.
#         """
#         user = self.create_user(
#             username,
#             password=password,
#         )
#         user.staff = True
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(
#             username,
#             password=password,
#         )
#         user.staff = True
#         user.admin = True
#         user.save(using=self._db)
#         return user
