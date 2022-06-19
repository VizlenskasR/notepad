
from django.contrib import admin
from .models import Notes, Category



# # Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author', 'category')
    readonly_fields = ('date_created',)


admin.site.register(Notes, NotesAdmin)
admin.site.register(Category)

