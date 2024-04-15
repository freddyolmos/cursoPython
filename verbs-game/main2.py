import verify_verbs

def run():
    round = 0
    cont = 0
    while True:
        for i in range(10):
            verify_verbs.verify_verbs()

        stop_button = input('Do you want to continue learning?(y/n):\n')
        if stop_button == 'y':
            continue
        else:
            print('See you later')
            break

if __name__ == '__main__' :
    run()