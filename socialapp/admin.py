from django.contrib import admin

from socialapp import models


admin.site.register(models.UserPost)
admin.site.register(models.UserPostComment)
admin.site.register(models.UserProfile)
readonly_fields = ('admin_thumbnail',)
