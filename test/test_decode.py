from main.decoder import decoder

def test_encoder():
    assert decoder('0A0B1A2A4A4B')=='ABAABABAABAB'
    assert decoder('0A0B1A2A4A4B3')=='ABAABABAABABAA'
    assert decoder('0A0B2C3A2A4A6B6')=='ABBCBCABABCAABCAABBCAA'
    assert decoder('0A1A2A3A4A')=='AAAAAAAAAAAAAAA'
    assert decoder('0A0B0C1B3A2C4C7A6')=='ABCABCABCABCABCABC'
    assert decoder('0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C')=='ABCDDEFGABCDEDBBDEAAEDAEDCDABC'
