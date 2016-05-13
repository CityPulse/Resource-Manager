CP_Resourcemanagement
=====================

The Resource Management componentis responsible for managing all Data Wrappers. During runtime an application developer or the CityPulse framework operator can deploy new Data Wrappers to include data from new data streams. The folder "wrapper_dev" contains examplary Data Wrappers for traffic and parking data of the city of Aarhus, Denmark as well as weather, air quality and incidents of the city of Brasov, Romania. 
The Resource Management component can be used for the following types of scenarios:
* Fetch live stream data via one or more Data wrappers
* Replay historic data embedded in a Data wrapper


Requirements
------------
The Resource management is implemented in the programming language Python. The following Python packages have to be installed before using the component. The packages are available either in the package repository of the Ubuntu operating system or can be installed using PIP.

* Pika
* CherryPy
* Psycopg2
* NumPy
* SciPy
* SKLearn
* RDFlib
* Requests (version > 2.8)
* Requests-oauthlib
* Chardet

In addition, the following Ubuntu packages need to be installed in order to run the Resource management:

* python-pip
* libgeos++-dev
* libgeos-3.4.2
* python-dev
* libpq-dev
* git
* zip

Dependencies to other CityPulse components
------------------------------------------
For the Resource management in order to run properly it needs to have access to the following CityPulse components: Message Bus; Geospatial Data Infrastructure and the Knowledge Base (Triplestore).

Installation
------------
As mentioned before, the CityPulse Resource management requires additional libraries, which can be installed using the following command on an Ubuntu Linux installation. The Resource management is not limited to Ubuntu Linux, but no other Linux distribution has been tested so far.

	sudo apt-get install python-pip libgeos++-dev libgeos-3.4.2 python-dev libpq-dev python-scipy git automake bison flex libtool gperf unzip python-matplotlib

In addition, using the following command required python packages will be installed:
	sudo pip install pika cherrypy shapely psycopg2 numpy sklearn rdflib chardet requests requests-oauthlib

The Resource management uses the Virtuoso triplestore to store annotated observations. As of February 2016, the virtuoso provided with the apt-repository in Ubuntu 14.04 LTS is outdated and lacks required features. Therefore, an installation from the sources is necessary. This can be achieved with the followings commands:

	wget --no-check-certificate -q https://github.com/openlink/virtuoso-opensource/archive/stable/7.zip -O virtuoso-opensource.zip
	unzip -q virtuoso-opensource.zip
	cd virtuoso-opensource
	./autogen.sh
	./configure
	make
	sudo make install

After that start the virtuoso:

	sudo /etc/init.d/virtuoso-opensource-7 start

NOTE: the make command may hang after "VAD Sticker vad_dav.xml creation ..." if there is a virtuoso process running. Check with "ps ax|grep virtuoso" and kill if a virtuoso is running.

Afterwards you can download the Resource Management source code from the Github repository:

	git clone https://github.com/CityPulse/CP_Resourcemanagement.git

The next step is to edit the configuration file with your favourite editor. An example configuration can be found in virtualisation/config.json. For details about the configuration file see Table 1.
When running the Resource management in replay mode the python process may require a lot of file descriptors to read the historical data. Users may be required to increase a limit for file descriptors in the operating system. To change the limit on Mac OS X 10.10 and higher run the following command in a terminal:

	sudo launchctl limit maxfiles 2560 unlimited

This will set the limit to 2560. On Linux

	ulimit -n 2560

should do the trick. Add the line into the .bashrc in your home directory to make it permanent.


Configuration
-------------
The Resource management uses a configuration file to store the connection details to other components of the framework. The configuration is provided as JSON document named “config.json” within the “virtualisation” folder. The configuration consists of a dictionary object, where each inner element holds the connection details to one component of the framework, also as a dictionary. The following table lists all inner dictionary keys (bold) and their content.

<table style="border: 1px solid grey;" border="1px">
	<tr><td colspan="2" style="vertical-align: top; "><b>triplestore</b></td></tr>
	<tr><td style="vertical-align: top;">driver</td><td>The Resource Management supports the use of either Virtuoso or Apache Fuseki as triplestore. The value “sparql” tells the Resource Management to use Virtuoso. “fuseki” for Fuseki.</td></tr>
	<tr><td>host</td><td>The hostname/IP of the triplestore as string.</td></tr>
	<tr><td>port</td><td>The port of the triplestore as integer.</td></tr>
	<tr><td>path</td><td>The path to the sparql-endpoint.</td></tr>
	<tr><td>base_uri</td><td>The base URI is used to create the graph name</td></tr>
	<tr><td colspan="2" style="vertical-align: top;"><b>rabbitmq</b></td></tr>
	<tr><td>host</td><td>The hostname/IP of the message bus as string.</td></tr>
	<tr><td>port</td><td>The port of the message bus as integer.</td></tr>
	<tr><td colspan="2" style="vertical-align: top; "><b>interface</b></td></tr>
	<tr><td colspan="2">The configuration of the HTTP based API interface. The API is realised using the CherryPy framework. The configuration here is directly passed to CherryPy’s ‘quickstart’ method. Therefore all configuration options CherryPy provides are available. For more details see https://cherrypy.readthedocs.org/en/3.2.6/concepts/config.html#configuration.</td></tr>
	<tr><td colspan="2" style="vertical-align: top;"><b>gdi_db</b></td></tr>
	<tr><td>host</td><td>The hostname/IP of the geo-spatial database as string.</td></tr>
	<tr><td>port</td><td>The port of the geo-spatial database as integer.</td></tr>
	<tr><td>username</td><td>The username for the database as string.</td></tr>
	<tr><td>password</td><td>The user’s password for the database as string.</td></tr>
	<tr><td>database</td><td>The name of the database to use as string.</td></tr>
</table>

Running the component
---------------------
The Resource management is started via command line terminal. There are a series of command line arguments available to control the behaviour of the Resource management. In the following all command line arguments and their purpose.

<table>
<tr><td>Argument</td><td>Purpose</td></tr>
<tr><td>replay</td><td>Start in replay mode. In replay mode historic sensor observations between the time frame START and END are used instead of live data. Also the replay speed can be influenced by the speed argument. Requires that the Resource Management has been started at least once before.</td></tr>
<tr><td>from START</td><td>In replay mode determines the start date. The format is “%Y-%m-%dT%H:%M:%S“.</td></tr>
<tr><td>to END</td><td>In replay mode determines the end date. The format is “%Y-%m-%dT%H:%M:%S”.</td></tr>
<tr><td>messagebus</td><td>Enable the message bus feature. The Resource Management will connect to the message bus and publish new observation as soon as they are made.</td></tr>
<tr><td>triplestore</td><td>Enable the triplestore feature.</td></tr>
<tr><td>aggregate</td><td>Use the aggregation method, as specified in the SensorDescription, to aggregate new observations.</td></tr>
<tr><td>speed SPEED</td><td>In replay mode determines the speed of the artificial clock. The value range is [0-1000]. An artificial second within the replay will take 1000 – SPEED milliseconds.</td></tr>
<tr><td>gdi</td><td>Geospatioal Database Injection. Newly registered Data wrappers are reported to the Geospatioal Database.</td></tr>
<tr><td>gentle</td><td>Reduces the CPU load in replay mode, but slower.</td></tr>
<tr><td>cleartriplestore</td><td>Deletes all graphs in the triplestore (may take up to 300s per wrapper!)</td></tr>
<tr><td>restart</td><td>Restarts the Resource Management with the same arguments as last time.</td></tr>
<tr><td>eventannotation</td><td>The Resource Management will listen on the message bus for new events to semantically annotate them and store them into the triplestore. Last feature requires the triplestore argument.</td></tr>
</table>

Link
----
TODO



License of historical data
--------------------------

Historical data sets for the [Aarhus parking](http://www.odaa.dk/dataset/parkeringshuse-i-aarhus) and the [Aarhus traffic](http://www.odaa.dk/dataset/realtids-trafikdata) data wrapper are collected from the Open Data Aarhus portal [ODAA](http://http://www.odaa.dk). The data is published under the Creative Commons-license CC0 or [CC-BY](https://creativecommons.org/licenses/by/4.0/legalcode). The format has been changed from JSON to CSV and the data has been sorted by the 'REPORT ID' or the 'GARAGECODE' respectively.