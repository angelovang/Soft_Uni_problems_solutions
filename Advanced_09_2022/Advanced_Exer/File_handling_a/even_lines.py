# Working files are in directory "txt_files"

try:
    with open('txt_files/text_1.txt', 'r') as txt_file :
        txt = txt_file.readlines()
except FileNotFoundError :
    print('No such file or directory !')

symbols = ["-", ",", ".", "!", "?"]     # Here are the symbols we need to replace with '@'
even = True           # Even line flag

for line in txt :
    if even :
        for symbol in symbols :
            if symbol in line :
                line = line.replace(symbol,'@')
        print(*line.split()[::-1])
        even = False    # The next line is odd
    else:
        even = True     # The next line is even





