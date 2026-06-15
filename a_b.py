# Dada uma string, consistendo apenas nos caracteres 'a' e 'b'
# Retorne verdadeiro se cada 'a' tiver um 'b' imediatamente à direita, e falso caso contrário.

string1 = "aabbb"
string2 = "abab"

if 'ba' in string1:
    print("A string 1 é falsa.")
else:
    print("A string 1 é verdadeira.")

if 'ba' in string2:
    print("A string 2 é falsa.")
else:    print("A string 2 é verdadeira.")