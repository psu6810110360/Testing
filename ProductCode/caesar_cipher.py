def caesar_cipher(s, k):
    result = ""
    k = k % 26
    for char in s:
        if "a" <= char <= "z":
            result += chr((ord(char) - ord("a") + k) % 26 + ord("a"))
        elif "A" <= char <= "Z":
            result += chr((ord(char) - ord("A") + k) % 26 + ord("A"))
        else:
            result += char
    return result
