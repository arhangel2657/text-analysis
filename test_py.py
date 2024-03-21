file = open("dds.text", "r")
file_data = file.read()
file.close()

out = {}

def Add_to_out(key, value):
    out[key] = value

def Culculate_symbol(symbol):
    num_of_symbols = 0
    for s in file_data:
        if s.lower() == symbol:
            num_of_symbols += 1
    return num_of_symbols

# add_to_out("lines", )
Add_to_out("words", len(file_data.split(" ")))
Add_to_out("symbols", len(file_data))

print(out)