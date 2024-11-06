class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1:    'I',
            4:    'IV',
            5:    'V',
            9:    'IX',
            10:    'X',
            40:    'XL',
            50:    'L',
            90:    'XC',
            100:    'C',
            400:    'CD',
            500:    'D',
            900:    'CM',
            1000:    'M'
        }
        integer = list(roman.keys())
        integer.sort(reverse=True)        
        result = ''
        i = 0
        while num:
            if integer[i] <= num:
                result += roman[integer[i]]
                num -= integer[i]
            else:
                i += 1
        return result