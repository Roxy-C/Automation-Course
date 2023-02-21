import os, sys
import unittest
from ddt import ddt, data, unpack, file_data


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from infrastructure import Infrastructure
sys.path.append(r'C:\Users\RosFi\Code\Python\SeleniumProject\Locators')
from homepage_locators import HomepageLocators as HPL


logger = Infrastructure()

@ddt
class TestHomepage(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(os.getenv('HOMEPAGE_URL'))
        
    def setUp(self):
        self.driver.refresh()

    def test_set_text(self):
        try:
            set_text_button = self.driver.find_element(*HPL.setTextButton_locator)
            paragraph = self.driver.find_element(*HPL.setText_locator)
            actions = ActionChains(self.driver)
            
            actions.move_to_element(set_text_button).click().perform()
            alert = Alert(self.driver)
            alert.send_keys(os.getenv('SETTEXT_TEXT'))
            alert.accept()
            self.assertEqual(paragraph.text, os.getenv('SETTEXT_TEXT'))
            logger.log("Test testSetText Done")
        except Exception as e:
            logger.log("Test testSetText Failed")
            logger.log(str(e))
            self.driver.save_screenshot(r'Screenshots\Screenshot.png')
            
    def test_start_loading(self):
        try:
            startLoading_button = self.driver.find_element(*HPL.startLoadingButton_locator)
            paragraph = self.driver.find_element(*HPL.startLoading_locator)
            wait = WebDriverWait(self.driver, 5)
            
            self.assertEqual(paragraph.text, os.getenv('LOADING_PARAGRAPH_PRIOR'))
            startLoading_button.click()
            paragraph = wait.until(EC.text_to_be_present_in_element(HPL.startLoading_locator, os.getenv('LOADING_PARAGRAPH_AFTER')))
            logger.log("Test testStartLoading Done")
        except Exception as e:
            logger.log("Test testStartLoading Failed")
            logger.log(str(e))
            self.driver.save_screenshot(r'Screenshots\Screenshot.png')
            
    @file_data('data.json')
    def test_submit_form(self, first_name, last_name, email):
        try:
            firstname_element = self.driver.find_element(*HPL.firstname_locator)
            lastname_element = self.driver.find_element(*HPL.lastname_locator)
            email_element = self.driver.find_element(*HPL.email_locator)
            send_element = self.driver.find_element(*HPL.send_locator)
            
            firstname_element.send_keys(first_name)
            lastname_element.send_keys(last_name)
            email_element.send_keys(email)
            send_element.click()
            
            for element in [firstname_element, lastname_element, email_element]:
                if (element.get_attribute("value") == "" or element.get_property("validity")["typeMismatch"]):
                    if (element.get_property("validity")["valid"]):
                        raise Exception("Element is valid unconditionally!")
                        
            logger.log("Test testSubmitForm Done")
                
        except Exception as e:
            logger.log("Test testSubmitForm Failed")
            logger.log(str(e))
            self.driver.save_screenshot(r'Screenshots\Screenshot.png')
            
    def test_clear_fields(self):
        locators = [
            HPL.firstname_locator,
            HPL.lastname_locator,
            HPL.city_locator,
            HPL.email_locator,
            HPL.area_locator,
            HPL.phone_locator,
            HPL.male_locator,
            HPL.math_locator,
            HPL.physics_locator,
            HPL.pop_locator,
            HPL.dud_locator,
            HPL.biology_locator,
            HPL.chem_locator,
            HPL.english_locator
        ]
        fields = []
        for locator in locators:
            try:
                field = self.driver.find_element(*locator)
                field.click()
                fields.append(field)
            except Exception as e:
                logger.log((f"Failed to find element: {locator}"))
                logger.log(str(e))
            
        try:
            clear = self.driver.find_element(*HPL.clear_locator)
            clear.click()
        except Exception as e:
                logger.log(("Failed to find and click the clear button"))
                logger.log(str(e))

            
        for field in fields:
            try:
                assert field.get_attribute('value') == '' or not field.is_selected()
            except Exception as e:
                logger.log((f"Failed to assert that field {field} is empty"))
                logger.log(str(e))
                
        logger.log("Test test_clear_fields Done")
        
    def test_checkboxes(self):
        locators = [
            HPL.firstname_locator,
            HPL.lastname_locator,
            HPL.city_locator,
            HPL.email_locator,
            HPL.area_locator,
            HPL.phone_locator,
            HPL.male_locator,
            HPL.female_locator,
            HPL.other_locator,
            HPL.math_locator,
            HPL.physics_locator,
            HPL.pop_locator,
            HPL.dud_locator,
            HPL.biology_locator,
            HPL.chem_locator,
            HPL.english_locator
        ]
        fields = []
        for locator in locators:
            try:
                field = self.driver.find_element(*locator)
                field.click()
                fields.append(field)
                
            except Exception as e:
                logger.log((f"Failed to find element: {locator}"))
                logger.log(str(e))
                logger.log("Test test_clear_fields Failed")
        
        logger.log("Test test_checkboxes Done")