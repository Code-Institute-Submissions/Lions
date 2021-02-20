from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    """
    A user profile model to maintain default
    billing information and subscription history
    """

    Choices = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_gender = models.CharField(max_length=10, choices=Choices)
    default_dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


# from https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/2c1b98a8efb748009445d5056c97483b/?child=first
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update the user profile """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
