import random

# write 'hello world' to the console
print('hello world')

# agrega una lista de elementos rock, paper o scissors
choices = ['rock', 'paper', 'scissors']

# debes crear un juego en python de piedra papel o tijera, donde el usuario pueda elegir una opción y la computadora elija una opción aleatoria
user_choice = input('rock, paper, or scissors? ')
computer_choice = random.choice(choices)
# la consola debe informar si el usuario eligió una opción inválida
# el juego debe informar si ganó, perdió o empató
# el juego debe imprimir el resultado en la consola
# debe preguntar si quiere seguir jugando y al final cuando elijan que no debe imprimir el puntaje del usuario y el de la computadora
user_score = 0
computer_score = 0
while True:
  if user_choice not in choices:
    print('invalid choice')
  elif user_choice == computer_choice:
    print('tie')
  elif user_choice == 'rock' and computer_choice == 'scissors':
    print('you win')
    user_score += 1
  elif user_choice == 'paper' and computer_choice == 'rock':
    print('you win')
    user_score += 1
  elif user_choice == 'scissors' and computer_choice == 'paper':
    print('you win')
    user_score += 1
  else:
    print('you lose')
    computer_score += 1
  print(f'user: {user_score} computer: {computer_score}')
  if input('play again? ') == 'no':
    break
  user_choice = input('rock, paper, or scissors? ')
  computer_choice = random.choice(choices)
# el juego debe permitir jugar indefinidamente hasta que el usuario decida dejar de jugar
# el juego debe llevar un puntaje de cuántas veces ganó el usuario y cuántas veces ganó la computadora
# el juego debe preguntar si se quiere jugar de nuevo y reiniciar el puntaje si se elige que sí
# el juego debe imprimir el puntaje del usuario y de la computadora al final del juego
