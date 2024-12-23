import requests
from bs4 import BeautifulSoup
import json

url = 'https://balad.ir/p/%D8%A8%DB%8C%D9%85%D8%A7%D8%B1%D8%B3%D8%AA%D8%A7%D9%86-%D8%AE%D8%A7%D8%AA%D9%85-%D8%A7%D9%84%D8%A7%D9%86%D8%A8%DB%8C%D8%A7-tehran-nei-zafar_hospital-11UoMVhyIx1fKp#15/35.76966/51.40822'


response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    comments = soup.find_all('p', class_='Comment_text__3C6If')

    comment_list = []
    for comment in comments:
        text = comment.get_text(strip=True)
        comment_list.append(text)
    
    with open('comments.json', 'w', encoding='utf-8') as f:
        json.dump(comment_list, f, ensure_ascii=False, indent=4)

    print("Comments have been written to 'comments.json'.")
else:
    print(f"خطا در دسترسی به صفحه: {response.status_code}")
