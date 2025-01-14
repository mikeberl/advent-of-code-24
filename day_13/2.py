# Find cheapest option to complete the game 
# 2 buttons to click, every botton with a different value and cost to click, a sum has to be reached by combining the 2 buttons
# 10000000000000 added to the sum to reach, solved with z3 solver to minimize the costs in reasonable time

import z3

def solve_with_z3(game_data):
    results = []
    
    for game in game_data:
        optimizer = z3.Optimize()
        
        # btn var
        a = z3.Int('a')
        b = z3.Int('b')
        
        prize_x = game['Prize']['x']
        prize_y = game['Prize']['y']
        button_a_dx = game['ButtonA']['dx']
        button_a_dy = game['ButtonA']['dy']
        button_b_dx = game['ButtonB']['dx']
        button_b_dy = game['ButtonB']['dy']
        
        optimizer.add(
            a * button_a_dx + b * button_b_dx == prize_x,
            a * button_a_dy + b * button_b_dy == prize_y
        )

        cost = 3 * z3.If(a >= 0, a, -a) + z3.If(b >= 0, b, -b)
        optimizer.minimize(cost)
        
        if optimizer.check() == z3.sat:
            m = optimizer.model()
            results.append({
                'a': m.evaluate(a).as_long(),
                'b': m.evaluate(b).as_long(),
                'cost': m.evaluate(cost).as_long()
            })
        else:
            results.append(None)
    
    return results

def parse_game_data(filename):
    gameData = []
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        
        for i in range(0, len(lines), 3):
            button_a = lines[i].split(': ')[1].split(', ')
            button_b = lines[i+1].split(': ')[1].split(', ')
            prize = lines[i+2].split(': ')[1].split(', ')
            
            game_block = {
                "ButtonA": {
                    "dx": int(button_a[0].split('+')[1]), 
                    "dy": int(button_a[1].split('+')[1])
                },
                "ButtonB": {
                    "dx": int(button_b[0].split('+')[1]), 
                    "dy": int(button_b[1].split('+')[1])
                },
                "Prize": {
                    "x": 10000000000000 + int(prize[0].split('=')[1]), 
                    "y": 10000000000000 + int(prize[1].split('=')[1])
                }
            }
            
            gameData.append(game_block)
    
    return gameData

filename = "input.txt"

game_data = parse_game_data(filename)
results = solve_with_z3(game_data)

sum = 0
for result in results:
    if result:
        sum += result['cost']
print("Final result: ", sum)