from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Setting(models.Model):
    company_name = models.CharField(max_length=100)
    company_description = RichTextUploadingField()
    company_contact = RichTextUploadingField()
    director_statement = RichTextUploadingField()
    faqs = RichTextUploadingField()
    email_host = models.CharField(max_length=100)
    email_password = models.CharField(max_length=100)
    login_logo = models.ImageField(upload_to='products/')
    cart_logo = models.ImageField(upload_to='products/', blank=True)
    cart_logo_description = RichTextUploadingField(default="Shop with us!!", blank=True)
    company_video = models.FileField(upload_to='products/', default="", blank=True)
    company_video_title = models.CharField(max_length=500, default="", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)

