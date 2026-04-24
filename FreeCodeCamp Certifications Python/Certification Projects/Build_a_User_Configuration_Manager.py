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
        result_text = 'Current User Settings:\n'
        for key, value in user_settings.items():
            result_text += f"{key.capitalize()}: {value}\n"
        return result_text

# ==========================================
# FINAL TEST: USER CONFIGURATION MANAGER
# ==========================================

# 0. Prepare an empty dictionary.
test_settings = {}
print("--- START TEST ---\n")

# ==========================================
# TEST 1: VIEW (Empty State)
# ==========================================
print("1. TEST VIEW (Empty)")
print(view_settings(test_settings))
# EXPECTED OUTPUT:
# No settings available.
print("-" * 40)

# ==========================================
# TEST 2: ADD (Normal and Mixed Case)
# ==========================================
print("2. TEST ADD (Normal and Mixed Case)")
print(add_setting(test_settings, ("THEME", "DARK")))
print(add_setting(test_settings, ("Language", "English")))
print(add_setting(test_settings, ("notifications", "ENABLED")))
# EXPECTED OUTPUT:
# Setting 'theme' added with value 'dark' successfully!
# Setting 'language' added with value 'english' successfully!
# Setting 'notifications' added with value 'enabled' successfully!
print("-" * 40)

# ==========================================
# TEST 3: ADD (Duplicate Failure)
# ==========================================
print("3. TEST ADD (Duplicate)")
print(add_setting(test_settings, ("theme", "light")))
# EXPECTED OUTPUT:
# Setting 'theme' already exists! Cannot add a new setting with this name.
print("-" * 40)

# ==========================================
# TEST 4: UPDATE (Success and Failure)
# ==========================================
print("4. TEST UPDATE")
print(update_setting(test_settings, ("Theme", "light"))) # Success
print(update_setting(test_settings, ("Volume", "high"))) # Failure (not found)
# EXPECTED OUTPUT:
# Setting 'theme' updated to 'light' successfully!
# Setting 'volume' does not exist! Cannot update a non-existing setting.
print("-" * 40)

# ==========================================
# TEST 5: VIEW (Populated State)
# ==========================================
print("5. TEST VIEW (Populated)")
print(view_settings(test_settings))
# EXPECTED OUTPUT:
# Current User Settings:
# Theme: light
# Language: english
# Notifications: enabled
print("-" * 40)

# ==========================================
# TEST 6: DELETE (Success and Failure)
# ==========================================
print("6. TEST DELETE")
print(delete_setting(test_settings, "LANGUAGE")) # Success
print(delete_setting(test_settings, "font_size")) # Failure
# EXPECTED OUTPUT:
# Setting 'language' deleted successfully!
# Setting not found!
print("-" * 40)

# ==========================================
# TEST 7: CHECK FINAL RESULT
# ==========================================
print("7. CHECK FINAL DICTIONARY RESULT")
print(test_settings)
# EXPECTED OUTPUT:
# {'theme': 'light', 'notifications': 'enabled'}
print("--- TEST FINISHED ---")
