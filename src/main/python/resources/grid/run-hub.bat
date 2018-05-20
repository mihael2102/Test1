set GRID_SERVER=C:/selenium-server-standalone-3.12.0.jar
set HUB_CONFIG=D:/automation-newforexqa/src/main/python/resources/grid/configurations/hub-config.json

java -jar %GRID_SERVER% -role hub -hubConfig %HUB_CONFIG%