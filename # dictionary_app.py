# dictionary_app.py
    
from red_black_tree import red_black_tree

class DictionaryApplication:
    def __init__(self, dictionary_file_path):
        self.dictionary_file_path = dictionary_file_path
        self.rbt = red_black_tree()

    def load_dictionary(self):
        with open(self.dictionary_file_path, 'r') as file:
            for word in file:
                self.rbt.insert(word.strip())

    def search_word(self, word):
        return self.rbt.search(word)

    def insertion_into_dictionary(self, new_word):
        if not self.rbt.search(new_word):
            self.rbt.insert(new_word)
            with open(self.dictionary_file_path, 'a') as file:
                file.write('\n'+new_word)
            print(f"'{new_word}' was added into the dictionary.")
        else:
            print("ERROR: Word already in the dictionary!")

if __name__ == "__main__":
    dictionary_file_path = r'C:\Users\DELL\Downloads\words.txt'
    app = DictionaryApplication(dictionary_file_path)
    app.load_dictionary()

    while True:
        choice = input("1- Insert word, 2- Search for word, 3- Exit: ")
        if choice == '1':
            new_word = input("Inserting word: \n")
            app.insertion_into_dictionary(new_word)
        elif choice == '2':
            search_for_word = input("Searching for word: ")
            if app.search_word(search_for_word):
                print("YES")
            else:
                print("NO")
        elif choice == '3':
            break
        else:
            print("Invalid input\n")

    print("Thanks for using the dictionary!")
