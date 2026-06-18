class Carteira:
    def __init__(self, moeda, saldo):
        self.moeda = moeda
        self.saldo = saldo

    def converter(self, valor_yuan):
        if self.moeda == "USD":
            return valor_yuan * 0.14
        elif self.moeda == "BRL":
            return valor_yuan * 0.85
        else:
            return valor_yuan

    def __add__(self, valor_yuan):
        return self.saldo + self.converter(valor_yuan)

    def __sub__(self, valor_yuan):
        return self.saldo - self.converter(valor_yuan)


carteira_usd = Carteira("USD", 10.0)

print(carteira_usd + 50)
print(carteira_usd - 50)
