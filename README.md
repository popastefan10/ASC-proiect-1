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
  
