from src.value_key import value_key

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
