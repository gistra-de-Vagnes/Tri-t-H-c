from django.db import models
from django.contrib.auth.models import User

class PhilosophySchool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Philosophy School"
        verbose_name_plural = "Philosophy Schools"

class Philosopher(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)
    schools = models.ManyToManyField(PhilosophySchool, blank=True)
    works = models.TextField(blank=True, help_text="Key works separated by commas")
    key_ideas = models.TextField(blank=True, help_text="Key ideas separated by commas")
    country = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(blank=True, help_text="URL to animated image (GIF/SVG)")
    
    def __str__(self):
        return self.name
    
    @property
    def lifespan(self):
        if self.birth_year and self.death_year:
            return f"{self.birth_year}-{self.death_year}"
        elif self.birth_year:
            return f"{self.birth_year}-present"
        else:
            return "Unknown"
    
    class Meta:
        verbose_name = "Philosopher"
        verbose_name_plural = "Philosophers"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_school = models.ForeignKey(PhilosophySchool, on_delete=models.SET_NULL, null=True, blank=True)
    avatar_url = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"