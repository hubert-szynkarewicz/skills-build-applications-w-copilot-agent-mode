from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Your logic to populate the database goes here
        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
