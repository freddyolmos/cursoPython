import games
import logic_game

def run():
    round = 0
    cont = 0
    while True:
        for i in range(10):
            round += 1
            answer, correct_answer = games.run_game()
            verify = logic_game.game_logic(answer, correct_answer)
            if verify:
                cont += 1

        stop_button = input('Do you want to continue learning?(y/n):\n')
        if stop_button == 'y':
            continue
        else:
            print('Score: '+str(cont)+'/'+str(round)+'.\n\nGame over!')
            break

run()