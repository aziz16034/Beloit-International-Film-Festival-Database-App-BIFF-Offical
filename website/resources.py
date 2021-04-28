from import_export import resources
from .models import Post

class DataSheet(resources.ModelResource):

    class meta:
        model = Post
