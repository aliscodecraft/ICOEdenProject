from django.core.management import BaseCommand
from icoprocessing.models import ICOModel


class Command(BaseCommand):

    def handle(self, *args, **options):

        ICOModel.objects.all().delete()
        print("All ICOModel objects have been successfully deleted.")