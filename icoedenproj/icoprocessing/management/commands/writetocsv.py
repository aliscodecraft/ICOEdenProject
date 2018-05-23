import csv
from django.core.management import BaseCommand
from icoprocessing.models import ICOModel


class Command(BaseCommand):

    file_path = 'c:/users/arali/desktop/objects.csv'

    def handle(self, *args, **options):
        objects = ICOModel.objects.all()
        #self.WriteListToCSV(self.file_path, ['min_cap_in_eth', 'max_cap_in_eth','tokens_per_eth', 'discount' , 'max_token_supply', 'pyth'])

        for obj in objects:
            self.WriteListToCSV(self.file_path, [obj.min_cap_in_eth, obj.max_cap_in_eth, obj.tokens_per_eth, obj.discount, obj.max_token_supply, obj.for_sale] )


    def WriteListToCSV(self, csv_file,  data_list):
        try:

            with open(csv_file, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)

                writer.writerow(data_list)
        except IOError  as e :
            print(e.strerror)
        return

