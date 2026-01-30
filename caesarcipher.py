import sys

def caesar(text: str, shift: int) -> str:
   
    result = []
    for ch in text:
        if 'A' <= ch <= 'Z':
            base = ord('A')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        elif 'a' <= ch <= 'z':
            base = ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)          
    return ''.join(result)


text   = input("Text : ")
mode   = int(input("Mode (1=encrypt, 2=decrypt): "))
raw_shift = int(input("Shift: "))

if mode == 1:
    shift = raw_shift
elif mode == 2:
    shift = -raw_shift
else:
    print("Invalid mode")
    sys.exit()

print("Output:", caesar(text, shift))
