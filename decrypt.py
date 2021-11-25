import sys

def main():
    # Format comanda: python decrypt.py output cheiecriptare input_recuperat.txt
    # !!! output este un fisier binar, contine un text criptat
    # !!! input_recuperat este fisier text, in el scriem continutul fisierului output, dar decriptat
    input_filename = sys.argv[1]                    # Fisierul input care contine un text criptat
    password = sys.argv[2]                          # parola citita este salvata
    output_filename = sys.argv[3]                   # Fisierul output care va contine textul decriptat

    with open(input_filename, 'rb') as input_bin:
        sir_criptat = input_bin.read()              # codul binar este salvat intr-un sir de caractere

    lsir = len(sir_criptat)                         # lungimea parolei
    lpassword = len(password)                       # lungimea sirului criptat
    output_list = [0] * lsir                        # am initializat un vector pentru a stoca caracterele decriptate

    for i in range(lsir-1, -1, -1):                 # for-ul este de la lsir - 1 pana la 0 pentru a putea aduga elemente in vector cat mai convenabil pt afisare
        caracter_parola = ord(password[i % lpassword])
        caracter_sir = sir_criptat[i]
        output_list[i] = (caracter_parola ^ caracter_sir)

    newFileBytes = bytearray(output_list)

    with open(output_filename, 'wb') as input_recuperat:
        input_recuperat.write(newFileBytes)

if __name__ == '__main__':
    main()
