from __future__ import unicode_literals

from django.apps import AppConfig


# App configuration to Seating Manager
class SeatingManagerConfig(AppConfig):
    name = 'seating_manager'
    # Change name to Seating Manager which will be displayed in admin panel
    verbose_name = 'Seating Manager'
