import time

def fib(n):
    """Dado un entero n se retorna el enésimo numero en la serie de Fibonacci
    """
    #Se tiene un arreglo donde se almacenara los numeros de la serie
    #de tal forma que fibonacci_list[n] almacene F(n)
    fibonacci_list = [] 
    #Se almacenan los casos base F(0)=0 y F(1) = 1
    fibonacci_list.append(0) 
    fibonacci_list.append(1) 
    #Si el numero n es mayor que 2 entonce se calcula el F(n) por medio
    #de los dos ultimos numeros de la serie anteriores, que se almacenados en
    #en arreglo de forma iterativa.
    if( n >= 2): 
        for i in range (2, n+1): 
            #Se suman F(n-1) y F(n=2) y se añade a la lista 
            fibonacci_list.append(fibonacci_list[i-1]+fibonacci_list[i-2])
    #Se retorna el enesimo numero de Fibonacci.
    return fibonacci_list[n]

def fib_2(n):
    """Dado un entero n se retorna el enésimo numero en la serie de Fibonacci
    """
    a = 0 # Se crea el primer numero de la serie
    b = 1 # Se crea el segundo numero de la serie
    if n == 0: # Si el numero es 0 se retorna 0
        return a
    elif n == 1: # Si el numero es 1 se retorna 1
        return b
    else: # Si el numero es mayor que 1 se retorna la suma de los dos ultimos numeros de la serie
        for _ in range(2, n + 1):
            a, b = b, a + b # Se suman los dos ultimos numeros de la serie
        return b # Se retorna el numero n de la serie

def time_function(func, *args):
    start = time.perf_counter()
    print(func(*args))
    end = time.perf_counter()
    print(f'Tiempo de ejecucion: {end - start:.4f} segundos')

def main():
    while (n := int(input('Ingrese el numero n menor que 100: '))) <= 100 and n >= 0:
        time_function(fib, n)
        time_function(fib_2, n)

if __name__ == '__main__':
    main()