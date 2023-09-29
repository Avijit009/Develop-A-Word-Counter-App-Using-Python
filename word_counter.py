search_words = ["Python", "C", "OOP", "Hello", "Java"]

# Open and read the contents of "input.txt"
file_path = "input.txt"

try:
    with open(file_path, "r") as file:
        file_contents = file.read().lower()
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except IOError as err:
    print(f"An error occurred while reading the file: {err}")

# Split the file contents into words
words = file_contents.split()
# print(words)

for word in search_words:
    word = word.lower()
    # print(word)
    count = words.count(word)
    print(f"{word.capitalize()} -> {count}")


