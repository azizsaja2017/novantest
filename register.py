import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRegister(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_register(self): 

        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("Novan Arditya P")
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("novan.zip11@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("qwerty123")
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')

    def test_b_register(self): 
        
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("Novan Arditya")
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("novan.zip@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Email/Username/Password tidak boleh kosong', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')

if __name__ == "__main__": 
    unittest.main()