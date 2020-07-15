from vase_lib import Salesman, DECLINE, ACCEPT, SalesmanAction


class ThresholdSalesman(Salesman):
    def __init__(self):
        self.max_price = 25

    def on_sold(self, full_price: int, my_action: SalesmanAction, seconds_action: SalesmanAction,
                thirds_action: SalesmanAction):
        pass

    def do_turn(self, price: int) -> SalesmanAction:
        if price >= self.max_price:
            return ACCEPT
        return DECLINE


class VengefulSalesman(Salesman):
    def __init__(self):
        self.max_price = None

    def on_sold(self, full_price: int, my_action: SalesmanAction, seconds_action: SalesmanAction,
                thirds_action: SalesmanAction):
        if not (my_action is ACCEPT and seconds_action is DECLINE and thirds_action is DECLINE):
            self.max_price = full_price - 5

    def do_turn(self, price: int) -> SalesmanAction:
        if self.max_price is None or price < self.max_price:
            return DECLINE
        return ACCEPT


class TitForTatSalesman(Salesman):
    def __init__(self):
        self.sell_price = None

    def on_sold(self, full_price: int, my_action: SalesmanAction, seconds_action: SalesmanAction,
                thirds_action: SalesmanAction):
        self.sell_price = full_price

    def do_turn(self, price: int) -> SalesmanAction:
        if self.sell_price is None or price < self.sell_price:
            return DECLINE
        return ACCEPT
