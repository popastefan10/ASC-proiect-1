import sys

def main():
    with open(sys.argv[2], "r") as input_file:
        sir = input_file.read()
    key = sys.argv[1]
    
    lsir = len(sir)
    lkey = len(key)
    output_list = list()
    for i in range(lsir):
        caracter_parola = ord( key[i % lkey] )
        caracter_sir = ord( sir[i] )
        output_list.append(caracter_parola ^ caracter_sir)

    newFileBytes = bytearray(output_list)

    with open(sys.argv[3], "wb") as output:
        output.write(newFileBytes)

if __name__ == '__main__':
    main()