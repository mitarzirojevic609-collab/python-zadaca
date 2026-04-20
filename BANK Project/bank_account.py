from data_base import Db
class BankAccount(Db):

    def __init__(self, id, owner, balance):
        super().__init__()
        self.id = id
        self.owner = owner
        self.balance = balance

    def deposit(self, iznos):
        if iznos < 0:
            raise ValueError("Iznos mora biti veci od 0")
        self.balance += iznos
        self.update_balance()


    def withdraw(self, iznos):
        if self.balance >= iznos:
            self.balance -= iznos

        else:
           raise ValueError("nemate dovoljan iznos na racunu")
        self.update_balance()

    def update_balance(self):
        self.cursor.execute(
            "UPDATE accounts SET balance = %s WHERE id = %s",
            (self.balance, self.id)
        )
        self.connection.commit()

    def account_info(self):
        return f"ID:{self.id}, owner:{self.owner}, balance:{self.balance}"

    def save_account(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO accounts (owner, balance) VALUES(%s, %s)",
                       (self.owner, self.balance)
                            )
        self.connection.commit()

    def load_accounts(self):
        self.cursor.execute("SELECT * from accounts")
        rows = self.cursor.fetchall()
        accounts = []
        for row in rows:
            account = BankAccount(row[0], row[1], row[2])
            accounts.append(account)
        return accounts

    def delete_account(self):
        self.cursor.execute("DELETE FROM accounts where id = %s",
                            (self.id,)
                            )
        self.connection.commit()



account = BankAccount(None, "Mitar", 1000)
account.save_account()
print(account.account_info())
account.deposit(800)
print(account.account_info())

