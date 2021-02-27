from django.db import models
from django.forms import ModelForm, TextInput, Textarea


class Message(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=50)
    note = models.CharField(blank=True, max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': ''}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': ''}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': ''}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': '', 'rows': '4', 'cols':'25'}),
        }
