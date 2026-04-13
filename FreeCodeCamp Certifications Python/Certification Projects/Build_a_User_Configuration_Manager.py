def add_setting(user_settings, setting_pair):

    key, value = setting_pair
    key = key.lower()
    value = value.lower()

    if key in user_settings:
            return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        user_settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(user_settings, setting_pair):
    
    key, value = setting_pair
    key = key.lower()
    value = value.lower()

    if key in user_settings:
        user_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(user_settings, setting_key):
    key = setting_key
    key = key.lower()

    if key in user_settings:
        del user_settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"
    

def view_settings(user_settings):
    if not user_settings:
        return 'No settings available.'
    else:
        teks_hasil = 'Current User Settings:\n'
        for key, value in user_settings.items():
            teks_hasil += f"{key.capitalize()}: {value}\n"
        return teks_hasil

# ==========================================
# UJIAN FINAL: USER CONFIGURATION MANAGER)
# ==========================================

# 0. Siapkan dictionary kosong
test_settings = {}
print("--- MULAI TES ---\n")

# ==========================================
# TES 1: VIEW (Saat Masih Kosong)
# ==========================================
print("1. TES VIEW (Kosong)")
print(view_settings(test_settings))
# EKSPEKTASI OUTPUT: 
# No settings available.
print("-" * 40)

# ==========================================
# TES 2: ADD (Normal & Jebakan Huruf Besar)
# ==========================================
print("2. TES ADD (Normal & Huruf Besar)")
print(add_setting(test_settings, ("THEME", "DARK")))
print(add_setting(test_settings, ("Language", "English")))
print(add_setting(test_settings, ("notifications", "ENABLED")))
# EKSPEKTASI OUTPUT: 
# Setting 'theme' added with value 'dark' successfully!
# Setting 'language' added with value 'english' successfully!
# Setting 'notifications' added with value 'enabled' successfully!
print("-" * 40)

# ==========================================
# TES 3: ADD (Gagal - Duplikat)
# ==========================================
print("3. TES ADD (Duplikat)")
print(add_setting(test_settings, ("theme", "light")))
# EKSPEKTASI OUTPUT: 
# Setting 'theme' already exists! Cannot add a new setting with this name.
print("-" * 40)

# ==========================================
# TES 4: UPDATE (Berhasil & Gagal)
# ==========================================
print("4. TES UPDATE")
print(update_setting(test_settings, ("Theme", "light"))) # Berhasil
print(update_setting(test_settings, ("Volume", "high"))) # Gagal (Belum ada)
# EKSPEKTASI OUTPUT:
# Setting 'theme' updated to 'light' successfully!
# Setting 'volume' does not exist! Cannot update a non-existing setting.
print("-" * 40)

# ==========================================
# TES 5: VIEW (Saat Sudah Ada Isi)
# ==========================================
print("5. TES VIEW (Ada Isi)")
print(view_settings(test_settings))
# EKSPEKTASI OUTPUT:
# Current User Settings:
# Theme: light
# Language: english
# Notifications: enabled
print("-" * 40)

# ==========================================
# TES 6: DELETE (Berhasil & Gagal)
# ==========================================
print("6. TES DELETE")
print(delete_setting(test_settings, "LANGUAGE")) # Berhasil
print(delete_setting(test_settings, "font_size")) # Gagal
# EKSPEKTASI OUTPUT:
# Setting 'language' deleted successfully!
# Setting not found!
print("-" * 40)

# ==========================================
# TES 7: CEK HASIL AKHIR
# ==========================================
print("7. CEK HASIL AKHIR DI DICTIONARY")
print(test_settings)
# EKSPEKTASI OUTPUT:
# {'theme': 'light', 'notifications': 'enabled'}
print("--- TES SELESAI ---")