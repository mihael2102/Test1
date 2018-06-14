set GRID_SERVER=server/selenium-server-standalone-3.12.0.jar
set HUB_CONFIG=configurations/hub-config.json

java -jar %GRID_SERVER% -role hub -hubConfig %HUB_CONFIG%