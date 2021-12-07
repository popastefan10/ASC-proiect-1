def sir_bin_to_bin(sir_criptat):
    # Transforma un sir de caractere 0 si 1 intr-un sir binar
    lsir_criptat = len(sir_criptat)
    list_criptat = [0] * (lsir_criptat // 8)

    temp = 0
    for i in range(lsir_criptat):
        if i % 8 == 0:
            list_criptat[i // 8 - 1] = (temp)
            temp = 0
        temp += pow(2, 7 - i % 8) * int(sir_criptat[i])

    return list_criptat


def main():
    # Citire dintr-un fisier cu caractere 0 si 1
    with open("fisier_criptat", "r") as output_file:
        sir_criptat = output_file.read()
    list_criptat = sir_bin_to_bin(sir_criptat)

    # Citire dintr-un fisier binar
    # output_bin_filename = "output"
    # with open(output_bin_filename, "rb") as output_file:
    #     list_criptat = output_file.read()
    
    # Caracterele care pot sa apara in parola
    caractere_parola = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # Caracterele care pot sa apara in input
    caractere_valide = caractere_parola + "-=~!@#$%^&*()_+"
    caractere_valide += ",./;'[]\<>?:\"{}|"
    caractere_valide += "\n" + " " + "\t"

    # Fixam lungimea posibila a parolei
    for l in range(10, 16):
        caractere_posibile_parola = []

        # Fixam pozitia caracterului din parola cu care facem verificarea
        for start in range(l):
            caractere_posibile = [c for c in caractere_parola]

            # Parcurg tot fisierul din l in l
            for poz in range(start, len(list_criptat), l):
                aux = list() # Lista cu noile caractere posibile

                for caracter_posibil in caractere_posibile:
                    if chr(list_criptat[poz] ^ ord(caracter_posibil)) in caractere_valide:
                        # caracter_posibil este in continuare posibil
                        aux.append(caracter_posibil)
                
                caractere_posibile = aux
            
            if len(caractere_posibile) > 0:
                caractere_posibile_parola.append(caractere_posibile)

        # Numarul de pozitii din parola cu caractere posibile trebuie sa fie egal cu lungimea parolei
        if len(caractere_posibile_parola) == l:
            # Verificam daca parola este unica
            parola_unica = True
            for x in caractere_posibile_parola:
                if len(x) > 1:
                    parola_unica = False
            
            if not parola_unica:
                print(caractere_posibile_parola)
            else:
                print(''.join(''.join(x) for x in caractere_posibile_parola))
            

if __name__ == '__main__':
    main()