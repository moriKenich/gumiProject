from django.db import models
from django.contrib.auth.models import AbstractUser
from gumi.models import GumiPost 

class CustomUser(AbstractUser):
    pass
   
'''お気に入りの関係を表すモデル'''
class Connection(models.Model):
    like = models.ForeignKey(CustomUser, related_name='like', on_delete=models.CASCADE)
    liked = models.ForeignKey(GumiPost, related_name='liked', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} : {}".format(self.like.username, self.liked.id)