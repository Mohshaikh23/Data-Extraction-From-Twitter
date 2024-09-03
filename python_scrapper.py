import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

def parse_html(element):
    html = element.get_attribute("outerHTML")
    soup = BeautifulSoup(html, 'html.parser')
    return soup


try:
    #Login Details
    driver.get("https://x.com/login")
    time.sleep(10)
    username= driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
    username.clear()
    username.send_keys("Your userID")
    next_button = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
    next_button.click()
    time.sleep(5)
    password = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.clear()
    password.send_keys("Your Password")
    login_btn = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
    login_btn.click()

    time.sleep(5)

    # Data Scrapping

    
    data = {
        "Name": [], 
        "Username": [],
        "Joining": [],
        "Following": [], 
        "Followers": [],
        "Posts": [],
        "Banner": [], 
        "Profile": [],
        "Article 1": [],
        "Article 2": [],
        "Article 3": [],
        "Article 4": [],
        "Article 5": []
    }

    with open('abc.txt', 'r') as f:
        characters = f.readlines()
    
    for character in characters:
        char = character.strip()
        new_char = char.replace("@", "")
        driver.get(f'https://x.com/{char}')
    
        print(f"Parsing data of - {char}")
        time.sleep(10)
        
        try:
            name_ele = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div')
            name_text = parse_html(name_ele).find('div',attrs={'class':'css-175oi2r r-xoduu5 r-1awozwy r-18u37iz r-dnmrzs'}).get_text(strip=True)
        except Exception as e:
            print(f"Error finding Name for {char}: {e}")
            name_text = None  
        try:
            username_ele = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/span')
            username_text = parse_html(username_ele).get_text()
        except Exception as e:
            print(f"Error finding Username for {char}: {e}")
            username_text = None

        try:
            posts_ele = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div')
            posts_num = parse_html(posts_ele).get_text().replace(" posts", "")
        except Exception as e:
            print(f"Error finding Posts number for {char}: {e}")
            posts_num = None

        try:
            banner_ele = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/a')
            banner_pic_link = "https://www.X.com" + BeautifulSoup(banner_ele.get_attribute("outerHTML"), 'html.parser').find('a')['href']
        except Exception as e:
            print(f"Error finding Banner link for {char}: {e}")
            banner_pic_link = None

        try:
            profile_pic_ele = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div/div[2]/div/a')
            profile_pic_link = "https://www.X.com" + BeautifulSoup(profile_pic_ele.get_attribute("outerHTML"), 'html.parser').find('a')['href']
        except Exception as e:
            print(f"Error finding Profile picture link for {char}: {e}")
            profile_pic_link = None

        try:
            data_ele = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div')
            soup = parse_html(data_ele)

            followers = soup.find("a", href=f'/{new_char}/verified_followers')
            followers_count = followers.get_text(strip=True).replace("Followers", "").strip() if followers else ""

            following = soup.find("a", href=f'/{new_char}/following')
            following_count = following.get_text(strip=True).replace("Following", "").strip() if following else ""

            joined_date = soup.find('span', attrs={'data-testid': "UserJoinDate"})
            joined_date_text = joined_date.get_text(strip=True).replace('Joined ', "").strip() if joined_date else ""
        except Exception as e:
            print(f"Error extracting data for {char}: {e}")
            followers_count, following_count, joined_date_text = None, None, None

        try:
            articles = soup.find_all('div', attrs={'data-testid': "tweetText"})
            for i in range(5):
                if i < len(articles):
                    data[f"Article {i+1}"].append(articles[i].get_text(strip=True))
                else:
                    data[f"Article {i+1}"].append("")
        except Exception as e:
            print(f"Error extracting articles for {char}: {e}")
            for i in range(5):
                data[f"Article {i+1}"].append("")

        data["Name"].append(name_text)
        data["Username"].append(username_text)
        data["Joining"].append(joined_date_text)
        data["Following"].append(following_count) 
        data["Followers"].append(followers_count)
        data["Posts"].append(posts_num)
        data["Banner"].append(banner_pic_link)
        data["Profile"].append(profile_pic_link)

        print(f"{char} data parsed")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(5)
    driver.quit()
    df = pd.DataFrame(data)
    df.to_csv('Fetched_Data.csv', index=False)
