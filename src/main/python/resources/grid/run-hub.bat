set GRID_SERVER=D:\automation-newforexqa\src\main\python\resources\grid\server\selenium-server-standalone-3.4.0.jar
set HUB_CONFIG=configurations/hub-config.json

java -jar %GRID_SERVER% -role hub -hubConfig %HUB_CONFIG%