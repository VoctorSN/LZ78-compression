from src.separador_str_int import separador_str_int

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
if __name__ == "__main__":
    def test_encoder():
        assert decoder('0A0B1A2A4A4B')=='ABAABABAABAB'
        assert decoder('0A0B1A2A4A4B3')=='ABAABABAABABAA'
        assert decoder('0A0B2C3A2A4A6B6')=='ABBCBCABABCAABCAABBCAA'
        assert decoder('0A1A2A3A4A')=='AAAAAAAAAAAAAAA'
        assert decoder('0A0B0C1B3A2C4C7A6')=='ABCABCABCABCABCABC'
        assert decoder('0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C')=='ABCDDEFGABCDEDBBDEAAEDAEDCDABC'