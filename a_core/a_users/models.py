from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='avatars/', null=True, blank=True)
    display_name = models.CharField(max_length=128, null=True, blank=True)
    info = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

    @property
    def name(self):
        if self.display_name:
            name = self.display_name
        else:
            name = self.user.username
        return name
    
    @property
    def avatar(self):
        if self.images:
            avatar = self.images.url
        else:
            avatar = static('images/avatar.svg')
        return avatar