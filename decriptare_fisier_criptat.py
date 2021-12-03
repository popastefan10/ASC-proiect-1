import sys

def main():
    with open(sys.argv[1], 'rb') as input_bin:
        sir_criptat = input_bin.read()              # codul binar este salvat intr-un sir de caractere

    password = sys.argv[2]                          # parola citita este salvata

    lsir = len(sir_criptat)
    lpassword = len(password)
    output_list = [0] * lsir

    for i in range(lsir-1, -1, -1):
        caracter_parola = ord(password[i % lpassword])
        caracter_sir = ord(sir_criptat[i])
        output_list[i] = (caracter_parola ^ caracter_sir)

    newFileBytes = bytearray(output_list)

    with open(sys.argv[3], 'wb') as input_recuperat:
        input_recuperat.write(newFileBytes)

if __name__ == '__main__':
    main()