import requests
from bs4 import BeautifulSoup

# Deadlines = []
Objects = []
Model = []

Modules=["mathematiques","arabe","histoire-geographie","francais","anglais","physique","sciences-naturelles"]
Level=["1am","2am","3am","4am","1as","2as","3as"]
for i in Level:
  for j in Modules :

    url = f"https://www.dzexams.com/fr/{i}/{j}"
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        # Deadline = soup.find_all('button', {'class':'btn-group-content'})
        # titel = [row.text.strip() for row in Deadline]
        # titel_counts = Counter(titel)


        # Deadline = soup.find('button', {'class':'btn-group-content'})
        Object = soup.find_all('a', {'class':'btn-group-content'})

        # for link in soup.find_all('a', {'class':'btn-group-content'}):
        for k in range(len(Object)):
            # title = link.text.strip()
            # href = link['class']
            # links.append((title))
            Model.append(j)
            Objects.append(Object[k].text.strip())
            # Deadlines.append(Deadline.text.strip())
            # Deadlines.append(titel[k])

        # for title,count in titel_counts.items():
        #     print(f"TITEL: {title}_ nb {count}")

    else:
        print(f"FAILED CONNECT TO WEBSITE: {response.status_code}")
        
        
        
        
        
        
import csv
from itertools import zip_longest

# file_list = [Model,Deadlines,Objects]
file_list = [Model,Objects]
exported = zip_longest(*file_list)
with open('dz_exam_mat-3as2.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    # writer.writerow(['Model','Deadlines','Contents'])
    writer.writerow(['Model','Contents'])
    writer.writerows(exported)
print("Data Saved In dz_exam_mat-3as.csv!")