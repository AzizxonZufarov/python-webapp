from django.db import models

class Articles(models.Model):
    title = models.CharField('Haзвание', max_length=50) 
    anons = models.CharField('AHOHC', max_length=250) 
    full_text= models.TextField('Cтатья')
    date = models.DateTimeField('Дarа публикии')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'        

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

