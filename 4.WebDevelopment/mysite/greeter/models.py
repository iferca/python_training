from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, default='Mx')
    
    def __str__(self):
        return ' '.join((self.title, self.name))
    
    def is_male(self):
        return self.title.lower() in ['mr', 'master']
    
    def is_female(self):
        return self.title.lower() not in ['mx'] and not self.is_male()