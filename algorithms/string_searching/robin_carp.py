def robin_carp(pattern, text):
    entries = []
    if len(pattern) > len(text):
        return entries 
    hash_pattern = 0    # hash value for pattern 
    hash_text = 0    # hash value for txt 
    h = 1 # hash init
    d = 256 # is the number of characters in the input alphabet
    q = 977 # TODO compute it from args sizes
    for i in range(len(pattern) - 1): 
        h = (h * d) % q 
  
    # hash by module q
    for i in range(len(pattern)): 
        hash_pattern = (d * hash_pattern + ord(pattern[i])) % q 
        hash_text = (d * hash_text + ord(text[i])) % q 

    # Slide the pattern over text one by one 
    for i in range(len(text) - len(pattern) + 1): 
        # Check the hash values of current window
        if hash_pattern is hash_text: 
            for j in range(len(pattern)): 
                if text[i+j] != pattern[j]: 
                    break
            if j + 1 == len(pattern): 
                entries.append(i)
  
        # Calculate hash value for next window of text: Remove 
        # leading digit, add trailing digit 
        if i < len(text) - len(pattern): 
            hash_text = (d * (hash_text - ord(text[i]) * h) + ord(text[i + len(pattern)])) % q 
            # We might get negative values of t
            if hash_text < 0: 
                hash_text = hash_text + q 
    return entries
