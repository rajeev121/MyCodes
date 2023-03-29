def roman_to_decimal(roman_numeral):
    roman_values = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                    'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                    'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    decimal_value = 0
    i = 0
    while i < len(roman_numeral):
        if i < len(roman_numeral) - 1 and roman_numeral[i:i+2] in roman_values:
            decimal_value += roman_values[roman_numeral[i:i+2]]
            i += 2
        else:
            decimal_value += roman_values[roman_numeral[i]]
            i += 1
    return decimal_value

roman_num = 'MCXVII'
result = roman_to_decimal(roman_num)
print(result)