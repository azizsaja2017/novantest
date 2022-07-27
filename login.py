import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_login(self): 
        
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("novan.zip@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("qwerty123")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(5)
        
        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_b_gagal_login_password_kosong(self): 
        
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("novan.zip@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(5)
        
        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_c_gagal_login_email_password_kosong(self): 
        
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(5)
        
        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Email tidak valid', response_data)
        self.assertEqual(response_message, 'Cek kembali email anda')

if __name__ == "__main__": 
    unittest.main()