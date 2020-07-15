from itertools import combinations
import sys
from typing import Type, List

from func_timeout import func_timeout

import vase_lib
from salesman import DECLINE, ACCEPT, Salesman


def get_disable_prints():
    stdout, stderr = sys.stdout, sys.stderr
    count = [0]

    class __T:
        def __enter__(self):
            sys.stdout, sys.stderr = None, None
            sys.__stdout__, sys.__stderr__ = None, None
            count[0] += 1

        def __exit__(self, exc_type, exc_val, exc_tb):
            count[0] -= 1
            if count[0] == 0:
                sys.stdout, sys.stderr = stdout, stderr
                sys.__stdout__, sys.__stderr__ = stdout, stderr

    return __T()


disable_prints = get_disable_prints()


def run_competition(bots: List[Type[Salesman]] = None, turns_per_match=100, max_bot_runtime=1):
    scores = {}
    if bots is None:
        bots = vase_lib.get_registered_classes()
    for i in bots:
        scores[i.__name__] = 0
    for cls1, cls2, cls3 in combinations(bots, 3):
        print(f'{cls1.__name__} - {cls2.__name__} - {cls3.__name__}')
        try:
            with disable_prints:
                p1 = func_timeout(max_bot_runtime, cls1)
        except BaseException as e:
            print(f'trying to create instance of {cls1.__name__} caused {e}')
            continue
        try:
            with disable_prints:
                p2 = func_timeout(max_bot_runtime, cls2)
        except BaseException as e:
            print(f'trying to create instance of {cls2.__name__} caused {e}')
            continue
        try:
            with disable_prints:
                p3 = func_timeout(max_bot_runtime, cls3)
        except BaseException as e:
            print(f'trying to create instance of {cls3.__name__} caused {e}')
            continue
        for i in range(turns_per_match):
            price = 5
            while True:
                try:
                    with disable_prints:
                        c1 = func_timeout(max_bot_runtime, p1.do_turn, args=(price,))
                except BaseException as e:
                    print(f'{cls1.__name__} crushed: {e}')
                    break
                try:
                    with disable_prints:
                        c2 = func_timeout(max_bot_runtime, p2.do_turn, args=(price,))
                except BaseException as e:
                    print(f'{cls2.__name__} crushed: {e}')
                    break
                try:
                    with disable_prints:
                        c3 = func_timeout(max_bot_runtime, p3.do_turn, args=(price,))
                except BaseException as e:
                    print(f'{cls3.__name__} crushed: {e}')
                    break
                if price > 10000:
                    c1 = c2 = c3 = ACCEPT
                if ACCEPT in [c1, c2, c3]:
                    score1, score2, score3 = Salesman.full_price_to_profits(price, c1, c2, c3)
                    scores[cls1.__name__] += score1
                    scores[cls2.__name__] += score2
                    scores[cls3.__name__] += score3
                    p1.on_sold(price, c1, c2, c3)
                    p2.on_sold(price, c2, c1, c3)
                    p3.on_sold(price, c3, c1, c2)
                    break
                price += 5

    return scores


def show_scores(scores: dict):
    name_score_tuples = list(scores.items())
    name_score_tuples.sort(key=lambda x: x[1], reverse=True)
    try:
        winners = name_score_tuples.copy()
        for place in ['FIRST', 'SECOND', 'THIRD']:
            print(f'{place} PLACE: {" & ".join(x[0] for x in winners if x[1] == winners[0][1])}')
            if place == 'THIRD':
                break
            winners = [x for x in winners if x[1] != winners[0][1]]
            if len(winners) == 0:
                break
    except IndexError:
        pass
    print()
    for index, (name, score) in enumerate(name_score_tuples):
        print(f'{index + 1}. {name} => {score}')


if __name__ == '__main__':
    print('finished registering competitors')
    print()
    print()
    print('running competition...')
    results = run_competition()
    print()
    print()
    print('finished running competitions')
    print('calculating results...')
    print()
    show_scores(results)
