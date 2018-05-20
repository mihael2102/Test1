set SELENIUM_SERVER=D:\automation-newforexqa\src\main\python\resources\grid\server\selenium-server-standalone-3.12.0.jar
set HUB_ADDRESS= http://10.0.0.94:4478/grid/register/
set NODE_CONFIG=D:\automation-newforexqa\src\main\python\resources\grid\configurations\chrome-node-config.json
set DRIVER=D:\automation-newforexqa\src\main\python\resources\grid\drivers\chromedriver.exe

java -Dwebdriver.chrome.driver=%DRIVER% -jar %SELENIUM_SERVER% -role node -hub %HUB_ADDRESS% -nodeConfig %NODE_CONFIG%



