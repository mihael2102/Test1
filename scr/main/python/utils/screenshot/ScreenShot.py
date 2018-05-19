
class ScreenShot(object):

    def __init__(self, driver):
        self.driver = driver

    def PerfomScreenShot(self, path):
        directory = "D:/automation-newforexqa/screen_errors"
        self.driver.get_screenshot_as_file(directory + path)
