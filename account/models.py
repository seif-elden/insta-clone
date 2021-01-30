from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class more_user_info(models.Model):
    profile_photo = models.ImageField(null=True , blank=True , default='user.png')
    user = models.OneToOneField(User , related_name='user_info',on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50 , null=True , blank=True)
    bio = models.CharField(max_length=50 , null=True , blank=True)
    
    def __str__(self):
        return f"{self.user}"

class follow(models.Model):
    more_followed_user_info = models.ForeignKey(more_user_info , related_name='more_followed_user_info',on_delete=models.CASCADE, null=True)
    followed_user = models.ForeignKey(User , related_name='followed_user',on_delete=models.CASCADE, null=True)
    followers = models.ForeignKey(User , related_name='followers',on_delete=models.CASCADE , null=True)
    more_follower_info =  models.ForeignKey(more_user_info , related_name='more_follower_info',on_delete=models.CASCADE, null=True)   
    def __str__(self):
        return f"{self.followed_user} {self.followers}"

class photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=50,blank=True)
    created_by = models.ForeignKey(User,related_name='User_uploaded_files',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    post_more_user_info = models.ForeignKey(more_user_info , related_name='more_user_info',on_delete=models.CASCADE, null=True,blank=True)
    like = models.ManyToManyField(User,related_name='like', blank=True)


    def __str__(self):
        return f"{self.image} | {self.created_by}"

class comments(models.Model):
    post = models.ForeignKey(photo,related_name='comments', on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=100)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True,null=True)
    created_by_photo = models.ForeignKey(more_user_info , related_name='photo_of_comment',on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.comment
    


    

