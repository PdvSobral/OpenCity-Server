from django.core.management.base import BaseCommand
from django.db import connections, transaction


SQL_SCRIPT = """
-- POSTGRSQL CODE TO INSERT DATA
"""


class Command(BaseCommand):
    help = "Inject full seed dataset into app_db using raw SQL"

    def handle(self, *args, **options):
        db_alias = "app_db"

        self.stdout.write(self.style.WARNING(f"Running seed on database: {db_alias}"))

        connection = connections[db_alias]

        with transaction.atomic(using=db_alias):
            with connection.cursor() as cursor:
                cursor.execute(SQL_SCRIPT)

        self.stdout.write(self.style.SUCCESS("Seed data inserted successfully."))
