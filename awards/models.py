from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='profiles',blank=True)
    user = models.OneToOneField(User,null = True,on_delete=models.CASCADE,related_name = "profile")
    bio=models.TextField(blank=True,null=True)
    contact=models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
