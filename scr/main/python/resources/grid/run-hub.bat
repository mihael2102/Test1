set GRID_SERVER=C:/selenium-server-standalone-3.4.0.jar
set HUB_CONFIG=D:/MyWork/Develop/panda-project/scr/main/python/resources/grid/configurations/hub-config.json

java -jar %GRID_SERVER% -role hub -hubConfig %HUB_CONFIG%