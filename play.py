

import code
import readline
# import rlcompleter
import sys

from space import put, get, states, sender
import space
import funcs

def get_block_number():
    return len(space.states)

# Create custom namespace with imported functions
namespace = {
    'put': put,
    'get': get, 
    'states': states,
    'blocknumber': get_block_number,
    'sender': sender,
    'space': space,
    'funcs': funcs,
    '__name__': '__console__',
    '__doc__': None,
}

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
>>> put('alice', 'USDC', 'balance', 100)
>>> get('USDC', 'balance')
100
>>> states
[{'asset-balance': {'alice': 100}}]
""")
