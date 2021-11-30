import time

# Metodo de Bolzano para encontrar raices de funciones
def biseccion (function, a, b, ite = 0, max_ite = 100, tol = 0.001):
    c = (a + b)/2 # Calcula punto medio
    error = abs(b - a) # Calcula error

    # Imprime una tabla con los valores de # de iteracion, a, b, error
    print(f"{ite:^11}\t{a:>12.5f}\t{b:>12.5f}\t±{error:>12.5f}")

    # si excede el numero maximo de iteraciones
    if ite > max_ite:
        return f"El metodo no converge en {max_ite} iteraciones"

    # Si f(a) y f(b) son del mismo signo --- No existe raiz
    if function(a)*function(b) > 0:
        print(f"\nNo hay raiz en el intervalo [{a}, {b}] ... ampliando el intervalo")
        # Amplia el intervalo en ambas direcciones la mitad de la diferencia
        a, b = a - (b - a)/2, b + (b - a)/2
        print(f"Intervalo: [{a}, {b}]\n")
        return biseccion(function, a, b, ite + 1, max_ite, tol)

    # Si la tolerancia es menor que el error
    if error < tol:
        return c, error # Retorna el punto medio y el error
    elif function(a) * function(c) < 0: # Si la funcion en el punto medio es menor que cero
        return biseccion(function, a, c, ite + 1, max_ite, tol) # Llamada recursiva con el intervalo [a, c]
    else:
        return biseccion(function, c, b, ite + 1, max_ite, tol) # Llamada recursiva con el intervalo [c, b]

def time_it(function, *args):
    start = time.perf_counter()
    result = function(*args)
    end = time.perf_counter()
    return result, end - start

def main():
    # function = lambda x:-x**4 + 30*(x**3) + 15*(x**2) + 34*x + 540
    # x0 = 0, x1 = 1000, tol=0.001
    # Declaracion de la funcion del modelo
    function_str = input("Ingrese la funcion con notacion de python: \n\tf(x) = ")
    function = lambda x: eval(function_str)
    x0 = float(input("Ingrese el valor inicial del intervalo: \n\tx0 = "))
    x1 = float(input("Ingrese el valor final del intervalo: \n\tx1 = "))
    tol = float(input("Ingrese la tolerancia de la resolucion \n\ttol = "))

    # Comienzo del intervalo
    print(f"\nEvaluando f(x): {function_str} en el intervalo [{x0}, {x1}]\n")
    print(f"{'Iteracion':^11}\t{'a':^12}\t{'b':^12}\t {'Error':^12}")
    print(f"{'-'*11}\t{'-'*12}\t{'-'*12}\t {'-'*12}")
    result, time_taken = time_it(biseccion, function, x0, x1, 0, 100, tol)
    print(f"\nRaiz: {result[0]:.5f} ± {result[1]:.5f}")
    print(f"Tiempo de ejecucion: {time_taken:.5f} segundos")

if __name__ == "__main__":
    main()
