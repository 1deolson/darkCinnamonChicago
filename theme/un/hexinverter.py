import re

with open('cinnamon.css', 'r') as f:
    text = f.read()



def hex_to_rgb(hex):
  rgb = []
  for i in (0, 2, 4):
    decimal = int(hex[i:i+2], 16)
    rgb.append(decimal)
  
  return tuple(rgb)

def rgb_to_hex(r, g, b):
  return ('{:X}{:X}{:X}').format(r, g, b)

match = 0
def invert_match(match_str):
    global match
    match += 1
    print(match_str)
    r,g,b = hex_to_rgb(match_str[1:])
    print(r, g, b)
    r = 255 - r
    g = 255 - g
    b = 255 - b
    converted = rgb_to_hex(r,g,b)
    if len(converted) < 6:
        while len(converted) < 6:
            converted += '0'
    print('#' + converted)
    print('*'*20)
    return '#' + converted
  
#print(text)

regex = re.compile(r'#[0-9a-fA-F][^#\ng-zG-Z]{6}')
# matches = regex.findall(text)
# print(matches)
#text_2 = text

text_2 = re.sub(regex, lambda x: invert_match(x.group()), text)

# print(match)
print(text_2)

with open('cinnamon.css', 'w') as f:
    f.write(text_2)