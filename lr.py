import sys

def replace_substrings(input_string):
    output_string = input_string.replace("PA", "R").replace("MA", "L")
    return output_string

# Read input from stdin
input_data = sys.stdin.read()

# Call the function to replace substrings
output_data = replace_substrings(input_data)

# Print the modified output
print(output_data)

