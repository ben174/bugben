from django.core.management.base import BaseCommand
from utilities.provision_data import Provisioner


class Command(BaseCommand):
    help = 'Provisions initial resume data'

    def handle(self, *args, **options):
        Provisioner.create_profile()
