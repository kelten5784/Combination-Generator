from itertools import permutations
import pyautogui

def combine_all(words, f):
    # Generate permutations of the given words
    perm = permutations(words)
    
    # Iterate through each permutation
    for p in perm:
        # Combine the words in the permutation
        strc = ''.join(p)
        # Remove spaces from the combined string
        strc = strc.replace(" ", "")
        
        # Output the combined string to the console
        print(strc)
        
        # Write the combined string to the CSV file
        f.write(strc + "\n")
        
        # Simulate typing the combined string using pyautogui
        pyautogui.typewrite(strc)
        pyautogui.typewrite('\n')

def word_to_combine_all(string):
    # Remove spaces from the input string and split it into a list of words
    words = string.replace(" ", "").split(',')
    ct1 = len(words)  # Get the number of words in the list
    
    # Open the CSV file for appending
    with open("combination.csv", "a") as f:
        # Iterate through each word in the list
        for a in range(ct1):
            first = words[a]
            
            # Combine the current word with all subsequent words
            combine_all([first], f)
            
            for b in range(a + 1, ct1):
                second = words[b]
                combine_all([first, second], f)
                
                for c in range(b + 1, ct1):
                    third = words[c]
                    combine_all([first, second, third], f)
                    
                    for d in range(c + 1, ct1):
                        fourth = words[d]
                        combine_all([first, second, third, fourth], f)
                        
                        if ct1 > 3:
                            for e in range(d + 1, ct1):
                                fifth = words[e]
                                combine_all([first, second, third, fourth, fifth], f)

if __name__ == "__main__":
    # Replace with your input string
    input_string = "435345345,something,l,765,$"
    
    # Call the main function to generate combinations
    word_to_combine_all(input_string)

