def generate_fibonacci(n):
 
    if n <= 0:
        return []
    
  
    fibonacci_sequence = [0, 1]
    
   
    while True:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_value >= n:
            break
        fibonacci_sequence.append(next_value)
    
    return fibonacci_sequence


n = 16
fibonacci_sequence = generate_fibonacci(n)
print(fibonacci_sequence)
