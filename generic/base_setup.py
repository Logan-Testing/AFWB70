import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Safari
from selenium.webdriver.support.wait import WebDriverWait
from pyjavaproperties import Properties
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BaseSetup:
    @pytest.fixture(autouse=True)
    def precondition(self):
        print('Accessing property file')
        pptobj = Properties()
        pptobj.load(open('config.properties'))
        gridurl = pptobj['GRIDURL']
        print("Grid URL", gridurl)
        usegrid = pptobj['USEGRID'].lower()
        print('UserGrid', usegrid)
        browser = pptobj['BROWSER'].lower()
        print('browser', browser)
        self.xl_path = pptobj['XL_PATH']
        print("XL PATH", self.xl_path)
        appurl = pptobj['APPURL']
        print('appurl', appurl)
        ito = pptobj['ITO']
        print('ito', ito)
        eto = pptobj['ETO']
        print('ETO', eto)

        if usegrid == 'yes':
            print("Executing in remote system")
            if browser == 'chrome':
                print('Open Chrome Browser')
                self.driver = Remote(gridurl, DesiredCapabilities.CHROME)
            elif browser == 'firefox':
                print('Open Firefox Browser')
                self.driver = Remote(gridurl, DesiredCapabilities.FIREFOX)
            else:
                print('Open Edge Browser')
                self.driver = Remote(gridurl, DesiredCapabilities.SAFARI)
        else:
            print("Executing in local system")
            if browser == 'chrome':
                print('Open Chrome Browser')
                self.driver = Chrome()
            elif browser == 'firefox':
                print('Open Firefox Browser')
                self.driver = Firefox()
            else:
                print('Open Edge Browser')
                self.driver = Safari()

        print('Enter the url', appurl)
        self.driver.get(appurl)
        print('maximize the browser')
        self.driver.maximize_window()
        print('Set ITO', ito, 'seconds')
        self.driver.implicitly_wait(ito)
        print('Set ETO', eto, 'seconds')
        self.wait = WebDriverWait(self.driver, eto)

    @pytest.fixture(autouse=True)
    def postcondtion(self):
        yield
        print('Close the browser')
        self.driver.quit()
