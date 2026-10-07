from src.bank_account.abstract_account import AbstractAccount
from src.bank_account.account_status import AccountStatus
from src.bank_account.currency import Currency
from src.bank_account.exceptions import AccountClosedError, AccountFrozenError, InsufficientFundsError, InvalidOperationError


class BankAccount(AbstractAccount):
        
    def __init__(
            self, 
            owner: str, 
            balance: float,
            account_number: str | None = None,
            currency: Currency = Currency.RUB        
    ):
        if not isinstance(owner, str) or not owner.strip():
            raise InvalidOperationError("Owner must be a non-empty string")

        if not isinstance(balance, (int, float)):
            raise InvalidOperationError("Balance must be a number")

        if balance < 0:
            raise InvalidOperationError("Balance cannot be negative")

        if not isinstance(currency, Currency):
            raise InvalidOperationError("Invalid currency")

        super().__init__(owner, balance, account_number)

        self.currency = currency

    def _check_account_status(self):
        if self.status == AccountStatus.FROZEN:
            raise AccountFrozenError("Account is frozen")
        if self.status == AccountStatus.CLOSED:
            raise AccountClosedError("Account is closed")

    def deposit(self, amount: float):
        self._check_account_status()

        if not isinstance(amount, (int, float)):
            raise InvalidOperationError("Amount must be a number")

        if amount <= 0:
            raise InvalidOperationError("Amount must be a positive number")

        self._balance += amount

    def withdraw(self, amount: float):
        self._check_account_status()

        if not isinstance(amount, (int, float)):
            raise InvalidOperationError("Amount must be a number")

        if amount <= 0:
            raise InvalidOperationError("Amount must be a positive number")

        if amount > self._balance:
            raise InsufficientFundsError("Insufficient funds")

        self._balance -= amount

    def get_account_info(self):
        return {
            "account_id": self.accountId,
            "owner": self.owner,
            "balance": self._balance,
            "currency": self.currency,
            "status": self.status
        }
    def __str__(self):
        return (
            f"BankAccount | "
            f"Client: {self.owner} | "
            f"Account: ****{self.accountId[-4:]} | "
            f"Status: {self.status.value} | "
            f"Balance: {self._balance:.2f} {self.currency.value}"
    )