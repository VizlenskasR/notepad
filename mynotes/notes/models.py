from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-name', )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Notes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField('Title name', max_length=255, help_text='Enter title')
    note = HTMLField('Note', null=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'


