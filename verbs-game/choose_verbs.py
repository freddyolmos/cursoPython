import random
import read_csv

def choose_list_verbs():
    random_num = random.randint(0,1)
    if random_num == 0:
        list_verbs = read_csv.read_csv('./reg-verbs.csv')
    else:
        list_verbs = read_csv.read_csv('./irreg-verbs.csv')
    return list_verbs


def make_list_verbs(list_verbs):
    new_list = []
    for i in range(3):
        new_list.append(random.choice(list_verbs))
    return new_list

def choose_verbs():
    list_verbs = choose_list_verbs()
    new_list = make_list_verbs(list_verbs)
    return new_list

if __name__ == "__main__":
    choose_verbs()