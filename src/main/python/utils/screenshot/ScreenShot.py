class ScreenShot(object):

    def __init__(self, driver):
        self.driver = driver

    def perform_screen_shot(self, path):
        directory = "D:/automation-newforexqa/src/screen_shots/passed_screenshots"
        self.driver.get_screenshot_as_file(directory + path)
