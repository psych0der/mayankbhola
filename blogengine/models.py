from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



# Create your models here. 
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/category/%s/" % self.slug


class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/tag/%s/" % self.slug

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = RichTextField()
    slug = models.SlugField(max_length=40, unique=True)
    author = models.ForeignKey(User)
    categories = models.ManyToManyField(Category, blank=True, null=True, through='CategoryToPost')
    tags = models.ManyToManyField(Tag, blank=True, null=True, through='TagToPost')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

    def save(self, force_insert=False, force_update=False):
        self.text_html = self.text
        super(Post, self).save(force_insert, force_update)


class CategoryToPost(models.Model):
    post = models.ForeignKey(Post)
    category = models.ForeignKey(Category)

class TagToPost(models.Model):
    post = models.ForeignKey(Post)
    tag = models.ForeignKey(Tag)
