import sys

def main():
    # Format comanda: python encrypt.py cheiecriptare input.txt output
    # !!! input este fisier text si output este fisier binar
    key = sys.argv[1]               # Cheia de criptare
    input_filename = sys.argv[2]    # Fisierul de input, care contine textul initial
    output_filename = sys.argv[3]   # Fisierul de output, in care scriem continutul textului criptat

    with open(input_filename, "r") as input_file:
        sir = input_file.read()

    lsir = len(sir)
    lkey = len(key)
    output_list = list()
    for i in range(lsir):
        caracter_parola = ord( key[i % lkey] )
        caracter_sir = ord( sir[i] )
        output_list.append(caracter_parola ^ caracter_sir)

    newFileBytes = bytearray(output_list)

    with open(output_filename, "wb") as output_file:
        output_file.write(newFileBytes)

if __name__ == '__main__':
    main()
