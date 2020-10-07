sentence = "Dit is een test"
masker = (1<<5) | (1<<3) | (1<<1)

code = ""
for char in sentence:
    code += chr(ord(char)^masker)
print( code )

decodeer = ""
for char in code:
    decodeer += chr(ord(char)^masker)
print( decodeer )