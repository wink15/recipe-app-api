"""
ESPERANDO LA BD
"""
from django.core.management.base import BaseCommand
import time

from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write("Waiting for db")

        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2OpError, OperationalError):
                self.stdout.write('db  unavailable, waiting 1 second')
                time.sleep(5)
        self.stdout.write(self.style.SUCCESS('db available'))
