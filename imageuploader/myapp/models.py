from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to="myimage/")
    caption = models.CharField(max_length=255, default="No caption")  # Added default value
    date = models.DateTimeField(auto_now_add=True)
    
# import logging

# # Create your models here.
# class Image(models.Model):
#     photo = models.ImageField(upload_to="myimage")
#     date = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         logging.info(f"Image saved: {self.photo}")
#         super().save(*args, **kwargs)

#     def delete(self, *args, **kwargs):
#         logging.info(f"Image deleted: {self.photo}")
#         super().delete(*args, **kwargs)