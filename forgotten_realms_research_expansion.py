import webbrowser

url = "https://forgottenrealms.fandom.com/wiki/"

print("Enter your list with items separated by commas: ")
items = input()
items_list = items.split(",")

for item in items_list:
    webbrowser.open_new_tab(f"{url}{item}")
