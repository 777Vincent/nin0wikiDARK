import requests
from bs4 import BeautifulSoup

# URL of the Userstyles.world page
url = 'https://userstyles.world/style/18562/nin0wiki-material-dark'

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the CSS from the <code> tag
code_tag = soup.find('code')
css_content = code_tag.text if code_tag else ''

# Save the CSS content to a file
with open('style.css', 'w') as file:
    file.write(css_content)

print("CSS has been extracted and saved to style.css")
