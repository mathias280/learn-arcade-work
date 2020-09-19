months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))

result = months[(n - 1) * 3:(n - 1) * 3 + 3]

print(result)
