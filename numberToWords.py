class Solution:
    def numberToWords(self, num: int) -> str:
        lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        if num == 0:
            return "Zero"
        def abc(num):
            result = ""
            hundred = num // 100
            remainder = num % 100
            if hundred:
                result += lessThan20[hundred] + " Hundred"
            if remainder:
                result += " " if result else ""
                if remainder < 20:
                    result += lessThan20[remainder]
                else:
                    result += tens[remainder // 10]
                    if remainder % 10:
                        result += " " + lessThan20[remainder % 10]

            return result
        result = ""
        for i in range(len(thousands)):
            if num % 1000 != 0:
                result = abc(num % 1000) + " " + thousands[i] + " " + result
            num //= 1000
        return result.strip()
