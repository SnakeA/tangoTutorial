from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



# Create your models here.

#Django creates an ID field for you automatically in each table relating to a model.
#You therefore do not need to explicitly define a primary key for each model  its done for you

class Category (models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    # Override save function so that name is saved without spaces (slug function)
    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        # if self.id is None:
        #self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    #Like Java's toString() - provides a unicode representation of the model
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural="Categories"


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField(null=True)
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # Additional attributes
    website = models.URLField(blank=True) # allows each of the fields to be blank if necessary
    picture = models.ImageField(upload_to='profile_images', blank=True) # <workspace>/tango_with_django_project/media/profile_images/

    # Override the unicode() to return something meaningful
    def __unicode__(self):
        return self.user.username

