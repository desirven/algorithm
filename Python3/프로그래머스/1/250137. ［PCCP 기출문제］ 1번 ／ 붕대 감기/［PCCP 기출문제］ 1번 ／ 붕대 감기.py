def solution(bandage, max_health, attacks):
    tick = 0
    health = max_health
    while len(attacks)>0:
        healAmount = [bandage[1]] * bandage[0]
        healAmount[-1] += bandage[2]
        while len(healAmount)>0:
            tick += 1
            if tick == attacks[0][0]:
                health -= attacks[0][1]
                attacks.pop(0)
                if health <= 0:
                    return -1
                break
            else:
                health += healAmount.pop(0)
                health = min(health, max_health)
            
    return health