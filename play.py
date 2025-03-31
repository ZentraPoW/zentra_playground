

import code
import readline
# import rlcompleter
import sys

from space import put, get, states, sender
import space
import funcs

class NamedFunction:
    def __init__(self, f, name):
        self.f = f
        self.name = name

    def __call__(self, *args):
        a = list(args)
        r = self.f({'sender': 'alice'}, {'p': 'zen', 'a': a, 'f': self.name})
        space.nextblock()
        return r

    def __str__(self):
        return self.f.__str__()

    def __repr__(self):
        return self.f.__repr__()

def get_block_number():
    return len(space.states)

# Create custom namespace with imported functions
namespace = {
    'put': put,
    'get': get, 
    'states': states,
    'blocknumber': get_block_number,
    'nextblock': space.nextblock,
    'sender': sender,
    'accounts': [],
    'a': [],
    '__name__': '__console__',
    '__doc__': None,
}

funcs_built = {'__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'string', 'put', 'get', 'handle_lookup'}
for func in dir(funcs):
    if func not in funcs_built:
        # print(type(func), funcs.__dict__[func])
        f = NamedFunction(funcs.__dict__[func], func)
        namespace[func] = f

# Enable tab completion
readline.parse_and_bind("tab: complete")

# Create and start interactive console
console = code.InteractiveConsole(namespace)
console.interact(banner="""
Zentra Interactive python console
Available commands:
- put(owner, asset, var, value, key=None)  # Store state
- get(asset, var, default=None, key=None)  # Get state
- blocknumber()  # Current block number
- states  # View all states
- sender  # Current sender

Example:
>>> put('alice', 'USDC', 'balance', 100, 'alice')
>>> get('USDC', 'balance', 0, 'alice')
100
>>> states
[{'asset-balance': {'alice': 100}}]
>>> nextblock()
>>> asset_create('USDC')
Ok, let's start!
""")
