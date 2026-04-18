class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description =''):
        self.ledger.append({"amount": float(amount), "description": description})
    
    def withdraw(self, amount_withdraw, description =''):
        if not self.check_funds(amount_withdraw):
            return False
        
        self.ledger.append({"amount": float(-amount_withdraw), "description": description})
        return True

    def get_balance(self):
        current_money = 0
        for dictionary in self.ledger:
            for value in dictionary.values():
                if isinstance(value, float):
                    current_money += value
        return current_money

    def transfer(self, amount_transfer, destination):        
        if not self.check_funds(amount_transfer):
            print(f"Tidak bisa melakukan transfer dengan jumlah: {amount_transfer} karena saldo tidak cukup.\n")
            return False
        
        description = f"Transfer to {destination.name}"
        self.ledger.append({"amount": float(-amount_transfer), "description": description})
        
        description = f"Transfer from {self.name}"
        destination.ledger.append({"amount": float(amount_transfer), "description": description})
        return True
        
    def check_funds(self, amount):
        current_money = self.get_balance()
        if amount > current_money:
            return False
        return True

    def __str__(self):
        baris_teks = [f"{self.name:*^30}"]
        
        for entry in self.ledger:
            deskripsi = entry['description'][:23]
            jumlah = entry['amount']

            baris_teks.append(f"{deskripsi:<23}{jumlah:>7.2f}")
            
        baris_teks.append(f"Total: {self.get_balance():.2f}")
            
        return "\n".join(baris_teks)

def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent -= item["amount"]
        spent_amounts.append(spent)

    total_spent = sum(spent_amounts)

    percentages = []
    for amount in spent_amounts:
        if total_spent > 0:
            percent = int((amount / total_spent) * 100)
            percentages.append(percent - (percent % 10))
        else:
            percentages.append(0)

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = 0
    for category in categories:
        if len(category.name) > max_len:
            max_len = len(category.name)

    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart


# ------------------------------- Batas -------------------------------
# My way of slowly thinking a solution for this problem
print(f"\n\n{'='*5} Latihan atau Experiment {'='*5}")

list_of_dict = [{
    'money': 10000,
    'description': "data ke 1"
}]

print('\n')
print(list_of_dict)
print('\n')
list_of_dict.append({
    'money2': 10000,
    'description': "data ke 2"
})
print(list_of_dict)

# gimana cara kita mengurangi uang yang ada di data ke 1? 
# ide awalnya sih, mungkin kita perlu fokus dan akses terlebih dahulu untuk list indeks 0
print('\n')
print(list_of_dict[0])
print('\n')


# misalkan ada dictionary doank
dictionaryku = {
    'name' : 'Muhammad Zaenal Abidin Abdurrahman',
    'uang': 20000 
}
print(dictionaryku['uang'])

print('\n')
print(list_of_dict[0]['money']) # i could do this i guess?

# can you do like subtraction?
list_of_dict[0]['money'] -= list_of_dict[0]['money']
print(list_of_dict[0]['money']) # hmm interesting, idk i feel like this the approach u know 

# so the class Category the method of deposit and withdraw should be have something that can connect each other u know. But how?? Let see


print(f"\n\n{'-'*10} percobaan pertama {'-'*10}\n")

class CategoryCoba2:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description =''):
        self.ledger.append({"amount": amount, "description": description})
        print(f"'amount deposit': {amount}, 'description': {description}")
    
    def withdraw(self, amount_withdraw, description =''):
        print(f"'amount withdraw': {amount_withdraw}, 'description': {description}")
        self.ledger[0]['amount'] -= amount_withdraw


    def __str__(self):
        return f"Keterangan/detail data saat ini : {self.ledger}"

drink = CategoryCoba2("Milk")
drink.deposit(100000)
drink.withdraw(50000)
print(drink)

# It is works but idk feels weird, there should be a better solution


print(f"\n\n{'-'*10} percobaan kedua {'-'*10}\n")
class CategoryLebihTepat:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description =''):
        self.ledger.append({"amount": amount, "description": description})
        print(f"'amount deposit': {amount}, 'description': {description}")
    
    def withdraw(self, amount_withdraw, description =''):
        self.ledger.append({"amount": -amount_withdraw, "description": description})

        print(f"'amount withdraw': {-amount_withdraw}, 'description': {description}")


    def __str__(self):
        return f"\nKeterangan/detail data saat ini : {self.ledger}"

drink2 = CategoryLebihTepat("Milk")
drink2.deposit(100000, 'initial deposit')
drink2.withdraw(50000, 'buy milk')
print(drink2)

# Ah, i think i get it what is it trying to do, so everything will have the history u could say. Nantinyaaaa masalh jumlah uang tingga foksu saja dengan kalimat 'amount" atau kata kuncu 'amount' lah. 


print(f"\n\n{'-'*10} percobaan ketiga {'-'*10}\n")
class CategoryLebihTepat2:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description =''):
        print(f"Proses deposit untuk {self.name} sedang berjalan...")
        self.ledger.append({"amount": float(amount), "description": description})
        print(f"'amount deposit': {amount}, 'description': {description}\n")
    
    def withdraw(self, amount_withdraw, description =''):
        print(f"Proses penarikan untuk {self.name} sedang berjalan...")
        if not self.check_funds(amount_withdraw):
            print(f"Tidak bisa melakukan penarikan dengan jumlah: {amount_withdraw} karena saldo tidak cukup.\n")
            return False
        
        self.ledger.append({"amount": float(-amount_withdraw), "description": description})
        print(f"'amount withdraw': {-amount_withdraw}, 'description': {description}")
        print(f"Berhasil mengambil saldo\n")
        return True

    def get_balance(self):
        current_money = 0

        for dictionary in self.ledger:
            for value in dictionary.values():
                if isinstance(value, float):
                    current_money += value

        print(f"Jumlah uang saat ini untuk {self.name} adalah : {current_money}")
        return current_money

    def transfer(self, amount_transfer, destination):
        print(f"Proses transfer dari {self.name} ke {destination.name} sedang berjalan...")
        
        # Ini berarti harus transfer dari kategori misal food ke drink, dan tentu saja perlu dicek dan perlu dilakukan update uang pada keduanya, lalu juga history untuk keduanya
        if not self.check_funds(amount_transfer):
            print(f"Tidak bisa melakukan transfer dengan jumlah: {amount_transfer} karena saldo tidak cukup.\n")
            return False
            
        # now what happend when u already check? yak update uang dan ngurangin uang ke masing masing kategori, hmm how?
        
        # Mengurangi saldo untuk kategori yang mengirim
        description = f"Mengirimkan uang ke kategori {destination.name}"
        self.ledger.append({"amount": float(-amount_transfer), "description": description})
        
        # Menambahkan saldo untuk kategori yang menerima, bagaimana caranya? idenya sih seharusnya sama kek bikin append lagi untuk ledger si penerima. Cara aksesnya
        description = f"Menerima uang dari kategori {self.name}"
        destination.ledger.append({"amount": float(amount_transfer), "description": description})
        
        print(f"Transfer from {self.name} to {destination.name} with amount: {amount_transfer}")
        print(f"Berhasil transfer\n")
        
    def check_funds(self, amount):
        current_money = self.get_balance()
        if amount > current_money:
            return False
        return True

    def __str__(self):
        print(f"{f'{self.name}':*^30}")
        for deskripsi, jumlah in [(entry['description'], entry['amount']) for entry in self.ledger]:
            print(f"{deskripsi[:23]:<23}{jumlah:>7.2f}")
        print(f"")
        return f"Keterangan/detail data saat ini : {self.ledger}\n"


drink3 = CategoryLebihTepat2("Milk")
drink3.deposit(100000, 'Masukin uang awal')
drink3.withdraw(20000, 'buy')
drink3.get_balance()
print()
print(drink3)


food3 = CategoryLebihTepat2("Food")
food3.deposit(200000, "Deposit awal")
food3.get_balance()
print()
food3.transfer(50000, drink3)
food3.get_balance()
print()
drink3.get_balance()
print()
print(drink3)
print()
print(food3)


# This is the final version of the code, and will try to make it more clean and best practise as possible
print(f"\n\n{'-'*10} percobaan keempat {'-'*10}\n")
class CategoryBestPractise:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description =''):
        self.ledger.append({"amount": float(amount), "description": description})
    
    def withdraw(self, amount_withdraw, description =''):
        if not self.check_funds(amount_withdraw):
            return False
        
        self.ledger.append({"amount": float(-amount_withdraw), "description": description})
        return True

    def get_balance(self):
        current_money = 0
        # This is kind of not the best way, but it's okay
        for dictionary in self.ledger:
            for value in dictionary.values():
                if isinstance(value, float):
                    current_money += value
        return current_money

    def transfer(self, amount_transfer, destination):        
        if not self.check_funds(amount_transfer):
            print(f"Tidak bisa melakukan transfer dengan jumlah: {amount_transfer} karena saldo tidak cukup.\n")
            return False
        
        # Both can use the method of withdraw and desposit (DRY), but it is okay
        description = f"Transfer to {destination.name}"
        self.ledger.append({"amount": float(-amount_transfer), "description": description})
        
        description = f"Transfer from {self.name}"
        destination.ledger.append({"amount": float(amount_transfer), "description": description})
        
        return True
        
    def check_funds(self, amount):
        current_money = self.get_balance()
        if amount > current_money:
            return False
        return True

    def __str__(self):
        # Buat list untuk menampung semua baris, dimulai dengan judul
        baris_teks = [f"{self.name:*^30}"]
        
        # Looping data ledger dan format masing-masing baris
        for entry in self.ledger:
            deskripsi = entry['description'][:23]
            jumlah = entry['amount']
            
            # Masukkan hasil format ke dalam list
            baris_teks.append(f"{deskripsi:<23}{jumlah:>7.2f}")
            
        baris_teks.append(f"Total: {self.get_balance():.2f}")
            
        # Gabungkan semua item di dalam list menjadi satu string dengan enter (\n)
        return "\n".join(baris_teks)

makanan = CategoryBestPractise('Food')
makanan.deposit(1000, 'initial deposit')
makanan.withdraw(10.15, 'groceries')
makanan.withdraw(15.89, 'restaurant and more food for dessert')
clothing = CategoryBestPractise('Clothing')
makanan.transfer(50, clothing)
print(makanan)