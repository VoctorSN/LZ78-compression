def separador_str_int(entry):
    lista=[]
    string=""
    for pos,char in enumerate(entry):
        string+=char
        if pos==len(entry)-1:
            lista.append(string)
        elif string.isnumeric() and entry[pos+1].isalpha():
            lista.append(string)
            string=""
        elif string.isalpha() and entry[pos+1].isnumeric():
            lista.append(string)
            string=""
    return lista  
            
