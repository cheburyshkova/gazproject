import requests
import openpyxl
from bs4 import BeautifulSoup

url = 'https://www.intergazcert.ru/register/certificates/active/products/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

def parse():
    try:
        req = requests.get(url=url, headers=headers)
        if req.status_code != 200:
            print(f'Error receiving page! Status code: {req.status_code}')
            return
    except Exception as err:
        print('Error', err)

    src = req.text
    soup = BeautifulSoup(src, 'lxml')

    col_headers = []
    for col_name in soup.find('thead').find('tr').find_all('th'):
        col_headers.append(col_name.text.strip().replace('\xa0', ''))

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.append(col_headers)

    for tr in soup.find('tbody').find_all('tr'):
        tr_data = tr.find_all('td')
        row = [i.text.strip().replace('\xab', '') for i in tr_data]
        worksheet.append(row)

    workbook.save('result.xlsx')

def main():
    parse()

if __name__ == '__main__':
    main()