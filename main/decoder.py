from src.separador_str_int import separador_str_int

def decoder(data):
    data=separador_str_int(data)
    index=1
    dic={0:""}
    string=""
    final_string=""
    for position,char in enumerate(data):
        # en el caso de que sea un str lo metera en el final string y al diccionario le añadira la nueva entry
        if char.isalpha():
            dic[index]=dic[int(data[position-1])]+char
            index+=1
            final_string+=char
        # Y en el caso de que sea un int y no sea 0 añadira al final string el entry segun la key correspondiente al char
        else:
            final_string+=dic[int(char)]
    return final_string
