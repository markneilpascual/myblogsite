from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = RichTextField(blank=True, null=True, config_name='awesome_ckeditor')
    post_image = models.ImageField(upload_to='post_image', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def approve_comments(self):
        return  self.comments.filter(approved_comment =True)

    def get_absolute_url(self):
        return  reverse("post_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    text = RichTextField(blank=True, null=True, config_name='awesome_ckeditor')
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_ulr(self):
        return  reverse('post_list')

    def __str__(self):
        return self.text
