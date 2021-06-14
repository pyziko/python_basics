15 & 22

# & return 1 if both are 1 else 0
# | return 1 if only one of them is 1 else 0
# ^ return 1 if exactly one of them is 1 else 0
# ~ return 1 for every zero and zero for every 1
print(bin(5))
print(bin(11))

print(20 | 5)
print(~200)
print(20&5)
print(2<<4)



# >>num shits bit by num to the right
# 1 0 1 0 1 0
#becomes  0 1 0 1 0 1

# <<num shits bit by num to the left
# 1 0 1 0 1 0
#becomes  0 1 0 1 0 0


print(22 // 2)  # ====>    print (22 >> 1)
print(22 // 4)  # ====>    print (22 >> 2)
print(22 * 2)   # ====>    print (22 << 1)
print(22 * 4)   # ====>    print (22 << 2)


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    print(decimal)

binaryToDecimal(1110)


print(int(1001))
print(22 << 1)
