from django.db import models
from django.urls import reverse


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})
