

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
    print('=test1 1 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('=test1 2 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 11, 'USDT', -11]})
    print(space.states[-1])
    space.nextblock()

    print('=test1 3 trade_market_order')
    funcs.trade_market_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', None, 'USDT', -22]})
    print(space.states[-1])
    space.nextblock()

    print('=test1 4 trade_market_order')
    funcs.trade_market_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', -30, 'USDT', None]})
    print(space.states[-1])
    space.nextblock()

    print('=test1 5 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('=test1 6 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 11, 'USDT', -11]})
    print(space.states[-1])
    space.nextblock()

def test1b():
    prepare()

    print('=test1b 1 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('=test1b 2 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -11, 'USDT', 11]})
    print(space.states[-1])
    space.nextblock()

    print('=test1b 3 trade_market_order')
    funcs.trade_market_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', -22, 'USDT', None]})
    print(space.states[-1])
    space.nextblock()

    print('=test1b 4 trade_market_order')
    funcs.trade_market_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', None, 'USDT', -20]})
    print(space.states[-1])
    space.nextblock()

    print('=test1b 5 trade_market_order')
    funcs.trade_market_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', None, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('=test1b 6 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('=test1b 7 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -11, 'USDT', 11]})
    print(space.states[-1])
    space.nextblock()


def test2():
    prepare()

    print('=test2 1 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('=test2 2 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('=test2 3 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -20, 'USDT', 20]})
    print(space.states[-1])

    print('=test2 4 trade_market_order')
    funcs.trade_market_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', None, 'USDT', -20]})
    print(space.states[-1])
    space.nextblock()

    print('=test2 5 trade_market_order')
    funcs.trade_market_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', None, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()


def test2b():
    prepare()

    print('=test2b 1 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('=test2b 2 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('=test2b 3 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 20, 'USDT', -20]})
    print(space.states[-1])

    print('=test2b 4 trade_market_order')
    funcs.trade_market_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', -20, 'USDT', None]})
    print(space.states[-1])
    space.nextblock()

    print('=test2b 5 trade_market_order')
    funcs.trade_market_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', -10, 'USDT', None]})
    print(space.states[-1])
    space.nextblock()


def test3():
    prepare()

    # limit orders buy and sell
    print('=test3 1 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('=test3 2 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -11, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('=test3 3 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 1, 'USDT', -1]})
    print(space.states[-1])
    space.nextblock()


# def test3b():
#     prepare()

#     # limit orders buy and sell
#     print('1======trade_limit_order')
#     funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 10]})
#     print(space.states[-1])
#     space.nextblock()

#     print('2======trade_limit_order')
#     funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 11, 'USDT', -10]})
#     print(space.states[-1])
#     space.nextblock()

#     print('3======trade_limit_order')
#     funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -1, 'USDT', 1]})
#     print(space.states[-1])
#     space.nextblock()


def test4():
    prepare()

    print('=test4 1 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('=test4 2 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 11, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('=test4 3 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 14, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('=test4 4 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 13, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('=test4 5 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 110, 'USDT', -100]})
    print(space.states[-1])
    space.nextblock()


def test5():
    prepare()

    print('=test5 1 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 50]})
    print(space.states[-1])
    space.nextblock()

    print('=test5 2 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 60]})
    print(space.states[-1])
    space.nextblock()

    print('=test5 3 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 70]})
    print(space.states[-1])
    space.nextblock()

    print('=test5 4 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 80]})
    print(space.states[-1])
    space.nextblock()

    print('=test5 5 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 60]})
    print(space.states[-1])
    space.nextblock()


# def test6():
#     prepare()

#     print('1======trade_limit_order')
#     funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
#     print(space.states[-1])
#     space.nextblock()

#     print('2======trade_limit_order')
#     funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 20, 'USDT', -20]})
#     print(space.states[-1])
#     space.nextblock()

#     print('3======trade_market_order')
#     funcs.trade_market_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', -5, 'USDT', None]})
#     print(space.states[-1])
#     space.nextblock()

#     print('4======trade_market_order')
#     funcs.trade_market_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', -3, 'USDT', None]})
#     print(space.states[-1])
#     space.nextblock()

#     print('5======trade_market_order')
#     funcs.trade_market_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_market_order', 'a':['BTC', -30, 'USDT', None]})
#     print(space.states[-1])
#     space.nextblock()


def test7():
    prepare()

    print('=test7 1 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('=test7 2 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -9, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('=test7 3 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -17, 'USDT', 20]})
    print(space.states[-1])



    print('=test7 4 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -11, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('=test7 5 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -12, 'USDT', 10]})
    print(space.states[-1])
    space.nextblock()

    print('=test7 6 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -25, 'USDT', 20]})
    print(space.states[-1])

    print('=test7 7 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])


def test8():
    prepare()

    print('=test8 1 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 10, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('=test8 2 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 9, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('=test8 3 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 17, 'USDT', -20]})
    print(space.states[-1])


    print('=test8 4 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x002'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 11, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('=test8 5 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 12, 'USDT', -10]})
    print(space.states[-1])
    space.nextblock()

    print('=test8 6 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', 25, 'USDT', -20]})
    print(space.states[-1])

    print('=test8 7 trade_limit_order')
    funcs.trade_limit_order({'sender':'0x001'}, {'p': 'zen', 'f': 'trade_limit_order', 'a':['BTC', -10, 'USDT', 10]})
    print(space.states[-1])


test1()
test1b()
test2()
test2b()
test3()
# test3b()
test4()
test5()
# test6()
test7()
test8()
