# ASC-proiect-1

## How to use

1. Fisiere
  
    * **input.txt**: contine textul care va fi criptat, este modificat de utilizator
    * **output**: va contine textul criptat, nu este modificat de utilizator
    * **input_recuperat.txt**: va contine textul din output decriptat, nu este modificat de utilizator
  
2. Rulare

   * Comanda criptare:
    
      ```bash
      python encrypt.py cheiecriptare input.txt output
      ```
      
   * Comanda decriptare:
     
      ```bash
      python decrypt.py input cheiecriptare output.txt
      ```
       
   * Exemplu:
     
      ```bash
      python encrypt.py parolamea2021 input.txt output
      python decrypt.py output parolamea2021 input_recuperat.txt
      ```
      
      Initial punem textul in _input.txt_. Cu prima comanda punem textul criptat in _output_ (fisier binar). Cu a doua comanda extragem textul din _output_,
      il decriptam si punem rezultatul in _input_recuperat.txt_.
  
## Continuare (prima parte)

Numele echipei noastre: _numeGeneric_

Numele echipei adverse: _Magnus Prafsen_

Cheia echipei adverse: _MagnusBlunder_

### Metoda de rezolvare

1. Ne folosim de urmatoarea proprietate a operatiei _xor_, pe care o vom nota in continuare cu ⊕:

   ```a ⊕ x ⊕ x = a```
   
   Procesul de criptare poate fi simplificat la formula:
   
   ```input ⊕ cheie_criptare = output_criptat```
   
   Prelucrand in continuare obtinem:
   
   ```input ⊕ input ⊕ cheie_criptare = input ⊕ output_criptat```
   
   ```cheie_criptare = input ⊕ output_criptat```
   
   Astfel, daca aplicam operatia ⊕ caracter cu caracter pe fisierele _input.txt_ si _output_ ale adversarilor vom obtine un sir de caractere in care avem cheia lor de criptare scrisa de foarte multe ori.

2. In acest moment cheia de criptare se poate vedea cu ochiul liber, dar se poate obtine si folosind algoritmul KMP pe sirul in care se gaseste cheia de criptare de multe ori. 
   Sirul acesta este periodic, deci daca gasim perioada minima a acestuia putem obtine si cheia de criptare. Fie _L_ lungimea sirului cu cheia de criptare; dupa ce calculam functia _prefix_ cu ajutorul KMP, perioada minima va fi ```T = L - prefix[L-1]``` (presupunem ca avem indexare de la 0). 
   In acest moment mai ramane sa aflam lungimea cheii de criptare, stiind ca este un multiplu al lui _T_ cuprins intre 10 si 15.
