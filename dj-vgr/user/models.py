from django.db import models

# table myUser
class myUser(models.Model):
    name = models.CharField(max_length=40)
    add_date = models.DateField('Date user added')