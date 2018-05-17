
class ScreenShot(object):

    def __init__(self, driver):
        self.driver = driver

    def PerfomScreenShot(self, path):
        directory = "D:/glo-panda-fx/glo-project/screen_shots"
        self.driver.get_screenshot_as_file(directory + path)
