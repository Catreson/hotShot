import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import subprocess

def getHotShot(url):
    driver = uc.Chrome(headless=False, use_subprocess=False)
    driver.get(url)
    try:
        example_div = driver.find_element(By.ID, 'hotShot')

        span_element = example_div.find_elements(By.TAG_NAME, 'span')
        p_element = example_div.find_elements(By.TAG_NAME, 'p')

        span_text = [x.text for x in span_element]
        p_text = [x.text for x in p_element]

    except:
        print('Eror')

    finally:
        driver.close()
        return span_text[2], p_text[0]

if __name__ == '__main__':
    url = 'https://x-kom.pl'
    result = 'eror'
    name, price = getHotShot(url)
    if name:
        result = subprocess.run(['ollama', 'run', 'dolphin-mixtral:latest',  f'\'Is {price} good price for {name}?\
                              Answer only "Yes, because it is below average price which is:"\
                              or "No, because it is above average price which is:"\''], stdout=subprocess.PIPE)
        result.stdout.decode('utf-8')
    print(result)