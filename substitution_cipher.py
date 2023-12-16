f = open('raw.txt', 'r')
text = str(f.readlines())
text2 = text


letters_so_far = []
for letter in text:
    if letter not in letters_so_far:
        letters_so_far += letter
        # print(letter + ': ' + str(text.count(letter)))

for symbol in text2:
    if symbol == ' ':
        text2 = text2.replace(symbol, 'v')
    
    
for symbol in text2:
    if symbol == '1':
        text2 = text2.replace(symbol, 't')
        
for symbol in text2:
    if symbol == '8':
        text2 = text2.replace(symbol, '~')

for symbol in text2:
    if symbol == ',':
        text2 = text2.replace(symbol, 'j')
   


for symbol in text:
    if symbol == '.': # character that i want to change here
        text2 = text2.replace(symbol, ' ') # (char_to_replace, new_char)
        
    
    elif symbol == 'G':
        text2 = text2.replace(symbol, 's')
    
    elif symbol == 'L':
        text2 = text2.replace(symbol, 'e')
    
    
    elif symbol == 'X':
        text2 = text2.replace(symbol, 'i')
    
    elif symbol == 'O':
        text2 = text2.replace(symbol, 'f')
    
    elif symbol == '7':
        text2 = text2.replace(symbol, 'r')
    
    elif symbol == 'D':
        text2 = text2.replace(symbol, 'o')
    
    elif symbol == 'S':
        text2 = text2.replace(symbol, 'm')
    
    elif symbol == 'W':
        text2 = text2.replace(symbol, 'h')
    
    elif symbol == 'V':
        text2 = text2.replace(symbol, 'a')
    
    elif symbol == 'H':
        text2 = text2.replace(symbol, 'n')
    
    elif symbol == 'Q':
        text2 = text2.replace(symbol, ',')
    
    elif symbol == 'Z':
        text2 = text2.replace(symbol, 'g')
        
    elif symbol == 'P':
        text2 = text2.replace(symbol, 'u')
        
    elif symbol == 'T':
        text2 = text2.replace(symbol, 'b')
        
    elif symbol == 'A':
        text2 = text2.replace(symbol, 'd')
        
    elif symbol == 'R':
        text2 = text2.replace(symbol, 'c')
        
    elif symbol == 'J':
        text2 = text2.replace(symbol, 'p')
        
    elif symbol == 'I':
        text2 = text2.replace(symbol, 'y')
        
    elif symbol == 'F':
        text2 = text2.replace(symbol, '3')
        
    elif symbol == 'M':
        text2 = text2.replace(symbol, '1')
        
    elif symbol == 'K':
        text2 = text2.replace(symbol, 'w')
        
    elif symbol == "9":
        text2 = text2.replace(symbol, 'k')
        
    elif symbol == '4':
        text2 = text2.replace(symbol, 'l')
        
    elif symbol == 'E':
        text2 = text2.replace(symbol, 'q')
        
    elif symbol == 'U':
        text2 = text2.replace(symbol, 'x')
        

new_f = open("jordan_plain.txt", "w")
new_f.write(text2)
        
print("OLD TEXT:\n" + text + "\n")  
print("\nNEW TEXT:\n" + text2 + "\n")       