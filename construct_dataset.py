from bs4 import BeautifulSoup
f = open("./2024-01/labor-stats.html", mode='r', encoding=None, newline=None)
soup = BeautifulSoup(f.read(), 'html.parser')

print(soup.get_text())

# for link in soup.find_all('li'):
#     print(link)

f.close()   