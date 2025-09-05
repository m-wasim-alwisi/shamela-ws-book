from bs4 import BeautifulSoup
import json
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from urllib.parse import urljoin

# قراءة ملف JSON يحتوي على عناوين URL
with open('C:\\Users\\user\\Desktop\\s_nav_links.json', 'r', encoding='utf-8') as f:
    urls_data = json.load(f)

# تأكد أن البيانات هي قائمة من عناوين URL
if isinstance(urls_data, list):
    urls = urls_data
elif isinstance(urls_data, dict) and 'urls' in urls_data:
    urls = urls_data['urls']
else:
    raise ValueError("صيغة ملف JSON غير صالحة. يجب أن تكون مصفوفة أو كائن يحتوي على مفتاح 'urls'")

output_file = "extracted_texts.txt"

# معالجة كل عنصر
for item in urls_data:
    # استخراج الـ URL من الهيكل
    if isinstance(item, dict) and 'url' in item:
        url = item['url']
        title = item.get('text', 'بدون عنوان')  # الحصول على النص إذا كان موجوداً
    elif isinstance(item, str):
        url = item
        title = url
    else:
        print(f"عنصر غير معروف: {item} - سيتم تخطيه")
        continue
        
    print(f"\n{'='*50}\nمعالجة الرابط: {title}\nالعنوان: {url}\n{'='*50}")
    try:
            
        service = Service()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")  # Run in headless mode
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(str(url))
        driver.implicitly_wait(10)  # Wait for dynamic content
        html = driver.page_source

        # Create a BeautifulSoup object
        soup = BeautifulSoup(html, 'html.parser')

        # Find all the program divs
        program_divs = soup.find_all("div", class_="nass")
        
        if not program_divs:
            print(f"لم يتم العثور على عناصر في: {url}")
            driver.quit()
            continue
        
        # فتح ملف الإخراج للإلحاق (بترميز UTF-8)
        with open(output_file, 'a', encoding='utf-8') as f_out:

            f_out.write(f"\n\n{'='*50}\nنتائج الرابط: {url}\n{'='*50}\n")
            
            for i, div in enumerate(program_divs, 1):
                text = div.get_text(strip=True)
                cleaned_text = ' '.join(text.split())

                # كتابة إلى الملف
                f_out.write(cleaned_text + "\n")
        
        print(f"تم حفظ النصوص من {url} في {output_file}")
        
    except Exception as e:
        print(f"حدث خطأ أثناء معالجة {url}: {str(e)}")
    finally:
        if driver:
            driver.quit()
print(urls)
print("\nFinished")
print(f"saved at {output_file}")