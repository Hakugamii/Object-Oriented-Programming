from abc import ABC, abstractmethod

class Wallet(ABC):
    @abstractmethod
    def transaction(self, trans_type, value):
        pass

    @property
    def balance(self):
        pass

class BitcoinWallet(Wallet):
    def __init__(self, name, btc_balance):
        self.name = name
        self.__btcBalance = float(btc_balance)

    def __str__(self):
        return f"{self.name}'s BTC Wallet"

    def transaction(self, trans_type, value):
        if trans_type == "buy":
            self.__btcBalance += value
        elif trans_type == "sell":
            self.__btcBalance -= value
        return trans_type, value

    def transaction_details(self, trans_type, value):
        print(f"{self}\nInitial Balance: {self.balance} ETH")
        if trans_type == "buy":
            print(f"Performing Transaction: {trans_type} {value} BTC\nNew Balance: {self.balance} BTC\n")
        elif trans_type == "sell":
            print(f"Performing Transaction: {trans_type} {value} BTC\nNew Balance: {self.balance} BTC\n")

    @property
    def balance(self):
        return self.__btcBalance

class EthereumWallet(Wallet):
    def __init__(self, name, eth_balance):
        self.name = name
        self.__ethBalance = float(eth_balance)

    def __str__(self):
        return f"{self.name}'s Ethereum Wallet"

    def transaction(self, trans_type, value):
        if trans_type == "buy":
            self.__ethBalance += value
        elif trans_type == "sell":
            self.__ethBalance -= value
        return trans_type, value

    def transaction_details(self, trans_type, value):
        print(f"{self}\nInitial Balance: {self.balance} ETH")
        if trans_type == "buy":
            print(f"Performing Transaction: {trans_type} {value} ETH\nNew Balance: {self.balance} ETH\n")
        elif trans_type == "sell":
            print(f"Performing Transaction: {trans_type} {value} ETH\nNew Balance: {self.balance} ETH\n")

    @property
    def balance(self):
        return self.__ethBalance

Alice = BitcoinWallet("Alice", 0.5)
Bob = EthereumWallet("Bob", 2.0)

alice_trans_type, alice_value = Alice.transaction("buy", 0.1)
Alice.transaction_details(alice_trans_type, alice_value)
bob_trans_type, bob_value = Bob.transaction("sell", 1.0)
Bob.transaction_details(bob_trans_type, bob_value)

