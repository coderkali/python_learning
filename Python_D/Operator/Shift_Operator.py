# << -> LEft Shift
'''
 If x << 2, then Take out the First 2 bits out and add 2 bits at the last as a 0
 Example  10<<2 = [00]000...01010 -> Remove the first 2 bit then add 2 bit at last -> 000...0101000 -> 40  
'''
print(10<<2)
# >> -> Right Shift
'''
 If x >> 2, then Take out the Last 2 bits out and add 2 bits at the last Sign Bit 
 Example  10 >>2 = 00000...010[10] -> Remove the last 2 bit then add 2 bit at first as sign bit -> 00000...010 -> 2

'''
print(10>>2)

print(True << 2)  # 1 << 2 
print(True >> 2)  # 1 >> 2

