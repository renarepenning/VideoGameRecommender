from django.db import models

# table myUser
class myUser(models.Model):
    name = models.CharField(max_length=40)
    add_date = models.DateField('Date user added')


# THIS MAY HAVE TO BE A SEPARATE APP. UNSURE THE ISSUE ATM
'''class Game(models.Model):
    gname = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)
    last_update = models.DateField('Date of last update')'''