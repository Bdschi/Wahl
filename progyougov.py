from bs4 import BeautifulSoup
import requests
from itertools import combinations
import prognosenfunc

# Example usage:
url = 'https://www.wahlrecht.de/umfragen/yougov.htm'  # Replace with the actual URL
table_id = 'wilko'  # Replace with the actual table ID

table_content = prognosenfunc.get_table_data(url, table_id)

# Print the table data
for row in table_content:
    print(row)

for j in range(3, len(table_content)-2):
    print(f"{j}. {table_content[j+2][0]}") 
    parties={}
    for i in range(0, len(table_content[0])-5):
        print(f"\t{i}. {table_content[0][i+2]} ({table_content[j+2][i+2]})")
        number = table_content[j+2][i+2].replace(",", ".").replace("%", "")
        number = number.replace('–','0')
        seats = float(number)*10
        if seats>=50:
            parties[table_content[0][i+2]]=float(number)
    coalitions=prognosenfunc.find_coalitions(parties)
    for coalition in coalitions:
        print(f"\t {coalition}")
