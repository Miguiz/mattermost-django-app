# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class MattermostConfig(AppConfig):
    name = 'mattermost'

    def ready(self):
        # Load and connect signal recievers
        import mattermost.signals
