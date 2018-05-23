from django.core.management import BaseCommand
from icoprocessing.models import ICOModel
import random
import string
from datetime import date

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('number', type=int)

    def handle(self, *args, **options):

        my_int_argument = options['number']


        for i in range (my_int_argument) :

            ico_start_date , ico_end_date = self.random_dates()
            min_cap_in_eth = random.choice(range(1000000))
            max_cap_in_eth = random.choice(range(min_cap_in_eth +10, 1000000000))
            tokens_per_eth = random.choice(range(500))
            discount = random.choice(range(50))
            max_token_supply = random.choice(range(1000000000))
            for_sale = random.choice(range(1000000))
            white_label_address = self.random_trash()
            admin_email = self.random_trash() + '@gmail.com'

            model = ICOModel()

            model.ico_start_date = ico_start_date
            model.ico_end_date = ico_end_date
            model.min_cap_in_eth = min_cap_in_eth
            model.max_cap_in_eth = max_cap_in_eth
            model.tokens_per_eth = tokens_per_eth
            model.discount = discount
            model.max_token_supply = max_token_supply
            model.for_sale = for_sale
            model.white_label_address = white_label_address
            model.admin_email = admin_email

            model.save()



    def random_trash(self):
        random_chunk = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(random.choice(range(6, 15)))])
        return random_chunk



    def random_dates (self):
        year = random.choice(range(2018, 2030))
        month = random.choice(range(1, 12))
        day = random.choice(range(1, 28))

        start_date = date(year, month, day)

        year = random.choice(range(year+1, 2040))
        month = random.choice(range(1, 12))
        day = random.choice(range(1, 28))

        end_date = date(year, month, day)

        return (start_date, end_date)


