import time

def brute_force(password: str, pattern: str) -> str:
    """ Brute force algorithm to find the password
    Arguments:
        password: the password to find (str)
        pattern: pattern used to find the password (str)
                d - digit
                l - lowercase letter
    
    Returns:
        The number of iterations needed to find the password
        Password found


    Example:
        password = '15za1c'
        pattern = 'ddlldl'
        Returns: 2805428, '15za1c'
    """
    guess = '' # Start position of guess depending on the pattern if d is 0, l is a
    complexity = 1 # Complexity is calculated if d multiplies by 10 if l multiplies by 26 
    for c in pattern:
        if c == 'd':
            guess += '0'
            complexity *= 10
        elif c == 'l':
            guess += 'a'
            complexity *= 26

    print(f'Max number of iterations: {complexity}')

    for num in range(complexity):
        if guess == password:
            print(f'Password is: \'{guess}\' found in {num + 1} guesses')
            break
        else:
            guess = increase_guess_by_1(guess)
    return num, guess

def increase_guess_by_1(guess):
    # if is letter a then b then c ... z then a
    # if is digit 0 then 1 then 2 ... 9 then 0
    # e.g. '00bd34z' -> '00bd35a'

    carry = 1
    for index, pat in enumerate(reversed(guess)):
        if carry == 1:
            if pat == '9':
                guess = guess[:len(guess) - index - 1] + '0' + guess[len(guess) - index:]
            elif pat == 'z':
                guess = guess[:len(guess) - index - 1] + 'a' + guess[len(guess) - index:]
            else:
                # if i is a digit then add 1
                # if i is a letter then add 1 to the next letter
                guess = guess[:len(guess) - index - 1] + chr(ord(pat) + 1) + guess[len(guess) - index:]
                carry = 0
        else:
            break
    return guess



def main():
    password = '15za1c'
    start_time = time.perf_counter()
    brute_force(password, 'ddlldl')
    end_time = time.perf_counter()

    print(f'Time taken: {end_time - start_time:.2f} seconds')

if __name__ == '__main__':
    main()