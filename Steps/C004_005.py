from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

''' Check  coverimage '''
''' Date Added Sort  '''
class C004_005():
    def __init__(self, url, email, password, collection_txt):

        ''' --- Initialize URL, Email, Password --- '''
        self.url = 'https://' + url
        self.email = email
        self.password = password
        self.collection_txt = collection_txt

    def startSteps(self):

        pTxt = "\n-------- Step 'C004_005' started!!! --------------------------------------------------------------------"
        print(pTxt)

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

        ''' 1. Navigate to staging.getkumbu.com '''
        pTxt = "\n1. Navigate to staging.getkumbu.com\n"
        print(pTxt)
        try:
            self.driver.get(self.url)
            pTxt = "\t\t(Success)\tLoad webpage successfully"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tFailed to load webpage"
            print(pTxt)
            self.driver.quit()
            return

        ''' 2. Input email adress: kumbutest@mailinator.com '''
        pTxt = "\n2. Input email adress: kumbutest@mailinator.com\n"
        print(pTxt)

        try:
            inputs = WebDriverWait(self.driver, 50).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.kumbu-input"))
            )
        except:
            pTxt = "\t\t(Error)\tCan't find 'Email' and 'Password' Inputs"
            print(pTxt)
            self.driver.quit()
            return

        try:
            email_input = inputs[0]
            email_input.send_keys(self.email)
            pTxt = "\t\t(Success)\tInput email successfully"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tFailed to input 'email'"
            print(pTxt)
            self.driver.quit()
            return

        ''' 3. Input password: “kumbu is cool” '''
        pTxt = "\n3. Input password: 'kumbu is cool'\n"
        print(pTxt)

        try:
            pwd_input = inputs[1]
            pwd_input.send_keys(self.password)
            pTxt = "\t\t(Success)\tInputted 'Password' successfully"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tFailed to input 'Password'"
            print(pTxt)
            self.driver.quit()
            return

        ''' 4. Click Sign in '''
        pTxt = "\n4. Click Sign in\n"
        print(pTxt)
        try:
            submit_btn = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input#login-submit"))
            )
            submit_btn.click()
            pTxt = "\t\t(Success)\tClicked 'Sign in' button. Logged in successfully"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tFailed to click 'Sign in' button"
            print(pTxt)
            self.driver.quit()
            return

        ''' 5. Click on 'Collection for Test $TEST_NUMBER' '''
        pTxt = "\n5. Click on 'Collection for Test $TEST_NUMBER'\n"
        print(pTxt)
        try:
            collections = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, "div.collection.columns.small-12.medium-3.text-center"))
            )
            flag = False
            for collection in collections:
                if self.collection_txt in collection.text.strip():
                    flag = True
                    break

            if flag:
                try:
                    collection.click()
                    pTxt = "\t\t(Success)\tClicked Successfully"
                    print(pTxt)
                except:
                    pTxt = "\t\t(Error)\tFailed to click"
                    print(pTxt)
                    self.driver.quit()
                    return
            else:
                pTxt = "\t\t(Failure)\tFailed to click"
                print(pTxt)
                self.driver.quit()
                return
        except:
            pTxt = "\t\t(Error)\tFailed to click"
            print(pTxt)
            self.driver.quit()
            return

        ''' 5. Reload page '''
        pTxt = "\n5. Reload page\n"
        print(pTxt)
        self.driver.refresh()

        ''' 6. Sortby '''
        pTxt = "\n6. Sortby\n"
        print(pTxt)

        try:
            sortby_btn = WebDriverWait(self.driver, 100).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "li.is-dropdown-submenu-parent.opens-left > a"))
            )

            sortby_btn.click()

            sortbydate_btn = WebDriverWait(self.driver, 100).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "li.sort-by-date > a"))
            )
            sortbydate_btn.click()
            pTxt = "\t\t(Success)\tSofted by 'Date added'"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tFailed to softed by 'Date added'"
            print(pTxt)
            self.driver.quit()
            return


        self.driver.quit()
        return

if __name__ == '__main__':
    app = C004_005(url='staging.getkumbu.com', email='kumbutest@mailinator.com', password='kumbu is cool',
               collection_txt='Kumbu Test 6')
    app.startSteps()
