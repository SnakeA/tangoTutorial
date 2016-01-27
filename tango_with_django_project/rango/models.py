from django.db import models

# Create your models here.
#Django creates an ID field for you automatically in each table relating to a model.
#You therefore do not need to explicitly define a primary key for each model  its done for you

class Category (models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

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
