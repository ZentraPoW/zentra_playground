

import code
import readline
import rlcompleter

import space
import funcs

def prepare():
    space.states = [{}]

    funcs.asset_create({'sender':'0x001'}, {'p': 'zen', 'f': 'asset_create', 'a':['BTC']})
    space.nextblock()

    funcs.token_create({'sender':'0x001'}, {'p': 'zen', 'f': 'token_create', 'a':['BTC', 'mock', 6]})
    space.nextblock()

    funcs.token_mint_once({'sender':'0x001'}, {'p': 'zen', 'f': 'token_mint_once', 'a':['BTC', 10000]})
    space.nextblock()


    funcs.asset_create({'sender':'0x002'}, {'p': 'zen', 'f': 'asset_create', 'a':['USDT']})
    space.nextblock()

    funcs.token_create({'sender':'0x002'}, {'p': 'zen', 'f': 'token_create', 'a':['USDT', 'mock', 6]})
    space.nextblock()

    funcs.token_mint_once({'sender':'0x002'}, {'p': 'zen', 'f': 'token_mint_once', 'a':['USDT', 10000]})
    space.nextblock()


    funcs.transfer({'sender':'0x001'}, {'p': 'zen', 'f': 'transfer', 'a':['BTC', '0x002', 5000]})
    space.nextblock()

    funcs.transfer({'sender':'0x002'}, {'p': 'zen', 'f': 'transfer', 'a':['USDT', '0x001', 5000]})
    space.nextblock()


def test1():
    prepare()

    # limit orders + market orders
    print('1======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('2======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 11, 'USDT', -11]})
    print(space.states[-1])
    space.nextblock()

    print('3======trade_market_order')
    funcs.trade_market_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', None, 'USDT', -22]})
    print(space.states[-1])
    space.nextblock()

    print('4======trade_market_order')
    funcs.trade_market_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', -30, 'USDT', None]})
    print(space.states[-1])
    space.nextblock()

    print('5======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('6======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 9, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('7======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 1, 'USDT', -1]})
    print(space.states[-1])
    space.nextblock()

    print('8======trade_market_order')
    funcs.trade_market_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', -30, 'USDT', None]})
    print(space.states[-1])
    space.nextblock()


def test2():
    prepare()

    print('1======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('2======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('3======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -20, 'USDT', 20]})
    print(space.states[-1])

    print('4======trade_market_order')
    funcs.trade_market_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', None, 'USDT', -20]})
    print(space.states[-1])
    space.nextblock()

    print('5======trade_market_order')
    funcs.trade_market_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', None, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()


def test2b():
    prepare()

    print('1======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('2======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('3======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 20, 'USDT', -20]})
    print(space.states[-1])

    print('4======trade_market_order')
    funcs.trade_market_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', -20, 'USDT', None]})
    print(space.states[-1])
    space.nextblock()

    print('5======trade_market_order')
    funcs.trade_market_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', -10, 'USDT', None]})
    print(space.states[-1])
    space.nextblock()


def test3():
    prepare()

    # limit orders buy and sell
    print('1======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('2======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -11, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('3======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 1, 'USDT', -1]})
    print(space.states[-1])
    space.nextblock()


def test4():
    prepare()

    print('1======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('2======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 11, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('3======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 14, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('4======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 13, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('5======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 110, 'USDT', -100]})
    print(space.states[-1])
    space.nextblock()


def test5():
    prepare()

    print('1======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 50]})
    print(space.states[-1])
    space.nextblock()

    print('2======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 60]})
    print(space.states[-1])
    space.nextblock()

    print('3======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 70]})
    print(space.states[-1])
    space.nextblock()

    print('4======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 80]})
    print(space.states[-1])
    space.nextblock()

    print('5======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 60]})
    print(space.states[-1])
    space.nextblock()


def test6():
    prepare()

    print('1======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('2======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 20, 'USDT', -20]})
    print(space.states[-1])
    space.nextblock()

    print('3======trade_market_order')
    funcs.trade_market_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', -5, 'USDT', None]})
    print(space.states[-1])
    space.nextblock()

    print('4======trade_market_order')
    funcs.trade_market_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', -3, 'USDT', None]})
    print(space.states[-1])
    space.nextblock()

    print('5======trade_market_order')
    funcs.trade_market_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', -30, 'USDT', None]})
    print(space.states[-1])
    space.nextblock()


def test7():
    prepare()

    print('1======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('2======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -9, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('3======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -17, 'USDT', 20]})
    print(space.states[-1])



    print('1======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -11, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('2======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -12, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('3======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -25, 'USDT', 20]})
    print(space.states[-1])

    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])


def test8():
    prepare()

    print('1======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('2======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 9, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('3======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 17, 'USDT', -20]})
    print(space.states[-1])



    print('1======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 11, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('2======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 12, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('3======trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 25, 'USDT', -20]})
    print(space.states[-1])

    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 10]})
    print(space.states[-1])

test1()
test2()
test2b()
test3()
test4()
test5()
test6()
test7()
test8()
