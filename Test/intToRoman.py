def romantoint(s):
    num_tuple = [1000, 900, 500, 400, 100,
                 90, 50, 40, 10, 9, 5, 4, 1]
    roman_tuple = ['M', 'CM', 'D', 'CD', 'C', 'XC',
                   'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result_str = ''
    for i in range(len(num_tuple)):
        while s >= num_tuple[i]:
            s -= num_tuple[i]
            result_str += roman_tuple[i]
            return result_str














