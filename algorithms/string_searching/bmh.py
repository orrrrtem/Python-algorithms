from copy import deepcopy

def get_int_image(x):
    image_dict = {}
    length = len(x)
    for idx, char in enumerate(x[:-1], start=1):
        # if char not in image_dict:
        image_dict[char] = length-idx

    if x[-1] not in image_dict:
        image_dict[x[-1]] = length

    image_dict['other'] = length

    return image_dict


def bmh(pattern, text):
# Boyer–Moore–Horspool algorithm
    entries = []
    if len(pattern) > len(text):
        return entries
    image_dict = get_int_image(pattern)
    length_text = len(text)
    length_pattern = image_dict['other']
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
            try:
                entry_point += image_dict[text[i-1]]
            except:
                entry_point += image_dict['other']
            i = deepcopy(entry_point)
            j = length_pattern
    return entries
