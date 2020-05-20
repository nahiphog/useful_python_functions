import timeit

listingggggggg = timeit.timeit(stmt = "[1,2,3,4,5]", number = int(1e6))

tuplessssssssssss = timeit.timeit(stmt = "(1,2,3,4,5)", number = int(1e6))

print(listingggggggg, tuplessssssssssss)

# 0.0529579 
# 0.008782600000000002
