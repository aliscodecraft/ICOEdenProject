from django.db import models

# Create your models here.


class ICOModel(models.Model):

    ico_start_date = models.DateField()
    ico_end_date = models.DateField()
    min_cap_in_eth = models.CharField( max_length=10)
    max_cap_in_eth = models.CharField(max_length=10)
    tokens_per_eth = models.IntegerField()
    discount = models.IntegerField()
    max_token_supply = models.CharField(max_length=10)
    for_sale = models.CharField(max_length=10)
    white_label_address = models.CharField(max_length=10)
    admin_email = models.EmailField()

    def __str__(self):
        return str(self.admin_email)