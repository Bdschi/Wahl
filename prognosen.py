from bs4 import BeautifulSoup
import requests
from itertools import combinations
import prognosenfunc

# Example usage:
url = 'https://www.wahlrecht.de/umfragen/'  # Replace with the actual URL
table_id = 'wilko'  # Replace with the actual table ID

table_content = prognosenfunc.get_table_data(url, table_id)

# Print the table data
for row in table_content:
    print(row)

for i in list(range(0, len(table_content[0])-4))+[len(table_content[0])-3]:
    print(f"{i}. {table_content[0][i+2]} ({table_content[1][i+2]})")
    parties={}
    for j in range(0, len(table_content)-4):
        print(f"\t{j}. {table_content[j+2][0]} {table_content[j+2][i+2]}") 
        number = table_content[j+2][i+2].replace(",", ".").replace("%", "")
        number = number.replace('–','0')
        seats = float(number)*10
        if seats>=50:
            parties[table_content[j+2][0]]=float(number)
    coalitions=prognosenfunc.find_coalitions(parties)
    for coalition in coalitions:
        print(f"\t {coalition}")
