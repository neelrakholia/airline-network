# Visualization of Airport Network by Location
# http://www.milanor.net/blog/maps-in-r-plotting-data-points-on-a-map/

library(maps)
setwd("/Users/poorvibhargava/Documents/Stanford/Fall 2016/CS224w/airline-network")

# Read in data
latlonData <- read.csv('airport_latlon.csv', header = TRUE , sep = ",")
airportData <- read.csv('15-01-network-data.csv', header = TRUE, sep = ",")
latlonData <- unique(latlonData)
rownames(latlonData) <- latlonData$AIRPORT_ID
airportData <- airportData[which(airportData$FL_DATE=="2015-01-01"),]

# join two datasets
for (i in 1:length(airportData$ORIGIN_AIRPORT_ID)) {
  airportData$originLat[i] = latlonData$LATITUDE[min(which(latlonData$AIRPORT_ID == airportData$ORIGIN_AIRPORT_ID[i]))]
  airportData$originLongitude[i] = latlonData$LONGITUDE[min(which(latlonData$AIRPORT_ID == airportData$ORIGIN_AIRPORT_ID[i]))]
  airportData$destLat[i] = latlonData$LATITUDE[min(which(latlonData$AIRPORT_ID == airportData$DEST_AIRPORT_ID[i]))]
  airportData$destLongitude[i] = latlonData$LONGITUDE[min(which(latlonData$AIRPORT_ID == airportData$DEST_AIRPORT_ID[i]))]
}

# Plotting
map(database = "world", regions = ".")
points(latlonData$LONGITUDE, latlonData$LATITUDE, col = "red", cex = .6)
lines(x = c(airportData$originLongitude,airportData$destLongitude), y = c(airportData$originLat,airportData$destLat), col = "blue", lwd = .1)



