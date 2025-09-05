from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

# إعداد كروم بوضع التخفي (بدون واجهة)
chrome_options = Options()
chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://shamela.ws/book/11788")

# الانتظار حتى يتم تحميل العناصر
driver.implicitly_wait(20)

# جلب جميع الروابط داخل عناصر class="s-nav"
links = driver.find_elements(By.CSS_SELECTOR, ".betaka-index a")

# تجهيز البيانات في قائمة قواميس مع منع التكرار
data = []
seen_urls = set()

for link in links:
    href = link.get_attribute("href")
    text = link.text.strip()

    # تجاهل الروابط الفارغة أو التي تبدأ بـ javascript:
    if not href or href.strip().lower().startswith("javascript:"):
        continue

    # تجاهل الروابط المكررة (نفس الرابط حتى لو النص مختلف)
    if href in seen_urls:
        continue
    seen_urls.add(href)

    data.append({"text": text, "url": href})

# حفظ البيانات في ملف JSON
with open("s_nav_links.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"تم حفظ {len(data)} رابط (بدون تكرار) في s_nav_links.json")

driver.quit()