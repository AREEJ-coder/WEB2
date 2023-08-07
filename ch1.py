# ===================================================FIRST TASK=============================================
def analyze_sentence(sentence):
    # Initialize counters
    word_count = 0
    vowel_count = 0
    
    # Define vowels
    vowels = "aeiouAEIOU"
    
    # Loop through each character in the sentence
    for char in sentence:
        if char == ' ':
            word_count += 1
        elif char in vowels:
            vowel_count += 1
    
    # Increment word_count for the last word (after the last space)
    word_count += 1
    
    # Display results
    print("Number of words:", word_count)
    print("Number of vowels:", vowel_count)

# Example sentence
sentence = input("Enter a sentence: ")

# Call the function to analyze the sentence
analyze_sentence(sentence)
# ===================================================SECOND TASK=============================================
def sum_of_distinct_elements(set1, set2):
    # Initialize sum
    sum = 0
    
    # Combine both sets
    combined_set = set1 + set2
    
    # Find distinct elements and add them to sum
    for element in combined_set:
        if element not in set1 or element not in set2:
            sum += element
    
    return sum

# Example sets
set1 = [3, 1, 7, 9]
set2 = [2, 4, 1, 9, 3]

# Call the function to calculate sum of distinct elements
result = sum_of_distinct_elements(set1, set2)
print("Sum of distinct elements:", result)