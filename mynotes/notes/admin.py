
from django.contrib import admin
from .models import Notes, Category



# # Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author', 'category')
#     list_filter = ('title', 'date_created', 'category')

#
    readonly_fields = ('date_created',)

#
#
#
#
#
admin.site.register(Notes, NotesAdmin)
admin.site.register(Category)
#
