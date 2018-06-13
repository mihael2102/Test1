
def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome", help="Type in browser type")
    parser.addoption("--url", action="store", default="https://qa.moodle.net/", help="url")
    parser.addoption("--username", action="store", default="manager", help="username")
    parser.addoption("--password", action="store", default="test", help="password")
