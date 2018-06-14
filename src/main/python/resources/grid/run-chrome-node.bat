set SELENIUM_SERVER=server/selenium-server-standalone-3.12.0.jar
set HUB_ADDRESS= http://localhost:4478/grid/register/
set NODE_CONFIG=configurations/chrome-node-config.json
set DRIVER=drivers/chromedriver.exe

java -Dwebdriver.chrome.driver=%DRIVER% -jar %SELENIUM_SERVER% -role node -hub %HUB_ADDRESS% -nodeConfig %NODE_CONFIG%