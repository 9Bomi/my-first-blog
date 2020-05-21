from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #define models(object)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #link to another model
    
    title = models.CharField(max_length=200) 	#limited char
    text = models.TextField()	#unlimited char
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #method = 
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title