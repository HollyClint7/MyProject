# Prompt user for a file name
fileName = input("Enter the file name: ")
print("")
inputFile = open(fileName, "r")  # Open the file for reading
text = inputFile.read()  # Read the entire content of the file

words = text.split()
print(words)  # Split the text into words
print("")

# Sort the words alphabetically
sorted_words = sorted(words) 
for word in sorted_words:
    print(word)  # Print each word on a new line
print("")
print("Total number of words:", len(words))  # Print the total number of words

inputFile.close()  # Close the file
