from abc import ABC, abstractmethod
from uuid import uuid4

from src.bank_account.account_status import AccountStatus

class AbstractAccount(ABC):

    def __init__(
            self, 
            owner: str, 
            balance: float, 
            account_number: str | None = None):
             
        self.owner = owner
        self._balance = balance
        self.accountId = account_number or str(uuid4())[:8]
        self.status = AccountStatus.ACTIVE

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def get_account_info(self):
        pass
   