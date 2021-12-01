# Metodo de biseccion de bolzano

## Funcionamiento

El codigo se ejecuta usando python este pedira

- la funcion a evaluar la cual se tiene que poner usando notacion de python es
    decir: La exponenciacion es `**` no se puede usar `^`

- x0 valor de inicio del intervalo

- x1 valor de fin del intervalo

- tol valor de la tolerancia aceptada para la resolucion

## Calculo de Complejidad

```python
def biseccion (function, a, b, ite = 0, max_ite = 100, tol = 0.001):
    c = (a + b)/2
    error = abs(b - a)

    print(f"{ite:^11}\t{a:>12.5f}\t{b:>12.5f}\t±{error:>12.5f}")

    if ite > max_ite:
        return f"El metodo no converge en {max_ite} iteraciones"

    if function(a)*function(b) > 0:
        print(f"\nNo hay raiz en el intervalo [{a}, {b}] ... ampliando el intervalo")

        a, b = a - (b - a)/2, b + (b - a)/2
        print(f"Intervalo: [{a}, {b}]\n")
        return biseccion(function, a, b, ite + 1, max_ite, tol)

    if error < tol:
        return c, error
    elif function(a) * function(c) < 0:
        return biseccion(function, a, c, ite + 1, max_ite, tol)
    else:
        return biseccion(function, c, b, ite + 1, max_ite, tol)
```
Tomemos n = max_ite, si la raíz no se encuentra en el intervalo la función biseccion es llamada n veces (hasta que ite = n sumándole 1 a ite en cada iteración), luego la complejidad es O(n). Sea m = error, si la raíz se encuentra en el intervalo m es dividido entre 2 cada vez que llamamos la función, luego la complejidad es O(log(m)).

## Output del programa

![image](https://user-images.githubusercontent.com/31489991/144049015-d410ca80-c5f8-4454-b32c-81ab8d0ffb87.png)
