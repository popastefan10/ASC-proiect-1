# Luam caracterele posibile din input si parola
# abcd123 -> poz 0
# bcg369  -> poz 10

def main():
    with open("fisier_criptat", "r") as output_file:
        sir_criptat = output_file.read()

    lsir_criptat = len(sir_criptat)
    list_criptat = [0] * (lsir_criptat // 8)
    temp = 0
    for i in range(lsir_criptat):
        if i % 8 == 0:
            list_criptat[i // 8 - 1] = (temp)
            temp = 0
        temp += pow(2, 7 - i % 8) * int(sir_criptat[i])

    caractere_parola = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    caractere_valide = caractere_parola + "`-=~!@#$%^&*()_+"
    caractere_valide += ",./;'[]\<>?:\"{}|"
    caractere_valide += "\n" + " " + "\t"

    print(list_criptat[130] ^ ord('M'))

    for l in range(13, 14):
        for start in range(0, 1):
            caractere_posibile = [c for c in caractere_parola]

            for poz in range(start, len(list_criptat), l):
                if len(caractere_posibile) > 0:
                    print(f'Before: poz: {poz}, l: {len(caractere_posibile)}')
                    print(''.join(caractere_posibile))
                aux = list()

                for caracter_posibil in caractere_posibile:
                    if chr(list_criptat[poz] ^ ord(caracter_posibil)) in caractere_valide:
                        # caracter_posibil este in continuare posibil
                        aux.append(caracter_posibil)
                
                caractere_posibile = aux
                if len(caractere_posibile) > 0:
                    print(f'After: poz: {poz}, l: {len(caractere_posibile)}')
                    print(''.join(caractere_posibile))
            
                # if len(caractere_posibile) > 0 and ''.join(caractere_posibile) in "MagnusBlunder":
                #     print(caractere_posibile)

            

if __name__ == '__main__':
    main()