from django.contrib import admin
from microblog.models import category, post, comment
admin.site.register(category)
admin.site.register(post)
admin.site.register(comment)
# Register your models here.
