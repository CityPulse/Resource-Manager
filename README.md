CP_Resourcemanagement
=====================

This is the Resource Management by the EU project CityPulse. For now only the code is uploaded into this repository. Further documentation will come later.

The purpose of the Resource Management is to manage Data Wrappers, which are able to fetch observation from Smart City data sources. The folder "wrapper_dev" contains examplary Data Wrappers for traffic and parking data of the city of Aarhus, Denmark as well as weather, air quality and incidents of the city of Brasov, Romania.

License of historical data
--------------------------

Historical data sets for the [Aarhus parking](http://www.odaa.dk/dataset/parkeringshuse-i-aarhus) and the [Aarhus traffic](http://www.odaa.dk/dataset/realtids-trafikdata) data wrapper are collected from the Open Data Aarhus portal [ODAA](http://http://www.odaa.dk). The data is published under the Creative Commons-license CC0 or [CC-BY](https://creativecommons.org/licenses/by/4.0/legalcode). The format has been changed from JSON to CSV and the data has been sorted by the 'REPORT ID' or the 'GARAGECODE' respectively.