binarystringarray= ["0b0111010101111110", "0b0010001000010000", "0b1010001101101011"]
checksum = int("0b1100010100000101",2)
result = 0
for x in binarystringarray:
    binarystringarray[binarystringarray.index(x)] = int(x,2)
for x in binarystringarray:
    print("     "+bin(x))
    print("+    "+bin(result))
    result = binarywrapadder(result, x)
    print("_______________________________")
    print("=     "+bin(result))
    print("_______________________________")
print("Ergebnis: " + bin(result))

print("Check Checksum:")
checksumcheck = result + checksum #checksum ^ result
print(bin(checksumcheck))

def binarywrapadder(bin1, bin2):
    carry  = "0b0000000000000001"
    delete = "0b1000000000000000"
    toomuch = "0b1111111111111111"

    carry = int(carry,2)
    delete = int(delete,2)
    toomuch = int(toomuch,2)

    result = bin1 + bin2
    if result > toomuch:
        result = result-delete-delete  #Warum funktioniert das mit 2 mal delete? lol, aber was solls.
        result = result+carry

    return result

