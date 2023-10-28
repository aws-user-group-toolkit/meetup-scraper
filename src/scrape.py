import requests
from bs4 import BeautifulSoup

def get_member_count(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Update the following line to use the provided CSS selector
        member_count_element = soup.select_one('#member-count-link div')
        if member_count_element:
            member_count_text = member_count_element.text
            # Remove non-numeric characters (e.g., commas) and convert to an integer
            member_count = int(''.join(filter(str.isdigit, member_count_text)))
            return member_count
    else:
        print(f'Failed to retrieve page: {response.status_code}')
        return None

url = 'https://www.meetup.com/amazon-web-services-aws-vienna/'
member_count = get_member_count(url)
if member_count is not None:
    print(f'Member count: {member_count}')
