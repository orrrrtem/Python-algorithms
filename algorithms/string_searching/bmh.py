from copy import deepcopy

def get_int_image(x):
    length = len(x)
    image_dict = {i: length for i in range(2048)}
    for idx, char in enumerate(x[:-1], start=1):
        # if char not in image_dict:
        image_dict[ord(char)] = length-idx

    return image_dict


def bmh(pattern, text):
    entries = []
    if len(pattern) > len(text):
        return entries
    image_dict = get_int_image(pattern)
    length_text = len(text)
    length_pattern = len(pattern)
    i = length_pattern  # for text
    j = length_pattern  # for pattern
    entry_point = length_pattern  # for position in full string
    while i <= length_text:
        if text[i-1] == pattern[j-1] and j>0:
            i -= 1
            j -= 1
        else:
            if j == 0:
                entries.append(entry_point - length_pattern)
            # print(text[i-1])
            entry_point += image_dict[ord(text[i-1])]
            i = deepcopy(entry_point)
            j = length_pattern
    return entries
