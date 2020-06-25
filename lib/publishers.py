from abc import ABC, abstractmethod
from lib.subscribers import AbstractSubscriber
from lib.helpers import StockInfo
from random import randint


class AbstractPublisher(ABC):

    @abstractmethod
    def add_subscriber(self, subscriber: AbstractSubscriber):
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber: AbstractSubscriber):
        pass

    @abstractmethod
    def notify_subscribers(self):
        pass


class Stock(AbstractPublisher):

    def __init__(self):
        self._stock_info = StockInfo()
        self._subscribers = []

    def add_subscriber(self, subscriber: AbstractSubscriber):
        self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: AbstractSubscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self):
        for sub in self._subscribers:
            sub.update(self._stock_info)

    def market(self):
        self._stock_info.usd = randint(25, 35)
        self._stock_info.eur = randint(28, 48)
        self.notify_subscribers()
