import random
def pick_lotto():
    pick_num = random.sample(range(1,46), 6)
    return pick_num

print(pick_lotto())
