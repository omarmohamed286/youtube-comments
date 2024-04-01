from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class CommentScraping:
    def __init__(self,video_url):
        self.video_url = video_url

    def get_comments(self):
        comments=[]

        driver = webdriver.Chrome()
        driver.get(self.video_url)

        driver.maximize_window()

        for i in range(30):
            driver.execute_script("window.scrollBy(0,700)","")
            sleep(2)
    
        comment=driver.find_elements(By.XPATH,"""//*[@id="content-text"]/span""")
        for i in comment:
            if i.text and i.text != ' ' and len(i.text) <= 512 :
                comments.append(i.text)

        return comments
