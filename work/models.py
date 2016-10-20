from django.db import models
from django.db.models import permalink
from django.utils import timezone


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='Client Name')

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Clients"

    def __str__(self):
        return '%s' % self.name


class Medium(models.Model):
    name = models.CharField(max_length=150, verbose_name='Medium Name')

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Media"

    def __str__(self):
        return '%s' % self.name


class Project(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Project Title')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')
    project_url = models.URLField(verbose_name='Project URL')
    description = models.CharField(max_length=500, verbose_name='Description', blank=True)
    client = models.ForeignKey(Client)
    media = models.ManyToManyField(Medium)
    completion_date = models.DateField(null=False, blank=False)
    in_development = models.BooleanField()
    is_public = models.BooleanField(default=True)
    data_group = models.CharField(max_length=150, verbose_name='Item Data Group Media', default='tech')
    meta_keywords = models.CharField(max_length=250, verbose_name='Meta Keywords', blank=True)
    project_image = models.ImageField(upload_to='projects')

    class Meta:
        ordering = ['-completion_date']
        verbose_name_plural = "Projects"

    def __str__(self):
        return '%s' % self.name

    @permalink
    def get_absolute_url(self):
        return 'view_project', None, {'slug': self.slug}
