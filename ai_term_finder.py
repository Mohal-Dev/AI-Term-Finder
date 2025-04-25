# ai_term_finder.py

# Print a welcome message for the user
print(" Welcome to the AI Term Finder!")
print("Type any sentence and I will find AI-related terms in it.\n")

# A list of basic AI-related terms that we want to detect
ai_terms = ["artificial intelligence", 
    "machine learning", 
    "deep learning", 
    "neural network", 
    "algorithm", 
    "data", 
    "model", 
    "training", 
    "ai"]

# Ask the user to enter a sentence
user_input = input("Enter a sentence: ").lower()
  # And .lower() is used to convert input to lowercase for easy matching



# Use list comprehension to find which AI terms are present in the user's sentence
found_terms = []
for term in ai_terms:
    if term in user_input:
        found_terms.append(term)

# Display the result based on what terms were found
if found_terms:
    print("\n AI-related terms found in your sentence:")
    for term in found_terms:
        print(f" - {term}")  # Print each found term
else:
    print("\n No AI-related terms found. Try again with another sentence!")
