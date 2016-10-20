from django.db import models


# Create your models here.
class About(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    occupation = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)
    dob = models.DateField()
    home_town = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=30)
    nationality = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_detail = models.TextField()
    skill_icon = models.CharField(max_length=50)
    skill_percent = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.skill_name


class ResumeStudyPlace(models.Model):
    name = models.CharField(max_length=50)
    start_year = models.DateField(auto_now=False, auto_now_add=False)
    end_year = models.DateField(auto_now=False, auto_now_add=False)
    certificate = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ResumeWorkPlace(models.Model):
    name = models.CharField(max_length=50)
    start_year = models.DateField(auto_now=False, auto_now_add=False)
    end_year = models.DateField(auto_now=False, auto_now_add=False)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AboutFeed(models.Model):
    client_name = models.CharField(max_length=50)
    client_feed = models.TextField(max_length=120)
    client_position = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100)

    def __str__(self):
        return self.client_name
