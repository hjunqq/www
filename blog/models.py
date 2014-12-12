from django.db import models
from django.contrib.auth.models import Permission,Group,GroupManager
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here. userprofile
class BlogGroup(models.Model): 
    """  """ 
    GroupName = models.CharField(max_length=80, unique=True) 
    Permissions = models.ManyToManyField(Permission, verbose_name='permissions', blank=True) 
    objects = GroupManager() 
    class Meta: 
        verbose_name = 'blog group'
        verbose_name_plural = 'blog groups'
    def __str__(self): 
        return self.GroupName 
    def natural_key(self): 
        return (self.GroupName,)
    
class UserManager(BaseUserManager):
    def create_user(self,UserName,Email,password=None):
        '''
        Create and Save a User with a given username,password
        '''        
        if not Email:
            raise ValueError('User must have an email address')
        user = self.model(
            UserName = UserName,
            Email = UserManager.normalize_email(Email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,UserName,Email,password=None):
        '''
        Create a SuperUser
        '''
        user = self.create_user(UserName,Email,password)
        user.is_admin = True
        user.save(using=self._db)
        return user
class BlogUser(AbstractBaseUser):
    UserName = models.CharField(max_length=100, unique=True)
    Groups = models.ManyToManyField(BlogGroup,blank = True,related_name = 'usergroup')
    Email = models.EmailField(max_length=100, unique=True)
    Avatar = models.URLField(blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    access_token = models.CharField(max_length=100, blank=True)
    refresh_token = models.CharField(max_length=100, blank=True)
    expires_in = models.BigIntegerField(max_length=100, default=0)
 
    objects = UserManager()
 
    USERNAME_FIELD = 'UserName'
    REQUIRED_FIELDS = ('Email',)
    
    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username
    
    def has_perm(self,perm,obj=None):
        "Does the user have a specific permission"
        return True
    
    def has_module_perms(self,app_label):
        return True
 
    class Meta:
        ordering = ('-Created_at',)
 
    def __str__(self):
        return self.username

class Category(models.Model):
    CategoryName = models.CharField(max_length = 50)
    CreateUser = models.ForeignKey(BlogUser)
    CreateTime = models.DateTimeField(auto_now=True)
    ParentId = models.ForeignKey('self',blank = True)
    Children = models.ManyToManyField('self',blank = True)
    
    def __str__(self):
        return self.CategoryName
    
class PostType(models.Model):
    Type = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.Type

class Comment(models.Model):
    User = models.ForeignKey(BlogUser)
    briefText = models.TextField(max_length = 50)
    CommentText = models.TextField(max_length = 5000)
    CommentTime = models.DateTimeField(auto_now=True)
    IPAddress = models.GenericIPAddressField()
    UserAgent = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.briefText

class Attached(models.Model):
    AttachName = models.CharField(max_length = 50)
    AttachedType = models.CharField(max_length = 50)
    AttachedPath = models.CharField(max_length = 50)
    AttachedSize = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.AttachName

class Post(models.Model):
    auther = models.ForeignKey(BlogUser)
    Title = models.CharField(max_length = 50)
    SubTitle = models.CharField(max_length = 50,blank = True)
    Category = models.ManyToManyField(Category,related_name ='Category')
    PostType = models.ManyToManyField(PostType,related_name ='PostType')
    AllowComment = models.BooleanField(default = True)
    Comment = models.ManyToManyField(Comment,related_name = 'Comment')
    Abstract = models.CharField(max_length = 400,blank=True)
    ContentText = models.TextField(max_length = 10000)
    CreateTime = models.DateTimeField(auto_now=True)
    LastModifyTime = models.DateTimeField(auto_now=True)
    IPAddress = models.GenericIPAddressField()
    UserAgent = models.CharField(max_length = 50)
    Attached = models.ManyToManyField(Attached,related_name = 'Attached')
    permissions = models.ManyToManyField(Permission, verbose_name='permissions', blank=True) 
    
    def __str__(self):
        return self.Title
    