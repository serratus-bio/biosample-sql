attrib = ["lat_lon", "latitude_and_longitude",
          "geographic_location_longitude",
          "geographic_location_latitude", "longitude", "latitude",
          "lat_lo_n", "decimallatitude", "decimallongitude", 
          "geographic_location_latitude_and_longitude", "geographic_location_longitude*",
          "geographic_location_latitude*", "decimal_longitude", "decimal_latitude",
          "lat_lo", "latitude_deg", "longitude_deg", "longitude_raw", "latitude_raw",
          "longitude.dd", "latitude.dd","lati", "longitdue", "latitudinal_degrees",
          "longitudinal_degrees","soil_lat_lon_site_1","soil_lat_lon_site_2",
          "lat_long","lat_lon_n:w","latitude_[n]","longitude_[e]", "gps_latitute_s",
          "gps_longitude_w", "longitude_provided", "latitude_provided",
          "source_longitude_latitude_elevm", "lat_lan", "latitude_longitude",
          "lon_lat", "latitude_and_longtitude","dec_longitude","dec_lattitude",
          "specimen_collection_location___longitude",
          "specimen_collection_location___latitude",
          "geographic_location_latitude_longitude", "longitude_latitude",
          "latitude_and_logitude", "lat___lon", "multiple_lat_lon",
          "submitted_lat_lon","longittude",
          "gographic_location_longitud",
          "geographic_location_latitude_and_____________________longitude",
          "geographical_location_longitude_and_longitude",
          "vv_long",
          "vv_lat",
          "geographic_coordinates", "latitude_and_longitude_3", "latlong_information",
          "latitude_and_longitude_2", "lat_lon_2", "lat_long_details",
          "geographical_location_lat_lon"]
potential_coord_attrs = set(attrib)
potential_geo_text_attrs = {"geo_loc_name"}
collection_date_attr = "collection_date"

# lat_lon_pattern = '^(-?\d+(\.\d+)?)\s*(\w)*\s*(-?\d+(\.\d+)?)\s*(\w)*$'
