import random
import choose_verbs

def game_one(list_verb):
  pc_election = random.randint(1, 4)
  verb_number = random.randint(0,2)
  choose_verb = list_verb[verb_number]

  if pc_election == 1:
    answer = input('How do you say "' + choose_verb['Spanish verb'] + '" in English?: ')

  elif pc_election == 2:
    answer = input('How do you say "' + choose_verb['Verb'] + '" in Spanish?: ')

  elif pc_election == 3:
    answer = input('How do you say "' + choose_verb['Spanish verb'] + '" in English?:\na)' +
                   list_verb[0]['Verb'] + ' b)' + list_verb[1]['Verb'] + '  c)' +
                   list_verb[2]['Verb']+'\n')

  else:
    answer = input('How do you say "' + choose_verb['Verb'] + '" in Spanish?:\na)' +
                   list_verb[0]['Spanish verb'] + ' b)' + list_verb[1]['Spanish verb'] + '  c)' +
                   list_verb[2]['Spanish verb']+'\n')

  return answer, choose_verb

def game_two(list_verbs):
  pc_election = random.randint(1, 6)
  verb_number = random.randint(0,2)
  choose_verb = list_verbs[verb_number]

  if pc_election == 1:
    answer = input('How do you say "' + choose_verb['Verb'] + '" in past simple?: ')
  elif pc_election == 2:
    answer = input('How do you say "' + choose_verb['Verb'] + '" in past participle?: ')
  elif pc_election == 3:
    answer = input('How do you say "' + choose_verb['Past simple'] + '" in simple form?: ')
  elif pc_election == 4:
    answer = input('How do you say "' + choose_verb['Past simple'] + '" in past participle?: ')
  elif pc_election == 5:
    answer = input('How do you say "' + choose_verb['Past participle'] + '" in simple form?: ')
  else:
    answer = input('How do you say "' + choose_verb['Past participle'] + '" in past simple?: ')

  return answer, choose_verb

def run_game():
  list_verbs = choose_verbs.choose_verbs()
  randon_num = random.randint(0, 1)

  if randon_num == 0:
    answer, dict_verb = game_one(list_verbs)
  else:
    answer, dict_verb = game_two(list_verbs)

  return answer, dict_verb

if __name__ == '__main__':
  answer, dict_verb = run_game()
  print(answer, dict_verb)