"""
THIS IS NOT THREAD SAFE
"""

import random

buttons = ['up', 'down', 'left', 'right', \
           'start', 'select', 'a', 'b']

combo_store = dict()
max_tries = 30
combo_length = 3

def create_one(length):
    combo = list()

    for i in range(length):
        combo.append(random.sample(buttons,1)[0])

    return '-'.join(combo)

def create_unique():
    global combo_length
    
    combo = None
    
    tries = 0
    while True:
        if tries == max_tries:
            combo_length += 1
            tries = 0
                
        combo = create_one(combo_length)

        tries += 1

        if not has(combo):
            break

    return combo
        
def has(combo):
    return combo in combo_store
    
def link_for(combo):
    return combo_store[combo]
    
def add_link(link, combo):
    global combo_store
    combo_store[combo] = link
