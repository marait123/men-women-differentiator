import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver_path = "C:\\Windows\\chromedriver.exe"

# This is the path I use
# Put the path for your ChromeDriver here
browser = webdriver.Chrome(executable_path=driver_path)

browser.get("https://www.google.com/search?q=men&sxsrf=ALeKk01ASrKkwyX4TgisNI5bKGm8AwSj5A:1620421119490&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj9p9qJu7jwAhWfUhUIHc-GCPcQ_AUoAXoECAIQAw&biw=1229&bih=578")
# print(elements)
# scroll down
for i in range(50):
    print("scroll - {}".format(i))
    browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
time.sleep(10)
elements = browser.find_elements_by_class_name("rg_i")

for i, element in enumerate(elements):
    # break
    # print()
    src = element.get_attribute("src")
    # print("src is ", src)
    # requests.get(src)
    # file = open("image{}.png".format(i), "wb")
    # file.write(response.content)
    # file.close()
    # # break
    with open('men/Logo'+str(i)+'.png', 'wb') as file:
        # write file
        file.write(element.screenshot_as_png)
# time.sleep(10)
browser.quit()
