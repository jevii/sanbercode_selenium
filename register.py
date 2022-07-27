import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegist(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_regist(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("usertest") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("user01@mail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("masuk") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')

    def test_b_failed_regist_with_email_have_been_regist(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("user123") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("user123@mail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("masuk") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('sudah terdaftar', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')

    def test_c_failed_regist_with_empty_name(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("user12@mail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("masuk") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('kosong', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')

    def test_c_failed_regist_with_empty_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("test") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("masuk") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('kosong', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')

    def test_c_failed_regist_with_empty_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("test") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("user12@mail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('kosong', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
