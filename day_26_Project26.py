# Day 26
# Project-26 = NATO phonetic mapping
nato_dict = {
    'A': 'Alpha',   'B': 'Bravo',    'C': 'Charlie',
    'D': 'Delta',   'E': 'Echo',     'F': 'Foxtrot',
    'G': 'Golf',    'H': 'Hotel',    'I': 'India',
    'J': 'Juliett', 'K': 'Kilo',     'L': 'Lima',
    'M': 'Mike',    'N': 'November', 'O': 'Oscar',
    'P': 'Papa',    'Q': 'Quebec',   'R': 'Romeo',
    'S': 'Sierra',  'T': 'Tango',    'U': 'Uniform',
    'V': 'Victor',  'W': 'Whiskey',  'X': 'X-ray',
    'Y': 'Yankee',  'Z': 'Zulu'
}

def generate_phonetic():
    nato_list = []
    while True:
        word = input("Enter a word (letters only): ").strip().upper()
        if not word.isalpha():
            print("❌ Invalid input: please enter only letters.")
        else:
            # Translate each letter to its NATO codeword
            codes = [nato_dict[letter] for letter in word]
            nato_list.extend(codes)
            print("Phonetic translation:", " ".join(codes))
        ans = input("Do you want to continue? (y/n): ").strip().lower()
        if ans != 'y':
            break
    print("Final accumulated phonetic list:", nato_list)

if __name__ == "__main__":
    generate_phonetic()
