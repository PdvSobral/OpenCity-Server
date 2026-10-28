from django.core.management.base import BaseCommand
from django.db import connections

class Command(BaseCommand):
    help = "Reset the PostgreSQL public schema on a specific database (DANGER: deletes all data!)"

    def add_arguments(self, parser):
        parser.add_argument(
            '--database',
            default='app_db',
            help='Specify the database alias to reset (default: app_db)',
        )

    def handle(self, *args, **options):
        db_alias = options['database']
        self.stdout.write(self.style.WARNING(
            f"⚠️  WARNING: This will delete all tables and data in database '{db_alias}'! ⚠️"
        ))
        confirm = input("Type 'YES' to continue: ")
        if confirm != 'YES':
            self.stdout.write(self.style.ERROR("Operation cancelled."))
            return

        with connections[db_alias].cursor() as cursor:
            cursor.execute("DROP SCHEMA public CASCADE;")
            cursor.execute("CREATE SCHEMA public;")
            self.stdout.write(self.style.SUCCESS(f"✅ Database schema 'public' on '{db_alias}' reset successfully."))
