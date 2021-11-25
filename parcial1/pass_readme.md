# Adivinador de contraseñas usando fuerza bruta

# Resumen

La funcion `brute_force()` realiza todas las posibles combinaciones de
contraseña con el patron de "dígito-dígito-digito-letra-letra-letra" y se
detiene cuando encuentra el password




```python
def brute_force():
    lower = list(string.ascii_lowercase)
    for num in range(1000): # O(n)
        for index in range(len(lower) ** 3): # O(m)
            letter_1 = lower[(index // (len(lower) ** 2)) % len(lower)] # O(1)
            letter_2 = lower[(index // len(lower)) % len(lower)] # O(1)
            letter_3 = lower[index % len(lower)] # O(1)
            guess = f'{num:03d}{letter_1}{letter_2}{letter_3}' # O(1)
            if try_guess(guess): # O(1)
                print(f'Password is: \'{guess}\' found in {num * index} guesses') # O(1)
                return guess # O(1)
    print('Password not found') # O(1)
    return None # O(1)
```


Dada una contraseña del formato _dígito-dígito-digito-letra-letra-letra_ nótese
que hay:

- 10 posibilidades para cada dígito

- 26 posibilidades para cada letra.

Así, hay 10^3 posibles combinaciones para 3 dígitos y 26^3 posibles
combinaciones para 3 letras.

En orden lexicográfico, supongamos que la n-esima combinación de dígitos y la
m-esima combinación de letras son las correctas.

Para encontrar las letras correctas:

- el ciclo `for` externo habrá iterado m veces, para encontrar los dígitos
  correctos el ciclo `for` interno habrá iterado n veces y por cada iteración
  el ciclo `for` en la línea 10 habrá iterado 26^3 veces, es decir, el programa
  habrá iterado `(n - 1) * 26 ** 3` veces para llegar a evaluar las opciones de
  contraseña que contengan la secuencia de dígitos correcta.

Una vez teniendo la secuencia de dígitos n, se va a proceder a evaluar esta
junto con todas las combinaciones de letras cuya posición en el orden sea menor
a m, y por último se evaluará m, es decir, el ciclo `for` externo habrá iterado
m veces.  Así, en total el programa habrá iterado `(n - 1) * 26 ** 3 + m` veces
para encontrar la contraseña.

Ahora, en el peor de los casos la contraseña contiene la combinación de dígitos
y la combinación de letras correspondientes al último puesto en sus respectivos
ordenes lexicográficos, esto es: '999zzz', que corresponden a las combinaciones
número `10 ** 3 = 100` y `26 ** 3 = 17576` respectivamente.

Entonces, el programa tendrá que iterar `(1000 - 1) * 26 ** 3 + 26 ** 3 = (10
** 3) * (26 ** 3)`

Así, a complejidad de este algoritmo es `O((10 ** 3) * (26 ** 3))` o `O(n * m)`
