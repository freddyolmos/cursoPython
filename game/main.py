import random

user_lifes = 3
computer_lifes = 3

print(
    'Piedra papel o tijera. Presiona:\n1 para Piedra\n2 para Papel\n3 para Tijera\n\n'
)


def choose_option():
  options = ('Piedra', 'Papel', 'Tijera')

  user_option = (input('Elige tu tiro: '))
  #if not (user_option == '1' or user_option == '2' or user_option == '3'):
  #print('No es una opcion correcta. Vuelva a intentar...')

  user_option = int(user_option)

  print('Has elegido ' + options[user_option - 1])

  computer_option = random.randint(1, 3)

  print('PC ha elegido: ' + options[computer_option - 1])

  return user_option, computer_option


def game(user_option, computer_option, user_lifes, computer_lifes):
  if user_option == computer_option:
    print('Empate')
  elif user_option == 1 and computer_option == 3:
    print('Has ganado')
    computer_lifes -= 1
  elif user_option == 2 and computer_option == 1:
    print('Has ganado')
    computer_lifes -= 1
  elif user_option == 3 and computer_option == 2:
    print('Has ganado')
    computer_lifes -= 1
  else:
    print('Has perdido')
    user_lifes -= 1

  return user_lifes, computer_lifes


while True:
  print('Vidas jugador: ' + str(user_lifes) + '   Vidas PC: ' +
        str(computer_lifes))

  user_option, computer_option = choose_option()
  user_lifes, computer_lifes = game(user_option, computer_option, user_lifes,
                                    computer_lifes)

  if user_lifes == 0:
    print('Perdiste!!')
    break

  if computer_lifes == 0:
    print('Ganaste!!')
    break
