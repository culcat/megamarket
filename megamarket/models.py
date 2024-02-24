from django.db import models

class Promo(models.Model):
    promo_code = models.CharField(max_length=150)

    def __str__(self):
        return self.promo_code

class Link(models.Model):
    link_code = models.CharField(max_length=150)
    def __str__(self):
        return self.link_code