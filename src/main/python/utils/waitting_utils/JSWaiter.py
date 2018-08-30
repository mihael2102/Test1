from selenium.webdriver.support.wait import WebDriverWait


class AngularLoad(object):
    def __init__(self, script_text_):
        self.script_text_ = script_text_

    def __call__(self, driver):
        return driver.execute_script(self.script_text_)

class JSWaiter(object):

    # Get the driver
    def set_driver(self, driver):
        js_wait_driver = driver
        js_wait = WebDriverWait(driver, 10)

    # Wait for Angular Load//Wait for Angular Load
    def wait_for_angular_load(self, driver):
        wait = WebDriverWait(driver, 10)


        angular_ready_script = "return angular.element(document).injector().get('$http').pendingRequests.length === 0"


        # Wait for ANGULAR to load обратить внимание на данный пункт. его логика для питона может быть не правильна
        # angular_load = driver.execute_script("return (window.angular !== undefined) && (angular.element(document).injector() !== undefined) && (angular.element(document).injector().get('$http').pendingRequests.length === 0)")


        # Get Angular is Ready
        is_ready_jquery_requests = driver.execute_script("return (window.jQuery != null)   && (jQuery.active === 0);")

        # Refactor and insert into JS executor
       function JsAndAjaxLoader(){
    // Loading of all elements on the page
    window.onload = function () { }

    // Checking the state of document
    counter = 1;
    var timerId = setInterval(function(counter) {
        if(counter < 7){
            if(document.readyState === 'complete') {
                clearInterval(timerId);
            }
        }
        counter = counter + 1;
      }, 1000);

    // Checking if there is any active ajax requests
    counter = 1;

    var interval = setInterval(function() {
        if((window.jQuery != null)   && (jQuery.active === 0)) {
            counter = counter + 1;
            clearInterval(interval);
            return true;
        } else if(counter < 7){
            clearInterval(interval);
            return false;
        }
    }, 100);
}


        # Wait ANGULAR until it is Ready!
        if not is_ready_jquery_requests:
            print("ANGULAR is NOT Ready!")
            wait.until(AngularLoad(angular_ready_script))
        else:
            print("Angular is ready")



