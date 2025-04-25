import string
from inspect import currentframe, getframeinfo

from space import put, get, handle_lookup
import space

def token_mint_once(info, args): # pragma: no cover
    tick = args['a'][0]
    assert type(tick) is str
    assert len(tick) > 0 and len(tick) < 42
    assert tick[0] in string.ascii_uppercase
    assert set(tick) <= set(string.ascii_uppercase+string.digits+'_')

    value = int(args['a'][1])
    assert value > 0

    assert args['f'] == 'token_mint_once'
    # print(get('asset', 'functions', [], tick))
    assert args['f'] in get('asset', 'functions', [], tick)

    sender = info['sender']
    handle = handle_lookup(sender)
    addr = handle or sender
    total = int(args['a'][1])
    assert get(tick, 'total', None) is None
    put(addr, tick, 'total', total)

    balance = get(tick, 'balance', 0, addr)
    balance += value
    put(addr, tick, 'balance', balance, addr)

def token_mint(info, args): # pragma: no cover
    tick = args['a'][0]
    assert type(tick) is str
    assert len(tick) > 0 and len(tick) < 42
    assert tick[0] in string.ascii_uppercase
    assert set(tick) <= set(string.ascii_uppercase+string.digits+'_')

    assert args['f'] == 'token_mint'
    assert args['f'] in get('asset', 'functions', [], tick)

    value = int(args['a'][1])
    assert value > 0
    sender = info['sender']
    handle = handle_lookup(sender)
    addr = handle or sender

    balance = get(tick, 'balance', 0, addr)
    balance += value
    put(addr, tick, 'balance', balance, addr)

def token_create(info, args): # pragma: no cover
    assert args['f'] == 'token_create'
    sender = info['sender']
    handle = handle_lookup(sender)
    addr = handle or sender

    tick = args['a'][0]
    assert type(tick) is str
    assert len(tick) > 0 and len(tick) < 42
    assert tick[0] in string.ascii_uppercase
    assert set(tick) <= set(string.ascii_uppercase+string.digits+'_')

    name = args['a'][1]
    assert type(name) is str
    decimal = int(args['a'][2])
    assert type(decimal) is int
    assert decimal >= 0 and decimal <= 18

    functions = ['transfer', 'approve', 'transfer_from', 'token_mint_once', 'asset_update_ownership', 'asset_update_functions']
    put(addr, tick, 'name', name)
    put(addr, tick, 'decimal', decimal)
    put(addr, 'asset', 'functions', functions, tick)

def transfer(info, args): # pragma: no cover
    tick = args['a'][0]
    assert set(tick) <= set(string.ascii_uppercase+'_')

    assert args['f'] == 'transfer'
    assert args['f'] in get('asset', 'functions', [], tick)

    receiver = args['a'][1].lower()
    assert len(receiver) <= 42
    assert type(receiver) is str
    if len(receiver) == 42:
        assert receiver.startswith('0x')
        assert set(receiver[2:]) <= set(string.digits+'abcdef')
    else:
        assert len(receiver) > 4

    sender = info['sender']
    handle = handle_lookup(sender)
    addr = handle or sender

    value = int(args['a'][2])
    assert value > 0

    sender_balance = get(tick, 'balance', 0, addr)
    assert sender_balance >= value
    sender_balance -= value
    put(addr, tick, 'balance', sender_balance, addr)
    receiver_balance = get(tick, 'balance', 0, receiver)
    receiver_balance += value
    put(receiver, tick, 'balance', receiver_balance, receiver)

def asset_create(info, args): # pragma: no cover
    assert args['f'] == 'asset_create'
    sender = info['sender']
    tick = args['a'][0]
    assert type(tick) is str
    assert len(tick) > 0 and len(tick) < 42
    assert tick[0] in string.ascii_uppercase
    assert set(tick) <= set(string.ascii_uppercase+string.digits+'_')
    handle = handle_lookup(sender)
    addr = handle or sender
    # print('handle', handle, 'addr', addr, 'sender', sender)
    owner = get('asset', 'owner', None, tick)
    # print(owner, addr)
    assert not owner

    put(addr, 'asset', 'owner', addr, tick)
    put(addr, 'asset', 'functions', ['asset_update_ownership', 'asset_update_functions'], tick)

def asset_update_ownership(info, args): # pragma: no cover
    assert args['f'] == 'asset_update_ownership'
    sender = info['sender']
    tick = args['a'][0]
    receiver = args['a'][1]
    assert type(tick) is str
    assert len(tick) > 0 and len(tick) < 42
    assert tick[0] in string.ascii_uppercase
    assert set(tick) <= set(string.ascii_uppercase+string.digits+'_')
    # print('sender', sender)
    handle = handle_lookup(sender)
    # print('handle', handle)
    addr = handle or sender

    owner = get('asset', 'owner', None, tick)
    # print( owner, addr)
    assert owner == addr
    functions = get('asset', 'functions', None, tick)
    assert type(functions) is list
    assert functions
    put(receiver, 'asset', 'owner', receiver, tick)
    put(receiver, 'asset', 'functions', functions, tick)

def asset_update_functions(info, args): # pragma: no cover
    assert args['f'] == 'asset_update_functions'
    sender = info['sender']
    handle = handle_lookup(sender)
    # print('handle', handle)

    tick = args['a'][0]
    assert type(tick) is str
    assert len(tick) > 0 and len(tick) < 42
    assert tick[0] in string.ascii_uppercase
    assert set(tick) <= set(string.ascii_uppercase+string.digits+'_')

    functions = args['a'][1]
    assert type(functions) is list
    assert functions


def bridge_incoming(info, args): # pragma: no cover
    assert args['f'] == 'bridge_incoming'
    print('bridge_incoming', args)

    tick = args['a'][0]
    assert type(tick) is str
    assert len(tick) > 0 and len(tick) < 42
    assert tick[0] in string.ascii_uppercase
    assert set(tick) <= set(string.ascii_uppercase+string.digits+'_')

    operator = get(tick, 'incoming_operator', None)
    assert operator is not None, "Bridge is not initialized"

    sender = info['sender']
    assert sender == operator, "Only the operator can perform this operation"

    amount = int(args['a'][1])
    assert amount > 0

    receiver = args['a'][2].lower()
    assert len(receiver) <= 42
    assert type(receiver) is str
    if len(receiver) == 42:
        assert receiver.startswith('0x')
        assert set(receiver[2:]) <= set(string.digits+'abcdef')
    else:
        assert len(receiver) > 4

    balance = int(get(tick, 'balance', 0, receiver))
    balance += amount
    put(receiver, tick, 'balance', balance, receiver)

    asset_owner = get('asset', 'owner', None, tick)
    total = int(get(tick, 'total', 0, receiver))
    total += amount
    put(asset_owner, tick, 'total', total)

# def bridge_set_operator(info, args):
#     assert args['f'] == 'bridge_set_operator'
#     print('bridge_set_operator', args)

#     tick = args['a'][0]
#     assert type(tick) is str
#     assert len(tick) > 0 and len(tick) < 42
#     assert tick[0] in string.ascii_uppercase
#     assert set(tick) <= set(string.ascii_uppercase+string.digits+'_')

#     asset_owner = get('asset', 'owner', None, tick)
#     sender = info['sender']
#     handle = handle_lookup(sender)
#     addr = handle or sender
#     print('bridge_set_operator', asset_owner, addr)
#     assert addr == asset_owner, "Only the asset owner can perform this operation"

#     operator = args['a'][1].lower()
#     assert type(operator) is str
#     assert len(operator) == 42
#     assert operator.startswith('0x')
#     assert set(operator[2:]) <= set(string.digits+'abcdef')

#     put(addr, tick, 'incoming_operator', operator)

# def bridge_with_token_purchase(info, args):
#     assert args['f'] == 'bridge_with_token_purchase'
#     print('bridge_with_token_purchase', args)

#     tick = args['a'][0]
#     assert type(tick) is str
#     assert len(tick) > 0 and len(tick) < 42
#     assert tick[0] in string.ascii_uppercase
#     assert set(tick) <= set(string.ascii_uppercase+string.digits+'_')

#     operator = get(tick, 'incoming_operator', None)
#     assert operator is not None, "Bridge is not initialized"

#     sender = info['sender']
#     assert sender == operator, "Only the operator can perform this operation"

#     amount = int(args['a'][1])
#     assert amount > 0

#     receiver = args['a'][2].lower()
#     assert len(receiver) <= 42
#     assert type(receiver) is str
#     if len(receiver) == 42:
#         assert receiver.startswith('0x')
#         assert set(receiver[2:]) <= set(string.digits+'abcdef')
#     else:
#         assert len(receiver) > 4

#     balance = int(get(tick, 'balance', 0, receiver))
#     balance += amount
#     put(receiver, tick, 'balance', balance, receiver)

#     asset_owner = get('asset', 'owner', None, tick)
#     total = int(get(tick, 'total', 0, receiver))
#     total += amount
#     put(asset_owner, tick, 'total', total)


# def token_sell_bondingcurve(info, args):
#     assert args['f'] == 'token_sell_bondingcurve'
#     print('token_sell_bondingcurve', args)

#     tick = args['a'][0]

# def token_set_bondingcurve(info, args):
#     assert args['f'] == 'token_set_bondingcurve'
#     tick = args['a'][0]


def trade_limit_order(info, args):
    assert args['f'] == 'trade_limit_order'
    sender = info['sender']
    handle = handle_lookup(sender)
    addr = handle or sender

    tick_1 = args['a'][0]
    tick_2 = args['a'][2]
    assert set(tick_1) <= set(string.ascii_uppercase+'_')
    assert set(tick_2) <= set(string.ascii_uppercase+'_')
    assert tick_1 < tick_2
    pair = '%s_%s' % tuple([tick_1, tick_2])

    value_1 = int(args['a'][1])
    value_2 = int(args['a'][3])

    print('pair', pair, value_1, value_2)
    assert value_1 * value_2 < 0

    trade_sell_start = get('trade', 'sell_start', 1)
    trade_sell_end = get('trade', 'sell_end', 1)
    trade_buy_start = get('trade', 'buy_start', 1)
    trade_buy_end = get('trade', 'buy_end', 1)
    if value_1 < 0 and value_2 > 0:
        sender_balance = get(tick_1, 'balance', 0, addr)
        # print('tick_1 balance', sender_balance, value_1, sender_balance + value_1)
        sender_balance += value_1
        assert sender_balance >= 0
        put(addr, tick_1, 'balance', sender_balance, addr)

        trade_sell_no = trade_sell_start
        while True:
            sell = get('trade', f'{pair}_sell', None, str(trade_sell_no))
            # print('%s:%s'%(getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno), trade_sell_no, sell)
            if sell is None:
                put(addr, 'trade', f'{pair}_sell', [addr, value_1, value_2, None, None], str(trade_sell_end))
                trade_sell_end += 1
                put(addr, 'trade', 'sell_end', trade_sell_end)
                break
            else:
                # print('%s:%s'%(getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno), 'price', -sell[1] / sell[2])
                if (- value_1 / value_2) <= (- sell[1] / sell[2]):
                    prev_sell_id = sell[4]
                    put(addr, 'trade', f'{pair}_sell', [addr, value_1, value_2, trade_sell_no, prev_sell_id], str(trade_sell_end))
                    if prev_sell_id is None:
                        put(addr, 'trade', 'sell_start', trade_sell_end)
                    last_sell_id = trade_sell_end
                    trade_sell_end += 1
                    print('trade_sell_end', trade_sell_end)
                    put(addr, 'trade', 'sell_end', trade_sell_end)
                    print('trade_sell_no', trade_sell_no)

                    print('last_sell_id', last_sell_id)
                    sell[4] = last_sell_id
                    put(addr, 'trade', f'{pair}_sell', sell, str(trade_sell_no))
                    if prev_sell_id is not None:
                        print('prev_buy_id', prev_sell_id)
                        prev_sell = get('trade', f'{pair}_sell', None, str(prev_sell_id))
                        if prev_sell is not None:
                            prev_sell[3] = last_sell_id
                            put(addr, 'trade', f'{pair}_sell', prev_sell, str(prev_sell_id))
                    break

                if sell[3] is None:
                    put(addr, 'trade', f'{pair}_sell', [addr, value_1, value_2, None, trade_sell_no], str(trade_sell_end))
                    put(addr, 'trade', f'{pair}_sell', [sell[0], sell[1], sell[2], trade_sell_end, sell[4]], str(trade_sell_no))
                    print('trade_sell_end', trade_sell_end)
                    trade_sell_end += 1
                    put(addr, 'trade', 'sell_end', trade_sell_end)
                    break

                print('trade_sell_no', trade_sell_no)
                trade_sell_no = sell[3]

        # THIS IS FOR DEBUG
        trade_sell_no = 1
        while trade_sell_no != trade_sell_end:
            sell = get('trade', f'{pair}_sell', None, str(trade_sell_no))
            print(trade_sell_no, 'sell', sell)
            trade_sell_no += 1
            # if sell is None:
            #     continue

        trade_sell_start = get('trade', 'sell_start', 1)
        print('trade_sell_start', trade_sell_start)
        trade_sell_no = trade_sell_start
        while True:
            sell = get('trade', f'{pair}_sell', None, str(trade_sell_no))
            print('>', trade_sell_no, 'sell', sell)
            if sell is None or sell[3] is None:
                break
            trade_sell_no = sell[3]

    elif value_1 > 0 and value_2 < 0:
        sender_balance = get(tick_2, 'balance', 0, addr)
        # print('tick_2 balance', sender_balance, value_2, sender_balance + value_2)
        print('price', -value_1 / value_2)
        sender_balance += value_2
        assert sender_balance >= 0
        put(addr, tick_2, 'balance', sender_balance, addr)

        trade_buy_no = trade_buy_start
        while True:
            buy = get('trade', f'{pair}_buy', None, str(trade_buy_no))
            # print('%s:%s'%(getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno), trade_buy_no, buy)
            if buy is None:
                put(addr, 'trade', f'{pair}_buy', [addr, value_1, value_2, None, None], str(trade_buy_end))
                trade_buy_end += 1
                put(addr, 'trade', 'buy_end', trade_buy_end)
                break
            else:
                # print('%s:%s'%(getframeinfo(currentframe()).filename, getframeinfo(currentframe()).lineno), 'price', -buy[1] / buy[2])
                if (- value_1 / value_2) > (- buy[1] / buy[2]):
                    prev_buy_id = buy[4]
                    put(addr, 'trade', f'{pair}_buy', [addr, value_1, value_2, trade_buy_no, prev_buy_id], str(trade_buy_end))
                    if prev_buy_id is None:
                        put(addr, 'trade', 'buy_start', trade_buy_end)
                    last_buy_id = trade_buy_end
                    trade_buy_end += 1
                    # print('trade_buy_end', trade_buy_end)
                    put(addr, 'trade', 'buy_end', trade_buy_end)
                    # print('trade_buy_no', trade_buy_no)

                    # print('buy1', buy)
                    # print('last_buy_id', last_buy_id)
                    # print('this_buy_id', this_buy_id)
                    buy[4] = last_buy_id
                    put(addr, 'trade', f'{pair}_buy', buy, str(trade_buy_no))
                    if prev_buy_id is not None:
                        print('prev_buy_id', prev_buy_id)
                        prev_buy = get('trade', f'{pair}_buy', None, str(prev_buy_id))
                        # print('prev_buy', prev_buy)
                        if prev_buy is not None:
                            prev_buy[3] = last_buy_id
                            put(addr, 'trade', f'{pair}_buy', prev_buy, str(prev_buy_id))
                    break

                if buy[3] is None:
                    put(addr, 'trade', f'{pair}_buy', [addr, value_1, value_2, None, trade_buy_no], str(trade_buy_end))
                    put(addr, 'trade', f'{pair}_buy', [buy[0], buy[1], buy[2], trade_buy_end, buy[4]], str(trade_buy_no))
                    print('trade_buy_end', trade_buy_end)
                    trade_buy_end += 1
                    put(addr, 'trade', 'buy_end', trade_buy_end)
                    break

                print('trade_buy_no', trade_buy_no)
                trade_buy_no = buy[3]

        # THIS IS FOR DEBUG
        trade_buy_no = 1
        while trade_buy_no != trade_buy_end:
            buy = get('trade', f'{pair}_buy', None, str(trade_buy_no))
            print(trade_buy_no, 'buy', buy)
            trade_buy_no += 1
            # if buy is None:
            #     continue

        trade_buy_start = get('trade', 'buy_start', 1)
        print('trade_buy_start', trade_buy_start)
        trade_buy_no = trade_buy_start
        while True:
            buy = get('trade', f'{pair}_buy', None, str(trade_buy_no))
            print('>', trade_buy_no, 'buy', buy)
            if buy is None or buy[3] is None:
                break
            trade_buy_no = buy[3]

    K = 10**18
    sell_to_refund = []
    buy_to_refund = []

    sell_to_remove = set([])
    trade_sell_no = trade_sell_start
    while trade_sell_no != trade_sell_end:
        sell = get('trade', f'{pair}_sell', None, str(trade_sell_no))
        print('sell', sell)
        if not sell:
            trade_sell_no += 1
            continue

        sell_price = - sell[2] * K // sell[1]
        buy_to_remove = set([])

        trade_buy_no = trade_buy_start
        while trade_buy_no != trade_buy_end:
            buy = get('trade', f'{pair}_buy', None, str(trade_buy_no))
            print('buy', buy)
            if not buy:
                trade_buy_no += 1
                continue
            buy_price = - buy[2] * K // buy[1]
            if sell_price > buy_price:
                trade_buy_no += 1
                continue

            matched_price = (buy_price + sell_price) // 2
            dx = min(-sell[1], sell[2] * K // matched_price, buy[1])
            print('match price', -sell[1], sell[2] * K // matched_price, buy[1], -buy[2] // matched_price)
            print(dx, matched_price)
            sell[1] += dx
            sell[2] -= dx * matched_price // K

            buy[1] -= dx
            buy[2] += dx * matched_price // K

            sender_balance = get(tick_1, 'balance', 0, sell[0])
            # print('tick_1 balance', sender_balance, sender_balance + dx)
            sender_balance += dx
            assert sender_balance >= 0
            put(sell[0], tick_1, 'balance', sender_balance, sell[0])

            sender_balance = get(tick_2, 'balance', 0, buy[0])
            # print('tick_2 balance', sender_balance, sender_balance + dx * matched_price // K, dx * matched_price // K)
            sender_balance += dx * matched_price // K
            assert sender_balance >= 0
            put(buy[0], tick_2, 'balance', sender_balance, buy[0])

            if buy[1] == 0:
                buy_to_remove.add(trade_buy_no)

                if buy[2] != 0:
                    buy_to_refund.append(buy)

            trade_buy_no += 1

        for i in buy_to_remove:
            put('', 'trade', f'{pair}_buy', None, str(i))

        if sell[1] == 0:
            sell_to_remove.add(trade_sell_no)

            if sell[2] * K // matched_price == 0:
                sell_to_refund.append(sell)

        trade_sell_no += 1

    for i in sell_to_remove:
        put('', 'trade', f'{pair}_sell', None, str(i))

    for i in buy_to_refund:
        sender_balance = get(tick_2, 'balance', 0, i[0])
        print('tick_2 balance', sender_balance, sender_balance - i[2])
        sender_balance -= i[2]
        assert sender_balance >= 0
        put(i[0], tick_2, 'balance', sender_balance, i[0])

    for i in sell_to_refund:
        print('sell_to_refund', i)


def trade_market_order(info, args):
    assert args['f'] == 'trade_market_order'
    sender = info['sender']
    handle = handle_lookup(sender)

    tick_1 = args['a'][0]
    tick_2 = args['a'][2]
    assert set(tick_1) <= set(string.ascii_uppercase+'_')
    assert set(tick_2) <= set(string.ascii_uppercase+'_')
    assert tick_1 < tick_2
    pair = '%s_%s' % tuple([tick_1, tick_2])

    value_1 = args['a'][1]
    value_2 = args['a'][3]
    print('pair', pair, value_1, value_2)
    if value_2 is None:
        assert value_1 < 0
    elif value_1 is None:
        assert value_2 < 0

    trade_sell_start = get('trade', 'sell_start', 1)
    # trade_sell_end = get('trade', 'sell_end', 1)
    trade_buy_start = get('trade', 'buy_start', 1)
    # trade_buy_end = get('trade', 'buy_end', 1)

    K = 10**18
    if value_2 is None and value_1 < 0:
        sender_balance = get(tick_1, 'balance', 0, handle)
        # print('tick_1 balance', sender_balance, value_1, sender_balance + value_1)
        sender_balance += value_1
        assert sender_balance >= 0
        put(handle, tick_1, 'balance', sender_balance, handle) # consider delay put

        print('trade_buy_start', trade_buy_start)
        trade_buy_no = trade_buy_start
        while True:
            buy = get('trade', f'{pair}_buy', None, str(trade_buy_no))
            if buy is None:
                break
            print('>', trade_buy_no, 'buy', -buy[1]/buy[2], buy)

            price = - buy[2] * K // buy[1]
            print(price, buy)
            dx = min(buy[1], -buy[2] * K // price, -value_1)
            print('price', buy[1], -buy[2] * K // price, -value_1)
            buy[1] -= dx
            buy[2] += dx * price // K
            print('dx1', dx, buy)
            if buy[1] == 0 and buy[2] == 0:
                put('', 'trade', f'{pair}_buy', None, str(trade_buy_no))
                # TODO set trade_buy_start to buy[3]
                put('', 'trade', 'buy_start', buy[3])
            else:
                put('', 'trade', f'{pair}_buy', buy, str(trade_buy_no))

            sender_balance = get(tick_2, 'balance', 0, handle)
            # print('tick_2 balance2', sender_balance)
            sender_balance += dx * price // K
            assert sender_balance >= 0
            put(handle, tick_2, 'balance', sender_balance, handle)

            if buy[3] is None:
                break
            trade_buy_no = buy[3]

            value_1 += dx
            print('value_1', value_1)
            assert value_1 <= 0
            if value_1 == 0:
                print('value_1 break')
                break

        print(value_1)
        sender_balance = get(tick_1, 'balance', 0, handle)
        sender_balance -= value_1
        assert sender_balance >= 0
        put(handle, tick_1, 'balance', sender_balance, handle)

    elif value_1 is None and value_2 < 0:
        sender_balance = get(tick_2, 'balance', 0, handle)
        # print('tick_2 balance', sender_balance, value_2, sender_balance + value_2)
        sender_balance += value_2
        assert sender_balance >= 0
        put(handle, tick_2, 'balance', sender_balance, handle)

        print('trade_sell_start', trade_sell_start)
        trade_sell_no = trade_sell_start
        while True:
            sell = get('trade', f'{pair}_sell', None, str(trade_sell_no))
            if sell is None:
                break
            print('>', trade_sell_no, 'sell', -sell[1]/sell[2], sell)

            price = - sell[1] * K // sell[2]
            print(price, sell)
            dx = min(-sell[1], sell[2] * K // price, -value_2)
            # print('price', -sell[1], sell[2] * K // price, -value_2)
            sell[1] -= dx
            sell[2] += dx * price // K
            print('dx2', dx, sell)
            if sell[1] == 0 and sell[2] == 0:
                put('', 'trade', f'{pair}_sell', None, str(trade_sell_no))
                # TODO set trade_sell_start to sell[3]
            else:
                put('', 'trade', f'{pair}_sell', sell, str(trade_sell_no))

            sender_balance = get(tick_1, 'balance', 0, handle)
            # print('tick_1 balance', sender_balance)
            sender_balance += dx * price // K
            assert sender_balance >= 0
            put(handle, tick_1, 'balance', sender_balance, handle)

            if sell[3] is None:
                break
            trade_sell_no = sell[3]

            value_2 += dx
            # print(value_2)
            assert value_2 <= 0
            if value_2 == 0:
                # print('value_2 break')
                break

        sender_balance = get(tick_2, 'balance', 0, handle)
        sender_balance -= value_2
        assert sender_balance >= 0
        put(handle, tick_2, 'balance', sender_balance, handle)
