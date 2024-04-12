import random
import choose_verbs

def game_one(list_verb):
  pc_election = random.randint(1, 4)
  verb_number = random.randint(0,2)
  choose_verb = list_verb[verb_number]

  if pc_election == 1:
    answer = input('How do you say "' + choose_verb['Spanish verb'] + '" in English?: ')
    correct_answer = choose_verb['Verb']

  elif pc_election == 2:
    answer = input('How do you say "' + choose_verb['Verb'] + '" in Spanish?: ')
    correct_answer = choose_verb['Spanish verb']

  elif pc_election == 3:
    answer = input('How do you say "' + choose_verb['Spanish verb'] + '" in English?:\na)' +
                   list_verb[0]['Verb'] + ' b)' + list_verb[1]['Verb'] + '  c)' +
                   list_verb[2]['Verb']+'\n')
    correct_answer = choose_verb['Verb']

  else:
    answer = input('How do you say "' + choose_verb['Verb'] + '" in Spanish?:\na)' +
                   list_verb[0]['Spanish verb'] + ' b)' + list_verb[1]['Spanish verb'] + '  c)' +
                   list_verb[2]['Spanish verb']+'\n')
    correct_answer = choose_verb['Spanish verb']

  answer = answer.lower()
  return answer, correct_answer

def game_two(list_verbs):
  pc_election = random.randint(1, 6)
  verb_number = random.randint(0,2)
  choose_verb = list_verbs[verb_number]

  if pc_election == 1:
    answer = input('How do you say "' + choose_verb['Verb'] + '"('+choose_verb['Spanish verb']+') in past simple?: ')
    correct_answer = choose_verb['Past simple']
  elif pc_election == 2:
    answer = input('How do you say "' + choose_verb['Verb'] + '"('+choose_verb['Spanish verb']+') in past participle?: ')
    correct_answer = choose_verb['Past participle']
  elif pc_election == 3:
    answer = input('How do you say "' + choose_verb['Past simple'] + '"('+choose_verb['Spanish verb']+') in simple form?: ')
    correct_answer = choose_verb['Verb']
  elif pc_election == 4:
    answer = input('How do you say "' + choose_verb['Past simple'] + '"('+choose_verb['Spanish verb']+') in past participle?: ')
    correct_answer = choose_verb['Past participle']
  elif pc_election == 5:
    answer = input('How do you say "' + choose_verb['Past participle'] + '"('+choose_verb['Spanish verb']+') in simple form?: ')
    correct_answer = choose_verb['Verb']
  else:
    answer = input('How do you say "' + choose_verb['Past participle'] + '"('+choose_verb['Spanish verb']+') in past simple?: ')
    correct_answer = choose_verb['Past simple']

  answer = answer.lower()
  return answer, correct_answer

def run_game():
  list_verbs = choose_verbs.choose_verbs()
  randon_num = random.randint(0, 1)

  if randon_num == 0:
    answer, correct_answer = game_one(list_verbs)
  else:
    answer, correct_answer = game_two(list_verbs)

  return answer, correct_answer

if __name__ == '__main__':
  answer, dict_verb = run_game()
  print(answer, dict_verb)