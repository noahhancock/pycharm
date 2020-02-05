from rpg_hero import *
from Armor import *
def switch_turns(turn):
    if turn == 0:
        turn = 1
        not_turn = 0
    else:
        turn = 0
        not_turn = 1
    return turn, not_turn
players =[]

for i in range(2):
    print("Create player", i)
    player = Hero()
    players.append(player)

for i in players:
    i.pop_inv()
turn = 0
not_turn = 1
while players[0].alive:
    x = players[turn].Attack_turn()
    players[not_turn].defend(x)
    if players[1].alive:
        xp, item = players[1].Die()
        player = Hero()
        players[1] = player
        players[turn].add_exp(xp)
        players[turn].add_to_inv(item)
        turn, not_turn = switch_turns(turn)
