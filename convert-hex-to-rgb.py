# Conversion: Hex to RGB

def Hex_to_Rgb(hex):
    h = hex.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
  
print(Hex_to_Rgb('#c96d9d'))  # (201, 109, 157)
print(Hex_to_Rgb('#fa0515')) # (250, 5, 21)
