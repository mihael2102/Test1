set SELENIUM_SERVER=C:/selenium-server-standalone-3.4.0.jar
set HUB_ADDRESS= http://172.28.157.18:4478/grid/register/
set NODE_CONFIG=D:\MyWork\Develop\panda-project\scr\main\python\resources\grid\configurations\chrome-node-config.json
set DRIVER=D:\MyWork\Develop\panda-project\scr\main\python\resources\grid\drivers\chromedriver.exe

java -Dwebdriver.chrome.driver=%DRIVER% -jar %SELENIUM_SERVER% -role node -hub %HUB_ADDRESS% -nodeConfig %NODE_CONFIG%