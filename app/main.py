from lib.publishers import Stock
from lib.subscribers import Broker, Bank


if __name__ == '__main__':

    stock = Stock()

    bank1 = Bank('Приват', stock)
    broker1 = Broker('Иван Иванович', stock)
    print('---------------------------------------------------')
    stock.market()

    bank2 = Bank('Укргазбанк', stock)
    broker2 = Broker('Степан Степанович', stock)
    print('---------------------------------------------------')
    broker1.stop_trade()
    stock.market()
