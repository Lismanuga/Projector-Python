import unittest
from unittest.mock import MagicMock
from tested_file import Bank, SavingsAccount
import sys
from io import StringIO


class TestBank(unittest.TestCase):

    def test_open_account(self):
        bank = Bank()
        savings_account = SavingsAccount(1000, "12345", 2)

        bank.open_account(savings_account)
        self.assertIn(savings_account, bank.accounts)
        self.assertEqual(savings_account.get_balance(), 1000)

    def test_update_accounts(self):
        bank = Bank()
        savings_account = SavingsAccount(1000, "12345", 2)
        bank.open_account(savings_account)

        mock_print = MagicMock()
        standart_print = __builtins__.print
        __builtins__.print = mock_print

        standart_stdout = sys.stdout
        mock_stdout = StringIO()
        sys.stdout = mock_stdout

        bank.update_accounts()
        self.assertTrue(savings_account.get_balance() > 1000)
        mock_print.assert_called()

        # print(mock_stdout.getvalue().strip()) не працює
        self.assertTrue(mock_stdout.getvalue().strip() == 'it`s print')

        __builtins__.print = standart_print
        sys.stdout = standart_stdout


if __name__ == '__main__':
    unittest.main()
