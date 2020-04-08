from selenium import webdriver
import pytest
from  selenium.webdriver.support import expected_conditions as EC
import time

class TestLogIn():
    def setup_method(self, method, driver='Firefox'):
        if driver == 'Firefox':
            self.driver = webdriver.Firefox()
        elif driver == 'Chrome':
            self.driver = webdriver.Chrome()
        elif driver =='IE':
            self.driver = webdriver.Ie()
        else:
            exit()

    def tear_down(self, method):
        self.driver.quit()

    def testLogin(self):
        self.driver.get(r'http://sso.test.k8s.ustax.com.cn/')
        self.driver.maximize_window()
        self.driver.find_element_by_css_selector("input.el-input__inner[type='text']")\
            .send_keys('17585571190')
        self.driver.find_element_by_css_selector("input.el-input__inner[type='password']") \
            .send_keys('resicoit999')
        self.driver.find_element_by_css_selector("button[class='el-button v-button-ok el-button--primary']"
                                                 "[type='button']") .click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//*[text()='客户管理']").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//*[text()='私有库']").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//*[text()='新增']").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//*[text()='保存']").click()
        self.driver.implicitly_wait(3)
        noCustName = self.driver.find_element_by_css_selector("from[class='el-form'] > div:nth-child(1)>div>div[class='el-input el-input--suffix']").text
        assert noCustName == '请输入客户名称'
        self.driver.find_element_by_css_selector("input.el-input__inner[placeholder='请输入客户名称']").send_keys('脚本私有库新增客户')

        '''    ul:nth-child(1)
        custMange = EC.visibility_of_all_elements_located(custmanger_element)
        if custMange:
            custmanger_element.click()
        else:
            pass
        '''