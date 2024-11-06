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
        converted_list = []
        decimal_cnt = 0
        for dec in range(4):
            num, remainder = divmod(num, 10)
            if remainder*(10**dec) in roman:
                converted_list.append(roman[remainder*(10**dec)])
            elif remainder < 5:
                converted_list.append(roman[(10**dec)]*remainder)
            else:
                converted_list.append(roman[(10**dec)*5]+roman[(10**dec)]*(remainder-5))
            if num<1:
                break
        converted_list.reverse()
        return "".join(converted_list)