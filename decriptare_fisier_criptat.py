# Intoarce perioada minima a sirului primit ca parametru
def perioada_minima(sir):
    lsir = len(sir)
    # prefix[i] = lungimea maxima a sufixului care se termina pe pozitia i si este prefix al sirului
    prefix = [0] * lsir

    # Calculez prefix cu KMP
    for i in range(1, lsir):
        crt = prefix[i - 1]
        while crt > 0 and sir[crt] != sir[i]:
            crt = prefix[crt - 1]

        if sir[crt] == sir[i]:
            crt += 1
        prefix[i] = crt

    return lsir - prefix[lsir - 1]

def main():
    # Format comanda: python encrypt.py cheiecriptare input.txt output
    # !!! input este fisier text si output este fisier binar

    with open("input.txt", "r") as input_file:
        sir = input_file.read()

    with open("output", "r") as output_file:
        sir_criptat = output_file.read()

    lsir = len(sir)
    lsir_criptat = len(sir_criptat)

    list_criptat = [0] * lsir
    temp = 0
    for i in range(lsir_criptat):
        if i % 8 == 0:
            list_criptat[i // 8 - 1] = (temp)
            temp = 0
        temp += pow(2, 7 - i % 8) * int(sir_criptat[i])

    output_list = list()
    for i in range(lsir):
        caracter_criptat = list_criptat[i]
        caracter_sir = ord( sir[i] )
        output_list.append(chr(caracter_criptat ^ caracter_sir))

    pmin = perioada_minima(output_list[:46])
    key = ''.join(output_list[:pmin])
    print(key)

    newFileBytes = bytearray(output_list)


    with open("key.txt", "wb") as output_file:
        output_file.write(newFileBytes)

if __name__ == '__main__':
    main()