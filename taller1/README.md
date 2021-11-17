# Encontrar substring en una cadena usando fuerza bruta

El codigo usado para resolver este problema es el siguiente:

```python
def fuerza_bruta(target, secuence):
    target_len = len(target)
    secuence_len = len(secuence)

    result = []
    # se itera sobre la secuecia (teniendo cuidado de no desbordarse)
    for i in range(secuence_len - target_len + 1):
        # se itera sobre la cadena objetivo
        for j, _ in enumerate(target): # j es el indice letter es la letra actual en target (target[j])
            if (target[j] == secuence[i + j]): # si la letra coincide con la secuencia sigue iterando la cadena objetivo
                continue
            break # si no coincide deja de iterar sobre la cadena objetivo

        if (j == target_len - 1): # si al finalizar la iteracion anterior se itero sobre toda la cadena entonces
            result.append(i, i + target_len - 1) # retorna el indice inicial y final donde se encuentra el objetivo
    
    return result # en caso tal que no se encuentre el objetivo en la secuencia retorna -1

pos_inicial, pos_final = fuerza_bruta(target, secuence)
```

donde target es la cadena objetivo y secuence es la secuencia donde se busca.

para demostrar su complejidad de tiempo, se puede calcular la complejidad de tiempo de la siguiente manera:

el tiempo de ejecucion de la funcion fuerza_bruta es O(n * m) donde n es la longitud de la secuencia y m es la longitud de la cadena objetivo