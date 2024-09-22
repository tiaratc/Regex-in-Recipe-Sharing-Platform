import re

def validasi(ingredient):
    pattern = r'^\d+(\/\d{1})?\s+(kg|gr|ml|l|buah|butir|lembar|bungkus|ikat|batang|sdm|sdt)\s+[a-zA-Z0-9\s]+$'
    return re.match(pattern, ingredient) is not None

def main():
    # Information for users
    print("\nHalo kontributor Yummii !")
    print("\nBahan harus diinput sesuai ketentuan berikut ini :")
    print("\n  - contoh penulisan (1 kg tepung terigu, 1/2 bungkus mie instant)\n")
    print("  - satuan yang diterima : kg, gr, ml, l, buah, butir, lembar, bungkus, ikat, batang, sdm, sdt\n")
    
    recipe_name = input("\nMasukkan Judul Resep Anda :  ")
    print(f"\nJudul resep: {recipe_name}\n")
    
    ingredients = []
    
    while True:
        ingredient = input("\nMasukkan bahan (atau ketik 'selesai' untuk mengakhiri input): ")
        
        if ingredient.lower() == 'selesai':
            break
            
        if validasi(ingredient):
            ingredients.append(ingredient)
            print(f"Bahan ditambahkan: {ingredient}")
        else:
            print("\nFormat invalid. Pastikan input bahan sesuai dengan ketentuan input.")
    
    print("\nRingkasan Resep Anda :")
    print(f"\nNama Resep: {recipe_name}")
    print("\nBahan : ")
    for ing in ingredients:
        print(f"- {ing}")


main()

