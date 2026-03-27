s = 'abcdefghij'

print(s[1:6:2]) # bdf -> begin to end -1 -> 1 to 5 every second character 
print(s[::1]) # abcdefghij
print(s[::-1]) # jihgfedcba
print(s[3:7:-1]) # #Empty String As we required from backward direction  -> 3 to 8 -> As we moved from backeward direction so it will empty 

print(s[7:4:-1]) # hgf -> 7 to 5 -> Backward direction 
print(s[0:10000:1]) # Slice operator never raise the index error  -> 0 to 99999 -> 
print(s[0:10000:-1]) # Slice operator never raise the index error  So empty
print(s[-4:1:-1]) # begin to end +1 -> -4 to 2 -> gfedc
print(s[-4:1:-2]) # -4 to 2 -> gec
print(s[5:0:1]) # END VALUE IS O , SO ITS EMAPTY 
print(s[5:0:1]) # 
#print(s[9:0:0]) # IN SLICE OPERATOR STEP OPERATOR CAN'T BE 0 #ValueError: slice step cannot be zero

print(s[0:-10:-1]) # begin to end +1 -> Backward to -1 -> 0 to -9 ->  Then its empty
print(s[0:-11:-1]) # 0 to -11+1 =-10 -> a o to -10  = a 
print(s[0:0:1]) # Emapty
print(s[0:-9:-2]) # #mpty 

print(s[-5:-9:-2]) # begin to end+1 => -5 to -8  => fd
print(s[10:-1:-2]) # backward direction -> begin to end+1 => 10 too -1+1 = Empty print(s[10:-1:-2]) 
print(s[10000:2:-1]) # backward direction -> begin to end+1 => 1000000 too 2+1 =  
