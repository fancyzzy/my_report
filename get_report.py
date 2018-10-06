# -*- coding: utf-8 -*-

from selenium import webdriver
import selenium
import os

#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import NoAlertPresentException

URL = "http://52.38.165.143:3000/?orgId=1"
URL_DATA = "http://52.38.165.143:3000/dashboard/db/daily-report-4know?orgId=1"
PWD = os.getenv("REPORT_PWD", None)


class Get_Report():
    def __init__(self):
        self.bw = webdriver.Firefox(executable_path = "C:\Program Files (x86)\Mozilla Firefox\geckodriver.exe")
        self.bw.implicitly_wait(30)


    def login(self):
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.set_headless()

        self.bw.get(URL)

        self.bw.find_element_by_name("username").send_keys("admin")
        self.bw.find_element_by_id("inputPassword").send_keys(PWD)
        self.bw.find_element_by_css_selector("button.btn.btn-large.p-x-3.btn-primary").click()

    def get_value(self):

        self.bw.get(URL_DATA)

        txt = self.bw.find_element_by_id("setf").text
        print("txt: {}".format(txt))

        '''
        urllist1 = {
            'launcher': 'http://52.38.165.143:3000/dashboard/db/daily-report-launcher?orgId=1',
            '4know': 'http://52.38.165.143:3000/dashboard/db/daily-report-4know?orgId=1',
            'appstore': 'http://52.38.165.143:3000/dashboard/db/daily-report-appstore?orgId=1',
            'basicservice': 'http://52.38.165.143:3000/dashboard/db/daily-report-basicservice?orgId=1',
        }
        '''
        self.bw.set_window_size(1920, 3800)

        for i in urllist1.keys():
            self.bw.get(urllist1[i])
            time.sleep(20)#60
            self.bw.get_screenshot_as_file(i + ".png")

if __name__ == "__main__":

    print("Start")
    my_report = Get_Report()
    my_report.login()
    my_report.get_value()
    print("Done.")




