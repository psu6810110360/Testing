def funny_string(s):
    
    ascii_chars = [ord(c) for c in s]
    
    reversed_ascii = ascii_chars[::-1]
    
    n = len(ascii_chars)
    
    for i in range(n - 1):
        diff1 = abs(ascii_chars[i] - ascii_chars[i+1])
        diff2 = abs(reversed_ascii[i] - reversed_ascii[i+1])
        
        
        if diff1 != diff2:
            return "Not Funny"
            
    return "Funny"