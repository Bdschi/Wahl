from bs4 import BeautifulSoup
import requests
from itertools import combinations
import prognosenfunc

states =[ 'hamburg', 'schleswig-holstein', 'niedersachsen', 'bremen', 'rheinland-pfalz', 'saarland', 'nordrhein-westfalen', 'hessen', 'baden-wuerttemberg', 'bayern', 'mecklenburg-vorpommern', 'brandenburg', 'berlin', 'thueringen', 'sachsen-anhalt', 'sachsen' ]
print("Available states of Germany:")
for i, state in enumerate(states):
        print(f"{i+1}. {state}")

# Get user input
choice = input("Enter the number of your choice: ")

# Validate user input
try:
    choice = int(choice)
    if 1 <= choice <= len(states):
                print(f"You chose: {states[choice-1]}")
    else:
                print("Invalid choice. Please enter a number between 1 and", len(states))
except ValueError:
        print("Invalid input. Please enter a number.")

url = 'https://www.wahlrecht.de/umfragen/landtage/' + states[choice-1]  + '.htm'
table_id = 'wilko'  # Replace with the actual table ID

table_content = prognosenfunc.get_table_data(url, table_id)

# Print the table data
for row in table_content:
    print(row)

for j in range(0, len(table_content)-2):
    if table_content[j+2][5] == '':
        continue
    print(f"{j}. {table_content[j+2][0]} ({table_content[j+2][3]})") 
    cols=len(table_content[0])-6
    parties={}
    for i in range(0, cols):
        print(f"\t{i}. {table_content[0][i+5]} ({table_content[j+2][i+5]})")
        number = table_content[j+2][i+5].replace(",", ".").replace("%", "").replace("?","0").replace("*","")
        number = number.replace('–','0')
        seats = float(number)*10
        if seats>=50:
            parties[table_content[0][i+5]]=float(number)
    coalitions=prognosenfunc.find_coalitions(parties)
    for coalition in coalitions:
        print(f"\t {coalition}")
