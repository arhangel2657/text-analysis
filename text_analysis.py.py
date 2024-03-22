file = open("text_for_analysis.txt", "r")
file_data = file.read().lower()
file.close()

Out = {}


def add_to_out(key, value):
    Out[key] = value


def culculate_symbol(symbol):
    num_of_symbols = 0
    for s in file_data:
        if s.lower() == symbol:
            num_of_symbols += 1
    return num_of_symbols


Symbol_number = 0
Symbol = ""
for i in file_data:
    Symbol = file_data[Symbol_number]
    if Symbol.isalpha():
        add_to_out(file_data[Symbol_number].upper(), file_data.count(Symbol))
    Symbol_number += 1

add_to_out("lines", file_data.count('.'))
add_to_out("words", len(file_data.split()))
add_to_out("symbols", len(file_data))

print(Out)
