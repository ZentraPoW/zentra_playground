
states = [{}]

sender = None

def put(_owner, _asset, _var, _value, _key = None):
    global sender

    assert type(_var) is str
    if _key is not None:
        assert type(_key) is str
        var = '%s:%s' % (_var, _key)
    else:
        var = _var

    asset_name = _asset
    # addr = _owner.lower()
    k = '%s-%s' % (asset_name, var)
    state = states[-1]
    state[k] = _value

def get(_asset, _var, _default = None, _key = None):
    global sender
    global states

    asset_name = _asset
    value = _default
    assert type(_var) is str
    if _key is not None:
        assert type(_key) is str
        var = '%s:%s' % (_var, _key)
    else:
        var = _var

    k = '%s-%s' % (asset_name, var)
    state = states[-1]
    v = state.get(k)
    if v is not None:
        return v

    return value

def handle_lookup(_addr):
    return _addr

def nextblock():
    global states
    states.append({})
