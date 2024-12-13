from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"
    verbose_name = "کاربران"

def ready(self):
    from user.permissions import populate_models

    post_migrate.connect(populate_models, sender=self)
