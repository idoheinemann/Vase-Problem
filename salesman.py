from vase_lib import Salesman, DECLINE, ACCEPT, SalesmanAction


class AcceptOnSpotSalesman(Salesman):

    def on_sold(self, full_price: int, my_action: SalesmanAction, seconds_action: SalesmanAction,
                thirds_action: SalesmanAction):
        pass

    def do_turn(self, price: int) -> SalesmanAction:
        return ACCEPT


class AlwaysDeclineSalesman(Salesman):

    def on_sold(self, full_price: int, my_action: SalesmanAction, seconds_action: SalesmanAction,
                thirds_action: SalesmanAction):
        pass

    def do_turn(self, price: int) -> SalesmanAction:
        return DECLINE


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


class DecreaseSalesman(Salesman):
    def __init__(self):
        self.sell_price = 500

    def on_sold(self, full_price: int, my_action: SalesmanAction, seconds_action: SalesmanAction,
                thirds_action: SalesmanAction):
        self.sell_price -= 5

    def do_turn(self, price: int) -> SalesmanAction:
        if price < self.sell_price:
            return DECLINE
        return ACCEPT


class EpsilonSalesman(Salesman):
    def __init__(self):
        self.epsilon = 0.02

    def on_sold(self, full_price: int, my_action: SalesmanAction, seconds_action: SalesmanAction,
                thirds_action: SalesmanAction):
        pass

    def do_turn(self, price: int) -> SalesmanAction:
        import random
        if random.random() > self.epsilon:
            return DECLINE
        return ACCEPT


class SuperVengefulSalesman(Salesman):
    def __init__(self):
        self.max_price = None

    def on_sold(self, full_price: int, my_action: SalesmanAction, seconds_action: SalesmanAction,
                thirds_action: SalesmanAction):
        if not (my_action is ACCEPT and seconds_action is DECLINE and thirds_action is DECLINE):
            self.max_price = full_price * 0.95

    def do_turn(self, price: int) -> SalesmanAction:
        if self.max_price is None or price < self.max_price:
            return DECLINE
        return ACCEPT
