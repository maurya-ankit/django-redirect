from django.db import models
from django.utils.crypto import get_random_string
import string
from django.contrib.auth.models import User
def uniquestring(self):
        unique = False
        while not unique:
            code = get_random_string(5, allowed_chars=string.ascii_uppercase + string.digits)
            if( not shorten.objects.filter(shorturi=code)):
                unique=True
        return code
# Create your models here.
class shorten(models.Model):
    uri = models.URLField('Enter original uri ')
    shorturi = models.CharField('save the model for shorten uri',max_length=10,unique=True,null=True,blank=True)
    count = models.IntegerField(default=0)
    
    

    def save(self,*args,**kwrgs):
        self.shorturi=get_random_string(5, allowed_chars=string.ascii_uppercase + string.digits)
        super(shorten,self).save(*args,**kwrgs)

class UserShort(models.Model):
    uri = models.URLField('Enter original uri ')
    shorturi = models.CharField('save the model for shorten uri',max_length=10,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


    def __str__(self):
        return self.shorturi