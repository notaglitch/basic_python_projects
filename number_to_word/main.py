def convert_to_word(n):
    if n == 0:
        return "Zero"
    
    def convert_hundreds(num):
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        if num == 0:
            return ""
        
        elif num < 10:
            return ones[num]
        
        elif num < 20:
            return teens[num - 10]
        
        elif num < 100:
            ten_val = num // 10
            one_val = num % 10
            return tens[ten_val] + (" " + ones[one_val] if one_val != 0 else "")
        
        else:  # num >= 100
            hundred_val = num // 100
            rest = num % 100
            return ones[hundred_val] + " Hundred" + (" " + convert_hundreds(rest) if rest != 0 else "")
    
    def convert_large_number(n):
        if n == 0:
            return ""
        
        units = ["", "Thousand", "Million", "Billion"]
        part = 0
        words = []
        
        while n > 0:
            if n % 1000 != 0:
                words.insert(0, convert_hundreds(n % 1000) + (" " + units[part] if units[part] else ""))
            n //= 1000
            part += 1
        
        return " ".join(words).strip()
    
    return convert_large_number(n)

number = int(input("Enter a number: "))
print(convert_to_word(number))
