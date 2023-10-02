import unittest
from tested_file import Bank
# from tested_file import Account
from tested_file import SavingsAccount


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

        class MockPrint:
            def __init__(self):
                self.called = False

            def __call__(self, *args, **kwargs):
                self.called = True

        mock_print = MockPrint()
        standart_print = __builtins__.print
        __builtins__.print = mock_print

        bank.update_accounts()

        self.assertTrue(savings_account.get_balance() > 1000)
        self.assertTrue(mock_print.called)

        __builtins__.print = standart_print


if __name__ == '__main__':
    unittest.main()
