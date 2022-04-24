from django.db import models
from ckeditor.fields import RichTextField

#Create Category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    category =models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    slug = models.SlugField()
    specs = RichTextField(null=True, blank=True)
    body = RichTextField()
    thumb = models.ImageField(default='default.png',blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def onlydate(self):
        return self.date.strftime('%B %d %Y')