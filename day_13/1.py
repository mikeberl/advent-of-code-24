# Find cheapest option to complete the game 
# 2 buttons to click, every botton with a different value and cost to click, a sum has to be reached by combining the 2 buttons

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
                    "x": int(prize[0].split('=')[1]), 
                    "y": int(prize[1].split('=')[1])
                }
            }
            
            gameData.append(game_block)
    
    return gameData

def find_prize_combinations(game_data):
    results = []
    
    for game_index, game in enumerate(game_data, 1):
        prize_x, prize_y = game['Prize']['x'], game['Prize']['y']
        
        button_a_dx, button_a_dy = game['ButtonA']['dx'], game['ButtonA']['dy']
        button_b_dx, button_b_dy = game['ButtonB']['dx'], game['ButtonB']['dy']
        
        valid_combinations = []
        
        for a in range(101):
            for b in range(101):
                final_x = a * button_a_dx + b * button_b_dx
                final_y = a * button_a_dy + b * button_b_dy
                
                if final_x == prize_x and final_y == prize_y:
                    total_cost = a * 3 + b * 1
                    
                    valid_combinations.append({
                        'button_a_presses': a,
                        'button_b_presses': b,
                        'total_cost': total_cost
                    })
        
        if valid_combinations:
            cheapest = min(valid_combinations, key=lambda x: x['total_cost'])
            results.append({
                'game': game_index,
                'valid_combinations': valid_combinations,
                'cheapest_option': cheapest
            })
        else:
            results.append({
                'game': game_index,
                'valid_combinations': [],
                'cheapest_option': None
            })
    
    return results



filename = "input.txt"

game_data = parse_game_data(filename)
results = find_prize_combinations(game_data)

sum = 0
for result in results:
    print(f"\nGame {result['game']}:")
    if result['cheapest_option']:
        sum += result['cheapest_option']['total_cost']
print("Final result: ", sum)