import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    expr = str(left) + " " + operator + " " + str(right) 
    answer = eval(expr)
    return expr, answer

wrong = 0
print("Press enter to start!")
print("---------------------------")

start_time = time.time()

for i in range(TOTAL_PROLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input(f"\nProblem #{str(i+1)}:\n{expr} = ")
        if guess == str(answer):
            break
        wrong += 1
    
end_time = time.time()
total_time = end_time - start_time

print("---------------------------")
print("Nice work!")
print(f"You finished all {TOTAL_PROLEMS} in {total_time:.2f} time!")





















