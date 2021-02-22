# Euclid's algorithm
def gcd(a,b):
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
# Function to return LCM of two numbers 
def lcm(a,b): 
    return (a * b) / gcd(a,b)

def reduce_(a,b):
    #FIXME: Finish this
    

    return a, b

def addition(num_1, num_2, denom_1, denom_2):
    denom_done = int(lcm(denom_1, denom_2))
    num_done = int((num_1 * (denom_done / denom_1)) + (num_2 * (denom_done / denom_2)))
    num_reduce, denom_reduce = reduce_(num_done, denom_done)
    return '{}/{}'.format(num_reduce, denom_reduce)


def subtraction(num_1, num_2, denom_1, denom_2):
    print('subtraction')
# FIXME: 


def multiplication(num_1, num_2, denom_1, denom_2):
    print('multiplication')
# FIXME: 


def division(num_1, num_2, denom_1, denom_2):
    print('division')
# FIXME: 




user_input = input("Enter a fraction calculation (operators: + - * /)(Format: x/y + a/b)\n")

operator = list(user_input.split())[1]

# Each variable as integers
num_1 = int(list(user_input.split())[0].split('/').pop(0))
num_2 = int(list(user_input.split())[2].split('/').pop(0))
denom_1 = int(list(user_input.split())[0].split('/').pop())
denom_2 = int(list(user_input.split())[2].split('/').pop())

if operator == '+':
    sum = addition(num_1, num_2, denom_1, denom_2)
    
    print(sum) #FIXME: CONVERT FRACTIONS TO MIXED NUMBERS
elif operator == '-':
    subtraction(num_1, num_2, denom_1, denom_2)
elif operator == '*':
    multiplication(num_1, num_2, denom_1, denom_2)
elif operator == '/':
    division(num_1, num_2, denom_1, denom_2)
else:
    print("Error. Invalid operator.")