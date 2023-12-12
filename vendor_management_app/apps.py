# vendor_management_app/apps.py
from django.apps import AppConfig

class VendorManagementAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vendor_management_app'

    def ready(self):
        import vendor_management_app.signals  # This import ensures that signals are connected when the app is ready
