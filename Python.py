import math

def round_up(deger):
    # round() fonksiyonu en yakın tam sayıya yuvarlar. 
    # Yukarı yuvarlamak için sayıya 0.5 ekleyip round kullanabilir veya math.ceil tercih edebilirsin.
    return math.ceil(deger)

def round_down(deger):
    # Aşağı yuvarlamak için math.floor kullanmak en güvenli yoldur.
    return math.floor(deger)

# Test edelim
print(f"Yukarı: {round_up(3.2)}")   # Sonuç: 4
print(f"Aşağı: {round_down(3.8)}")  # Sonuç: 3
