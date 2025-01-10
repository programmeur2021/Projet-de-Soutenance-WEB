from django.db import models

# Create your models here.

class Utilisateur(models.Model):
        
    nom_user = models.CharField(max_length = 65)
    login_user = models.CharField(max_length  = 45)
    password_user = models.CharField(max_length=60)
    confirmationpassword_user = models.CharField(max_length  =60)
    email_user = models.EmailField()
    role_user = models.CharField(max_length=45)
    dateincription_user = models.DateField(auto_now = True)

    def __str__(self):
     return '{} {} {} {}'.format(self.nom_user, self.login_user, self.password_user, self.email_user, self.role_user)