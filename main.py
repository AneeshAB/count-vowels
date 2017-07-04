vowels = ['a', 'e', 'i', 'o', 'u']

# Main function
def main():
    # Get input
    str_input = raw_input('Enter a string: ')

    # Count vowels
    dictionary = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    for c in str_input:
        if c in vowels:
            dictionary[c] = dictionary[c] + 1

    # Return output
    for key, value in dictionary.iteritems():
        print(key + ': ' + str(value))

if __name__ == '__main__':
    main()
