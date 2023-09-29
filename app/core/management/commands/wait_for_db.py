"""Django command to wait for the database to be available"""

from django.core.management.base import BaseCommand

import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError

class Command(BaseCommand):
    """Django command to wait for database"""
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")