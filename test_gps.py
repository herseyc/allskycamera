###################################
# function which returns GPS data #
###################################
from gps3 import agps3
import time

USE_GPS = True

def get_gps_data():
    '''
    Get GPS Data from GPS device or user configured values  and return tuple 
    (gpsfixtype, gpslatdms, gpslondms, gpsaltitude, gpslatitude, gpslongitude, gps_data)
    '''
    gps_data = []

    if USE_GPS:   
        # GPS Data
        the_connection = agps3.GPSDSocket()
        the_fix = agps3.DataStream()
        the_connection.connect()
        the_connection.watch()
        for new_data in the_connection:
           if new_data:
              the_fix.unpack(new_data)
              if the_fix.mode != "n/a" and the_fix.lat != "n/a" and the_fix.lon != "n/a":
                  gpsfixtype = the_fix.mode
                  gpslatitude = the_fix.lat
                  gpslongitude = the_fix.lon
                  if gpsfixtype != 3:
                      gpsaltitude = MY_ELEVATION
                  else:
                     gpsaltitude = the_fix.alt

                  gpslatdms = gpslatitude
                  gpslondms = gpslongitude
                  #gpslatdms = convert_dd_to_dms(gpslatitude)
                  #gpslondms = convert_dd_to_dms(gpslongitude)
                  gps_data = [gpsfixtype, gpslatdms, gpslondms, gpsaltitude]
                  break
              else:
                 time.sleep(.5)

        the_connection.close()
        
    return (gpsfixtype, gpslatdms, gpslondms, gpsaltitude, gpslatitude, gpslongitude, gps_data)


print(get_gps_data())
