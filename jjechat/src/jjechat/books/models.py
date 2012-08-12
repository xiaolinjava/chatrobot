from django.db import models

# Create your models here.
class Publisher (models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Author (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')
    
    def __unicode__(self):
        return self.last_name + self.first_name
    
    class Meta:
        ordering = ['last_name']

    
    
class Book (models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['publication_date']





























