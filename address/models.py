from django.db import models


class State(models.Model):
    name = models.CharField(max_length=40, unique=True, blank=False)

    class Meta:
        verbose_name_plural = 'State'
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.name)


class City(models.Model):
    name = models.CharField(max_length=40, unique=True, blank=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'City'
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.name)


class Locality(models.Model):
    name = models.CharField(max_length=40, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Locality'
        unique_together = ('name', 'city')
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.name)


class Address(models.Model):
    # As company name is unique, maintaining address and company together in the same table
    company_name = models.CharField(max_length=40, unique=True, blank=False)
    building_number = models.CharField(max_length=10, blank=False)
    postal_code = models.CharField(max_length=10, blank=False)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Address'
        ordering = ('postal_code',)

    def __str__(self):
        return '{} : {}'.format(self.company_name, self.locality)