from bs4 import BeautifulSoup
import requests
from itertools import combinations

def find_coalitions(parties):
  """
  Finds all coalitions with a majority of seats.

  Args:
    parties: A dictionary mapping party names to their number of seats.
    seats: The total number of seats in Parliament.
    majority_threshold: The minimum number of seats needed for a majority.

  Returns:
    A list of lists, where each inner list represents a coalition with a majority.
  """

  seats = sum(parties.values())
  majority_threshold = seats // 2 + 1
  coalitions = []
  for i in range(1, len(parties) + 1):
    for combination in combinations(parties.keys(), i):
      total_seats = sum(parties[party] for party in combination)
      if total_seats >= majority_threshold:
        # Check if a subset of this coalition already has a majority
        is_redundant = False
        for j in range(1, len(combination)):
          for subset in combinations(combination, j):
            if sum(parties[party] for party in subset) >= majority_threshold:
              is_redundant = True
              break
          if is_redundant:
            break
        if not is_redundant:
          coalitions.append(list(combination))
  return coalitions


def get_table_data(url, table_id):
    """
    This function fetches a table from a web page and loads it into a Python list of lists.

    Args:
        url (str): The URL of the web page containing the table.
        table_id (str): The ID of the table element on the web page.

    Returns:
        list: A list of lists representing the table data.
    """

    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': table_id})

    table_data = []
    for row in table.find_all('tr'):
        row_data = []
        for cell in row.find_all(['th', 'td']):
            colspan = int(cell.get('colspan', 1))
            row_data.append(cell.text.strip())
            for _ in range(colspan - 1):
                row_data.append('')
        table_data.append(row_data)

    return table_data
