import logging
import random
import string
import requests

from mattermostdriver import Driver, exceptions

from django.dispatch import receiver

from .settings import *


logger = logging.getLogger(__name__)


def randomStringDigits(stringLength=8):
    # Generate a random string of letters and digits
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


@receiver(new_membership)
def adding_mattermost_user(sender, **kwargs):
    # Add new member on the mattermost server
    _user = kwargs['user']
    _pass = randomStringDigits()

    mtm = Driver({
        'url': MATTERMOST_HOST,
        'port': MATTERMOST_PORT,
        'login_id': MATTERMOST_ADMIN,
        'password': MATTERMOST_PASSWORD,
        'token': MATTERMOST_TOKEN,
        'scheme': ('http', 'https')[MATTERMOST_USE_HTTPS is True],
        'verify': MATTERMOST_SSL_IS_SIGNED,
    })

    try:
        mtm.login()
        _user_data = mtm.users.get_user_by_username(_user.username)
        mtm.users.update_user_active_status(_user_data["id"], options={'active': True})
    except exceptions.ResourceNotFound:
        _user_data = mtm.users.create_user(options={'email': _user.email, 'username': _user.username, 'password': _pass})
    except requests.exceptions.ConnectionError as err:
        logger.debug('adding_mattermost_user: ConnectionError %s' % err)
    except requests.exceptions.HTTPError as err:
        logger.debug('adding_mattermost_user: HTTPError %s' % err)
    else:
        try:
            if MATTERMOST_USER_TEAM is not None:
                _team_data = mtm.teams.get_team_by_name(MATTERMOST_USER_TEAM)
                mtm.teams.add_user_to_team(_team_data["id"], options={'team_id': _team_data["id"], 'user_id': _user_data["id"]})
            mtm.logout()
        except requests.exceptions.HTTPError as err:
            logger.debug('adding_mattermost_user: HTTPError %s' % err)
        else:
            logger.debug('Adding user %s success' % _user.username)


@receiver(ending_membership)
def deactivating_mattermost_user(sender, **kwargs):
    # Deactivate member on the mattermost server
    _user = kwargs['user']

    mtm = Driver({
        'url': MATTERMOST_HOST,
        'login_id': MATTERMOST_ADMIN,
        'password': MATTERMOST_PASSWORD,
        'token': MATTERMOST_TOKEN,
        'scheme': ('http', 'https')[MATTERMOST_USE_HTTPS is True],
        'verify': MATTERMOST_SSL_IS_SIGNED,
    })

    try:
        mtm.login()
        _user_data = mtm.users.get_user_by_username(_user.username)
        mtm.users.deactivate_user(_user_data["id"])
        mtm.logout()
    except requests.exceptions.ConnectionError as err:
        logger.debug('deactivating_mattermost_user: ConnectionError %s' % err)
    except requests.exceptions.HTTPError as err:
        logger.debug('deactivating_mattermost_user: HTTPError %s' % err)
    else:
        logger.debug('Deactivating user %s success' % _user.username)


@receiver(changing_membership_password)
def changing_mattermost_user_password(sender, **kwargs):
    # Change user password on the mattermost server
    _user = kwargs['user']
    _pass = kwargs['password']

    mtm = Driver({
        'url': MATTERMOST_HOST,
        'login_id': MATTERMOST_ADMIN,
        'password': MATTERMOST_PASSWORD,
        'token': MATTERMOST_TOKEN,
        'scheme': ('http', 'https')[MATTERMOST_USE_HTTPS is True],
        'verify': MATTERMOST_SSL_IS_SIGNED,
    })

    try:
        _usr_me = mtm.login()
        _user_data = mtm.users.get_user_by_username(_user.username)
        if _usr_me["id"] == _user_data["id"]:
            logger.debug('changing_mattermost_user_password: Can not change admin api password with this app')
        else:
            mtm.users.update_user_password(_user_data["id"], options={'new_password': _pass})
        mtm.logout()
    except requests.exceptions.ConnectionError as err:
        logger.debug('changing_mattermost_user_password: ConnectionError %s' % err)
    except requests.exceptions.HTTPError as err:
        logger.debug('changing_mattermost_user_password: HTTPError %s' % err)
    else:
        logger.debug('Changing user %s password success' % _user.username)
