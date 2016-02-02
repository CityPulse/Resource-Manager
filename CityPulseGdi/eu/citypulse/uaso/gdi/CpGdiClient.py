'''
Created on Aug 4, 2015

@author: danielk,uaso
'''

import uuid
from CityPulseGDInterface import CityPulseGDInterface

if __name__ == '__main__':
    print('starting GdiTest')
    gdi=CityPulseGDInterface()
    uuid1=str(uuid.uuid4())
    uuid2=str(uuid.uuid4())
    print(uuid1)
    print(gdi.registerSensorStreamFromPointLonLat(uuid1, "900913", "Aarhus_Road_Traffic",uuid2,10.0, 56.0))
    #next one should become false due to same uuid
    print(gdi.registerSensorStreamFromPointLonLat(uuid1, "900913", "Aarhus_Road_Traffic",uuid2,10.0, 56.0))
    print(gdi.registerSensorStreamFromPoint(str(uuid.uuid4()), "900913", "Aarhus_Road_Traffic",uuid2,10.0, 56.0,4326))
    print(gdi.registerSensorStreamFromPoint(str(uuid.uuid4()), "900913", "Brasov_Road_Traffic",uuid2,25.55691529433881, 45.587838521405224 ,4326))
    print(gdi.registerSensorStreamFromPoint(str(uuid.uuid4()), "900913", "Brasov_Road_Traffic",uuid2,543596.363572, 454379.287188, 31700))
    print(gdi.registerSensorStreamFromWKT(str(uuid.uuid4()), "900913", "Aarhus_Road_Traffic",uuid2,"POINT(10.0 56.0)", 4326))
    print(gdi.registerSensorStreamFromWKT(str(uuid.uuid4()), "900913", "Aarhus_Road_Traffic",uuid2,"POINT(543596.363572 454379.287188)", 31700))
    print(gdi.getSensorStream(uuid1))
    print(gdi.removeSensorStream(uuid1))
    print("finished GdiTest")