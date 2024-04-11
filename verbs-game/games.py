import random
import choose_verbs

def game_one(list_verb):
  pc_election = random.randint(1, 4)
  verb_number = random.randint(0,2)
  choose_verb = list_verb[verb_number]
  verb_english = choose_verb['Verb']
  verb_spanish = choose_verb['Spanish verb']
  if pc_election == 1:
    answer = input('How do you say "' + verb_spanish.title() + '" in English?: ')

  elif pc_election == 2:
    answer = input('How do you say "' + verb_english.title() + '" in Spanish?: ')

  elif pc_election == 3:
    answer = input('How do you say "' + verb_spanish.title() + '" in English?:\na)' +
                   list_verb[0]['Verb'] + ' b)' + list_verb[1]['Verb'] + '  c)' +
                   list_verb[2]['Verb']+'\n')

  else:
    answer = input('How do you say "' + verb_english.title() + '" in Spanish?:\na)' +
                   list_verb[0]['Spanish verb'] + ' b)' + list_verb[1]['Spanish verb'] + '  c)' +
                   list_verb[2]['Spanish verb']+'\n')

  return answer, verb_english, verb_spanish

list_verbs = choose_verbs.choose_verbs()

answers = game_one(list_verbs)

