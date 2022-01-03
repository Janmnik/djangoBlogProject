from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
    def authorget(self):
        return self.author

class Comments(models.Model):
    post_id = models.ManyToManyField('Post')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #email = models.EmailField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date =models.DateTimeField(auto_now = True)
    active = models.BooleanField( default = True)
    
    def authorget(self):
        return self.author
    
   # class Meta:
       # ordering = ('created',)
    def __str__(self):
        return 'Komentarz dodany przez {} dla posta {}'.format(self.name, self.post)