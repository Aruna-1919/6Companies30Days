def encode(string):
    if not string:
        return ""

    encoded_string = ""
    count = 1
    prev_char = string[0]

    for i in range(1, len(string)):
        if string[i] == prev_char:
            count += 1
        else:
            encoded_string += prev_char + str(count)
            count = 1
            prev_char = string[i]

    encoded_string += prev_char + str(count)
    return encoded_string

