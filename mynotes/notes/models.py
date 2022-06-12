from django.db import models

# Create your models here.
from django.db import models
from django.template.defaultfilters import truncatechars
from django.urls import reverse
# from PIL import Image
from django.contrib.auth.models import User


# Create your models here.

# class Category(models.Model):
#     name = models.CharField('Category', max_length=70, help_text='choose category', unique=True)
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'

# def display_category(self):
#     return ', '.join(category.name for category in self.category.all()[:3])

# display_category.short_description = 'Category'
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Notes(models.Model):
    title = models.CharField('Title name', max_length=255, help_text='Enter title')
    # kolkas bus textfield, veliau pakeisiu i html
    note = models.TextField('Note', help_text='enter your note here')
    date_created = models.DateField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
    #
    # @property
    # def short_description(self):
    #     return truncatechars(self.note, 100)

# class Author(models.Model):
#     first_name = models.CharField('First name', max_length=50, help_text='Enter your first name')
#     last_name = models.CharField('Last name', max_length=50, help_text='Enter your last name')
