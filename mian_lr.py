import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    ascii_code = int(line)
    character = chr(ascii_code)
    print(character)