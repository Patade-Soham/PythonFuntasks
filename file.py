import os

def extract_words_by_length(filename, lengths):
    """Reads a text file and prints words of specified lengths."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            words = [word.strip('.,!?()[]{}":;') for word in words]  # Remove punctuation

            result = {length: [] for length in lengths}
            for word in words:
                if len(word) in lengths:
                    result[len(word)].append(word)
           
            for length, words in result.items():
                print(f"Words with {length} letters: {set(words)}")
   
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = "sample.txt"  # Automatically using sample.txt
    lengths = list(map(int, input("Enter word lengths (comma-separated): ").split(',')))
    extract_words_by_length(filename, lengths)
