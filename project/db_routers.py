from django.db.models import Model
from typing import Dict

# project/db_routers.py

# https://docs.djangoproject.com/en/6.0/topics/db/multi-db/#topics-db-multi-db-routing
class AppRouter:
    route_app_labels: Dict[str, str] = {
        'app': "app_db",
        'default': 'default',
    }

    def db_for_read(self, model: Model, **hints) -> str:
        if model._meta.app_label in self.route_app_labels:
            return self.route_app_labels[model._meta.app_label]
        return self.route_app_labels["default"]

    def db_for_write(self, model: Model, **hints) -> str:
        if model._meta.app_label in self.route_app_labels:
            return self.route_app_labels[model._meta.app_label]
        return self.route_app_labels["default"]

    def allow_relation(obj1, obj2, router_hint, **hints) -> bool | None:
        # it is called on relations of many to many or between tables.
        # If it always returns True, it forces the logic to be on the db
        # As of now, simply return None, so let other db_routers decide
        # FIX_ME: If having problems with db, change to True
        return None

    def allow_migrate(self, db: str, app_label: str, model_name: str | None = None, **hints) -> bool | None:
        # Determine if the migration operation is allowed to run on the database
        # with alias db.Return True if the operation should run, False if it shouldn’t run,
        # None if the router has no opinion.
        if app_label == "app":
            return db == "app_db"  # only run app migrations on app_db
        # all other apps (django.contrib.*) stay on default and nothing more
        return db == "default"
