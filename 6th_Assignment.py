def generate_latin_square(n): 
    # Initialize an empty n x n matrix 
    matrix = [[0] * n for _ in range(n)] 
    
    # Fill the matrix with numbers from 1 to n following Latin Square rules
    for i in range(n): 
        for j in range(n): 
            matrix[i][j] = (i + j) % n + 1  # Ensures each number appears once per row and column
    
    return matrix 

def print_matrix(matrix): 
    for row in matrix: 
        print(" ".join(map(str, row)))  # Convert each number to string and join with space

# Input value for n 
n = int(input("Enter the value of n: ")) 

# Generate the n x n matrix 
matrix = generate_latin_square(n) 

# Print the matrix 
print("Generated Latin Square:")
print_matrix(matrix)