from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time, pyperclip

''' Update Name '''
class P002():
    def __init__(self, url, email, password, profile_name):

        ''' --- Initialize URL, Email, Password --- '''
        self.url = 'https://' + url
        self.email = email
        self.password = password
        self.profile_name = profile_name

    def startSteps(self):

        pTxt = "\n-------- Step 'P002' started!!! --------------------------------------------------------------------"
        print(pTxt)

        #self.driver = webdriver.Firefox()
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

        ''' 5. Click on 'Kumbu Test' '''
        pTxt = "\n5. Click on 'Kumbu Test'\n"
        print(pTxt)
        try:
            profile_btn = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.profile-link"))
            )
            profile_btn.click()
            pTxt = "\t\t(Success)\tClicked 'Kumbu Test'"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tFailed to click 'Kumbu Test'"
            print(pTxt)
            self.driver.quit()
            return

        ''' 6. Click 'Edit Profile' '''
        pTxt = "\n6. Click 'Edit Profile'\n"
        print(pTxt)
        try:
            edit_btn = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a#show-edit-profile"))
            )
            edit_btn.click()
            pTxt = "\t\t(Success)\tClicked 'Edit Profile'"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tFailed to click 'Edit Profile'"
            print(pTxt)
            self.driver.quit()
            return

        ''' 7. Add $TEST_NUMBER at the end of the name field '''
        pTxt = "\n7. Add $TEST_NUMBER at the end of the name field\n"
        print(pTxt)
        try:
            inputs = WebDriverWait(self.driver, 50).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "form#profile-form > input"))
            )

            actionChains = ActionChains(self.driver)
            actionChains.click(inputs[0]).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL) \
                .send_keys(Keys.DELETE).send_keys(self.profile_name).perform()

            pTxt = "\t\t(Success)\t"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        ''' 8. Click Save Changes '''
        pTxt = "\n8. Click Save Changes\n"
        print(pTxt)
        try:
            save_btn = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input#profile-submit"))
            )

            save_btn.click()

            pTxt = "\t\t(Success)\tClicked Save Changes"
            print(pTxt)
        except:
            pTxt = "\t\t(Error)\tFailed to click Save Changes"
            print(pTxt)
            self.driver.quit()
            return

        ''' 9. Verify the 'Your personal data has been successfully changed' is displayed '''
        pTxt = "\n9. Verify the 'Your personal data has been successfully changed' is displayed\n"
        print(pTxt)
        try:
            usrname_txt = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "p.usernameValue"))
            )

            if self.profile_name is usrname_txt.text.strip():
                pTxt = "\t\t(Success)\t"
                print(pTxt)
            else:
                pTxt = "\t\t(Failure)\t"
                print(pTxt)
        except:
            pTxt = "\t\t(Error)\t"
            print(pTxt)
            self.driver.quit()
            return

        self.driver.quit()
        return

if __name__ == '__main__':
    app = P002(url='staging.getkumbu.com', email='kumbutest@mailinator.com', password='kumbu is cool',
               profile_name='Kumbu Test 5')
    app.startSteps()
