import ee

def initialize_earth_engine():
    ee.Initialize()

def get_historical_imagery(location, start_date, end_date):
    point = ee.Geometry.Point(location)
    collection = (ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')
                  .filterBounds(point)
                  .filterDate(start_date, end_date))
    return collection