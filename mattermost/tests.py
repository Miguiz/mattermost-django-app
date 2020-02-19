from django.test import TestCase
from django.contrib.auth.models import User

from unittest.mock import patch

from .models.alerts import MemberAlertManager
from .signals import randomStringDigits

import logging

logging.basicConfig(level=logging.DEBUG)

_logger = logging.getLogger(__name__)


class MattermostTestCase(TestCase):

    myClass = MemberAlertManager()
    _pass = randomStringDigits()

    def setUp(self):
        self._usr = User.objects.create_user('4321_test_1234', email='test@example.com', password='password')

    def tearDown(self):
        self._usr.delete()

    @patch('mattermost.signals.logger')
    def test_adding_mattermost_user(self, mock_logger):
        self.myClass.handle_new_membership(self._usr)
        mock_logger.debug.assert_called_with('Adding user %s success' % self._usr.username)
        _logger.debug('test_adding_mattermost_user %s success' % self._usr.username)

    @patch('mattermost.signals.logger')
    def test_changing_mattermost_user_password(self, mock_logger):
        self.myClass.handle_changing_membership_password(self._usr, self._pass)
        mock_logger.debug.assert_called_with('Changing user %s password success' % self._usr.username)
        _logger.debug('test_changing_mattermost_user_password %s success' % self._usr)

    @patch('mattermost.signals.logger')
    def test_deactivating_mattermost_user(self, mock_logger):
        self.myClass.handle_ending_membership(self._usr)
        mock_logger.debug.assert_called_with('Deactivating user %s success' % self._usr.username)
        _logger.debug('test_deactivating_mattermost_user %s success' % self._usr)
