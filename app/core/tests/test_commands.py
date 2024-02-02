from unittest.mock import patch  # to mock behaviour

# to call the command we are testing
from psycopg2 import OperationalError as Psycopg2Error
# another error may while connecting db
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase  # for creating our unittest


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test Commands"""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database is ready"""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError."""
        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        # self.assertEqual(patched_check.call_command, 6)   # noqa
        patched_check.assert_called_with(databases=['default'])
