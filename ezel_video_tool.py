import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

init(autoreset=True)  # Renkleri otomatik sıfırlar

# Renkli "EZEL" Banner
print(Fore.RED + Style.BRIGHT + """
███████╗███████╗███████╗██╗     
██╔════╝██╔════╝██╔════╝██║     
█████╗  █████╗  █████╗  ██║     
██╔══╝  ██╔══╝  ██╔══╝  ██║     
███████╗███████╗██║     ███████╗
╚══════╝╚══════╝╚═╝     ╚══════╝
""")

url = input(Fore.CYAN + "Video URL'sini gir: ")

headers = {
    'authority': 'fbvideodownloaderapp.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://fbvideodownloaderapp.com',
    'referer': 'https://fbvideodownloaderapp.com/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36'
}
data = {'URLz': url}

response = requests.post('https://fbvideodownloaderapp.com/download.php', headers=headers, data=data)
soup = BeautifulSoup(response.text, 'html.parser')
wizard = soup.find_all('a', class_='btn btn-primary btn-sm')

print(Fore.GREEN + "\n[+] Bulunan Video Linkleri:\n")
for wizo in wizard:
    print(Fore.YELLOW + wizo['href'] + "\n")
