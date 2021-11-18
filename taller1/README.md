# Encontrar substring en una cadena usando fuerza bruta

El codigo usado para resolver este problema es el siguiente:

```python
# O(1) + O(1) + O(1) + O(n) * [ O(m) * [ O(1) + O(1) + O(1) + O(1) + O(1) + O(1) ] ] + O(1)
# O(1) + O(1) + O(1) + O(n) * [ O(m) * [ O(1) ] ] + O(1)
# O(1) + O(1) + O(1) + O(n) * [ O(m) ] + O(1)
# O(n*m)
def fuerza_bruta(target, sequence):
    target_len = len(target) # O(1)
    sequence_len = len(sequence) # O(1)

    result = [] # O(1)
    for i in range(sequence_len - target_len + 1): # O(n)
        for j, _ in enumerate(target): # O(m)
            if (target[j] == sequence[i + j]): # O(1)
                if (j < target_len - 1): # O(1)
                    continue # O(1)
                result.append((i, i + target_len - 1)) # O(1)
                break # O(1)
            break # O(1)

    return result # O(1)
```

donde `target` es la cadena objetivo y `sequence` es la secuencia donde se busca.

para demostrar su complejidad de tiempo, se puede calcular la complejidad de tiempo de la siguiente manera:

Para empezar, nótese que las funciones `len(target)`, `len(sequence)`, la creación de la variable `result`, y `return` tienen complejidad O(1)

Ahora analicemos las funciones anidadas dentro de `for i in range(sequence_len - target_len + 1):` de adentro hacia afuera:

Todo `if` tiene complejidad O(1)

Como `continue` tiene complejidad O(1) e `if (j < target_len - 1):` tiene complejidad O(1) * O(1) = O(1),

la función `.append()` tiene complejidad O(1), luego `result.append((i, i + target_len - 1))` tiene complejidad O(1),

todo `break` tiene complejidad O(1),

Por lo anterior `if (target[j] == sequence[i + j]):` tiene complejidad O(1) * O(1) * O(1) * O(1) = O(1).

Todo `for` tiene complejidad O(n),

Como el tiempo de ejecución del ciclo `for j, _ in enumerate(target):` depende del numero m de caracteres de la subcadena `target` y no del numero de caracteres n de la cadena `sequence`, se dice que una complejidad O(m) * O(1) * O(1) = O(m).  

Así, `for i in range(sequence_len - target_len + 1):` tiene por si solo una complejidad O(n), con n siendo la cantidad de caracteres de la cadena `sequence` que recorre. Multiplicandose por la complejidad de su cuerpo se tiene una complejidad O(n) * O(m) = O(n*m)

De modo que la función `fuerza_bruta()` tiene complejidad O(1) + O(1) + O(1) + O(n*m) + O(1) = O(n*m). 