from django.test import TestCase

from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as i_mock:
            i_mock.return_value = True
            call_command('wait_for_db')
            self.assertEqual(i_mock.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as i_mock:
            i_mock.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(i_mock.call_count, 6)
