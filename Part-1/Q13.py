def letter_combinations(n):
    if n == "":
        return []
    
    string_maps = {
        "1": "abc",
        "2": "def",
        "3": "ghi",
        "4": "jkl",
        "5": "mno",
        "6": "pqrs",
        "7": "tuv",
        "8": "wxy",
        "9": "z"
    }
    
    result = [""]
    
    for num in n:
        temp = []
        
        for an in result:
            for char in string_maps[num]:
                temp.append(an + char)
        result = temp
    
    return result


digit_string = "123"
print(letter_combinations(digit_string))
