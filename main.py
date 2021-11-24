# 1. Luam parametrii din linia de comanda
# 2. Citirea => str
#
#

def main():
    input_file = open("input.txt", "r")
    sir = input_file.read()
    key = "123"
    
    lsir = len(sir)
    lkey = len(key)
    output_list = list()
    for i in range(lsir):
        caracter_parola = ord( key[i % lkey] )
        caracter_sir = ord( sir[i] )
        output_list.append(caracter_parola ^ caracter_sir)

    newFileBytes = bytearray(output_list)

    newFile = open("output.bin", "wb")

    newFile.write(newFileBytes)

if __name__ == '__main__':
    main()