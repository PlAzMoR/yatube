from django.contrib import admin
from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    list_editable = ('group',)
    search_filters = ('text',)
    list_filter = ('pub_date', 'author')

    empty_value_display = '-пусто-'

class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('pk', 'title', 'slug', 'description',)
    search_filters = ('title',)
    list_filter = ('title',)
    
    empty_value_display = '-пусто-'

admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
