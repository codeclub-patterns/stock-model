from abc import ABC, abstractmethod
from lib.helpers import StockInfo


class AbstractSubscriber(ABC):

    @abstractmethod
    def update(self, stock_info: StockInfo):
        pass


class Bank(AbstractSubscriber):

    def __init__(self, name: str, stock):
        self._name = name
        self._stock = stock
        self._stock.add_subscriber(self)

    def update(self,  stock_info: StockInfo):
        if stock_info.eur > 40:
            print(f'Банк {self._name} продает евро. Курс - {stock_info.eur}')
        else:
            print(f'Банк {self._name} покупает евро. Курс - {stock_info.eur}')


class Broker(AbstractSubscriber):

    def __init__(self, name: str, stock):
        self._name = name
        self._stock = stock
        self._stock.add_subscriber(self)

    def update(self,  stock_info: StockInfo):
        if stock_info.usd > 30:
            print(f'Брокер {self._name} продает доллары. Курс - {stock_info.usd}')
        else:
            print(f'Брокер {self._name} покупает доллары. Курс - {stock_info.usd}')

    def stop_trade(self):
        self._stock.remove_subscriber(self)
        print(f'Брокер {self._name} - вышел из торгов')
