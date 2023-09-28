class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self._interest_rate = interest_rate

    def add_interest(self):
        self._balance += self._balance * (self._interest_rate / 100)


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self._balance < 0:
            print(f"Overdraft letter sent for account {self._account_number}")


class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def close_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                self.accounts.remove(account)

    def pay_dividend(self, amount):
        for account in self.accounts:
            account.deposit(amount)

    def update_accounts(self):
        # print('it`s print')
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                if account.get_balance() < 0:
                    account.send_overdraft_letter()


savings_account = SavingsAccount(1000, "12345", 2)
current_account = CurrentAccount(1000, "67890", -1000)
bank = Bank()
bank.open_account(savings_account)
bank.open_account(current_account)
savings_account.deposit(500)
current_account.withdraw(500)
bank.update_accounts()
bank.pay_dividend(500)
# bank.close_account("12345")
for account in bank.accounts:
    print(account)
