from num2words import num2words
# english is default

for integer in range(1, 100 + 1):
    print( num2words(integer, to="ordinal_num"), end=' ' )
