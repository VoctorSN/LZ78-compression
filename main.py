def value_key(value,dic):
    return str(list(dic.keys())[list(dic.values()).index(value)])       

def separador_str_int(entry):
    lista=[]
    string=""
    for pos,char in enumerate(entry):
        string+=char
        if pos==len(entry)-1:
            lista.append(str)
        elif str.isnumeric() and entry[pos+1].isalpha():
            lista.append(str)
            string=""
        elif str.isalpha() and entry[pos+1].isnumeric():
            lista.append(str)
            string=""
    return lista  
            

def encoder(data):
    dic={0:""}
    index=1
    string=""
    final_string=""
    for position,char in enumerate(data):
        string+=char

        if string not in dic.values():
            dic[index]=string
            index+=1
            if len(string)==1:
                final_string+="0"+string
            else:
                final_string+=value_key(string[:len(string)-1],dic)+char
            string=""
        elif string in dic.values() and len(data)!=position+1:
            continue
        else:
            final_string+=value_key(string,dic)
    return final_string


def decoder(data):
    data=separador_str_int(data)
    index=1
    dic={0:""}
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

