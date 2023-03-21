def front_coding(strings):
    # Find the common prefix of all strings
    prefix_len = 0
    for i in range(min([len(s) for s in strings])):
        if len(set([s[i] for s in strings])) > 1:
            break
        prefix_len += 1
    prefix = strings[0][:prefix_len]

    # Create the encoded string
    encoded = str(len(strings)) + '|' + str(prefix_len) + '|' + prefix

    for string in strings:
        # Add the remaining part of the string after the prefix
        encoded += string[prefix_len:]

    return encoded

# Example usage
strings = ['apple', 'apricot', 'apply', 'application']
encoded = front_coding(strings)
print(encoded)