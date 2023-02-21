import unittest, os
from selenium import webdriver
from dotenv import load_dotenv
from infrastracture import Infrastracture

logger = Infrastracture()

class BasePageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('file:///C:/Users/RosFi/Code/Python/SeleniumProject/Tests/Automation%20Project.html')

    def tearDown(self):
        self.driver.quit()
        
    def testTitle(self, titleENV):
        try:
            self.assertEqual(self.driver.title, os.getenv(titleENV))
            logger.log("Test testTitle Done")
        except Exception:
            logger.log("Test testTitle Failed")