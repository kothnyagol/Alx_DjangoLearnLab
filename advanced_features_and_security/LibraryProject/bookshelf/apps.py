from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        Book = self.get_model('Book')
        content_type = ContentType.objects.get_for_model(Book)
        permissions = Permission.objects.filter(content_type=content_type)

        # Create groups if they don't exist
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        editors, _ = Group.objects.get_or_create(name='Editors')
        admins, _ = Group.objects.get_or_create(name='Admins')

        # Assign permissions
        viewers.permissions.set(permissions.filter(codename='can_view'))
        editors.permissions.set(permissions.filter(codename__in=['can_create', 'can_edit']))
        admins.permissions.set(permissions)
