test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

def add_setting(settings, key_value_pair):
    key, value = key_value_pair

    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, key_value_pair):
    key, value = key_value_pair

    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    else:
        return f"Setting '{key}' does not exist! Cannot update a non- existing setting."

def delete_setting(settings, key):
    key = key.lower()

    if key not in settings:
        return "Setting not found!"

    del settings[key]
    return f"Setting '{key}' deleted successfully!"
    

def view_settings(settings):
    if not settings:
        return "No settings available."

    current_settings = "Current User Settings:\n"
    for setting, value in settings.items():
        current_settings += f"{setting.capitalize()}: {value}\n"
        #print(f"{setting.capitalize()}: {value}")
    
    return current_settings.strip()


print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
