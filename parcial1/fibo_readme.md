# Numeros de Fibonacci

La función `fib(n)` retorna el enesimo numero en la serie de Fibonacci:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89... para numeros menores que 100.

## Codigo

```python
   def fib(n):
    """Dado un entero n retorna el enésimo numero en la serie de Fibonacci
    """
    #Se tiene un arreglo donde se almacenara los numeros de la serie
    #de tal forma que fibonacci_list[n] almacene F(n)
    fibonacci_list = [] #O(1)
    #Se almacenan los casos base F(0)=0 y F(1) = 1
    fibonacci_list.append(0) #O(1)
    fibonacci_list.append(1) #O(1)
    #Si el numero n es mayor que 2 entonce se calcula el F(n) por medio
    #de los dos ultimos numeros de la serie anteriores, que se almacenados en
    #en arreglo de forma iterativa.
    if( n >= 2): #O(1)
        for i in range (2, n+1): #O(n)
            #Se suman F(n-1) y F(n=2) y se añade a la lista 
            fibonacci_list.append(fibonacci_list[i-1]+fibonacci_list[i-2]) #O(1)
    #Se retorna el numero de Fibonacci.
    return fibonacci_list[n]
```

## Complejidad

La función `fib(n)` comienza con la inicialización de una lista `fibonacci_list` que almacenará los números de la serie de Fibonacci. Esta inicialización tiene una complejidad constante O(1).
 
Luego se añaden dos elementos a la lista por medio del método `append`, cómo se añade al final de esta tiene una complejidad de O(1).
 
Se tiene un condicional que sólo se ejecuta una vez, `if( n >= 2): O(1)` con una complejidad de O(1)
 
Si la condición anterior se cumple, se llega a un bucle, `for i in range (2, n+1): O(n)` que corre desde 2 hasta n, es decir n-1 veces. Como depende de n y aumenta de forma lineal tiene una complejidad de O(n). Dentro de este bucle se tiene otro `append` a la lista `fibonacci_list`, esta línea tiene por sí sola una complejidad O(1) y tambien correra n-1 veces.
 
Finalmente se retorna un valor de la lista, complejidad O(1)
 
Así tenemos la ecuación
 
O(1)+O(1)+O(1)+O(1)+O(n)(O(1))+O(1) = O(n)
`fib(n)` tiene complejidad O(n)

## Funcionamiento

El script fibonacci.py recibe un entero menor que 100 desde la entrada estándar. 










