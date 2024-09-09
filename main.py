import ee
from earth_engine_utils import initialize_earth_engine, get_historical_imagery
from image_processing import perform_image_segmentation
from mindsdb_integration import connect_to_mindsdb, analyze_with_mindsdb

def detect_deforestation(location, start_date, end_date):
    imagery = get_historical_imagery(location, start_date, end_date)
    sorted_imagery = imagery.sort('system:time_start')
    earliest_image = ee.Image(sorted_imagery.first())
    latest_image = ee.Image(sorted_imagery.sort('system:time_start', False).first())
    
    earliest_segmented = perform_image_segmentation(earliest_image)
    latest_segmented = perform_image_segmentation(latest_image)
    
    change_map = latest_segmented.subtract(earliest_segmented)
    return change_map

if __name__ == "__main__":
    initialize_earth_engine()
    mdb = connect_to_mindsdb()
    
    location = [-63.0, -9.0]  # Example: A point in the Amazon rainforest
    start_date = '2015-01-01'
    end_date = '2023-01-01'
    
    change_map = detect_deforestation(location, start_date, end_date)
    deforestation_prediction = analyze_with_mindsdb(mdb, change_map)
    
    print(f"Deforestation prediction: {deforestation_prediction}")