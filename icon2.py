import re
a="010101000110100001100101011100100110010100100000011000010111001001100101001000000111001101101111001000000110110101100001011011100111100100100000011100110110010101100011011100100110010101110100011100110010000001111001011011110111010100100000011000110110000101101110001000000111000001101100011000010110001101100101001000000110100101101110001000000110100001100101011100100110010100100001001000000101010001101000011001010010000001101001011011010110000101100111011001010010000001101001011100110010000000110011001100100111100000110011001100100010000000101101001000000110010101110110011001010110111000100000011010010110011000100000011010010111010000100000011101110110000101110011001000000110011101110010011000010111100101110011011000110110000101101100011001010010000001100001011011100110010000100000011110010110111101110101001000000110111101101110011011000111100100100000011101010111001101100101011001000010000001100001001000000111001101101001011011100110011101101100011001010010000001100010011010010111010000100000011100000110010101110010001000000111000001101001011110000110010101101100001011000010000001110100011010000110000101110100001001110111001100100000001100010011000000110010001101000010000001100010011010010111010001110011001000000110111101110010001000000011000100110010001110000010000001100011011010000110000101110010011000010110001101110100011001010111001001110011001011100010000001010100011010000110000101110100001001110111001100100000011001010110111001101111011101010110011101101000001000000110011001101111011100100010000001100001001000000111001001100101011000010111001101101111011011100110000101100010011011000110010100100000011100110111100101101101011011010110010101110100011100100110100101100011001000000110000101101100011001110110111101110010011010010111010001101000011011010010000001101011011001010111100100100001001000000101001101110000011001010110000101101011011010010110111001100111001000000110111101100110001000000111011101101000011010010110001101101000001011000010000001110100011010000110010100100000011100110110010101100011011100100110010101110100001000000110011001101111011100100010000001000110011100100110010101100101011011000110000101101110011000110110010101110010001011100110001101101111011011010010000001101001011100110011101000100000010110000111100101100101011010100111001101101011011001010101001101111001001100110011100101111010001100110010111000100000001100110010111000110001001101000011000100110101001110010011001000110110001101010011001100110101001110000011100100110111001110010011001100110010001100110011010000110011001100110011100000110011001100100011011100111001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
b=re.findall(r'.{8}',a)
#print(bytes(b[0],encoding='utf8'))
#print(bytes(int(b[0],2)).decode("ascii"))

al = []
for i in range(0, len(a), 8):
  b = a[i:i+8]
  al.append(chr(int(b, 2)))
print ''.join(al)
