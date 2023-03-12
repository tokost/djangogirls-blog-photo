from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

# pridane kvoli kombinacii
class PhotosConfig(AppConfig):
    name = 'photos'