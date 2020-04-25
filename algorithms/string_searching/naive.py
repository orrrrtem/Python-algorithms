def naive(pattern, text):
    entries = []
    if len(pattern) > len(text):
        return entries
    for text_index in range(len(text) - len(pattern) + 1):
        pattern_index = 0
        while(pattern_index < len(pattern)): 
            if (text[text_index + pattern_index] != pattern[pattern_index]): 
                break
            pattern_index += 1
        if pattern_index is len(pattern):
            entries.append(text_index)
    return entries
