import string
import itertools
import time

password = '' # variable global para la contraseña

def try_guess(guess):
    global password
    return guess == password

def brute_force():
    lower = list(string.ascii_lowercase) # lista de todas las letras minusculas
    for num in range(1000): # recorre los numeros del 0 al 999
        for index in range(len(lower) ** 3): # recorre todas las combinaciones de 3 letras
            # letter_1 es la primera letra de la combinacion de derecha a izquierda
            letter_1 = lower[(index // (len(lower) ** 2)) % len(lower)] # obtiene la primera letra
            letter_2 = lower[(index // len(lower)) % len(lower)] # obtiene la segunda letra
            letter_3 = lower[index % len(lower)] # obtiene la tercera letra

            # Combina el numero con las letras obtenidas
            guess = f'{num:03d}{letter_1}{letter_2}{letter_3}' # genera la contraseña

            if try_guess(guess): # si la contraseña es igual a la contraseña que se busca
                print(f'Password is: \'{guess}\' found in {num * index} guesses')
                return guess # retorna la contraseña
    print('Password not found') # si no se encuentra la contraseña
    return None # retorna None

def time_function(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    print(f'Tiempo de ejecucion: {end - start:.4f}')

def main():
    global password
    password = input('Ingrese la contraseña: ')
    time_function(brute_force)

if __name__ == '__main__':
    main()