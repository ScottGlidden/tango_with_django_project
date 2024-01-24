from django.db import models
from django.template.defaultfilters import slugify

# Task 5.3
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0) # Exercise 5
    likes = models.IntegerField(default=0) # Exercise 5
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)                           

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

# Task 5.3
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title