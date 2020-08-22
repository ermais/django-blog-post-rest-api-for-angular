from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=False, blank=False)
    slug = models.SlugField(max_length=200,null=True, blank=True)
    body = models.TextField(null=False, blank=True)
    likes = models.IntegerField(null=True, blank=True, default=0)
    comment_count = models.IntegerField(null=True, blank=True, default=0)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title,allow_unicode=True)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
        



@receiver(post_save, sender=User)
def post_save_token(sender, instance, created=None, **kwargs):
    if created:
        Token.objects.get_or_create(user=instance)