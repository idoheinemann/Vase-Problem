import abc
from copy import copy
from typing import Tuple


def _():  # make the registered classes variable invisible
    __registered_classes = []

    def _register(cls):
        if hasattr(cls, 'do_turn'):
            print(f'registering {cls.__name__}...')
            __registered_classes.append(cls)
        else:
            print(f'class {cls.__name__} does not have a method do_turn')

    def _get_registered_classes():
        return copy(__registered_classes)

    return _register, _get_registered_classes


register, get_registered_classes = _()


class SalesmanAction:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name

    def __repr__(self):
        return str(self)


ACCEPT = SalesmanAction('ACCEPT')
DECLINE = SalesmanAction('DECLINE')


class Salesman(abc.ABC):
    """
    prisoner base class
    all prisoner bots must inherit from the prisoner class

    Note! constructor for this class cannot accept any arguments
    Note! printing will not work when using do_turn
    """

    def __init_subclass__(cls, **kwargs):
        register(cls)

    @staticmethod
    def full_price_to_profits(full_price: int, first_action: SalesmanAction, seconds_action: SalesmanAction,
                              thirds_action: SalesmanAction) -> Tuple[int, int, int]:
        """
        calculates the profit each salesman made according to his action

        :param full_price: the full price in which the vase was sold
        :param first_action: the action the first salesman took
        :param seconds_action: the action the second salesman took
        :param thirds_action: the action the third salesman took
        :return: a tuple of the way the profit was divided (first profit, second profit, third profit)
        """
        if first_action is ACCEPT and seconds_action is DECLINE and thirds_action is DECLINE:
            return full_price, 0, 0
        if first_action is DECLINE and seconds_action is ACCEPT and thirds_action is DECLINE:
            return 0, full_price, 0
        if first_action is DECLINE and seconds_action is DECLINE and thirds_action is ACCEPT:
            return 0, 0, full_price
        if first_action is ACCEPT and seconds_action is ACCEPT and thirds_action is DECLINE:
            return full_price // 4, full_price // 4, full_price // 2
        if first_action is ACCEPT and seconds_action is DECLINE and thirds_action is ACCEPT:
            return full_price // 4, full_price // 2, full_price // 4
        if first_action is DECLINE and seconds_action is ACCEPT and thirds_action is ACCEPT:
            return full_price // 2, full_price // 4, full_price // 4
        return full_price // 3, full_price // 3, full_price // 3

    @abc.abstractmethod
    def on_sold(self, full_price: int, my_action: SalesmanAction, seconds_action: SalesmanAction,
                thirds_action: SalesmanAction):
        """
        called when the vase is sold
        allows the agent to know what the others have chosen to do and prepare for the next round

        :param full_price: the full price at which the vase was sold
        :param my_action: the action
        :param seconds_action:
        :param thirds_action:
        :return:
        """

    @abc.abstractmethod
    def do_turn(self, price: int) -> SalesmanAction:
        """
        runs a single turn and return's the prisoners choice

        :param price: the current price of the vase

        :return: the action for this turn, either LOYAL or BETRAY
        """
