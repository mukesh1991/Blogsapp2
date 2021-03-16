from django.contrib import admin
from .models import Post,Comments
class postAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','created','updated','status']
    list_filter = ['author','publish','status',]
    search_fields = ['title','body',]
    prepopulated_fields = {'slug':('title',)}
    row_id_fields=('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
class commentAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','body','created','updated','active']
    list_filter = ['created','updated','active']
    search_fields = ['name','email','body']


# Register your models here.


admin.site.register(Post,postAdmin)
admin.site.register(Comments,commentAdmin)
