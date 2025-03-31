import string

from space import put, get, handle_lookup

def token_mint_once(info, args):
    tick = args['a'][0]
    assert type(tick) is str
    assert len(tick) > 0 and len(tick) < 42
    assert tick[0] in string.ascii_uppercase
    assert set(tick) <= set(string.ascii_uppercase+string.digits+'_')

    value = int(args['a'][1])
    assert value > 0

    assert args['f'] == 'token_mint_once'
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

def token_mint(info, args):
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

def token_create(info, args):
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
    decemal = int(args['a'][2])
    assert type(decemal) is int
    assert decemal >= 0 and decemal <= 18

    functions = ['transfer', 'approve', 'transfer_from', 'token_mint_once', 'asset_update_ownership', 'asset_update_functions']
    put(addr, tick, 'name', name)
    put(addr, tick, 'decemal', decemal)
    put(addr, 'asset', 'functions', functions, tick)

def transfer(info, args):
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

def asset_create(info, args):
    assert args['f'] == 'asset_create'
    sender = info['sender']
    tick = args['a'][0]
    assert type(tick) is str
    assert len(tick) > 0 and len(tick) < 42
    assert tick[0] in string.ascii_uppercase
    assert set(tick) <= set(string.ascii_uppercase+string.digits+'_')
    handle = handle_lookup(sender)
    addr = handle or sender
    print('handle', handle, 'addr', addr, 'sender', sender)
    owner = get('asset', 'owner', None, tick)
    print(owner, addr)
    assert not owner

    put(addr, 'asset', 'owner', addr, tick)
    put(addr, 'asset', 'functions', ['asset_update_ownership', 'asset_update_functions'], tick)

def asset_update_ownership(info, args):
    assert args['f'] == 'asset_update_ownership'
    sender = info['sender']
    tick = args['a'][0]
    receiver = args['a'][1]
    assert type(tick) is str
    assert len(tick) > 0 and len(tick) < 42
    assert tick[0] in string.ascii_uppercase
    assert set(tick) <= set(string.ascii_uppercase+string.digits+'_')
    print('sender', sender)
    handle = handle_lookup(sender)
    print('handle', handle)
    addr = handle or sender

    owner = get('asset', 'owner', None, tick)
    print( owner, addr)
    assert owner == addr
    functions = get('asset', 'functions', None, tick)
    assert type(functions) is list
    assert functions
    put(receiver, 'asset', 'owner', receiver, tick)
    put(receiver, 'asset', 'functions', functions, tick)

def asset_update_functions(info, args):
    assert args['f'] == 'asset_update_functions'
    sender = info['sender']
    handle = handle_lookup(sender)
    print('handle', handle)

    tick = args['a'][0]
    assert type(tick) is str
    assert len(tick) > 0 and len(tick) < 42
    assert tick[0] in string.ascii_uppercase
    assert set(tick) <= set(string.ascii_uppercase+string.digits+'_')

    functions = args['a'][1]
    assert type(functions) is list
    assert functions
