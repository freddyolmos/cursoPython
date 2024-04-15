import read_csv

reg_verbs = read_csv.read_csv('./reg-verbs.csv')
irreg_verbs = read_csv.read_csv('./irreg-verbs.csv')

def verify_verbs():

    valor_buscado = input('Write the verb: ')
    clave_buscada = "Verb"

    for diccionario in reg_verbs:
        if clave_buscada in diccionario and diccionario[clave_buscada] == valor_buscado:
            print('The verb ' +valor_buscado+ ' is regular')
            print(diccionario)
    else:
        print('The verb is not regular.')

    for diccionario in irreg_verbs:
        if clave_buscada in diccionario and diccionario[clave_buscada] == valor_buscado:
            print('The verb ' +valor_buscado+ ' is irregular')
            print(diccionario)
    else:
        print('The verb is not irregular.')
