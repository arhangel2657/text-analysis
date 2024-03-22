file = open("text_for_analysis.txt", "r")
file_data = file.read()
file.close()

out = {}

def add_to_out(key, value):
    out[key] = value
def culculate_symbol(symbol):
    num_of_symbols = 0
    for s in file_data:
        if s.lower() == symbol:
            num_of_symbols += 1
    return num_of_symbols

symbol_namber =0
symbol = ""
for i in file_data:
    sym = file_data[symbol_namber]
    if sym.isalpha():
        add_to_out(file_data[symbol_namber].upper(),file_data.count(symbol))
    symbol_namber += 1

add_to_out("lines", len(file_data.split(".")))
add_to_out("words", len(file_data.split(" ")))
add_to_out("symbols", len(file_data))

print(out)