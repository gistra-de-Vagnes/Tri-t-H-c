from django.db import models
from django.contrib.auth.models import User
from philosophers.models import PhilosophySchool
from django.urls import reverse

class DiscussionCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    school = models.ForeignKey(PhilosophySchool, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.school:
            return f"{self.school.name} Discussions"
        return self.name
    
    def get_absolute_url(self):
        return reverse('discussions:category_detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Discussion Categories"

class DiscussionTopic(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(DiscussionCategory, on_delete=models.CASCADE, related_name='topics')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_pinned = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('discussions:topic_detail', kwargs={'pk': self.pk})
    
    def get_reply_count(self):
        return self.replies.count()
    
    def get_last_reply(self):
        return self.replies.order_by('-created_at').first()
    
    class Meta:
        ordering = ['-is_pinned', '-updated_at']

class DiscussionReply(models.Model):
    topic = models.ForeignKey(DiscussionTopic, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Reply by {self.author.username} to {self.topic.title}"
    
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Discussion Replies"