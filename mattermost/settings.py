from django.conf import settings

from .models.alerts import new_membership, ending_membership, changing_membership_password

MATTERMOST_HOST = getattr(settings, 'MATTERMOST_HOST', 'your-mattermost-url.com')
MATTERMOST_PORT = getattr(settings, 'MATTERMOST_PORT', 8065)
MATTERMOST_ADMIN = getattr(settings, 'MATTERMOST_ADMIN', 'someone@nowhere.com')
MATTERMOST_PASSWORD = getattr(settings, 'MATTERMOST_PASSWORD', 'thisisabadpassword')
MATTERMOST_TOKEN = getattr(settings, 'MATTERMOST_TOKEN', None)

MATTERMOST_USE_HTTPS = getattr(settings, 'MATTERMOST_USE_HTTPS', True)
MATTERMOST_SSL_IS_SIGNED = getattr(settings, 'MATTERMOST_SSL_IS_SIGNED', True)

MATTERMOST_USER_TEAM = getattr(settings, 'MATTERMOST_USER_TEAM', None)
