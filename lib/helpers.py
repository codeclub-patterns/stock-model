class StockInfo(object):

    def __init__(self):
        self._usd = 0.0
        self._eur = 0.0

    @property
    def usd(self) -> float:
        return self._usd

    @usd.setter
    def usd(self, usd) -> None:
        self._usd = usd

    @property
    def eur(self) -> float:
        return self._eur

    @eur.setter
    def eur(self, eur) -> None:
        self._eur = eur

    def __str__(self) -> str:
        return f'USD: {self._usd}; EUR: {self._eur}'
