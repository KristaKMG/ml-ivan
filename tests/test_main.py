from src.bank_account.account_status import AccountStatus
from src.bank_account.bank_account import BankAccount
from src.bank_account.currency import Currency
from src.bank_account.exceptions import AccountFrozenError


active_account = BankAccount(
    owner="Ivan",
    balance=1000,
    currency=Currency.RUB
)

print("Активный счёт Ивана:")
print(active_account)

active_account.deposit(500)
print("\nПосле пополнения:")
print(active_account)

active_account.withdraw(300)
print("\nПосле снятия:")
print(active_account)


frozen_account = BankAccount(
    owner="Petr",
    balance=2000,
    currency=Currency.USD
)
print("\nНовый счёт Петра:")
print(frozen_account)

print("\nСчет Петра заморожен")
frozen_account.status = AccountStatus.FROZEN

try:
    print("\nПробуем пополнить счёт Петра:")
    frozen_account.deposit(500)
except AccountFrozenError as e:
    print(f"Ошибка: {e}")

print("\nБаланс счета Петра:")
print(frozen_account)
