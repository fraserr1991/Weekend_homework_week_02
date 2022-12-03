class Guest:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet

    def pay_entry_fee_from_wallet(self, amount):
        self.wallet -= amount