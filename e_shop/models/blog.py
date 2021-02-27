from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User


class BlogCategory(models.Model):
    name = models.CharField(max_length=200, default="")

    class Meta:
        verbose_name_plural = "Blog categories"

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return BlogCategory.objects.all()


class Blog(models.Model):
    title = models.CharField(max_length=200)
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, default="")
    description = RichTextUploadingField()
    image = models.ImageField(upload_to="uploads/images", blank=True, default="")
    video = models.FileField(upload_to="uploads/video", blank=True, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_all_blogs():
        return Blog.objects.all().order_by("-created_on")

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} commented on {self.topic}.'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': Textarea(attrs={'class': 'input', 'placeholder': 'Your comment', 'rows': '7', 'cols':'25'}),
        }
