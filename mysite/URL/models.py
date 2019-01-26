from django.db import models

class URLPattern (models.Model):
    longURL = models.CharField(max_length=1000)
    shortURL = models.CharField(max_length=200, blank=True)
    visits = models.IntegerField(default=0)
    def __str__(self):
        return str(self.longURL) + " | " + str(self.shortURL) + " | Visits: " + str(self.visits)
