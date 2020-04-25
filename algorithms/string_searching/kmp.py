def prefix(string):
    prefix_function = [0] * len(string)
    for i in range(1,len(string)):
        k = prefix_function[i-1]
        while k > 0 and string[k] != string[i]:
            k = prefix_function[k-1]
        if string[k] == string[i]:
            k = k + 1
        prefix_function[i] = k
    return prefix_function

def kmp(pattern, text):
# Knuth Morris Pratt algorithm
    entries = []
    if len(pattern) > len(text):
        return entries
    prefix_function = prefix(pattern)
    text_index = pattern_index = 0
    while text_index < len(text) and pattern_index < len(pattern):
        if text[text_index] == pattern[pattern_index]:
            if pattern_index == len(pattern) - 1:
                entries.append(text_index - len(pattern) + 1)
                pattern_index = 0
            else:
                pattern_index += 1
            text_index += 1
        elif pattern_index is not 0:     
            pattern_index = prefix_function[pattern_index-1]
        else:
            text_index += 1
    return entries
