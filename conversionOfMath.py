import math
from unicodedata import name

def linear(type:None,num):
    if type == None:
        print("error")
    elif type == "in_mm":
        return num*25.4
    elif type == "in_cm":
        return num*2.540
    elif type == "in_m":
        return num*0.0254
    elif type == "ft_m":
        return num*0.3048
    elif type == "yard_m":
        return num*0.9144
    elif type == "mile_km":
        return num*1.609344
    elif type == "mile_m":
        return num*1609.344
    elif type == "ft_cm":
        return num*30.48
    # Reverse
    elif type == "mm_in":
        return num/25.4
    elif type == "cm_in":
        return num/2.540
    elif type == "m_in":
        return num/0.0254
    elif type == "m_ft":
        return num/0.3048
    elif type == "m_yard":
        return num/0.9144
    elif type == "km_mile":
        return num/1.609344
    elif type == "m_mile":
        return num/1609.344
    elif type == "cm_ft":
        return num/30.48
    
    else:
        return None


def area(type:None,num):
    if type == None:
        print("error")
    elif type == "in_cm":
        return num*6.4516
    elif type == "ft_cm":
        return num*929.03
    elif type == "ft_m":
        return num*0.092903
    elif type == "yard_m":
        return num*0.8361
    elif type == "miles_km":
        return num*2.58999
    elif type == "mile_hectare":
        return num*258.999
    elif type == "acre_metre":
        return num*4046.856
    elif type == "acre_hecare":
        return num*0.40469
    #Reverse
    elif type == "cm_in":
        return num/6.4516
    elif type == "cm_ft":
        return num/929.03
    elif type == "m_ft":
        return num/0.092903
    elif type == "m_yard":
        return num/0.8361
    elif type == "km_miles":
        return num/2.58999
    elif type == "hectare_mile":
        return num/258.999
    elif type == "metre_acre":
        return num/4046.856
    elif type == "hecare_acre":
        return num/0.40469
    else:
        return None


def volume_capacity(type:None,num,default='uk'):
    if type == None:
        print("error")
    elif type == "in_cm":
        return num*16.3871
    elif type == "in_litre":
        return num*0.0016387
    elif type == "ft_m":
        return num*0.028317
    elif type == "ft_litre":
        return num*28.32
    elif type == "pint_litre":
        return num*0.56826
    elif type == "quart_litre":
        return num*1.13652
    elif type == "yard_m":
        return num*0.07646
    elif type == "gallon_litre" and default=="uk":
        return num*4.54609
    elif type == "gallon_litre" and default=="us":
        return num*3.7854
    #Reverse
    elif type == "cm_in":
        return num/16.3871
    elif type == "litre_in":
        return num/0.0016387
    elif type == "m_ft":
        return num/0.028317
    elif type == "litre_ft":
        return num/28.32
    elif type == "litre_pint":
        return num/0.56826
    elif type == "litre_quart":
        return num/1.13652
    elif type == "m_yard":
        return num/0.07646
    elif type == "litre_gallon" and default=="uk":
        return num/4.54609
    elif type == "litre_gallon" and default=="us":
        return num/3.7854
    else:
        return None


def mass(type:None,num,default='uk'):
    if type == None:
        print("error")
    elif type == "ounce_g":
        return num*28.3495
    elif type == "pound_g":
        return num*453.6
    elif type == "pound_kg":
        return num*0.4536
    elif type == "ton_kg":
        return num*1016.047
    elif type == "tahil_g":
        return num*37.799
    elif type == "kati_kg":
        return num*0.60479
    elif type == "grain_g":
        return num*0.0648
    #Reverese
    elif type == "g_ounce":
        return num/28.3495
    elif type == "g_pound":
        return num/453.6
    elif type == "kg_pound":
        return num/0.4536
    elif type == "kg_ton":
        return num/1016.047
    elif type == "g_tahil":
        return num/37.799
    elif type == "g_kati":
        return num/0.60479
    elif type == "g_grain":
        return num/0.0648
    else:
        return None



if name == '__main__':
    print(volume_capacity('gallon_litre',1))