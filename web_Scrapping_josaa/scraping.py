import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('./final_web_scraping/JoSAA_2020_6.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table with the specified ID
table = soup.find('table', {'id': 'ctl00_ContentPlaceHolder1_GridView1'})

# Initialize a list to store the data
data = []

# Extract data from the table
rows = table.find_all('tr')
serial_number = 1

# # finding out the number of elements in the table
print(len(rows))
# print()
# for i in rows[1].find_all('td'):
#     print(i.text.strip())   

len(rows)
for row in rows[1:]:  # Skip the header row
    columns = row.find_all('td')
    if columns[1].span == None:
        break
    
    if serial_number <len(rows):
        
        
        # Extract data from each column
        institute = columns[0].text.strip()
        program_name = columns[1].span.text.strip()
        quota = columns[2].span.text.strip()
        category = columns[3].span.text.strip()
        gender = columns[4].span.text.strip()
        opening_rank = columns[5].span.text.strip()
        closing_rank = columns[6].span.text.strip()

        #print all
        print(f"{serial_number}. {institute}, {program_name}, {quota}, {category},{gender},{opening_rank}, {closing_rank}")  
    
    # Create a dictionary for the row
    row_data = {
        'Serial Number': serial_number,
        'Institute': institute,
        'Program Name': program_name,
        'Quota': quota,
        'Category': category,
        'Gender': gender,
        'Opening Rank': opening_rank,
        'Closing Rank': closing_rank
    }
    
    data.append(row_data)
    serial_number += 1

# Write the data to a CSV file
with open('./final_web_scraping/files/2020-6_with_serial.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Serial Number', 'Institute', 'Program Name', 'Quota', 'Category', 'Gender', 'Opening Rank', 'Closing Rank']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(data)

print("Data has been written to output.csv")