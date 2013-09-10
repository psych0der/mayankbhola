from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from markdown import markdown
from django.conf import settings
#from redactor.fields import RedactorField

def markdown_to_html( markdownText, images ):    
    image_ref = ""

    for image in images:
        image_url =  image.image.url
        image_ref = "%s\n[%s]: %s\n--%s\n" % ( image_ref, image, image_url,image_url )

    md = "%s\n%s" % ( markdownText, image_ref )
    html = markdown(md, ['codehilite'])

    return html

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

class Image( models.Model ):
    name = models.CharField( max_length=100 )
    image = models.ImageField( upload_to="image" )

    def __unicode__( self ):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()
    images = models.ManyToManyField( Image, blank=True )
    '''
    RedactorField(
        verbose_name=u'Text',
        redactor_options={'lang': 'en', 'focus': 'true'},
        upload_to='../project_static/',
        allow_file_upload=True,
        allow_image_upload=True
    )


    '''
    slug = models.SlugField(max_length=40, unique=True)
    author = models.ForeignKey(User)
    categories = models.ManyToManyField(Category, blank=True, null=True, through='CategoryToPost')
    tags = models.ManyToManyField(Tag, blank=True, null=True, through='TagToPost')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

    def text_html( self ):
        return markdown_to_html( self.text, self.images.all() )


class CategoryToPost(models.Model):
    post = models.ForeignKey(Post)
    category = models.ForeignKey(Category)

class TagToPost(models.Model):
    post = models.ForeignKey(Post)
    tag = models.ForeignKey(Tag)
