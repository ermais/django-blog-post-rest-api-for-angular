from django.db import models
from post.models import Post
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)
    commented_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    

    def __str__(self):
        return self.body



    

@receiver(post_save, sender=Comment)
def update_comment_count(sender, instance, created=None, **kwargs):
    if created:
        post = Post.objects.get(pk=instance.post.pk)
        post.comment_count = int(post.comment_count) + 1
        post.save()