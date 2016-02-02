
# ===================================================================
# = model.py - Core and External Classes of the SAO Ontology
# 						SAOPY version 002
# =            Generated automatically on Wed Jan  6 14:54:12 2016
# ===================================================================


import sys
from saopy.PropertySet import PropertySet, protector


def objToStr(c):
	s = "-- "+c.shortname
	if c.URI != None :
		s+=" @ "+unicode(c.URI)
	s+=" --\n"
	for p in c._props.keys():
		for v in c._props[p]:
			s+=c._props[p].shortname + " : "
			if isinstance(v, c._props[p].Lits):
				s+=unicode(v)
			else:
				s+=str(type(v))
				if hasattr(v,"URI") and v.URI != None:
					s+=" @ "+v.URI
			s +="\n"
	return s.encode(sys.getdefaultencoding(), 'replace')

# ======================== Property Docstrings ====================== 

propDocs = {}
propDocs["allValuesFrom"]=""
propDocs["backwardCompatibleWith"]=""
propDocs["backwardCompatibleWith"]=""
propDocs["cardinality"]=""
propDocs["complementOf"]=""
propDocs["differentFrom"]=""
propDocs["disjointWith"]=""
propDocs["distinctMembers"]=""
propDocs["equivalentClass"]=""
propDocs["equivalentProperty"]=""
propDocs["hasValue"]=""
propDocs["imports"]=""
propDocs["imports"]=""
propDocs["incompatibleWith"]=""
propDocs["incompatibleWith"]=""
propDocs["intersectionOf"]=""
propDocs["inverseOf"]=""
propDocs["maxCardinality"]=""
propDocs["minCardinality"]=""
propDocs["onProperty"]=""
propDocs["oneOf"]=""
propDocs["priorVersion"]=""
propDocs["priorVersion"]=""
propDocs["sameAs"]=""
propDocs["someValuesFrom"]=""
propDocs["unionOf"]=""
propDocs["versionInfo"]=""
propDocs["versionInfo"]=""
propDocs["hasAvgSpeed"]=""
propDocs["hasCityName"]=\
"""Name of the city for the Feature Of Interest"""
propDocs["hasCountryName"]=\
"""Name of the country for the Feature Of Interest"""
propDocs["hasMeasureTime"]=""
propDocs["hasPostCode"]=\
"""Post code the Feature Of Interest"""
propDocs["hasStreetName"]=\
"""Name of the street for the Feature Of Interest"""
propDocs["hasTRID"]=""
propDocs["hasTotalSpace"]=""
propDocs["hasVehicleCount"]=""
propDocs["locatesIn"]=""
propDocs["hasAbsoluteQuality"]=\
"""Describes the absolute value of the measured quality."""
propDocs["hasProvenance"]=\
"""describes the provenance of an entity/data stream"""
propDocs["hasQuality"]=\
"""describes the quality values an entity has"""
propDocs["hasRatedQuality"]=\
"""Describes the rated value of the measured quality in comparison with the annotated stream description."""
propDocs["hasReputation"]=\
"""Describes the value range for the Reputation."""
propDocs["hasReputationValue"]=\
"""Describes the value range for the Reputation."""
propDocs["hasUnitOfMeasurement"]=\
"""Describes the measurement unit of the absolute measured quality."""
propDocs["Timestamp"]=""
propDocs["alphabetsize"]=\
"""describes the alphabet size that have been used for a stream analysis technique (e.g. SymbolicAggregateApproximation)"""
propDocs["beginsAtLocation"]=\
"""Describes dynamic location of a sensor using a relation from ssn:FeatureOfInterest to geo:SpatialThing to describe the beginning location of the sensory measurement."""
propDocs["computeby"]=\
"""relates a stream data to a computed result"""
propDocs["computedfrom"]=\
"""relates a computed result to a stream data"""
propDocs["endsAtLocation"]=\
"""Describes dynamic location of a sensor using a relation from ssn:FeatureOfInterest to geo:SpatialThing to describe the ending location of the sensory measurement."""
propDocs["hasDatatype"]=""
propDocs["hasID"]=\
"""describes the identification of the stream data"""
propDocs["hasPoint"]=""
propDocs["hasSegment"]=""
propDocs["hasURI"]=""
propDocs["hasUnitOfMeasurement"]=\
"""Relates a stream data to Unit Of Measurement"""
propDocs["minwindowsize"]=\
"""describes the window size that is used for Adaptive SensorSAX algorithm"""
propDocs["nColumns"]=""
propDocs["nRows"]=""
propDocs["quality"]=\
"""Relates a stream data to an information entity regarding the quality"""
propDocs["samplesize"]=\
"""describes the number of samples that a stream data involve; or used for a stream analysis technique"""
propDocs["samplingrate"]=""
propDocs["segmentsize"]=\
"""Describes the number of segments that have been used for a stream data/analysis"""
propDocs["sensitivity"]=\
"""describes the threshold of the sensitivity that is used for Adaptive SensorSAX algorithm"""
propDocs["stepsize"]=\
"""Describes the step size in other words the size of overlapping frames that have been used for a stream data/analysis"""
propDocs["time"]=\
"""Relates a segment to the time interval concept in Timeline Ontology"""
propDocs["value"]=\
"""describes the value of the stream data or stream analysis output; it can be an array of values"""
propDocs["altSymbol"]=\
"""Alternate (standarized) symbol of the entity"""
propDocs["derivesFrom"]=\
"""This property relates a unit with another unit from which the former is derived. For instance, square meter derives from meter."""
propDocs["dimensionalSize"]=\
"""The dimensional size of a simple derived unit, i.e., the exponent of the dimension in the dimensional equation. For instance, for square meters, the dimensional size is two."""
propDocs["factor"]=\
"""Modification factor that multiples the base value of the unit"""
propDocs["inTime"]=\
"""The time of a particular quality value (e.g. the weight of Carlos yesterday)."""
propDocs["measuredIn"]=\
"""The unit used in the measurement of a particular quality value"""
propDocs["measuresQuality"]=\
"""The physical quality the unit is able to measure."""
propDocs["modifierPrefix"]=\
"""The modifier prefix that applies to a derived unit of measurement"""
propDocs["prefSymbol"]=\
"""Standarized symbol of the entity"""
propDocs["qualityLiteralValue"]=""
propDocs["qualityValue"]=\
"""The quality value of a measurable physical quality of an entity or phenomenon."""
propDocs["attachedSystem"]=\
"""Relation between a Platform and any Systems (e.g., Sensors) that are attached to the Platform."""
propDocs["deployedOnPlatform"]=\
"""Relation between a deployment and the platform on which the system was deployed."""
propDocs["deployedSystem"]=\
"""Relation between a deployment and the deployed system."""
propDocs["deploymentProcessPart"]=\
"""Has part relation between a deployment process and its constituent processes."""
propDocs["detects"]=\
"""A relation from a sensor to the Stimulus that the sensor can detect.   
The Stimulus itself will be serving as a proxy for (see isProxyOf) some observable property."""
propDocs["endTime"]=""
propDocs["featureOfInterest"]=\
"""A relation between an observation and the entity whose quality was observed.   For example, in an observation of the weight of a person, the feature of interest is the person and the quality is weight."""
propDocs["forProperty"]=\
"""A relation between some aspect of a sensing entity and a property.  For example, from a sensor to the properties it can observe, or from a deployment to the properties it was installed to observe.  Also from a measurement capability to the property the capability is described for.  (Used in conjunction with ofFeature)."""
propDocs["hasDeployment"]=\
"""Relation between a System and a Deployment, recording that the System/Sensor was deployed in that Deployment."""
propDocs["hasInput"]=""
propDocs["hasLocation"]=\
"""Relates a stream data to an obervation"""
propDocs["hasMeasurementCapability"]=\
"""Relation from a Sensor to a MeasurementCapability describing the measurement properties of the sensor."""
propDocs["hasMeasurementProperty"]=\
"""Relation from a MeasurementCapability to a MeasurementProperty.  For example, to an accuracy (see notes at MeasurementCapability)."""
propDocs["hasOperatingProperty"]=\
"""Relation from an OperatingRange to a Property.  For example, to a battery lifetime."""
propDocs["hasOperatingRange"]=\
"""Relation from a System to an OperatingRange describing the normal operating environment of the System."""
propDocs["hasOutput"]=""
propDocs["hasProperty"]=\
"""A relation between a FeatureOfInterest and a Property of that feature."""
propDocs["hasSubSystem"]=\
"""Haspart relation between a system and its parts."""
propDocs["hasSurvivalProperty"]=\
"""Relation from a SurvivalRange to a Property describing the survial range of a system.  For example, to the temperature extreme that a system can withstand before being considered damaged."""
propDocs["hasSurvivalRange"]=\
"""A Relation from a System to a SurvivalRange."""
propDocs["hasValue"]=""
propDocs["implementedBy"]=\
"""A relation between the description of an algorithm, procedure or method and an entity that implements that method in some executable way.  For example, between a scientific measuring method and a sensor the senses via that method."""
propDocs["implements"]=\
"""A relation between an entity that implements a method in some executable way and the description of an algorithm, procedure or method.  For example, between a Sensor and the scientific measuring method that the Sensor uses to observe a Property."""
propDocs["inCondition"]=\
"""Describes the prevailing environmental conditions for MeasurementCapabilites, OperatingConditions and SurvivalRanges.  Used for example to say that a sensor has a particular accuracy in particular conditions.  (see also MeasurementCapability)"""
propDocs["inDeployment"]=\
"""Relation between a Platform and a Deployment, recording that the object was used as a platform for a system/sensor for a particular deployment: as in this PhysicalObject is acting as a Platform inDeployment Deployment."""
propDocs["isProducedBy"]=\
"""Relation between a producer and a produced entity: for example, between a sensor and the produced output."""
propDocs["isPropertyOf"]=\
"""Relation between a FeatureOfInterest and a Property (a Quality observable by a sensor) of that feature."""
propDocs["isProxyFor"]=\
"""A relation from a Stimulus to the Property that the Stimulus is serving as a proxy for.  For example, the expansion of the quicksilver is a stimulus that serves as a proxy for temperature, or an increase or decrease in the spinning of cups on a wind sensor is serving as a proxy for wind speed."""
propDocs["madeObservation"]=\
"""Relation between a Sensor and Observations it has made."""
propDocs["observationResult"]=\
"""Relation linking an Observation (i.e., a description of the context, the Situation, in which the observatioin was made) and a Result, which contains a value representing the value associated with the observed Property."""
propDocs["observationResultTime"]=\
"""Relates a data point to a time instant or a time interval concept in Timeline Ontology
The result time is the time when the procedure associated with the observation act was applied.
The result time shall describe the time when the result became available, typically when the procedure associated with the observation was completed For some observations this is identical to the phenomenonTime. However, there are important cases where they differ.[O&M]"""
propDocs["observationSamplingTime"]=\
"""The sampling time is the time that the result applies to the feature-of-interest. This is the time usually required for geospatial analysis of the result.
Rebadged as phenomenon time in [O&M]. The phenomenon time shall describe the time that the result applies to the property of the feature-of-interest. This is often the time of interaction by a sampling procedure or observation procedure with a real-world feature.
Relates a Stream Analysis or Stream Event output to a time instant or a time interval concept in Timeline Ontology"""
propDocs["observedBy"]=""
propDocs["observedProperty"]=\
"""Relation linking an Observation to the Property that was observed.  The observedProperty should be a Property (hasProperty) of the FeatureOfInterest (linked by featureOfInterest) of this observation."""
propDocs["observes"]=\
"""Relation between a Sensor and a Property that the sensor can observe.

Note that, given the DUL modelling of Qualities, a sensor defined with 'observes only Windspeed' technically links the sensor to particular instances of Windspeed, not to the concept itself - OWL can't express concept-concept relations, only individual-individual.  The property composition ensures that if an observation is made of a particular quality then one can infer that the sensor observes that quality."""
propDocs["ofFeature"]=\
"""A relation between some aspect of a sensing entity and a feature.  For example, from a sensor to the features it can observe properties of, or from a deployment to the features it was installed to observe.  Also from a measurement capability to the feature the capability is described for.  (Used in conjunction with forProperty)."""
propDocs["onPlatform"]=\
"""Relation between a System (e.g., a Sensor) and a Platform.  The relation locates the sensor relative to other described entities entities: i.e., the Sensor s1's location is Platform p1.  More precise locations for sensors in space (relative to other entities, where attached to another entity, or in 3D space) are made using DOLCE's Regions (SpaceRegion)."""
propDocs["qualityOfObservation"]=\
"""Relation linking an Observation to the adjudged quality of the result.  This is of course complimentary to the MeasurementCapability information recorded for the Sensor that made the Observation."""
propDocs["sensingMethodUsed"]=\
"""A (measurement) procedure is a detailed description of a measurement according to one or more measurement principles and to a given measurement method, based on a measurement model and including any calculation to obtain a measurement result [VIM 2.6]"""
propDocs["startTime"]=""
propDocs["at"]=\
"""refers to a point or an interval on the time line, through an explicit datatype"""
propDocs["atDate"]=\
"""A subproperty of :at, allowing to address a date (beginning of it for an instant, all of it for an interval)"""
propDocs["atDateTime"]=\
"""This property links an instant defined on the universal time line to an XSD date/time value"""
propDocs["atDuration"]=\
"""A property enabling to adress a time point P through the duration of the interval [0,P] on a continuous timeline"""
propDocs["atInt"]=\
"""A subproperty of :at, having as a specific range xsd:int"""
propDocs["atReal"]=\
"""subproperty of :at, having xsd:float as a range"""
propDocs["atYear"]=\
"""A subproperty of :at, allowing to address a year (beginning of it for an instant, all of it for an interval)"""
propDocs["atYearMonth"]=\
"""A subproperty of :at, allowing to address a year/month (beginning of it for an instant, all of it for an interval)"""
propDocs["beginsAt"]=\
"""refers to the beginning of a time interval, through an explicit datatype. time:hasBeginning can be used as well, if you want to associate the beginning of the interval to an explicit time point resource"""
propDocs["beginsAtDateTime"]=\
"""A subproperty of :beginsAt, allowing to address the beginning of an interval as a date/time"""
propDocs["beginsAtDuration"]=\
"""A property enabling to adress a start time point P of an interval [P,E] through the duration of the interval [0,P] on a continuous timeline"""
propDocs["beginsAtInt"]=\
"""A subproperty of :beginsAt, having xsd:int as a range"""
propDocs["delay"]=\
"""associate a shift map to a particular delay"""
propDocs["domainTimeLine"]=\
"""associates a timeline map to its domain timeline"""
propDocs["duration"]=\
"""the duration of a time interval"""
propDocs["durationInt"]=\
"""A subproperty of :duration, having xsd:int as a range"""
propDocs["durationXSD"]=\
"""A subproperty of :duration, having xsd:duration as a range"""
propDocs["endsAt"]=\
"""refers to the end of a time interval, through an explicit datatype. time:hasEnd can be used as well, if you want to associate the end of the interval to an explicit time point resource"""
propDocs["endsAtDateTime"]=\
"""A subproperty of :endsAt, allowing to address the end of an interval as a date/time"""
propDocs["endsAtDuration"]=\
"""A property enabling to adress an end time point P of an interval [S,P] through the duration of the interval [0,P] on a continuous timeline"""
propDocs["endsAtInt"]=\
"""A subproperty of :endsAt, having xsd:int as a range"""
propDocs["hopSize"]=\
"""hop size, associated to a uniform windowing map"""
propDocs["onTimeLine"]=\
"""Relates an interval or an instant to the timeline on which it is defined.
            
            The 29th of August, 2007 would be linked through this property to the universal timeline, whereas
            "from 2s to 5s on this particular signal" would be defined on the signal' timeline."""
propDocs["origin"]=\
"""associate an origin map to its origin on the domain physical timeline"""
propDocs["rangeTimeLine"]=\
"""associates a timeline map to its range timeline"""
propDocs["sampleRate"]=\
"""associates a sample rate value to a uniform sampling map"""
propDocs["windowLength"]=\
"""window length, associated to a uniform windowing map"""
propDocs["creator"]=\
"""An entity primarily responsible for making 
		        the resource."""
propDocs["description"]=\
"""An account of the resource."""
propDocs["title"]=\
"""A name given to the resource."""
propDocs["presents"]=""
propDocs["supports"]=""
propDocs["serviceCategory"]=""
propDocs["serviceCategoryName"]=""
propDocs["serviceParameter"]=""
propDocs["OWLDataProperty"]=""
propDocs["accuracyWeight"]=""
propDocs["availabilityWeight"]=""
propDocs["bandwidthConsumptionWeight"]=""
propDocs["energyConsumptionWeight"]=""
propDocs["hasAggregation"]=""
propDocs["hasCardinality"]=""
propDocs["hasConstraint"]=""
propDocs["hasEventPayload"]=""
propDocs["hasExchangeName"]=\
"""The name of exchange server for the grounding."""
propDocs["hasExpression"]=""
propDocs["hasFilter"]=""
propDocs["hasInternalNodeID"]=""
propDocs["hasNFP"]=""
propDocs["hasPattern"]=""
propDocs["hasPhysicalEventSource"]=""
propDocs["hasPreference"]=""
propDocs["hasSelection"]=""
propDocs["hasServerAddress"]=\
"""The name of exchange server for the grounding."""
propDocs["hasService"]=""
propDocs["hasSubPattern"]=""
propDocs["hasTopic"]=\
"""The name of exchange server for the grounding."""
propDocs["hasWindow"]=""
propDocs["httpService"]=""
propDocs["jmsService"]=""
propDocs["latencyWeight"]=""
propDocs["onEvent"]=""
propDocs["onPayload"]=""
propDocs["onProperty"]=""
propDocs["priceWeight"]=""
propDocs["reliabilityWeight"]=""
propDocs["securityWeight"]=""
propDocs["selectedProperty"]=""
propDocs["weight"]=""
propDocs["describes"]=""
propDocs["hasLocation"]=""
propDocs["hasPart"]=""
propDocs["hasParticipant"]=""
propDocs["hasQuality"]=""
propDocs["hasRegion"]=""
propDocs["includesEvent"]=""
propDocs["includesObject"]=""
propDocs["isDescribedBy"]=""
propDocs["isLocationOf"]=""
propDocs["isObjectIncludedIn"]=""
propDocs["isParticipantIn"]=""
propDocs["isQualityOf"]=""
propDocs["isRegionFor"]=""
propDocs["isSettingFor"]=""
propDocs["satisfies"]=""
propDocs["label"]=\
"""A human-readable name for the subject."""
propDocs["alt"]=\
"""The WGS84 altitude of a SpatialThing (decimal meters 
above the local reference ellipsoid)."""
propDocs["lat"]=\
"""The WGS84 latitude of a SpatialThing (decimal degrees)."""
propDocs["lat_long"]=\
"""A comma-separated representation of a latitude, longitude coordinate."""
propDocs["location"]=\
"""The relation between something and the point, 
 or other geometrical thing in space, where it is.  For example, the realtionship between
 a radio tower and a Point with a given lat and long.
 Or a relationship between a park and its outline as a closed arc of points, or a road and
 its location as a arc (a sequence of points).
 Clearly in practice there will be limit to the accuracy of any such statement, but one would expect
 an accuracy appropriate for the size of the object and uses such as mapping ."""
propDocs["long"]=\
"""The WGS84 longitude of a SpatialThing (decimal degrees)."""
propDocs["after"]=""
propDocs["before"]=""
propDocs["day"]=""
propDocs["dayOfWeek"]=""
propDocs["dayOfYear"]=""
propDocs["days"]=""
propDocs["hasBeginning"]=""
propDocs["hasDateTimeDescription"]=""
propDocs["hasDurationDescription"]=""
propDocs["hasEnd"]=""
propDocs["hour"]=""
propDocs["hours"]=""
propDocs["inDateTime"]=""
propDocs["inXSDDateTime"]=""
propDocs["inside"]=""
propDocs["intervalAfter"]=""
propDocs["intervalBefore"]=""
propDocs["intervalContains"]=""
propDocs["intervalDuring"]=""
propDocs["intervalEquals"]=""
propDocs["intervalFinishedBy"]=""
propDocs["intervalFinishes"]=""
propDocs["intervalMeets"]=""
propDocs["intervalMetBy"]=""
propDocs["intervalOverlappedBy"]=""
propDocs["intervalOverlaps"]=""
propDocs["intervalStartedBy"]=""
propDocs["intervalStarts"]=""
propDocs["minute"]=""
propDocs["minutes"]=""
propDocs["month"]=""
propDocs["months"]=""
propDocs["second"]=""
propDocs["seconds"]=""
propDocs["timeZone"]=""
propDocs["unitType"]=""
propDocs["week"]=""
propDocs["weeks"]=""
propDocs["xsdDateTime"]=""
propDocs["year"]=""
propDocs["years"]=""
propDocs["actedOnBehalfOf"]=\
"""An object property to express the accountability of an agent towards another agent. The subordinate agent acted on behalf of the responsible agent in an actual activity."""
propDocs["activity"]=""
propDocs["agent"]=""
propDocs["alternateOf"]=""
propDocs["atLocation"]=\
"""This property has multiple RDFS domains to suit multiple OWL Profiles. See <a href="#owl-profile">PROV-O OWL Profile</a>.
The Location of any resource."""
propDocs["atTime"]=\
"""The time at which an InstantaneousEvent occurred, in the form of xsd:dateTime."""
propDocs["endedAtTime"]=\
"""The time at which an activity ended. See also prov:startedAtTime."""
propDocs["entity"]=""
propDocs["generated"]=""
propDocs["generatedAtTime"]=\
"""The time at which an entity was completely created and is available for use."""
propDocs["hadActivity"]=\
"""The _optional_ Activity of an Influence, which used, generated, invalidated, or was the responsibility of some Entity. This property is _not_ used by ActivityInfluence (use prov:activity instead).
This property has multiple RDFS domains to suit multiple OWL Profiles. See <a href="#owl-profile">PROV-O OWL Profile</a>."""
propDocs["hadGeneration"]=\
"""The _optional_ Generation involved in an Entity's Derivation."""
propDocs["hadMember"]=""
propDocs["hadPlan"]=\
"""The _optional_ Plan adopted by an Agent in Association with some Activity. Plan specifications are out of the scope of this specification."""
propDocs["hadPrimarySource"]=""
propDocs["hadRole"]=\
"""The _optional_ Role that an Entity assumed in the context of an Activity. For example, :baking prov:used :spoon; prov:qualified [ a prov:Usage; prov:entity :spoon; prov:hadRole roles:mixing_implement ].
This property has multiple RDFS domains to suit multiple OWL Profiles. See <a href="#owl-profile">PROV-O OWL Profile</a>."""
propDocs["hadUsage"]=\
"""The _optional_ Usage involved in an Entity's Derivation."""
propDocs["influenced"]=""
propDocs["influencer"]=\
"""Subproperties of prov:influencer are used to cite the object of an unqualified PROV-O triple whose predicate is a subproperty of prov:wasInfluencedBy (e.g. prov:used, prov:wasGeneratedBy). prov:influencer is used much like rdf:object is used."""
propDocs["invalidated"]=""
propDocs["invalidatedAtTime"]=\
"""The time at which an entity was invalidated (i.e., no longer usable)."""
propDocs["qualifiedAssociation"]=\
"""If this Activity prov:wasAssociatedWith Agent :ag, then it can qualify the Association using prov:qualifiedAssociation [ a prov:Association;  prov:agent :ag; :foo :bar ]."""
propDocs["qualifiedAttribution"]=\
"""If this Entity prov:wasAttributedTo Agent :ag, then it can qualify how it was influenced using prov:qualifiedAttribution [ a prov:Attribution;  prov:agent :ag; :foo :bar ]."""
propDocs["qualifiedCommunication"]=\
"""If this Activity prov:wasInformedBy Activity :a, then it can qualify how it was influenced using prov:qualifiedCommunication [ a prov:Communication;  prov:activity :a; :foo :bar ]."""
propDocs["qualifiedDelegation"]=\
"""If this Agent prov:actedOnBehalfOf Agent :ag, then it can qualify how with prov:qualifiedResponsibility [ a prov:Responsibility;  prov:agent :ag; :foo :bar ]."""
propDocs["qualifiedDerivation"]=\
"""If this Entity prov:wasDerivedFrom Entity :e, then it can qualify how it was derived using prov:qualifiedDerivation [ a prov:Derivation;  prov:entity :e; :foo :bar ]."""
propDocs["qualifiedEnd"]=\
"""If this Activity prov:wasEndedBy Entity :e1, then it can qualify how it was ended using prov:qualifiedEnd [ a prov:End;  prov:entity :e1; :foo :bar ]."""
propDocs["qualifiedGeneration"]=\
"""If this Activity prov:generated Entity :e, then it can qualify how it performed the Generation using prov:qualifiedGeneration [ a prov:Generation;  prov:entity :e; :foo :bar ]."""
propDocs["qualifiedInfluence"]=\
"""Because prov:qualifiedInfluence is a broad relation, the more specific relations (qualifiedCommunication, qualifiedDelegation, qualifiedEnd, etc.) should be used when applicable."""
propDocs["qualifiedInvalidation"]=\
"""If this Entity prov:wasInvalidatedBy Activity :a, then it can qualify how it was invalidated using prov:qualifiedInvalidation [ a prov:Invalidation;  prov:activity :a; :foo :bar ]."""
propDocs["qualifiedPrimarySource"]=\
"""If this Entity prov:hadPrimarySource Entity :e, then it can qualify how using prov:qualifiedPrimarySource [ a prov:PrimarySource; prov:entity :e; :foo :bar ]."""
propDocs["qualifiedQuotation"]=\
"""If this Entity prov:wasQuotedFrom Entity :e, then it can qualify how using prov:qualifiedQuotation [ a prov:Quotation;  prov:entity :e; :foo :bar ]."""
propDocs["qualifiedRevision"]=\
"""If this Entity prov:wasRevisionOf Entity :e, then it can qualify how it was revised using prov:qualifiedRevision [ a prov:Revision;  prov:entity :e; :foo :bar ]."""
propDocs["qualifiedStart"]=\
"""If this Activity prov:wasStartedBy Entity :e1, then it can qualify how it was started using prov:qualifiedStart [ a prov:Start;  prov:entity :e1; :foo :bar ]."""
propDocs["qualifiedUsage"]=\
"""If this Activity prov:used Entity :e, then it can qualify how it used it using prov:qualifiedUsage [ a prov:Usage; prov:entity :e; :foo :bar ]."""
propDocs["specializationOf"]=""
propDocs["startedAtTime"]=\
"""The time at which an activity started. See also prov:endedAtTime."""
propDocs["used"]=\
"""Relates a stream analysis to associated entity
A prov:Entity that was used by this prov:Activity. For example, :baking prov:used :spoon, :egg, :oven ."""
propDocs["value"]=""
propDocs["wasAssociatedWith"]=\
"""An prov:Agent that had some (unspecified) responsibility for the occurrence of this prov:Activity.
Relates a stream analysis to associated entity"""
propDocs["wasAttributedTo"]=\
"""Attribution is the ascribing of an entity to an agent."""
propDocs["wasDerivedFrom"]=\
"""Relates a stream data to an obervation
The more specific subproperties of prov:wasDerivedFrom (i.e., prov:wasQuotedFrom, prov:wasRevisionOf, prov:hadPrimarySource) should be used when applicable."""
propDocs["wasEndedBy"]=\
"""End is when an activity is deemed to have ended. An end may refer to an entity, known as trigger, that terminated the activity."""
propDocs["wasGeneratedBy"]=""
propDocs["wasInfluencedBy"]=\
"""This property has multiple RDFS domains to suit multiple OWL Profiles. See <a href="#owl-profile">PROV-O OWL Profile</a>.
Because prov:wasInfluencedBy is a broad relation, its more specific subproperties (e.g. prov:wasInformedBy, prov:actedOnBehalfOf, prov:wasEndedBy, etc.) should be used when applicable."""
propDocs["wasInformedBy"]=\
"""An activity a2 is dependent on or informed by another activity a1, by way of some unspecified entity that is generated by a1 and used by a2."""
propDocs["wasInvalidatedBy"]=""
propDocs["wasQuotedFrom"]=\
"""An entity is derived from an original entity by copying, or 'quoting', some or all of it."""
propDocs["wasRevisionOf"]=\
"""A revision is a derivation that revises an entity into a revised version."""
propDocs["wasStartedBy"]=\
"""Start is when an activity is deemed to have started. A start may refer to an entity, known as trigger, that initiated the activity."""
propDocs["accountName"]=\
"""Indicates the name (identifier) associated with this online account."""
propDocs["accountName"]=\
"""Indicates the name (identifier) associated with this online account."""
propDocs["accountServiceHomepage"]=\
"""Indicates a homepage of the service provide for this online account."""
propDocs["accountServiceHomepage"]=\
"""Indicates a homepage of the service provide for this online account."""
propDocs["aimChatID"]=\
"""An AIM chat ID"""
propDocs["aimChatID"]=\
"""An AIM chat ID"""
propDocs["based_near"]=\
"""A location that something is based near, for some broadly human notion of near."""
propDocs["based_near"]=\
"""A location that something is based near, for some broadly human notion of near."""
propDocs["birthday"]=\
"""The birthday of this Agent, represented in mm-dd string form, eg. '12-31'."""
propDocs["birthday"]=\
"""The birthday of this Agent, represented in mm-dd string form, eg. '12-31'."""
propDocs["currentProject"]=\
"""A current project this person works on."""
propDocs["currentProject"]=\
"""A current project this person works on."""
propDocs["depiction"]=\
"""A depiction of some thing."""
propDocs["depiction"]=\
"""A depiction of some thing."""
propDocs["depicts"]=\
"""A thing depicted in this representation."""
propDocs["depicts"]=\
"""A thing depicted in this representation."""
propDocs["dnaChecksum"]=\
"""A checksum for the DNA of some thing. Joke."""
propDocs["dnaChecksum"]=\
"""A checksum for the DNA of some thing. Joke."""
propDocs["family_name"]=\
"""The family_name of some person."""
propDocs["family_name"]=\
"""The family_name of some person."""
propDocs["firstName"]=\
"""The first name of a person."""
propDocs["firstName"]=\
"""The first name of a person."""
propDocs["fundedBy"]=\
"""An organization funding a project or person."""
propDocs["fundedBy"]=\
"""An organization funding a project or person."""
propDocs["geekcode"]=\
"""A textual geekcode for this person, see http://www.geekcode.com/geek.html"""
propDocs["geekcode"]=\
"""A textual geekcode for this person, see http://www.geekcode.com/geek.html"""
propDocs["gender"]=\
"""The gender of this Agent (typically but not necessarily 'male' or 'female')."""
propDocs["gender"]=\
"""The gender of this Agent (typically but not necessarily 'male' or 'female')."""
propDocs["givenname"]=\
"""The given name of some person."""
propDocs["givenname"]=\
"""The given name of some person."""
propDocs["holdsAccount"]=\
"""Indicates an account held by this agent."""
propDocs["holdsAccount"]=\
"""Indicates an account held by this agent."""
propDocs["homepage"]=\
"""A homepage for some thing."""
propDocs["homepage"]=\
"""A homepage for some thing."""
propDocs["icqChatID"]=\
"""An ICQ chat ID"""
propDocs["icqChatID"]=\
"""An ICQ chat ID"""
propDocs["img"]=\
"""An image that can be used to represent some thing (ie. those depictions which are particularly representative of something, eg. one's photo on a homepage)."""
propDocs["img"]=\
"""An image that can be used to represent some thing (ie. those depictions which are particularly representative of something, eg. one's photo on a homepage)."""
propDocs["interest"]=\
"""A page about a topic of interest to this person."""
propDocs["interest"]=\
"""A page about a topic of interest to this person."""
propDocs["isPrimaryTopicOf"]=\
"""A document that this thing is the primary topic of."""
propDocs["jabberID"]=\
"""A jabber ID for something."""
propDocs["jabberID"]=\
"""A jabber ID for something."""
propDocs["knows"]=\
"""A person known by this person (indicating some level of reciprocated interaction between the parties)."""
propDocs["knows"]=\
"""A person known by this person (indicating some level of reciprocated interaction between the parties)."""
propDocs["logo"]=\
"""A logo representing some thing."""
propDocs["logo"]=\
"""A logo representing some thing."""
propDocs["made"]=\
"""Something that was made by this agent."""
propDocs["made"]=\
"""Something that was made by this agent."""
propDocs["maker"]=\
"""An agent that  made this thing."""
propDocs["maker"]=\
"""An agent that  made this thing."""
propDocs["mbox"]=\
"""A  personal mailbox, ie. an Internet mailbox associated with exactly one owner, the first owner of this mailbox. This is a 'static inverse functional property', in that  there is (across time and change) at most one individual that ever has any particular value for foaf:mbox."""
propDocs["mbox"]=\
"""A  personal mailbox, ie. an Internet mailbox associated with exactly one owner, the first owner of this mailbox. This is a 'static inverse functional property', in that  there is (across time and change) at most one individual that ever has any particular value for foaf:mbox."""
propDocs["mbox_sha1sum"]=\
"""The sha1sum of the URI of an Internet mailbox associated with exactly one owner, the  first owner of the mailbox."""
propDocs["mbox_sha1sum"]=\
"""The sha1sum of the URI of an Internet mailbox associated with exactly one owner, the  first owner of the mailbox."""
propDocs["member"]=\
"""Indicates a member of a Group"""
propDocs["member"]=\
"""Indicates a member of a Group"""
propDocs["membershipClass"]=\
"""Indicates the class of individuals that are a member of a Group"""
propDocs["msnChatID"]=\
"""An MSN chat ID"""
propDocs["msnChatID"]=\
"""An MSN chat ID"""
propDocs["myersBriggs"]=\
"""A Myers Briggs (MBTI) personality classification."""
propDocs["myersBriggs"]=\
"""A Myers Briggs (MBTI) personality classification."""
propDocs["name"]=\
"""A name for some thing."""
propDocs["name"]=\
"""A name for some thing."""
propDocs["nick"]=\
"""A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames)."""
propDocs["nick"]=\
"""A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames)."""
propDocs["openid"]=\
"""An OpenID  for an Agent."""
propDocs["openid"]=\
"""An OpenID  for an Agent."""
propDocs["page"]=\
"""A page or document about this thing."""
propDocs["page"]=\
"""A page or document about this thing."""
propDocs["pastProject"]=\
"""A project this person has previously worked on."""
propDocs["pastProject"]=\
"""A project this person has previously worked on."""
propDocs["phone"]=\
"""A phone,  specified using fully qualified tel: URI scheme (refs: http://www.w3.org/Addressing/schemes.html#tel)."""
propDocs["phone"]=\
"""A phone,  specified using fully qualified tel: URI scheme (refs: http://www.w3.org/Addressing/schemes.html#tel)."""
propDocs["plan"]=\
"""A .plan comment, in the tradition of finger and '.plan' files."""
propDocs["plan"]=\
"""A .plan comment, in the tradition of finger and '.plan' files."""
propDocs["primaryTopic"]=\
"""The primary topic of some page or document."""
propDocs["primaryTopic"]=\
"""The primary topic of some page or document."""
propDocs["publications"]=\
"""A link to the publications of this person."""
propDocs["publications"]=\
"""A link to the publications of this person."""
propDocs["schoolHomepage"]=\
"""A homepage of a school attended by the person."""
propDocs["schoolHomepage"]=\
"""A homepage of a school attended by the person."""
propDocs["sha1"]=\
"""A sha1sum hash, in hex."""
propDocs["sha1"]=\
"""A sha1sum hash, in hex."""
propDocs["surname"]=\
"""The surname of some person."""
propDocs["surname"]=\
"""The surname of some person."""
propDocs["theme"]=\
"""A theme."""
propDocs["theme"]=\
"""A theme."""
propDocs["thumbnail"]=\
"""A derived thumbnail image."""
propDocs["thumbnail"]=\
"""A derived thumbnail image."""
propDocs["tipjar"]=\
"""A tipjar document for this agent, describing means for payment and reward."""
propDocs["tipjar"]=\
"""A tipjar document for this agent, describing means for payment and reward."""
propDocs["title"]=\
"""Title (Mr, Mrs, Ms, Dr. etc)"""
propDocs["title"]=\
"""Title (Mr, Mrs, Ms, Dr. etc)"""
propDocs["topic"]=\
"""A topic of some page or document."""
propDocs["topic"]=\
"""A topic of some page or document."""
propDocs["topic_interest"]=\
"""A thing of interest to this person."""
propDocs["topic_interest"]=\
"""A thing of interest to this person."""
propDocs["weblog"]=\
"""A weblog of some thing (whether person, group, company etc.)."""
propDocs["weblog"]=\
"""A weblog of some thing (whether person, group, company etc.)."""
propDocs["workInfoHomepage"]=\
"""A work info homepage of some person; a page about their work for some organization."""
propDocs["workInfoHomepage"]=\
"""A work info homepage of some person; a page about their work for some organization."""
propDocs["workplaceHomepage"]=\
"""A workplace homepage of some person; the homepage of an organization they work for."""
propDocs["workplaceHomepage"]=\
"""A workplace homepage of some person; the homepage of an organization they work for."""
propDocs["yahooChatID"]=\
"""A Yahoo chat ID"""
propDocs["yahooChatID"]=\
"""A Yahoo chat ID"""




# ========================  Class Definitions  ====================== 

class owl___Thing(object):
	"""
	owl:Thing
	"""
	def __init__(self,URI=None):
		self._initialised = False
		self.shortname = "Thing"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["depiction"] = PropertySet("depiction","http://xmlns.com/foaf/0.1/depiction", foaf___Image, False)
		self._props["fundedBy"] = PropertySet("fundedBy","http://xmlns.com/foaf/0.1/fundedBy", owl___Thing, False)
		self._props["homepage"] = PropertySet("homepage","http://xmlns.com/foaf/0.1/homepage", foaf___Document, False)
		self._props["img"] = PropertySet("img","http://xmlns.com/foaf/0.1/img", foaf___Image, False)
		self._props["isPrimaryTopicOf"] = PropertySet("isPrimaryTopicOf","http://xmlns.com/foaf/0.1/isPrimaryTopicOf", foaf___Document, False)
		self._props["logo"] = PropertySet("logo","http://xmlns.com/foaf/0.1/logo", owl___Thing, False)
		self._props["maker"] = PropertySet("maker","http://xmlns.com/foaf/0.1/maker", foaf___Agent, False)
		self._props["name"] = PropertySet("name","http://xmlns.com/foaf/0.1/name", None, True)
		self._props["openid"] = PropertySet("openid","http://xmlns.com/foaf/0.1/openid", foaf___Document, False)
		self._props["page"] = PropertySet("page","http://xmlns.com/foaf/0.1/page", foaf___Document, False)
		self._props["theme"] = PropertySet("theme","http://xmlns.com/foaf/0.1/theme", owl___Thing, False)
		self._props["tipjar"] = PropertySet("tipjar","http://xmlns.com/foaf/0.1/tipjar", foaf___Document, False)
		self._props["weblog"] = PropertySet("weblog","http://xmlns.com/foaf/0.1/weblog", foaf___Document, False)
		self._initialised = True
	classURI = "http://www.w3.org/2002/07/owl#Thing"


	# Python class properties to wrap the PropertySet objects
	depiction = property(fget=lambda x: x._props["depiction"].get(), fset=lambda x,y : x._props["depiction"].set(y), fdel=None, doc=propDocs["depiction"])
	fundedBy = property(fget=lambda x: x._props["fundedBy"].get(), fset=lambda x,y : x._props["fundedBy"].set(y), fdel=None, doc=propDocs["fundedBy"])
	homepage = property(fget=lambda x: x._props["homepage"].get(), fset=lambda x,y : x._props["homepage"].set(y), fdel=None, doc=propDocs["homepage"])
	img = property(fget=lambda x: x._props["img"].get(), fset=lambda x,y : x._props["img"].set(y), fdel=None, doc=propDocs["img"])
	isPrimaryTopicOf = property(fget=lambda x: x._props["isPrimaryTopicOf"].get(), fset=lambda x,y : x._props["isPrimaryTopicOf"].set(y), fdel=None, doc=propDocs["isPrimaryTopicOf"])
	logo = property(fget=lambda x: x._props["logo"].get(), fset=lambda x,y : x._props["logo"].set(y), fdel=None, doc=propDocs["logo"])
	maker = property(fget=lambda x: x._props["maker"].get(), fset=lambda x,y : x._props["maker"].set(y), fdel=None, doc=propDocs["maker"])
	name = property(fget=lambda x: x._props["name"].get(), fset=lambda x,y : x._props["name"].set(y), fdel=None, doc=propDocs["name"])
	openid = property(fget=lambda x: x._props["openid"].get(), fset=lambda x,y : x._props["openid"].set(y), fdel=None, doc=propDocs["openid"])
	page = property(fget=lambda x: x._props["page"].get(), fset=lambda x,y : x._props["page"].set(y), fdel=None, doc=propDocs["page"])
	theme = property(fget=lambda x: x._props["theme"].get(), fset=lambda x,y : x._props["theme"].set(y), fdel=None, doc=propDocs["theme"])
	tipjar = property(fget=lambda x: x._props["tipjar"].get(), fset=lambda x,y : x._props["tipjar"].set(y), fdel=None, doc=propDocs["tipjar"])
	weblog = property(fget=lambda x: x._props["weblog"].get(), fset=lambda x,y : x._props["weblog"].set(y), fdel=None, doc=propDocs["weblog"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___OnlineAccount(owl___Thing):
	"""
	foaf:OnlineAccount
	An online account.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		owl___Thing.__init__(self)
		self._initialised = False
		self.shortname = "OnlineAccount"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["accountName"] = PropertySet("accountName","http://xmlns.com/foaf/0.1/accountName", None, True)
		self._props["accountServiceHomepage"] = PropertySet("accountServiceHomepage","http://xmlns.com/foaf/0.1/accountServiceHomepage", foaf___Document, False)
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/OnlineAccount"


	# Python class properties to wrap the PropertySet objects
	accountName = property(fget=lambda x: x._props["accountName"].get(), fset=lambda x,y : x._props["accountName"].set(y), fdel=None, doc=propDocs["accountName"])
	accountServiceHomepage = property(fget=lambda x: x._props["accountServiceHomepage"].get(), fset=lambda x,y : x._props["accountServiceHomepage"].set(y), fdel=None, doc=propDocs["accountServiceHomepage"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___OnlineEcommerceAccount(foaf___OnlineAccount):
	"""
	foaf:OnlineEcommerceAccount
	An online e-commerce account.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___OnlineAccount.__init__(self)
		self._initialised = False
		self.shortname = "OnlineEcommerceAccount"
		self.URI = URI
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/OnlineEcommerceAccount"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___FeatureOfInterest(owl___Thing):
	"""
	ssn:FeatureOfInterest
	A feature is an abstraction of real world phenomena (thing, person, event, etc).
	"""
	def __init__(self,URI=None):
		# Initialise parents
		owl___Thing.__init__(self)
		self._initialised = False
		self.shortname = "FeatureOfInterest"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["beginsAtLocation"] = PropertySet("beginsAtLocation","http://purl.oclc.org/NET/UNIS/sao/sao#beginsAtLocation", geo___SpatialThing, False)
		self._props["endsAtLocation"] = PropertySet("endsAtLocation","http://purl.oclc.org/NET/UNIS/sao/sao#endsAtLocation", geo___SpatialThing, False)
		self._props["hasLocation"] = PropertySet("hasLocation","http://purl.oclc.org/NET/ssnx/ssn#hasLocation", geo___SpatialThing, False)
		self._props["hasMeasurementCapability"] = PropertySet("hasMeasurementCapability","http://purl.oclc.org/NET/ssnx/ssn#hasMeasurementCapability", (ssn___Property,ssn___MeasurementCapability), False)
		self._props["hasMeasurementProperty"] = PropertySet("hasMeasurementProperty","http://purl.oclc.org/NET/ssnx/ssn#hasMeasurementProperty", (ssn___Property,ssn___MeasurementProperty), False)
		self._props["hasOperatingProperty"] = PropertySet("hasOperatingProperty","http://purl.oclc.org/NET/ssnx/ssn#hasOperatingProperty", (ssn___Property,ssn___OperatingProperty), False)
		self._props["hasOperatingRange"] = PropertySet("hasOperatingRange","http://purl.oclc.org/NET/ssnx/ssn#hasOperatingRange", (ssn___Property,ssn___OperatingRange), False)
		self._props["hasProperty"] = PropertySet("hasProperty","http://purl.oclc.org/NET/ssnx/ssn#hasProperty", (ssn___Property,ssn___FeatureOfInterest), False)
		self._props["hasSurvivalProperty"] = PropertySet("hasSurvivalProperty","http://purl.oclc.org/NET/ssnx/ssn#hasSurvivalProperty", (ssn___Property,ssn___SurvivalProperty), False)
		self._props["hasSurvivalRange"] = PropertySet("hasSurvivalRange","http://purl.oclc.org/NET/ssnx/ssn#hasSurvivalRange", (ssn___Property,ssn___SurvivalRange), False)
		self._props["isPropertyOf"] = PropertySet("isPropertyOf","http://purl.oclc.org/NET/ssnx/ssn#isPropertyOf", (ssn___Property,ssn___FeatureOfInterest), False)
		self._props["qualityOfObservation"] = PropertySet("qualityOfObservation","http://purl.oclc.org/NET/ssnx/ssn#qualityOfObservation", ssn___Property, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#FeatureOfInterest"


	# Python class properties to wrap the PropertySet objects
	beginsAtLocation = property(fget=lambda x: x._props["beginsAtLocation"].get(), fset=lambda x,y : x._props["beginsAtLocation"].set(y), fdel=None, doc=propDocs["beginsAtLocation"])
	endsAtLocation = property(fget=lambda x: x._props["endsAtLocation"].get(), fset=lambda x,y : x._props["endsAtLocation"].set(y), fdel=None, doc=propDocs["endsAtLocation"])
	hasLocation = property(fget=lambda x: x._props["hasLocation"].get(), fset=lambda x,y : x._props["hasLocation"].set(y), fdel=None, doc=propDocs["hasLocation"])
	hasMeasurementCapability = property(fget=lambda x: x._props["hasMeasurementCapability"].get(), fset=lambda x,y : x._props["hasMeasurementCapability"].set(y), fdel=None, doc=propDocs["hasMeasurementCapability"])
	hasMeasurementProperty = property(fget=lambda x: x._props["hasMeasurementProperty"].get(), fset=lambda x,y : x._props["hasMeasurementProperty"].set(y), fdel=None, doc=propDocs["hasMeasurementProperty"])
	hasOperatingProperty = property(fget=lambda x: x._props["hasOperatingProperty"].get(), fset=lambda x,y : x._props["hasOperatingProperty"].set(y), fdel=None, doc=propDocs["hasOperatingProperty"])
	hasOperatingRange = property(fget=lambda x: x._props["hasOperatingRange"].get(), fset=lambda x,y : x._props["hasOperatingRange"].set(y), fdel=None, doc=propDocs["hasOperatingRange"])
	hasProperty = property(fget=lambda x: x._props["hasProperty"].get(), fset=lambda x,y : x._props["hasProperty"].set(y), fdel=None, doc=propDocs["hasProperty"])
	hasSurvivalProperty = property(fget=lambda x: x._props["hasSurvivalProperty"].get(), fset=lambda x,y : x._props["hasSurvivalProperty"].set(y), fdel=None, doc=propDocs["hasSurvivalProperty"])
	hasSurvivalRange = property(fget=lambda x: x._props["hasSurvivalRange"].get(), fset=lambda x,y : x._props["hasSurvivalRange"].set(y), fdel=None, doc=propDocs["hasSurvivalRange"])
	isPropertyOf = property(fget=lambda x: x._props["isPropertyOf"].get(), fset=lambda x,y : x._props["isPropertyOf"].set(y), fdel=None, doc=propDocs["isPropertyOf"])
	qualityOfObservation = property(fget=lambda x: x._props["qualityOfObservation"].get(), fset=lambda x,y : x._props["qualityOfObservation"].set(y), fdel=None, doc=propDocs["qualityOfObservation"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class rdfs___Resource(owl___Thing):
	"""
	rdfs:Resource
	"""
	def __init__(self,URI=None):
		# Initialise parents
		owl___Thing.__init__(self)
		self._initialised = False
		self.shortname = "Resource"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["creator"] = PropertySet("creator","http://purl.org/dc/elements/1.1/creator", foaf___Agent, False)
		self._props["description"] = PropertySet("description","http://purl.org/dc/elements/1.1/description", None, True)
		self._props["title"] = PropertySet("title","http://purl.org/dc/elements/1.1/title", None, True)
		self._props["label"] = PropertySet("label","http://www.w3.org/2000/01/rdf-schema#label", None, True)
		self._props["name"] = PropertySet("name","http://xmlns.com/foaf/0.1/name", None, True)
		self._initialised = True
	classURI = "http://www.w3.org/2000/01/rdf-schema#Resource"


	# Python class properties to wrap the PropertySet objects
	creator = property(fget=lambda x: x._props["creator"].get(), fset=lambda x,y : x._props["creator"].set(y), fdel=None, doc=propDocs["creator"])
	description = property(fget=lambda x: x._props["description"].get(), fset=lambda x,y : x._props["description"].set(y), fdel=None, doc=propDocs["description"])
	title = property(fget=lambda x: x._props["title"].get(), fset=lambda x,y : x._props["title"].set(y), fdel=None, doc=propDocs["title"])
	label = property(fget=lambda x: x._props["label"].get(), fset=lambda x,y : x._props["label"].set(y), fdel=None, doc=propDocs["label"])
	name = property(fget=lambda x: x._props["name"].get(), fset=lambda x,y : x._props["name"].set(y), fdel=None, doc=propDocs["name"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class geo___SpatialThing(rdfs___Resource):
	"""
	geo:SpatialThing
	Anything with spatial extent, i.e. size, shape, or position.
 e.g. people, places, bowling balls, as well as abstract areas like cubes.

	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "SpatialThing"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasCityName"] = PropertySet("hasCityName","http://ict-citypulse.eu/city#hasCityName", None, True)
		self._props["hasCountryName"] = PropertySet("hasCountryName","http://ict-citypulse.eu/city#hasCountryName", None, True)
		self._props["hasPostCode"] = PropertySet("hasPostCode","http://ict-citypulse.eu/city#hasPostCode", None, True)
		self._props["hasStreetName"] = PropertySet("hasStreetName","http://ict-citypulse.eu/city#hasStreetName", None, True)
		self._props["alt"] = PropertySet("alt","http://www.w3.org/2003/01/geo/wgs84_pos#alt", None, False)
		self._props["lat"] = PropertySet("lat","http://www.w3.org/2003/01/geo/wgs84_pos#lat", None, False)
		self._props["location"] = PropertySet("location","http://www.w3.org/2003/01/geo/wgs84_pos#location", geo___SpatialThing, False)
		self._props["long"] = PropertySet("long","http://www.w3.org/2003/01/geo/wgs84_pos#long", None, False)
		self._props["based_near"] = PropertySet("based_near","http://xmlns.com/foaf/0.1/based_near", geo___SpatialThing, False)
		self._initialised = True
	classURI = "http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing"


	# Python class properties to wrap the PropertySet objects
	hasCityName = property(fget=lambda x: x._props["hasCityName"].get(), fset=lambda x,y : x._props["hasCityName"].set(y), fdel=None, doc=propDocs["hasCityName"])
	hasCountryName = property(fget=lambda x: x._props["hasCountryName"].get(), fset=lambda x,y : x._props["hasCountryName"].set(y), fdel=None, doc=propDocs["hasCountryName"])
	hasPostCode = property(fget=lambda x: x._props["hasPostCode"].get(), fset=lambda x,y : x._props["hasPostCode"].set(y), fdel=None, doc=propDocs["hasPostCode"])
	hasStreetName = property(fget=lambda x: x._props["hasStreetName"].get(), fset=lambda x,y : x._props["hasStreetName"].set(y), fdel=None, doc=propDocs["hasStreetName"])
	alt = property(fget=lambda x: x._props["alt"].get(), fset=lambda x,y : x._props["alt"].set(y), fdel=None, doc=propDocs["alt"])
	lat = property(fget=lambda x: x._props["lat"].get(), fset=lambda x,y : x._props["lat"].set(y), fdel=None, doc=propDocs["lat"])
	location = property(fget=lambda x: x._props["location"].get(), fset=lambda x,y : x._props["location"].set(y), fdel=None, doc=propDocs["location"])
	long = property(fget=lambda x: x._props["long"].get(), fset=lambda x,y : x._props["long"].set(y), fdel=None, doc=propDocs["long"])
	based_near = property(fget=lambda x: x._props["based_near"].get(), fset=lambda x,y : x._props["based_near"].set(y), fdel=None, doc=propDocs["based_near"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tm___DayOfWeek(rdfs___Resource):
	"""
	tm:DayOfWeek
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "DayOfWeek"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#DayOfWeek"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tm___TemporalEntity(rdfs___Resource):
	"""
	tm:TemporalEntity
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "TemporalEntity"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["after"] = PropertySet("after","http://www.w3.org/2006/time#after", tm___TemporalEntity, False)
		self._props["before"] = PropertySet("before","http://www.w3.org/2006/time#before", tm___TemporalEntity, False)
		self._props["hasBeginning"] = PropertySet("hasBeginning","http://www.w3.org/2006/time#hasBeginning", tm___Instant, False)
		self._props["hasDurationDescription"] = PropertySet("hasDurationDescription","http://www.w3.org/2006/time#hasDurationDescription", tm___DurationDescription, False)
		self._props["hasEnd"] = PropertySet("hasEnd","http://www.w3.org/2006/time#hasEnd", tm___Instant, False)
		self._props["intervalBefore"] = PropertySet("intervalBefore","http://www.w3.org/2006/time#intervalBefore", (tm___ProperInterval,tm___TemporalEntity,tl___Interval), False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#TemporalEntity"


	# Python class properties to wrap the PropertySet objects
	after = property(fget=lambda x: x._props["after"].get(), fset=lambda x,y : x._props["after"].set(y), fdel=None, doc=propDocs["after"])
	before = property(fget=lambda x: x._props["before"].get(), fset=lambda x,y : x._props["before"].set(y), fdel=None, doc=propDocs["before"])
	hasBeginning = property(fget=lambda x: x._props["hasBeginning"].get(), fset=lambda x,y : x._props["hasBeginning"].set(y), fdel=None, doc=propDocs["hasBeginning"])
	hasDurationDescription = property(fget=lambda x: x._props["hasDurationDescription"].get(), fset=lambda x,y : x._props["hasDurationDescription"].set(y), fdel=None, doc=propDocs["hasDurationDescription"])
	hasEnd = property(fget=lambda x: x._props["hasEnd"].get(), fset=lambda x,y : x._props["hasEnd"].set(y), fdel=None, doc=propDocs["hasEnd"])
	intervalBefore = property(fget=lambda x: x._props["intervalBefore"].get(), fset=lambda x,y : x._props["intervalBefore"].set(y), fdel=None, doc=propDocs["intervalBefore"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tzont___TimeZone(rdfs___Resource):
	"""
	tzont:TimeZone
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "TimeZone"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/2006/timezone#TimeZone"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Agent(rdfs___Resource):
	"""
	prov:Agent
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Agent"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasReputation"] = PropertySet("hasReputation","http://purl.oclc.org/NET/UASO/qoi#hasReputation", qoi___Reputation, False)
		self._props["actedOnBehalfOf"] = PropertySet("actedOnBehalfOf","http://www.w3.org/ns/prov#actedOnBehalfOf", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["atLocation"] = PropertySet("atLocation","http://www.w3.org/ns/prov#atLocation", prov___Location, False)
		self._props["hadMember"] = PropertySet("hadMember","http://www.w3.org/ns/prov#hadMember", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["hadPrimarySource"] = PropertySet("hadPrimarySource","http://www.w3.org/ns/prov#hadPrimarySource", (prov___Entity,sao___StreamData,sao___StreamAnalysis), False)
		self._props["qualifiedAssociation"] = PropertySet("qualifiedAssociation","http://www.w3.org/ns/prov#qualifiedAssociation", (prov___Association,prov___Influence), False)
		self._props["qualifiedAttribution"] = PropertySet("qualifiedAttribution","http://www.w3.org/ns/prov#qualifiedAttribution", (prov___Influence,prov___Attribution), False)
		self._props["qualifiedCommunication"] = PropertySet("qualifiedCommunication","http://www.w3.org/ns/prov#qualifiedCommunication", (prov___Influence,prov___Communication), False)
		self._props["qualifiedDelegation"] = PropertySet("qualifiedDelegation","http://www.w3.org/ns/prov#qualifiedDelegation", (prov___Delegation,prov___Influence), False)
		self._props["qualifiedDerivation"] = PropertySet("qualifiedDerivation","http://www.w3.org/ns/prov#qualifiedDerivation", (prov___Derivation,prov___Influence), False)
		self._props["qualifiedEnd"] = PropertySet("qualifiedEnd","http://www.w3.org/ns/prov#qualifiedEnd", (prov___End,prov___Influence), False)
		self._props["qualifiedGeneration"] = PropertySet("qualifiedGeneration","http://www.w3.org/ns/prov#qualifiedGeneration", (prov___Generation,prov___Influence), False)
		self._props["qualifiedInfluence"] = PropertySet("qualifiedInfluence","http://www.w3.org/ns/prov#qualifiedInfluence", prov___Influence, False)
		self._props["qualifiedInvalidation"] = PropertySet("qualifiedInvalidation","http://www.w3.org/ns/prov#qualifiedInvalidation", (prov___Invalidation,prov___Influence), False)
		self._props["qualifiedPrimarySource"] = PropertySet("qualifiedPrimarySource","http://www.w3.org/ns/prov#qualifiedPrimarySource", (prov___PrimarySource,prov___Influence), False)
		self._props["qualifiedQuotation"] = PropertySet("qualifiedQuotation","http://www.w3.org/ns/prov#qualifiedQuotation", (prov___Quotation,prov___Influence), False)
		self._props["qualifiedRevision"] = PropertySet("qualifiedRevision","http://www.w3.org/ns/prov#qualifiedRevision", (prov___Revision,prov___Influence), False)
		self._props["qualifiedStart"] = PropertySet("qualifiedStart","http://www.w3.org/ns/prov#qualifiedStart", (prov___Influence,prov___Start), False)
		self._props["qualifiedUsage"] = PropertySet("qualifiedUsage","http://www.w3.org/ns/prov#qualifiedUsage", (prov___Influence,prov___Usage), False)
		self._props["used"] = PropertySet("used","http://www.w3.org/ns/prov#used", (prov___Entity,sao___StreamData,prov___Activity,sao___StreamAnalysis,prov___Agent), False)
		self._props["wasAssociatedWith"] = PropertySet("wasAssociatedWith","http://www.w3.org/ns/prov#wasAssociatedWith", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["wasAttributedTo"] = PropertySet("wasAttributedTo","http://www.w3.org/ns/prov#wasAttributedTo", (ssn___Property,prov___Entity,ssn___Sensor,prov___Agent,prov___Activity), False)
		self._props["wasDerivedFrom"] = PropertySet("wasDerivedFrom","http://www.w3.org/ns/prov#wasDerivedFrom", (prov___Entity,sao___StreamData,prov___Activity,sao___StreamAnalysis,prov___Agent), False)
		self._props["wasEndedBy"] = PropertySet("wasEndedBy","http://www.w3.org/ns/prov#wasEndedBy", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["wasGeneratedBy"] = PropertySet("wasGeneratedBy","http://www.w3.org/ns/prov#wasGeneratedBy", (prov___Entity,sao___StreamEvent,prov___Activity,prov___Agent), False)
		self._props["wasInfluencedBy"] = PropertySet("wasInfluencedBy","http://www.w3.org/ns/prov#wasInfluencedBy", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["wasInformedBy"] = PropertySet("wasInformedBy","http://www.w3.org/ns/prov#wasInformedBy", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["wasInvalidatedBy"] = PropertySet("wasInvalidatedBy","http://www.w3.org/ns/prov#wasInvalidatedBy", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["wasQuotedFrom"] = PropertySet("wasQuotedFrom","http://www.w3.org/ns/prov#wasQuotedFrom", (prov___Entity,sao___StreamData,sao___StreamAnalysis), False)
		self._props["wasRevisionOf"] = PropertySet("wasRevisionOf","http://www.w3.org/ns/prov#wasRevisionOf", (prov___Entity,sao___StreamData,sao___StreamAnalysis), False)
		self._props["wasStartedBy"] = PropertySet("wasStartedBy","http://www.w3.org/ns/prov#wasStartedBy", (prov___Entity,prov___Agent,prov___Activity), False)
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Agent"


	# Python class properties to wrap the PropertySet objects
	hasReputation = property(fget=lambda x: x._props["hasReputation"].get(), fset=lambda x,y : x._props["hasReputation"].set(y), fdel=None, doc=propDocs["hasReputation"])
	actedOnBehalfOf = property(fget=lambda x: x._props["actedOnBehalfOf"].get(), fset=lambda x,y : x._props["actedOnBehalfOf"].set(y), fdel=None, doc=propDocs["actedOnBehalfOf"])
	atLocation = property(fget=lambda x: x._props["atLocation"].get(), fset=lambda x,y : x._props["atLocation"].set(y), fdel=None, doc=propDocs["atLocation"])
	hadMember = property(fget=lambda x: x._props["hadMember"].get(), fset=lambda x,y : x._props["hadMember"].set(y), fdel=None, doc=propDocs["hadMember"])
	hadPrimarySource = property(fget=lambda x: x._props["hadPrimarySource"].get(), fset=lambda x,y : x._props["hadPrimarySource"].set(y), fdel=None, doc=propDocs["hadPrimarySource"])
	qualifiedAssociation = property(fget=lambda x: x._props["qualifiedAssociation"].get(), fset=lambda x,y : x._props["qualifiedAssociation"].set(y), fdel=None, doc=propDocs["qualifiedAssociation"])
	qualifiedAttribution = property(fget=lambda x: x._props["qualifiedAttribution"].get(), fset=lambda x,y : x._props["qualifiedAttribution"].set(y), fdel=None, doc=propDocs["qualifiedAttribution"])
	qualifiedCommunication = property(fget=lambda x: x._props["qualifiedCommunication"].get(), fset=lambda x,y : x._props["qualifiedCommunication"].set(y), fdel=None, doc=propDocs["qualifiedCommunication"])
	qualifiedDelegation = property(fget=lambda x: x._props["qualifiedDelegation"].get(), fset=lambda x,y : x._props["qualifiedDelegation"].set(y), fdel=None, doc=propDocs["qualifiedDelegation"])
	qualifiedDerivation = property(fget=lambda x: x._props["qualifiedDerivation"].get(), fset=lambda x,y : x._props["qualifiedDerivation"].set(y), fdel=None, doc=propDocs["qualifiedDerivation"])
	qualifiedEnd = property(fget=lambda x: x._props["qualifiedEnd"].get(), fset=lambda x,y : x._props["qualifiedEnd"].set(y), fdel=None, doc=propDocs["qualifiedEnd"])
	qualifiedGeneration = property(fget=lambda x: x._props["qualifiedGeneration"].get(), fset=lambda x,y : x._props["qualifiedGeneration"].set(y), fdel=None, doc=propDocs["qualifiedGeneration"])
	qualifiedInfluence = property(fget=lambda x: x._props["qualifiedInfluence"].get(), fset=lambda x,y : x._props["qualifiedInfluence"].set(y), fdel=None, doc=propDocs["qualifiedInfluence"])
	qualifiedInvalidation = property(fget=lambda x: x._props["qualifiedInvalidation"].get(), fset=lambda x,y : x._props["qualifiedInvalidation"].set(y), fdel=None, doc=propDocs["qualifiedInvalidation"])
	qualifiedPrimarySource = property(fget=lambda x: x._props["qualifiedPrimarySource"].get(), fset=lambda x,y : x._props["qualifiedPrimarySource"].set(y), fdel=None, doc=propDocs["qualifiedPrimarySource"])
	qualifiedQuotation = property(fget=lambda x: x._props["qualifiedQuotation"].get(), fset=lambda x,y : x._props["qualifiedQuotation"].set(y), fdel=None, doc=propDocs["qualifiedQuotation"])
	qualifiedRevision = property(fget=lambda x: x._props["qualifiedRevision"].get(), fset=lambda x,y : x._props["qualifiedRevision"].set(y), fdel=None, doc=propDocs["qualifiedRevision"])
	qualifiedStart = property(fget=lambda x: x._props["qualifiedStart"].get(), fset=lambda x,y : x._props["qualifiedStart"].set(y), fdel=None, doc=propDocs["qualifiedStart"])
	qualifiedUsage = property(fget=lambda x: x._props["qualifiedUsage"].get(), fset=lambda x,y : x._props["qualifiedUsage"].set(y), fdel=None, doc=propDocs["qualifiedUsage"])
	used = property(fget=lambda x: x._props["used"].get(), fset=lambda x,y : x._props["used"].set(y), fdel=None, doc=propDocs["used"])
	wasAssociatedWith = property(fget=lambda x: x._props["wasAssociatedWith"].get(), fset=lambda x,y : x._props["wasAssociatedWith"].set(y), fdel=None, doc=propDocs["wasAssociatedWith"])
	wasAttributedTo = property(fget=lambda x: x._props["wasAttributedTo"].get(), fset=lambda x,y : x._props["wasAttributedTo"].set(y), fdel=None, doc=propDocs["wasAttributedTo"])
	wasDerivedFrom = property(fget=lambda x: x._props["wasDerivedFrom"].get(), fset=lambda x,y : x._props["wasDerivedFrom"].set(y), fdel=None, doc=propDocs["wasDerivedFrom"])
	wasEndedBy = property(fget=lambda x: x._props["wasEndedBy"].get(), fset=lambda x,y : x._props["wasEndedBy"].set(y), fdel=None, doc=propDocs["wasEndedBy"])
	wasGeneratedBy = property(fget=lambda x: x._props["wasGeneratedBy"].get(), fset=lambda x,y : x._props["wasGeneratedBy"].set(y), fdel=None, doc=propDocs["wasGeneratedBy"])
	wasInfluencedBy = property(fget=lambda x: x._props["wasInfluencedBy"].get(), fset=lambda x,y : x._props["wasInfluencedBy"].set(y), fdel=None, doc=propDocs["wasInfluencedBy"])
	wasInformedBy = property(fget=lambda x: x._props["wasInformedBy"].get(), fset=lambda x,y : x._props["wasInformedBy"].set(y), fdel=None, doc=propDocs["wasInformedBy"])
	wasInvalidatedBy = property(fget=lambda x: x._props["wasInvalidatedBy"].get(), fset=lambda x,y : x._props["wasInvalidatedBy"].set(y), fdel=None, doc=propDocs["wasInvalidatedBy"])
	wasQuotedFrom = property(fget=lambda x: x._props["wasQuotedFrom"].get(), fset=lambda x,y : x._props["wasQuotedFrom"].set(y), fdel=None, doc=propDocs["wasQuotedFrom"])
	wasRevisionOf = property(fget=lambda x: x._props["wasRevisionOf"].get(), fset=lambda x,y : x._props["wasRevisionOf"].set(y), fdel=None, doc=propDocs["wasRevisionOf"])
	wasStartedBy = property(fget=lambda x: x._props["wasStartedBy"].get(), fset=lambda x,y : x._props["wasStartedBy"].set(y), fdel=None, doc=propDocs["wasStartedBy"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Entity(rdfs___Resource):
	"""
	prov:Entity
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Entity"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["actedOnBehalfOf"] = PropertySet("actedOnBehalfOf","http://www.w3.org/ns/prov#actedOnBehalfOf", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["alternateOf"] = PropertySet("alternateOf","http://www.w3.org/ns/prov#alternateOf", prov___Entity, False)
		self._props["atLocation"] = PropertySet("atLocation","http://www.w3.org/ns/prov#atLocation", prov___Location, False)
		self._props["generatedAtTime"] = PropertySet("generatedAtTime","http://www.w3.org/ns/prov#generatedAtTime", str, False)
		self._props["hadMember"] = PropertySet("hadMember","http://www.w3.org/ns/prov#hadMember", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["hadPrimarySource"] = PropertySet("hadPrimarySource","http://www.w3.org/ns/prov#hadPrimarySource", (prov___Entity,sao___StreamData,sao___StreamAnalysis), False)
		self._props["invalidatedAtTime"] = PropertySet("invalidatedAtTime","http://www.w3.org/ns/prov#invalidatedAtTime", str, False)
		self._props["qualifiedAssociation"] = PropertySet("qualifiedAssociation","http://www.w3.org/ns/prov#qualifiedAssociation", (prov___Association,prov___Influence), False)
		self._props["qualifiedAttribution"] = PropertySet("qualifiedAttribution","http://www.w3.org/ns/prov#qualifiedAttribution", (prov___Influence,prov___Attribution), False)
		self._props["qualifiedCommunication"] = PropertySet("qualifiedCommunication","http://www.w3.org/ns/prov#qualifiedCommunication", (prov___Influence,prov___Communication), False)
		self._props["qualifiedDelegation"] = PropertySet("qualifiedDelegation","http://www.w3.org/ns/prov#qualifiedDelegation", (prov___Delegation,prov___Influence), False)
		self._props["qualifiedDerivation"] = PropertySet("qualifiedDerivation","http://www.w3.org/ns/prov#qualifiedDerivation", (prov___Derivation,prov___Influence), False)
		self._props["qualifiedEnd"] = PropertySet("qualifiedEnd","http://www.w3.org/ns/prov#qualifiedEnd", (prov___End,prov___Influence), False)
		self._props["qualifiedGeneration"] = PropertySet("qualifiedGeneration","http://www.w3.org/ns/prov#qualifiedGeneration", (prov___Generation,prov___Influence), False)
		self._props["qualifiedInfluence"] = PropertySet("qualifiedInfluence","http://www.w3.org/ns/prov#qualifiedInfluence", prov___Influence, False)
		self._props["qualifiedInvalidation"] = PropertySet("qualifiedInvalidation","http://www.w3.org/ns/prov#qualifiedInvalidation", (prov___Invalidation,prov___Influence), False)
		self._props["qualifiedPrimarySource"] = PropertySet("qualifiedPrimarySource","http://www.w3.org/ns/prov#qualifiedPrimarySource", (prov___PrimarySource,prov___Influence), False)
		self._props["qualifiedQuotation"] = PropertySet("qualifiedQuotation","http://www.w3.org/ns/prov#qualifiedQuotation", (prov___Quotation,prov___Influence), False)
		self._props["qualifiedRevision"] = PropertySet("qualifiedRevision","http://www.w3.org/ns/prov#qualifiedRevision", (prov___Revision,prov___Influence), False)
		self._props["qualifiedStart"] = PropertySet("qualifiedStart","http://www.w3.org/ns/prov#qualifiedStart", (prov___Influence,prov___Start), False)
		self._props["qualifiedUsage"] = PropertySet("qualifiedUsage","http://www.w3.org/ns/prov#qualifiedUsage", (prov___Influence,prov___Usage), False)
		self._props["specializationOf"] = PropertySet("specializationOf","http://www.w3.org/ns/prov#specializationOf", prov___Entity, False)
		self._props["used"] = PropertySet("used","http://www.w3.org/ns/prov#used", (prov___Entity,sao___StreamData,prov___Activity,sao___StreamAnalysis,prov___Agent), False)
		self._props["value"] = PropertySet("value","http://www.w3.org/ns/prov#value", None, False)
		self._props["wasAssociatedWith"] = PropertySet("wasAssociatedWith","http://www.w3.org/ns/prov#wasAssociatedWith", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["wasAttributedTo"] = PropertySet("wasAttributedTo","http://www.w3.org/ns/prov#wasAttributedTo", (ssn___Property,prov___Entity,ssn___Sensor,prov___Agent,prov___Activity), False)
		self._props["wasDerivedFrom"] = PropertySet("wasDerivedFrom","http://www.w3.org/ns/prov#wasDerivedFrom", (prov___Entity,sao___StreamData,prov___Activity,sao___StreamAnalysis,prov___Agent), False)
		self._props["wasEndedBy"] = PropertySet("wasEndedBy","http://www.w3.org/ns/prov#wasEndedBy", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["wasGeneratedBy"] = PropertySet("wasGeneratedBy","http://www.w3.org/ns/prov#wasGeneratedBy", (prov___Entity,sao___StreamEvent,prov___Activity,prov___Agent), False)
		self._props["wasInfluencedBy"] = PropertySet("wasInfluencedBy","http://www.w3.org/ns/prov#wasInfluencedBy", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["wasInformedBy"] = PropertySet("wasInformedBy","http://www.w3.org/ns/prov#wasInformedBy", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["wasInvalidatedBy"] = PropertySet("wasInvalidatedBy","http://www.w3.org/ns/prov#wasInvalidatedBy", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["wasQuotedFrom"] = PropertySet("wasQuotedFrom","http://www.w3.org/ns/prov#wasQuotedFrom", (prov___Entity,sao___StreamData,sao___StreamAnalysis), False)
		self._props["wasRevisionOf"] = PropertySet("wasRevisionOf","http://www.w3.org/ns/prov#wasRevisionOf", (prov___Entity,sao___StreamData,sao___StreamAnalysis), False)
		self._props["wasStartedBy"] = PropertySet("wasStartedBy","http://www.w3.org/ns/prov#wasStartedBy", (prov___Entity,prov___Agent,prov___Activity), False)
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Entity"


	# Python class properties to wrap the PropertySet objects
	actedOnBehalfOf = property(fget=lambda x: x._props["actedOnBehalfOf"].get(), fset=lambda x,y : x._props["actedOnBehalfOf"].set(y), fdel=None, doc=propDocs["actedOnBehalfOf"])
	alternateOf = property(fget=lambda x: x._props["alternateOf"].get(), fset=lambda x,y : x._props["alternateOf"].set(y), fdel=None, doc=propDocs["alternateOf"])
	atLocation = property(fget=lambda x: x._props["atLocation"].get(), fset=lambda x,y : x._props["atLocation"].set(y), fdel=None, doc=propDocs["atLocation"])
	generatedAtTime = property(fget=lambda x: x._props["generatedAtTime"].get(), fset=lambda x,y : x._props["generatedAtTime"].set(y), fdel=None, doc=propDocs["generatedAtTime"])
	hadMember = property(fget=lambda x: x._props["hadMember"].get(), fset=lambda x,y : x._props["hadMember"].set(y), fdel=None, doc=propDocs["hadMember"])
	hadPrimarySource = property(fget=lambda x: x._props["hadPrimarySource"].get(), fset=lambda x,y : x._props["hadPrimarySource"].set(y), fdel=None, doc=propDocs["hadPrimarySource"])
	invalidatedAtTime = property(fget=lambda x: x._props["invalidatedAtTime"].get(), fset=lambda x,y : x._props["invalidatedAtTime"].set(y), fdel=None, doc=propDocs["invalidatedAtTime"])
	qualifiedAssociation = property(fget=lambda x: x._props["qualifiedAssociation"].get(), fset=lambda x,y : x._props["qualifiedAssociation"].set(y), fdel=None, doc=propDocs["qualifiedAssociation"])
	qualifiedAttribution = property(fget=lambda x: x._props["qualifiedAttribution"].get(), fset=lambda x,y : x._props["qualifiedAttribution"].set(y), fdel=None, doc=propDocs["qualifiedAttribution"])
	qualifiedCommunication = property(fget=lambda x: x._props["qualifiedCommunication"].get(), fset=lambda x,y : x._props["qualifiedCommunication"].set(y), fdel=None, doc=propDocs["qualifiedCommunication"])
	qualifiedDelegation = property(fget=lambda x: x._props["qualifiedDelegation"].get(), fset=lambda x,y : x._props["qualifiedDelegation"].set(y), fdel=None, doc=propDocs["qualifiedDelegation"])
	qualifiedDerivation = property(fget=lambda x: x._props["qualifiedDerivation"].get(), fset=lambda x,y : x._props["qualifiedDerivation"].set(y), fdel=None, doc=propDocs["qualifiedDerivation"])
	qualifiedEnd = property(fget=lambda x: x._props["qualifiedEnd"].get(), fset=lambda x,y : x._props["qualifiedEnd"].set(y), fdel=None, doc=propDocs["qualifiedEnd"])
	qualifiedGeneration = property(fget=lambda x: x._props["qualifiedGeneration"].get(), fset=lambda x,y : x._props["qualifiedGeneration"].set(y), fdel=None, doc=propDocs["qualifiedGeneration"])
	qualifiedInfluence = property(fget=lambda x: x._props["qualifiedInfluence"].get(), fset=lambda x,y : x._props["qualifiedInfluence"].set(y), fdel=None, doc=propDocs["qualifiedInfluence"])
	qualifiedInvalidation = property(fget=lambda x: x._props["qualifiedInvalidation"].get(), fset=lambda x,y : x._props["qualifiedInvalidation"].set(y), fdel=None, doc=propDocs["qualifiedInvalidation"])
	qualifiedPrimarySource = property(fget=lambda x: x._props["qualifiedPrimarySource"].get(), fset=lambda x,y : x._props["qualifiedPrimarySource"].set(y), fdel=None, doc=propDocs["qualifiedPrimarySource"])
	qualifiedQuotation = property(fget=lambda x: x._props["qualifiedQuotation"].get(), fset=lambda x,y : x._props["qualifiedQuotation"].set(y), fdel=None, doc=propDocs["qualifiedQuotation"])
	qualifiedRevision = property(fget=lambda x: x._props["qualifiedRevision"].get(), fset=lambda x,y : x._props["qualifiedRevision"].set(y), fdel=None, doc=propDocs["qualifiedRevision"])
	qualifiedStart = property(fget=lambda x: x._props["qualifiedStart"].get(), fset=lambda x,y : x._props["qualifiedStart"].set(y), fdel=None, doc=propDocs["qualifiedStart"])
	qualifiedUsage = property(fget=lambda x: x._props["qualifiedUsage"].get(), fset=lambda x,y : x._props["qualifiedUsage"].set(y), fdel=None, doc=propDocs["qualifiedUsage"])
	specializationOf = property(fget=lambda x: x._props["specializationOf"].get(), fset=lambda x,y : x._props["specializationOf"].set(y), fdel=None, doc=propDocs["specializationOf"])
	used = property(fget=lambda x: x._props["used"].get(), fset=lambda x,y : x._props["used"].set(y), fdel=None, doc=propDocs["used"])
	value = property(fget=lambda x: x._props["value"].get(), fset=lambda x,y : x._props["value"].set(y), fdel=None, doc=propDocs["value"])
	wasAssociatedWith = property(fget=lambda x: x._props["wasAssociatedWith"].get(), fset=lambda x,y : x._props["wasAssociatedWith"].set(y), fdel=None, doc=propDocs["wasAssociatedWith"])
	wasAttributedTo = property(fget=lambda x: x._props["wasAttributedTo"].get(), fset=lambda x,y : x._props["wasAttributedTo"].set(y), fdel=None, doc=propDocs["wasAttributedTo"])
	wasDerivedFrom = property(fget=lambda x: x._props["wasDerivedFrom"].get(), fset=lambda x,y : x._props["wasDerivedFrom"].set(y), fdel=None, doc=propDocs["wasDerivedFrom"])
	wasEndedBy = property(fget=lambda x: x._props["wasEndedBy"].get(), fset=lambda x,y : x._props["wasEndedBy"].set(y), fdel=None, doc=propDocs["wasEndedBy"])
	wasGeneratedBy = property(fget=lambda x: x._props["wasGeneratedBy"].get(), fset=lambda x,y : x._props["wasGeneratedBy"].set(y), fdel=None, doc=propDocs["wasGeneratedBy"])
	wasInfluencedBy = property(fget=lambda x: x._props["wasInfluencedBy"].get(), fset=lambda x,y : x._props["wasInfluencedBy"].set(y), fdel=None, doc=propDocs["wasInfluencedBy"])
	wasInformedBy = property(fget=lambda x: x._props["wasInformedBy"].get(), fset=lambda x,y : x._props["wasInformedBy"].set(y), fdel=None, doc=propDocs["wasInformedBy"])
	wasInvalidatedBy = property(fget=lambda x: x._props["wasInvalidatedBy"].get(), fset=lambda x,y : x._props["wasInvalidatedBy"].set(y), fdel=None, doc=propDocs["wasInvalidatedBy"])
	wasQuotedFrom = property(fget=lambda x: x._props["wasQuotedFrom"].get(), fset=lambda x,y : x._props["wasQuotedFrom"].set(y), fdel=None, doc=propDocs["wasQuotedFrom"])
	wasRevisionOf = property(fget=lambda x: x._props["wasRevisionOf"].get(), fset=lambda x,y : x._props["wasRevisionOf"].set(y), fdel=None, doc=propDocs["wasRevisionOf"])
	wasStartedBy = property(fget=lambda x: x._props["wasStartedBy"].get(), fset=lambda x,y : x._props["wasStartedBy"].set(y), fdel=None, doc=propDocs["wasStartedBy"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Influence(rdfs___Resource):
	"""
	prov:Influence
	Because prov:Influence is a broad relation, its most specific subclasses (e.g. prov:Communication, prov:Delegation, prov:End, prov:Revision, etc.) should be used when applicable.
	An instance of prov:Influence provides additional descriptions about the binary prov:wasInfluencedBy relation from some influenced Activity, Entity, or Agent to the influencing Activity, Entity, or Agent. For example, :stomach_ache prov:wasInfluencedBy :spoon; prov:qualifiedInfluence [ a prov:Influence; prov:entity :spoon; :foo :bar ] . Because prov:Influence is a broad relation, the more specific relations (Communication, Delegation, End, etc.) should be used when applicable.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Influence"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["activity"] = PropertySet("activity","http://www.w3.org/ns/prov#activity", (owl___Thing,prov___Activity), False)
		self._props["agent"] = PropertySet("agent","http://www.w3.org/ns/prov#agent", (owl___Thing,prov___Agent), False)
		self._props["entity"] = PropertySet("entity","http://www.w3.org/ns/prov#entity", (prov___Entity,owl___Thing), False)
		self._props["hadActivity"] = PropertySet("hadActivity","http://www.w3.org/ns/prov#hadActivity", prov___Activity, False)
		self._props["hadRole"] = PropertySet("hadRole","http://www.w3.org/ns/prov#hadRole", prov___Role, False)
		self._props["influencer"] = PropertySet("influencer","http://www.w3.org/ns/prov#influencer", owl___Thing, False)
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Influence"


	# Python class properties to wrap the PropertySet objects
	activity = property(fget=lambda x: x._props["activity"].get(), fset=lambda x,y : x._props["activity"].set(y), fdel=None, doc=propDocs["activity"])
	agent = property(fget=lambda x: x._props["agent"].get(), fset=lambda x,y : x._props["agent"].set(y), fdel=None, doc=propDocs["agent"])
	entity = property(fget=lambda x: x._props["entity"].get(), fset=lambda x,y : x._props["entity"].set(y), fdel=None, doc=propDocs["entity"])
	hadActivity = property(fget=lambda x: x._props["hadActivity"].get(), fset=lambda x,y : x._props["hadActivity"].set(y), fdel=None, doc=propDocs["hadActivity"])
	hadRole = property(fget=lambda x: x._props["hadRole"].get(), fset=lambda x,y : x._props["hadRole"].set(y), fdel=None, doc=propDocs["hadRole"])
	influencer = property(fget=lambda x: x._props["influencer"].get(), fset=lambda x,y : x._props["influencer"].set(y), fdel=None, doc=propDocs["influencer"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Location(rdfs___Resource):
	"""
	prov:Location
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Location"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Location"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Person(prov___Agent):
	"""
	prov:Person
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___Agent.__init__(self)
		self._initialised = False
		self.shortname = "Person"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Person"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Role(rdfs___Resource):
	"""
	prov:Role
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Role"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Role"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___Agent(rdfs___Resource):
	"""
	foaf:Agent
	An agent (eg. person, group, software or physical artifact).
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Agent"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["aimChatID"] = PropertySet("aimChatID","http://xmlns.com/foaf/0.1/aimChatID", None, True)
		self._props["birthday"] = PropertySet("birthday","http://xmlns.com/foaf/0.1/birthday", None, True)
		self._props["gender"] = PropertySet("gender","http://xmlns.com/foaf/0.1/gender", None, True)
		self._props["holdsAccount"] = PropertySet("holdsAccount","http://xmlns.com/foaf/0.1/holdsAccount", foaf___OnlineAccount, False)
		self._props["icqChatID"] = PropertySet("icqChatID","http://xmlns.com/foaf/0.1/icqChatID", None, True)
		self._props["jabberID"] = PropertySet("jabberID","http://xmlns.com/foaf/0.1/jabberID", None, True)
		self._props["made"] = PropertySet("made","http://xmlns.com/foaf/0.1/made", owl___Thing, False)
		self._props["mbox"] = PropertySet("mbox","http://xmlns.com/foaf/0.1/mbox", owl___Thing, False)
		self._props["mbox_sha1sum"] = PropertySet("mbox_sha1sum","http://xmlns.com/foaf/0.1/mbox_sha1sum", None, True)
		self._props["msnChatID"] = PropertySet("msnChatID","http://xmlns.com/foaf/0.1/msnChatID", None, True)
		self._props["openid"] = PropertySet("openid","http://xmlns.com/foaf/0.1/openid", foaf___Document, False)
		self._props["tipjar"] = PropertySet("tipjar","http://xmlns.com/foaf/0.1/tipjar", foaf___Document, False)
		self._props["weblog"] = PropertySet("weblog","http://xmlns.com/foaf/0.1/weblog", foaf___Document, False)
		self._props["yahooChatID"] = PropertySet("yahooChatID","http://xmlns.com/foaf/0.1/yahooChatID", None, True)
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/Agent"


	# Python class properties to wrap the PropertySet objects
	aimChatID = property(fget=lambda x: x._props["aimChatID"].get(), fset=lambda x,y : x._props["aimChatID"].set(y), fdel=None, doc=propDocs["aimChatID"])
	birthday = property(fget=lambda x: x._props["birthday"].get(), fset=lambda x,y : x._props["birthday"].set(y), fdel=None, doc=propDocs["birthday"])
	gender = property(fget=lambda x: x._props["gender"].get(), fset=lambda x,y : x._props["gender"].set(y), fdel=None, doc=propDocs["gender"])
	holdsAccount = property(fget=lambda x: x._props["holdsAccount"].get(), fset=lambda x,y : x._props["holdsAccount"].set(y), fdel=None, doc=propDocs["holdsAccount"])
	icqChatID = property(fget=lambda x: x._props["icqChatID"].get(), fset=lambda x,y : x._props["icqChatID"].set(y), fdel=None, doc=propDocs["icqChatID"])
	jabberID = property(fget=lambda x: x._props["jabberID"].get(), fset=lambda x,y : x._props["jabberID"].set(y), fdel=None, doc=propDocs["jabberID"])
	made = property(fget=lambda x: x._props["made"].get(), fset=lambda x,y : x._props["made"].set(y), fdel=None, doc=propDocs["made"])
	mbox = property(fget=lambda x: x._props["mbox"].get(), fset=lambda x,y : x._props["mbox"].set(y), fdel=None, doc=propDocs["mbox"])
	mbox_sha1sum = property(fget=lambda x: x._props["mbox_sha1sum"].get(), fset=lambda x,y : x._props["mbox_sha1sum"].set(y), fdel=None, doc=propDocs["mbox_sha1sum"])
	msnChatID = property(fget=lambda x: x._props["msnChatID"].get(), fset=lambda x,y : x._props["msnChatID"].set(y), fdel=None, doc=propDocs["msnChatID"])
	openid = property(fget=lambda x: x._props["openid"].get(), fset=lambda x,y : x._props["openid"].set(y), fdel=None, doc=propDocs["openid"])
	tipjar = property(fget=lambda x: x._props["tipjar"].get(), fset=lambda x,y : x._props["tipjar"].set(y), fdel=None, doc=propDocs["tipjar"])
	weblog = property(fget=lambda x: x._props["weblog"].get(), fset=lambda x,y : x._props["weblog"].set(y), fdel=None, doc=propDocs["weblog"])
	yahooChatID = property(fget=lambda x: x._props["yahooChatID"].get(), fset=lambda x,y : x._props["yahooChatID"].set(y), fdel=None, doc=propDocs["yahooChatID"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___Group(foaf___Agent):
	"""
	foaf:Group
	A class of Agents.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___Agent.__init__(self)
		self._initialised = False
		self.shortname = "Group"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["member"] = PropertySet("member","http://xmlns.com/foaf/0.1/member", foaf___Agent, False)
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/Group"


	# Python class properties to wrap the PropertySet objects
	member = property(fget=lambda x: x._props["member"].get(), fset=lambda x,y : x._props["member"].set(y), fdel=None, doc=propDocs["member"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___OnlineChatAccount(foaf___OnlineAccount):
	"""
	foaf:OnlineChatAccount
	An online chat account.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___OnlineAccount.__init__(self)
		self._initialised = False
		self.shortname = "OnlineChatAccount"
		self.URI = URI
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/OnlineChatAccount"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___Organization(foaf___Agent):
	"""
	foaf:Organization
	An organization.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___Agent.__init__(self)
		self._initialised = False
		self.shortname = "Organization"
		self.URI = URI
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/Organization"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___Project(rdfs___Resource):
	"""
	foaf:Project
	A project (a collective endeavour of some kind).
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Project"
		self.URI = URI
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/Project"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ns1___DayOfWeek(rdfs___Resource):
	"""
	ns1:DayOfWeek
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "DayOfWeek"
		self.URI = URI
		self._initialised = True
	classURI = "file:///Users/sefki/Desktop/Desktop/SAOcodesTestCopy/Ontologies/DayOfWeek"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___CongestionFactor(rdfs___Resource):
	"""
	ct:CongestionFactor
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "CongestionFactor"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#CongestionFactor"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___ReportID(rdfs___Resource):
	"""
	ct:ReportID
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "ReportID"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#ReportID"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Quality(rdfs___Resource):
	"""
	qoi:Quality
	The Quality is the description of some values for the quality of a data stream.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Quality"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasAbsoluteQuality"] = PropertySet("hasAbsoluteQuality","http://purl.oclc.org/NET/UASO/qoi#hasAbsoluteQuality", None, False)
		self._props["hasRatedQuality"] = PropertySet("hasRatedQuality","http://purl.oclc.org/NET/UASO/qoi#hasRatedQuality", None, False)
		self._props["hasUnitOfMeasurement"] = PropertySet("hasUnitOfMeasurement","http://purl.oclc.org/NET/UASO/qoi#hasUnitOfMeasurement", muo___UnitOfMeasurement, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Quality"


	# Python class properties to wrap the PropertySet objects
	hasAbsoluteQuality = property(fget=lambda x: x._props["hasAbsoluteQuality"].get(), fset=lambda x,y : x._props["hasAbsoluteQuality"].set(y), fdel=None, doc=propDocs["hasAbsoluteQuality"])
	hasRatedQuality = property(fget=lambda x: x._props["hasRatedQuality"].get(), fset=lambda x,y : x._props["hasRatedQuality"].set(y), fdel=None, doc=propDocs["hasRatedQuality"])
	hasUnitOfMeasurement = property(fget=lambda x: x._props["hasUnitOfMeasurement"].get(), fset=lambda x,y : x._props["hasUnitOfMeasurement"].set(y), fdel=None, doc=propDocs["hasUnitOfMeasurement"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Reputation(rdfs___Resource):
	"""
	qoi:Reputation
	Reputation value to measure the trustworthiness of a data stream. Reputation cannot be negative and only reach 1 (0-100%)
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Reputation"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasReputationValue"] = PropertySet("hasReputationValue","http://purl.oclc.org/NET/UASO/qoi#hasReputationValue", None, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Reputation"


	# Python class properties to wrap the PropertySet objects
	hasReputationValue = property(fget=lambda x: x._props["hasReputationValue"].get(), fset=lambda x,y : x._props["hasReputationValue"].set(y), fdel=None, doc=propDocs["hasReputationValue"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Security(qoi___Quality):
	"""
	qoi:Security
	This cetagory describes security and confidentiality related attributes of a data stream.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Quality.__init__(self)
		self._initialised = False
		self.shortname = "Security"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Security"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Timeliness(qoi___Quality):
	"""
	qoi:Timeliness
	Category to describe time related attributes of a data stream.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Quality.__init__(self)
		self._initialised = False
		self.shortname = "Timeliness"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Timeliness"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class muo___PhysicalQuality(rdfs___Resource):
	"""
	muo:PhysicalQuality
	The physical qualities such as mass, weight, speed, etc. are kind of properties that can be quantified i.e. that can be perceived, measured or even calculated. The concept of physical quality is similar to the notion of quality, used in metrology, the science of measurement. We distinguish between: 1) A physical quality in the general sense: a kind of physical property ascribed to phenomena that can be quantified for a particular phenomenon (e.g. length and electrical charge); 2) A physical quantity in the particular sense: a quantifiable property ascribed to a particular phenomenon (e.g. the weight of my device). MUO only uses physical quantities in the general sense.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "PhysicalQuality"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/muo/muo#PhysicalQuality"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class muo___QualityValue(rdfs___Resource):
	"""
	muo:QualityValue
	The value of an individual quality, for instance, the weight of an individual object.   If we consider metrology, the value of a physical quality Q is expressed as the product of a numerical value {Q} and a physical unit [Q]: Q = {Q} x [Q]. In MUO, the class muo:QualityValue is used to represent the values of qualities, Q. Instances of this class are related with 1) exactly one unit, suitable for measure the physical quality (meters for length, grams for weight, etc), by means of the property muo:measuredIn, [Q]; 2) a number, which express the relationship between the value and the unit by means of the rdf:value property, {Q}; 3) a time, which expresses the quality value along the line of time. Quality values can be temporalized, but this is not always necessary.

	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "QualityValue"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["inTime"] = PropertySet("inTime","http://purl.oclc.org/NET/muo/muo#inTime", str, False)
		self._props["measuredIn"] = PropertySet("measuredIn","http://purl.oclc.org/NET/muo/muo#measuredIn", muo___UnitOfMeasurement, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/muo/muo#QualityValue"


	# Python class properties to wrap the PropertySet objects
	inTime = property(fget=lambda x: x._props["inTime"].get(), fset=lambda x,y : x._props["inTime"].set(y), fdel=None, doc=propDocs["inTime"])
	measuredIn = property(fget=lambda x: x._props["measuredIn"].get(), fset=lambda x,y : x._props["measuredIn"].set(y), fdel=None, doc=propDocs["measuredIn"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class muo___UnitOfMeasurement(rdfs___Resource):
	"""
	muo:UnitOfMeasurement
	Measurement units are standards for measurement of physical properties or qualities. Every unit is related to a particular kind of property. For instance, the meter unit is uniquely related to the length property. Under our ontological approach, units are abstract spaces used as a reference metrics for quality spaces, such as physical qualia, and they are counted by some number. For instance, weight-units define some quality spaces for the weight-quality where specific weights of objects, like devices or persons, are located by means of comparisons with the proper weight-value of the selected weight-unit.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "UnitOfMeasurement"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["altSymbol"] = PropertySet("altSymbol","http://purl.oclc.org/NET/muo/muo#altSymbol", None, False)
		self._props["measuresQuality"] = PropertySet("measuresQuality","http://purl.oclc.org/NET/muo/muo#measuresQuality", muo___PhysicalQuality, False)
		self._props["prefSymbol"] = PropertySet("prefSymbol","http://purl.oclc.org/NET/muo/muo#prefSymbol", None, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/muo/muo#UnitOfMeasurement"


	# Python class properties to wrap the PropertySet objects
	altSymbol = property(fget=lambda x: x._props["altSymbol"].get(), fset=lambda x,y : x._props["altSymbol"].set(y), fdel=None, doc=propDocs["altSymbol"])
	measuresQuality = property(fget=lambda x: x._props["measuresQuality"].get(), fset=lambda x,y : x._props["measuresQuality"].set(y), fdel=None, doc=propDocs["measuresQuality"])
	prefSymbol = property(fget=lambda x: x._props["prefSymbol"].get(), fset=lambda x,y : x._props["prefSymbol"].set(y), fdel=None, doc=propDocs["prefSymbol"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Input(rdfs___Resource):
	"""
	ssn:Input
	Any information that is provided to a process for its use [MMI OntDev]
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Input"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Input"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Output(rdfs___Resource):
	"""
	ssn:Output
	Any information that is reported from a process. [MMI OntDev]
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Output"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Output"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___DiscreteInstant(rdfs___Resource):
	"""
	tl:DiscreteInstant
	An instant defined on a discrete timeline
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "DiscreteInstant"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["atInt"] = PropertySet("atInt","http://purl.org/NET/c4dm/timeline.owl#atInt", int, True)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#DiscreteInstant"


	# Python class properties to wrap the PropertySet objects
	atInt = property(fget=lambda x: x._props["atInt"].get(), fset=lambda x,y : x._props["atInt"].set(y), fdel=None, doc=propDocs["atInt"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___Instant(rdfs___Resource):
	"""
	tl:Instant
	An instant (same as in OWL-Time)
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Instant"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["at"] = PropertySet("at","http://purl.org/NET/c4dm/timeline.owl#at", None, True)
		self._props["atDate"] = PropertySet("atDate","http://purl.org/NET/c4dm/timeline.owl#atDate", None, True)
		self._props["atDateTime"] = PropertySet("atDateTime","http://purl.org/NET/c4dm/timeline.owl#atDateTime", None, True)
		self._props["atDuration"] = PropertySet("atDuration","http://purl.org/NET/c4dm/timeline.owl#atDuration", str, True)
		self._props["atInt"] = PropertySet("atInt","http://purl.org/NET/c4dm/timeline.owl#atInt", int, True)
		self._props["atReal"] = PropertySet("atReal","http://purl.org/NET/c4dm/timeline.owl#atReal", float, True)
		self._props["atYear"] = PropertySet("atYear","http://purl.org/NET/c4dm/timeline.owl#atYear", int, True)
		self._props["atYearMonth"] = PropertySet("atYearMonth","http://purl.org/NET/c4dm/timeline.owl#atYearMonth", str, True)
		self._props["onTimeLine"] = PropertySet("onTimeLine","http://purl.org/NET/c4dm/timeline.owl#onTimeLine", tl___TimeLine, False)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#Instant"


	# Python class properties to wrap the PropertySet objects
	at = property(fget=lambda x: x._props["at"].get(), fset=lambda x,y : x._props["at"].set(y), fdel=None, doc=propDocs["at"])
	atDate = property(fget=lambda x: x._props["atDate"].get(), fset=lambda x,y : x._props["atDate"].set(y), fdel=None, doc=propDocs["atDate"])
	atDateTime = property(fget=lambda x: x._props["atDateTime"].get(), fset=lambda x,y : x._props["atDateTime"].set(y), fdel=None, doc=propDocs["atDateTime"])
	atDuration = property(fget=lambda x: x._props["atDuration"].get(), fset=lambda x,y : x._props["atDuration"].set(y), fdel=None, doc=propDocs["atDuration"])
	atInt = property(fget=lambda x: x._props["atInt"].get(), fset=lambda x,y : x._props["atInt"].set(y), fdel=None, doc=propDocs["atInt"])
	atReal = property(fget=lambda x: x._props["atReal"].get(), fset=lambda x,y : x._props["atReal"].set(y), fdel=None, doc=propDocs["atReal"])
	atYear = property(fget=lambda x: x._props["atYear"].get(), fset=lambda x,y : x._props["atYear"].set(y), fdel=None, doc=propDocs["atYear"])
	atYearMonth = property(fget=lambda x: x._props["atYearMonth"].get(), fset=lambda x,y : x._props["atYearMonth"].set(y), fdel=None, doc=propDocs["atYearMonth"])
	onTimeLine = property(fget=lambda x: x._props["onTimeLine"].get(), fset=lambda x,y : x._props["onTimeLine"].set(y), fdel=None, doc=propDocs["onTimeLine"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___RelativeInstant(rdfs___Resource):
	"""
	tl:RelativeInstant
	An instant defined on a relative timeline
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "RelativeInstant"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["atDuration"] = PropertySet("atDuration","http://purl.org/NET/c4dm/timeline.owl#atDuration", str, True)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#RelativeInstant"


	# Python class properties to wrap the PropertySet objects
	atDuration = property(fget=lambda x: x._props["atDuration"].get(), fset=lambda x,y : x._props["atDuration"].set(y), fdel=None, doc=propDocs["atDuration"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___TimeLine(rdfs___Resource):
	"""
	tl:TimeLine
	Represents a linear and coherent piece of time -- can be either abstract (such as the one behind a score) or concrete (such as the universal time line).
            Two timelines can be mapped using timeline maps.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "TimeLine"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#TimeLine"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___UTInstant(rdfs___Resource):
	"""
	tl:UTInstant
	This concept expresses that an instant defined on the universal timeline must be associated to a dateTime value
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "UTInstant"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["atDateTime"] = PropertySet("atDateTime","http://purl.org/NET/c4dm/timeline.owl#atDateTime", None, True)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#UTInstant"


	# Python class properties to wrap the PropertySet objects
	atDateTime = property(fget=lambda x: x._props["atDateTime"].get(), fset=lambda x,y : x._props["atDateTime"].set(y), fdel=None, doc=propDocs["atDateTime"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class owlsg___Grounding(rdfs___Resource):
	"""
	owlsg:Grounding
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Grounding"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.daml.org/services/owl-s/1.2/Grounding.owl#Grounding"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class owlss___Service(rdfs___Resource):
	"""
	owlss:Service
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Service"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.daml.org/services/owl-s/1.2/Service.owl#Service"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class owlssrp___ServiceParameter(rdfs___Resource):
	"""
	owlssrp:ServiceParameter
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "ServiceParameter"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.daml.org/services/owl-s/1.2/ServiceParameter.owl#ServiceParameter"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___Constraint(rdfs___Resource):
	"""
	ces:Constraint
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Constraint"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasExpression"] = PropertySet("hasExpression","http://www.insight-centre.org/ces#hasExpression", None, False)
		self._props["onProperty"] = PropertySet("onProperty","http://www.insight-centre.org/ces#onProperty", owlssrp___ServiceParameter, False)
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#Constraint"


	# Python class properties to wrap the PropertySet objects
	hasExpression = property(fget=lambda x: x._props["hasExpression"].get(), fset=lambda x,y : x._props["hasExpression"].set(y), fdel=None, doc=propDocs["hasExpression"])
	onProperty = property(fget=lambda x: x._props["onProperty"].get(), fset=lambda x,y : x._props["onProperty"].set(y), fdel=None, doc=propDocs["onProperty"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___EventPattern(rdfs___Resource):
	"""
	ces:EventPattern
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "EventPattern"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasAggregation"] = PropertySet("hasAggregation","http://www.insight-centre.org/ces#hasAggregation", (ces___EventPattern,ces___Aggregation), False)
		self._props["hasFilter"] = PropertySet("hasFilter","http://www.insight-centre.org/ces#hasFilter", (ces___EventPattern,ces___Filter), False)
		self._props["hasPattern"] = PropertySet("hasPattern","http://www.insight-centre.org/ces#hasPattern", ces___EventPattern, False)
		self._props["hasSelection"] = PropertySet("hasSelection","http://www.insight-centre.org/ces#hasSelection", (ces___EventPattern,ces___Selection), False)
		self._props["hasSubPattern"] = PropertySet("hasSubPattern","http://www.insight-centre.org/ces#hasSubPattern", (ces___EventPattern,ces___EventService), False)
		self._props["hasWindow"] = PropertySet("hasWindow","http://www.insight-centre.org/ces#hasWindow", ces___SlidingWindow, False)
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#EventPattern"


	# Python class properties to wrap the PropertySet objects
	hasAggregation = property(fget=lambda x: x._props["hasAggregation"].get(), fset=lambda x,y : x._props["hasAggregation"].set(y), fdel=None, doc=propDocs["hasAggregation"])
	hasFilter = property(fget=lambda x: x._props["hasFilter"].get(), fset=lambda x,y : x._props["hasFilter"].set(y), fdel=None, doc=propDocs["hasFilter"])
	hasPattern = property(fget=lambda x: x._props["hasPattern"].get(), fset=lambda x,y : x._props["hasPattern"].set(y), fdel=None, doc=propDocs["hasPattern"])
	hasSelection = property(fget=lambda x: x._props["hasSelection"].get(), fset=lambda x,y : x._props["hasSelection"].set(y), fdel=None, doc=propDocs["hasSelection"])
	hasSubPattern = property(fget=lambda x: x._props["hasSubPattern"].get(), fset=lambda x,y : x._props["hasSubPattern"].set(y), fdel=None, doc=propDocs["hasSubPattern"])
	hasWindow = property(fget=lambda x: x._props["hasWindow"].get(), fset=lambda x,y : x._props["hasWindow"].set(y), fdel=None, doc=propDocs["hasWindow"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___EventService(owlss___Service):
	"""
	ces:EventService
	"""
	def __init__(self,URI=None):
		# Initialise parents
		owlss___Service.__init__(self)
		self._initialised = False
		self.shortname = "EventService"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["supports"] = PropertySet("supports","http://www.daml.org/services/owl-s/1.2/Service.owl#supports", (ces___HttpGrounding,ces___WebSocketGrounding,owlsg___Grounding,ces___MessageBusGrounding), False)
		self._props["hasPhysicalEventSource"] = PropertySet("hasPhysicalEventSource","http://www.insight-centre.org/ces#hasPhysicalEventSource", ssn___Sensor, False)
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#EventService"


	# Python class properties to wrap the PropertySet objects
	supports = property(fget=lambda x: x._props["supports"].get(), fset=lambda x,y : x._props["supports"].set(y), fdel=None, doc=propDocs["supports"])
	hasPhysicalEventSource = property(fget=lambda x: x._props["hasPhysicalEventSource"].get(), fset=lambda x,y : x._props["hasPhysicalEventSource"].set(y), fdel=None, doc=propDocs["hasPhysicalEventSource"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___HttpGrounding(owlsg___Grounding):
	"""
	ces:HttpGrounding
	"""
	def __init__(self,URI=None):
		# Initialise parents
		owlsg___Grounding.__init__(self)
		self._initialised = False
		self.shortname = "HttpGrounding"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["httpService"] = PropertySet("httpService","http://www.insight-centre.org/ces#httpService", str, False)
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#HttpGrounding"


	# Python class properties to wrap the PropertySet objects
	httpService = property(fget=lambda x: x._props["httpService"].get(), fset=lambda x,y : x._props["httpService"].set(y), fdel=None, doc=propDocs["httpService"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___MessageBusGrounding(owlsg___Grounding):
	"""
	ces:MessageBusGrounding
	"""
	def __init__(self,URI=None):
		# Initialise parents
		owlsg___Grounding.__init__(self)
		self._initialised = False
		self.shortname = "MessageBusGrounding"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasExchangeName"] = PropertySet("hasExchangeName","http://www.insight-centre.org/ces#hasExchangeName", str, False)
		self._props["hasServerAddress"] = PropertySet("hasServerAddress","http://www.insight-centre.org/ces#hasServerAddress", str, False)
		self._props["hasTopic"] = PropertySet("hasTopic","http://www.insight-centre.org/ces#hasTopic", str, False)
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#MessageBusGrounding"


	# Python class properties to wrap the PropertySet objects
	hasExchangeName = property(fget=lambda x: x._props["hasExchangeName"].get(), fset=lambda x,y : x._props["hasExchangeName"].set(y), fdel=None, doc=propDocs["hasExchangeName"])
	hasServerAddress = property(fget=lambda x: x._props["hasServerAddress"].get(), fset=lambda x,y : x._props["hasServerAddress"].set(y), fdel=None, doc=propDocs["hasServerAddress"])
	hasTopic = property(fget=lambda x: x._props["hasTopic"].get(), fset=lambda x,y : x._props["hasTopic"].set(y), fdel=None, doc=propDocs["hasTopic"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___Preference(rdfs___Resource):
	"""
	ces:Preference
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Preference"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#Preference"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___QosWeightPreference(ces___Preference):
	"""
	ces:QosWeightPreference
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___Preference.__init__(self)
		self._initialised = False
		self.shortname = "QosWeightPreference"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["accuracyWeight"] = PropertySet("accuracyWeight","http://www.insight-centre.org/ces#accuracyWeight", long, False)
		self._props["availabilityWeight"] = PropertySet("availabilityWeight","http://www.insight-centre.org/ces#availabilityWeight", long, False)
		self._props["bandwidthConsumptionWeight"] = PropertySet("bandwidthConsumptionWeight","http://www.insight-centre.org/ces#bandwidthConsumptionWeight", long, False)
		self._props["energyConsumptionWeight"] = PropertySet("energyConsumptionWeight","http://www.insight-centre.org/ces#energyConsumptionWeight", long, False)
		self._props["latencyWeight"] = PropertySet("latencyWeight","http://www.insight-centre.org/ces#latencyWeight", long, False)
		self._props["priceWeight"] = PropertySet("priceWeight","http://www.insight-centre.org/ces#priceWeight", long, False)
		self._props["reliabilityWeight"] = PropertySet("reliabilityWeight","http://www.insight-centre.org/ces#reliabilityWeight", long, False)
		self._props["securityWeight"] = PropertySet("securityWeight","http://www.insight-centre.org/ces#securityWeight", long, False)
		self._props["weight"] = PropertySet("weight","http://www.insight-centre.org/ces#weight", long, False)
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#QosWeightPreference"


	# Python class properties to wrap the PropertySet objects
	accuracyWeight = property(fget=lambda x: x._props["accuracyWeight"].get(), fset=lambda x,y : x._props["accuracyWeight"].set(y), fdel=None, doc=propDocs["accuracyWeight"])
	availabilityWeight = property(fget=lambda x: x._props["availabilityWeight"].get(), fset=lambda x,y : x._props["availabilityWeight"].set(y), fdel=None, doc=propDocs["availabilityWeight"])
	bandwidthConsumptionWeight = property(fget=lambda x: x._props["bandwidthConsumptionWeight"].get(), fset=lambda x,y : x._props["bandwidthConsumptionWeight"].set(y), fdel=None, doc=propDocs["bandwidthConsumptionWeight"])
	energyConsumptionWeight = property(fget=lambda x: x._props["energyConsumptionWeight"].get(), fset=lambda x,y : x._props["energyConsumptionWeight"].set(y), fdel=None, doc=propDocs["energyConsumptionWeight"])
	latencyWeight = property(fget=lambda x: x._props["latencyWeight"].get(), fset=lambda x,y : x._props["latencyWeight"].set(y), fdel=None, doc=propDocs["latencyWeight"])
	priceWeight = property(fget=lambda x: x._props["priceWeight"].get(), fset=lambda x,y : x._props["priceWeight"].set(y), fdel=None, doc=propDocs["priceWeight"])
	reliabilityWeight = property(fget=lambda x: x._props["reliabilityWeight"].get(), fset=lambda x,y : x._props["reliabilityWeight"].set(y), fdel=None, doc=propDocs["reliabilityWeight"])
	securityWeight = property(fget=lambda x: x._props["securityWeight"].get(), fset=lambda x,y : x._props["securityWeight"].set(y), fdel=None, doc=propDocs["securityWeight"])
	weight = property(fget=lambda x: x._props["weight"].get(), fset=lambda x,y : x._props["weight"].set(y), fdel=None, doc=propDocs["weight"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___Selection(ces___EventPattern):
	"""
	ces:Selection
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___EventPattern.__init__(self)
		self._initialised = False
		self.shortname = "Selection"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["selectedProperty"] = PropertySet("selectedProperty","http://www.insight-centre.org/ces#selectedProperty", ssn___Property, False)
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#Selection"


	# Python class properties to wrap the PropertySet objects
	selectedProperty = property(fget=lambda x: x._props["selectedProperty"].get(), fset=lambda x,y : x._props["selectedProperty"].set(y), fdel=None, doc=propDocs["selectedProperty"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___ServiceNode(ces___EventPattern):
	"""
	ces:ServiceNode
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___EventPattern.__init__(self)
		self._initialised = False
		self.shortname = "ServiceNode"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasInternalNodeID"] = PropertySet("hasInternalNodeID","http://www.insight-centre.org/ces#hasInternalNodeID", str, False)
		self._props["hasService"] = PropertySet("hasService","http://www.insight-centre.org/ces#hasService", ces___EventService, False)
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#ServiceNode"


	# Python class properties to wrap the PropertySet objects
	hasInternalNodeID = property(fget=lambda x: x._props["hasInternalNodeID"].get(), fset=lambda x,y : x._props["hasInternalNodeID"].set(y), fdel=None, doc=propDocs["hasInternalNodeID"])
	hasService = property(fget=lambda x: x._props["hasService"].get(), fset=lambda x,y : x._props["hasService"].set(y), fdel=None, doc=propDocs["hasService"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___WebSocketGrounding(owlsg___Grounding):
	"""
	ces:WebSocketGrounding
	"""
	def __init__(self,URI=None):
		# Initialise parents
		owlsg___Grounding.__init__(self)
		self._initialised = False
		self.shortname = "WebSocketGrounding"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#WebSocketGrounding"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class DUL___Event(rdfs___Resource):
	"""
	DUL:Event
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Event"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.loa-cnr.it/ontologies/DUL.owl#Event"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class DUL___InformationObject(rdfs___Resource):
	"""
	DUL:InformationObject
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "InformationObject"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.loa-cnr.it/ontologies/DUL.owl#InformationObject"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class DUL___Object(rdfs___Resource):
	"""
	DUL:Object
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Object"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.loa-cnr.it/ontologies/DUL.owl#Object"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class DUL___Process(rdfs___Resource):
	"""
	DUL:Process
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Process"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasInput"] = PropertySet("hasInput","http://purl.oclc.org/NET/ssnx/ssn#hasInput", ssn___Input, False)
		self._props["hasOutput"] = PropertySet("hasOutput","http://purl.oclc.org/NET/ssnx/ssn#hasOutput", ssn___Output, False)
		self._initialised = True
	classURI = "http://www.loa-cnr.it/ontologies/DUL.owl#Process"


	# Python class properties to wrap the PropertySet objects
	hasInput = property(fget=lambda x: x._props["hasInput"].get(), fset=lambda x,y : x._props["hasInput"].set(y), fdel=None, doc=propDocs["hasInput"])
	hasOutput = property(fget=lambda x: x._props["hasOutput"].get(), fset=lambda x,y : x._props["hasOutput"].set(y), fdel=None, doc=propDocs["hasOutput"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class DUL___Region(rdfs___Resource):
	"""
	DUL:Region
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Region"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.loa-cnr.it/ontologies/DUL.owl#Region"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class rdfs___Bag(rdfs___Resource):
	"""
	rdfs:Bag
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Bag"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/2000/01/rdf-schema#Bag"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class rdfs___Seq(rdfs___Resource):
	"""
	rdfs:Seq
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Seq"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/2000/01/rdf-schema#Seq"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tm___DurationDescription(rdfs___Resource):
	"""
	tm:DurationDescription
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "DurationDescription"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["days"] = PropertySet("days","http://www.w3.org/2006/time#days", str, False)
		self._props["hours"] = PropertySet("hours","http://www.w3.org/2006/time#hours", str, False)
		self._props["minutes"] = PropertySet("minutes","http://www.w3.org/2006/time#minutes", str, False)
		self._props["months"] = PropertySet("months","http://www.w3.org/2006/time#months", str, False)
		self._props["seconds"] = PropertySet("seconds","http://www.w3.org/2006/time#seconds", str, False)
		self._props["weeks"] = PropertySet("weeks","http://www.w3.org/2006/time#weeks", str, False)
		self._props["years"] = PropertySet("years","http://www.w3.org/2006/time#years", str, False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#DurationDescription"


	# Python class properties to wrap the PropertySet objects
	days = property(fget=lambda x: x._props["days"].get(), fset=lambda x,y : x._props["days"].set(y), fdel=None, doc=propDocs["days"])
	hours = property(fget=lambda x: x._props["hours"].get(), fset=lambda x,y : x._props["hours"].set(y), fdel=None, doc=propDocs["hours"])
	minutes = property(fget=lambda x: x._props["minutes"].get(), fset=lambda x,y : x._props["minutes"].set(y), fdel=None, doc=propDocs["minutes"])
	months = property(fget=lambda x: x._props["months"].get(), fset=lambda x,y : x._props["months"].set(y), fdel=None, doc=propDocs["months"])
	seconds = property(fget=lambda x: x._props["seconds"].get(), fset=lambda x,y : x._props["seconds"].set(y), fdel=None, doc=propDocs["seconds"])
	weeks = property(fget=lambda x: x._props["weeks"].get(), fset=lambda x,y : x._props["weeks"].set(y), fdel=None, doc=propDocs["weeks"])
	years = property(fget=lambda x: x._props["years"].get(), fset=lambda x,y : x._props["years"].set(y), fdel=None, doc=propDocs["years"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tm___Interval(tm___TemporalEntity):
	"""
	tm:Interval
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tm___TemporalEntity.__init__(self)
		self._initialised = False
		self.shortname = "Interval"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["inside"] = PropertySet("inside","http://www.w3.org/2006/time#inside", tm___Instant, False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#Interval"


	# Python class properties to wrap the PropertySet objects
	inside = property(fget=lambda x: x._props["inside"].get(), fset=lambda x,y : x._props["inside"].set(y), fdel=None, doc=propDocs["inside"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tm___ProperInterval(tm___Interval):
	"""
	tm:ProperInterval
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tm___Interval.__init__(self)
		self._initialised = False
		self.shortname = "ProperInterval"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["at"] = PropertySet("at","http://purl.org/NET/c4dm/timeline.owl#at", None, True)
		self._props["atDate"] = PropertySet("atDate","http://purl.org/NET/c4dm/timeline.owl#atDate", None, True)
		self._props["atDateTime"] = PropertySet("atDateTime","http://purl.org/NET/c4dm/timeline.owl#atDateTime", None, True)
		self._props["atDuration"] = PropertySet("atDuration","http://purl.org/NET/c4dm/timeline.owl#atDuration", str, True)
		self._props["atInt"] = PropertySet("atInt","http://purl.org/NET/c4dm/timeline.owl#atInt", int, True)
		self._props["atReal"] = PropertySet("atReal","http://purl.org/NET/c4dm/timeline.owl#atReal", float, True)
		self._props["atYear"] = PropertySet("atYear","http://purl.org/NET/c4dm/timeline.owl#atYear", int, True)
		self._props["atYearMonth"] = PropertySet("atYearMonth","http://purl.org/NET/c4dm/timeline.owl#atYearMonth", str, True)
		self._props["beginsAt"] = PropertySet("beginsAt","http://purl.org/NET/c4dm/timeline.owl#beginsAt", None, False)
		self._props["beginsAtDateTime"] = PropertySet("beginsAtDateTime","http://purl.org/NET/c4dm/timeline.owl#beginsAtDateTime", str, False)
		self._props["beginsAtDuration"] = PropertySet("beginsAtDuration","http://purl.org/NET/c4dm/timeline.owl#beginsAtDuration", str, False)
		self._props["beginsAtInt"] = PropertySet("beginsAtInt","http://purl.org/NET/c4dm/timeline.owl#beginsAtInt", int, False)
		self._props["duration"] = PropertySet("duration","http://purl.org/NET/c4dm/timeline.owl#duration", None, False)
		self._props["durationInt"] = PropertySet("durationInt","http://purl.org/NET/c4dm/timeline.owl#durationInt", int, False)
		self._props["durationXSD"] = PropertySet("durationXSD","http://purl.org/NET/c4dm/timeline.owl#durationXSD", str, False)
		self._props["endsAt"] = PropertySet("endsAt","http://purl.org/NET/c4dm/timeline.owl#endsAt", None, False)
		self._props["endsAtDateTime"] = PropertySet("endsAtDateTime","http://purl.org/NET/c4dm/timeline.owl#endsAtDateTime", str, False)
		self._props["endsAtDuration"] = PropertySet("endsAtDuration","http://purl.org/NET/c4dm/timeline.owl#endsAtDuration", str, False)
		self._props["endsAtInt"] = PropertySet("endsAtInt","http://purl.org/NET/c4dm/timeline.owl#endsAtInt", int, False)
		self._props["onTimeLine"] = PropertySet("onTimeLine","http://purl.org/NET/c4dm/timeline.owl#onTimeLine", tl___TimeLine, False)
		self._props["intervalAfter"] = PropertySet("intervalAfter","http://www.w3.org/2006/time#intervalAfter", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalBefore"] = PropertySet("intervalBefore","http://www.w3.org/2006/time#intervalBefore", (tm___ProperInterval,tm___TemporalEntity,tl___Interval), False)
		self._props["intervalContains"] = PropertySet("intervalContains","http://www.w3.org/2006/time#intervalContains", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalDuring"] = PropertySet("intervalDuring","http://www.w3.org/2006/time#intervalDuring", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalEquals"] = PropertySet("intervalEquals","http://www.w3.org/2006/time#intervalEquals", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalFinishedBy"] = PropertySet("intervalFinishedBy","http://www.w3.org/2006/time#intervalFinishedBy", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalFinishes"] = PropertySet("intervalFinishes","http://www.w3.org/2006/time#intervalFinishes", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalMeets"] = PropertySet("intervalMeets","http://www.w3.org/2006/time#intervalMeets", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalMetBy"] = PropertySet("intervalMetBy","http://www.w3.org/2006/time#intervalMetBy", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalOverlappedBy"] = PropertySet("intervalOverlappedBy","http://www.w3.org/2006/time#intervalOverlappedBy", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalOverlaps"] = PropertySet("intervalOverlaps","http://www.w3.org/2006/time#intervalOverlaps", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalStartedBy"] = PropertySet("intervalStartedBy","http://www.w3.org/2006/time#intervalStartedBy", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalStarts"] = PropertySet("intervalStarts","http://www.w3.org/2006/time#intervalStarts", (tm___ProperInterval,tl___Interval), False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#ProperInterval"


	# Python class properties to wrap the PropertySet objects
	at = property(fget=lambda x: x._props["at"].get(), fset=lambda x,y : x._props["at"].set(y), fdel=None, doc=propDocs["at"])
	atDate = property(fget=lambda x: x._props["atDate"].get(), fset=lambda x,y : x._props["atDate"].set(y), fdel=None, doc=propDocs["atDate"])
	atDateTime = property(fget=lambda x: x._props["atDateTime"].get(), fset=lambda x,y : x._props["atDateTime"].set(y), fdel=None, doc=propDocs["atDateTime"])
	atDuration = property(fget=lambda x: x._props["atDuration"].get(), fset=lambda x,y : x._props["atDuration"].set(y), fdel=None, doc=propDocs["atDuration"])
	atInt = property(fget=lambda x: x._props["atInt"].get(), fset=lambda x,y : x._props["atInt"].set(y), fdel=None, doc=propDocs["atInt"])
	atReal = property(fget=lambda x: x._props["atReal"].get(), fset=lambda x,y : x._props["atReal"].set(y), fdel=None, doc=propDocs["atReal"])
	atYear = property(fget=lambda x: x._props["atYear"].get(), fset=lambda x,y : x._props["atYear"].set(y), fdel=None, doc=propDocs["atYear"])
	atYearMonth = property(fget=lambda x: x._props["atYearMonth"].get(), fset=lambda x,y : x._props["atYearMonth"].set(y), fdel=None, doc=propDocs["atYearMonth"])
	beginsAt = property(fget=lambda x: x._props["beginsAt"].get(), fset=lambda x,y : x._props["beginsAt"].set(y), fdel=None, doc=propDocs["beginsAt"])
	beginsAtDateTime = property(fget=lambda x: x._props["beginsAtDateTime"].get(), fset=lambda x,y : x._props["beginsAtDateTime"].set(y), fdel=None, doc=propDocs["beginsAtDateTime"])
	beginsAtDuration = property(fget=lambda x: x._props["beginsAtDuration"].get(), fset=lambda x,y : x._props["beginsAtDuration"].set(y), fdel=None, doc=propDocs["beginsAtDuration"])
	beginsAtInt = property(fget=lambda x: x._props["beginsAtInt"].get(), fset=lambda x,y : x._props["beginsAtInt"].set(y), fdel=None, doc=propDocs["beginsAtInt"])
	duration = property(fget=lambda x: x._props["duration"].get(), fset=lambda x,y : x._props["duration"].set(y), fdel=None, doc=propDocs["duration"])
	durationInt = property(fget=lambda x: x._props["durationInt"].get(), fset=lambda x,y : x._props["durationInt"].set(y), fdel=None, doc=propDocs["durationInt"])
	durationXSD = property(fget=lambda x: x._props["durationXSD"].get(), fset=lambda x,y : x._props["durationXSD"].set(y), fdel=None, doc=propDocs["durationXSD"])
	endsAt = property(fget=lambda x: x._props["endsAt"].get(), fset=lambda x,y : x._props["endsAt"].set(y), fdel=None, doc=propDocs["endsAt"])
	endsAtDateTime = property(fget=lambda x: x._props["endsAtDateTime"].get(), fset=lambda x,y : x._props["endsAtDateTime"].set(y), fdel=None, doc=propDocs["endsAtDateTime"])
	endsAtDuration = property(fget=lambda x: x._props["endsAtDuration"].get(), fset=lambda x,y : x._props["endsAtDuration"].set(y), fdel=None, doc=propDocs["endsAtDuration"])
	endsAtInt = property(fget=lambda x: x._props["endsAtInt"].get(), fset=lambda x,y : x._props["endsAtInt"].set(y), fdel=None, doc=propDocs["endsAtInt"])
	onTimeLine = property(fget=lambda x: x._props["onTimeLine"].get(), fset=lambda x,y : x._props["onTimeLine"].set(y), fdel=None, doc=propDocs["onTimeLine"])
	intervalAfter = property(fget=lambda x: x._props["intervalAfter"].get(), fset=lambda x,y : x._props["intervalAfter"].set(y), fdel=None, doc=propDocs["intervalAfter"])
	intervalBefore = property(fget=lambda x: x._props["intervalBefore"].get(), fset=lambda x,y : x._props["intervalBefore"].set(y), fdel=None, doc=propDocs["intervalBefore"])
	intervalContains = property(fget=lambda x: x._props["intervalContains"].get(), fset=lambda x,y : x._props["intervalContains"].set(y), fdel=None, doc=propDocs["intervalContains"])
	intervalDuring = property(fget=lambda x: x._props["intervalDuring"].get(), fset=lambda x,y : x._props["intervalDuring"].set(y), fdel=None, doc=propDocs["intervalDuring"])
	intervalEquals = property(fget=lambda x: x._props["intervalEquals"].get(), fset=lambda x,y : x._props["intervalEquals"].set(y), fdel=None, doc=propDocs["intervalEquals"])
	intervalFinishedBy = property(fget=lambda x: x._props["intervalFinishedBy"].get(), fset=lambda x,y : x._props["intervalFinishedBy"].set(y), fdel=None, doc=propDocs["intervalFinishedBy"])
	intervalFinishes = property(fget=lambda x: x._props["intervalFinishes"].get(), fset=lambda x,y : x._props["intervalFinishes"].set(y), fdel=None, doc=propDocs["intervalFinishes"])
	intervalMeets = property(fget=lambda x: x._props["intervalMeets"].get(), fset=lambda x,y : x._props["intervalMeets"].set(y), fdel=None, doc=propDocs["intervalMeets"])
	intervalMetBy = property(fget=lambda x: x._props["intervalMetBy"].get(), fset=lambda x,y : x._props["intervalMetBy"].set(y), fdel=None, doc=propDocs["intervalMetBy"])
	intervalOverlappedBy = property(fget=lambda x: x._props["intervalOverlappedBy"].get(), fset=lambda x,y : x._props["intervalOverlappedBy"].set(y), fdel=None, doc=propDocs["intervalOverlappedBy"])
	intervalOverlaps = property(fget=lambda x: x._props["intervalOverlaps"].get(), fset=lambda x,y : x._props["intervalOverlaps"].set(y), fdel=None, doc=propDocs["intervalOverlaps"])
	intervalStartedBy = property(fget=lambda x: x._props["intervalStartedBy"].get(), fset=lambda x,y : x._props["intervalStartedBy"].set(y), fdel=None, doc=propDocs["intervalStartedBy"])
	intervalStarts = property(fget=lambda x: x._props["intervalStarts"].get(), fset=lambda x,y : x._props["intervalStarts"].set(y), fdel=None, doc=propDocs["intervalStarts"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tm___Year(tm___DurationDescription):
	"""
	tm:Year
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tm___DurationDescription.__init__(self)
		self._initialised = False
		self.shortname = "Year"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["days"] = PropertySet("days","http://www.w3.org/2006/time#days", str, False)
		self._props["hours"] = PropertySet("hours","http://www.w3.org/2006/time#hours", str, False)
		self._props["minutes"] = PropertySet("minutes","http://www.w3.org/2006/time#minutes", str, False)
		self._props["months"] = PropertySet("months","http://www.w3.org/2006/time#months", str, False)
		self._props["seconds"] = PropertySet("seconds","http://www.w3.org/2006/time#seconds", str, False)
		self._props["weeks"] = PropertySet("weeks","http://www.w3.org/2006/time#weeks", str, False)
		self._props["years"] = PropertySet("years","http://www.w3.org/2006/time#years", str, False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#Year"


	# Python class properties to wrap the PropertySet objects
	days = property(fget=lambda x: x._props["days"].get(), fset=lambda x,y : x._props["days"].set(y), fdel=None, doc=propDocs["days"])
	hours = property(fget=lambda x: x._props["hours"].get(), fset=lambda x,y : x._props["hours"].set(y), fdel=None, doc=propDocs["hours"])
	minutes = property(fget=lambda x: x._props["minutes"].get(), fset=lambda x,y : x._props["minutes"].set(y), fdel=None, doc=propDocs["minutes"])
	months = property(fget=lambda x: x._props["months"].get(), fset=lambda x,y : x._props["months"].set(y), fdel=None, doc=propDocs["months"])
	seconds = property(fget=lambda x: x._props["seconds"].get(), fset=lambda x,y : x._props["seconds"].set(y), fdel=None, doc=propDocs["seconds"])
	weeks = property(fget=lambda x: x._props["weeks"].get(), fset=lambda x,y : x._props["weeks"].set(y), fdel=None, doc=propDocs["weeks"])
	years = property(fget=lambda x: x._props["years"].get(), fset=lambda x,y : x._props["years"].set(y), fdel=None, doc=propDocs["years"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___ActivityInfluence(prov___Influence):
	"""
	prov:ActivityInfluence
	ActivityInfluence provides additional descriptions of an Activity's binary influence upon any other kind of resource. Instances of ActivityInfluence use the prov:activity property to cite the influencing Activity.
	It is not recommended that the type ActivityInfluence be asserted without also asserting one of its more specific subclasses.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___Influence.__init__(self)
		self._initialised = False
		self.shortname = "ActivityInfluence"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["activity"] = PropertySet("activity","http://www.w3.org/ns/prov#activity", (owl___Thing,prov___Activity), False)
		self._props["hadActivity"] = PropertySet("hadActivity","http://www.w3.org/ns/prov#hadActivity", prov___Activity, False)
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#ActivityInfluence"


	# Python class properties to wrap the PropertySet objects
	activity = property(fget=lambda x: x._props["activity"].get(), fset=lambda x,y : x._props["activity"].set(y), fdel=None, doc=propDocs["activity"])
	hadActivity = property(fget=lambda x: x._props["hadActivity"].get(), fset=lambda x,y : x._props["hadActivity"].set(y), fdel=None, doc=propDocs["hadActivity"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Bundle(prov___Entity):
	"""
	prov:Bundle
	Note that there are kinds of bundles (e.g. handwritten letters, audio recordings, etc.) that are not expressed in PROV-O, but can be still be described by PROV-O.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___Entity.__init__(self)
		self._initialised = False
		self.shortname = "Bundle"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Bundle"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Communication(prov___ActivityInfluence):
	"""
	prov:Communication
	An instance of prov:Communication provides additional descriptions about the binary prov:wasInformedBy relation from an informed prov:Activity to the prov:Activity that informed it. For example, :you_jumping_off_bridge prov:wasInformedBy :everyone_else_jumping_off_bridge; prov:qualifiedCommunication [ a prov:Communication; prov:activity :everyone_else_jumping_off_bridge; :foo :bar ].
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___ActivityInfluence.__init__(self)
		self._initialised = False
		self.shortname = "Communication"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Communication"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___EntityInfluence(prov___Influence):
	"""
	prov:EntityInfluence
	It is not recommended that the type EntityInfluence be asserted without also asserting one of its more specific subclasses.
	EntityInfluence provides additional descriptions of an Entity's binary influence upon any other kind of resource. Instances of EntityInfluence use the prov:entity property to cite the influencing Entity.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___Influence.__init__(self)
		self._initialised = False
		self.shortname = "EntityInfluence"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["entity"] = PropertySet("entity","http://www.w3.org/ns/prov#entity", (prov___Entity,owl___Thing), False)
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#EntityInfluence"


	# Python class properties to wrap the PropertySet objects
	entity = property(fget=lambda x: x._props["entity"].get(), fset=lambda x,y : x._props["entity"].set(y), fdel=None, doc=propDocs["entity"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___InstantaneousEvent(rdfs___Resource):
	"""
	prov:InstantaneousEvent
	An instantaneous event, or event for short, happens in the world and marks a change in the world, in its activities and in its entities. The term 'event' is commonly used in process algebra with a similar meaning. Events represent communications or interactions; they are assumed to be atomic and instantaneous.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "InstantaneousEvent"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["atLocation"] = PropertySet("atLocation","http://www.w3.org/ns/prov#atLocation", prov___Location, False)
		self._props["atTime"] = PropertySet("atTime","http://www.w3.org/ns/prov#atTime", str, False)
		self._props["hadRole"] = PropertySet("hadRole","http://www.w3.org/ns/prov#hadRole", prov___Role, False)
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#InstantaneousEvent"


	# Python class properties to wrap the PropertySet objects
	atLocation = property(fget=lambda x: x._props["atLocation"].get(), fset=lambda x,y : x._props["atLocation"].set(y), fdel=None, doc=propDocs["atLocation"])
	atTime = property(fget=lambda x: x._props["atTime"].get(), fset=lambda x,y : x._props["atTime"].set(y), fdel=None, doc=propDocs["atTime"])
	hadRole = property(fget=lambda x: x._props["hadRole"].get(), fset=lambda x,y : x._props["hadRole"].set(y), fdel=None, doc=propDocs["hadRole"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Organization(prov___Agent):
	"""
	prov:Organization
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___Agent.__init__(self)
		self._initialised = False
		self.shortname = "Organization"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Organization"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___SoftwareAgent(prov___Agent):
	"""
	prov:SoftwareAgent
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___Agent.__init__(self)
		self._initialised = False
		self.shortname = "SoftwareAgent"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#SoftwareAgent"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Usage(prov___EntityInfluence, prov___InstantaneousEvent):
	"""
	prov:Usage
	An instance of prov:Usage provides additional descriptions about the binary prov:used relation from some prov:Activity to an prov:Entity that it used. For example, :keynote prov:used :podium; prov:qualifiedUsage [ a prov:Usage; prov:entity :podium; :foo :bar ].
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___EntityInfluence.__init__(self)
		prov___InstantaneousEvent.__init__(self)
		self._initialised = False
		self.shortname = "Usage"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Usage"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___Image(rdfs___Resource):
	"""
	foaf:Image
	An image.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Image"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["depicts"] = PropertySet("depicts","http://xmlns.com/foaf/0.1/depicts", owl___Thing, False)
		self._props["thumbnail"] = PropertySet("thumbnail","http://xmlns.com/foaf/0.1/thumbnail", foaf___Image, False)
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/Image"


	# Python class properties to wrap the PropertySet objects
	depicts = property(fget=lambda x: x._props["depicts"].get(), fset=lambda x,y : x._props["depicts"].set(y), fdel=None, doc=propDocs["depicts"])
	thumbnail = property(fget=lambda x: x._props["thumbnail"].get(), fset=lambda x,y : x._props["thumbnail"].set(y), fdel=None, doc=propDocs["thumbnail"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___Person(geo___SpatialThing):
	"""
	foaf:Person
	A person.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		geo___SpatialThing.__init__(self)
		self._initialised = False
		self.shortname = "Person"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["currentProject"] = PropertySet("currentProject","http://xmlns.com/foaf/0.1/currentProject", owl___Thing, False)
		self._props["family_name"] = PropertySet("family_name","http://xmlns.com/foaf/0.1/family_name", None, True)
		self._props["firstName"] = PropertySet("firstName","http://xmlns.com/foaf/0.1/firstName", None, True)
		self._props["geekcode"] = PropertySet("geekcode","http://xmlns.com/foaf/0.1/geekcode", None, True)
		self._props["img"] = PropertySet("img","http://xmlns.com/foaf/0.1/img", foaf___Image, False)
		self._props["interest"] = PropertySet("interest","http://xmlns.com/foaf/0.1/interest", foaf___Document, False)
		self._props["knows"] = PropertySet("knows","http://xmlns.com/foaf/0.1/knows", foaf___Person, False)
		self._props["myersBriggs"] = PropertySet("myersBriggs","http://xmlns.com/foaf/0.1/myersBriggs", None, True)
		self._props["pastProject"] = PropertySet("pastProject","http://xmlns.com/foaf/0.1/pastProject", owl___Thing, False)
		self._props["plan"] = PropertySet("plan","http://xmlns.com/foaf/0.1/plan", None, True)
		self._props["publications"] = PropertySet("publications","http://xmlns.com/foaf/0.1/publications", foaf___Document, False)
		self._props["schoolHomepage"] = PropertySet("schoolHomepage","http://xmlns.com/foaf/0.1/schoolHomepage", foaf___Document, False)
		self._props["surname"] = PropertySet("surname","http://xmlns.com/foaf/0.1/surname", None, True)
		self._props["topic_interest"] = PropertySet("topic_interest","http://xmlns.com/foaf/0.1/topic_interest", owl___Thing, False)
		self._props["workInfoHomepage"] = PropertySet("workInfoHomepage","http://xmlns.com/foaf/0.1/workInfoHomepage", foaf___Document, False)
		self._props["workplaceHomepage"] = PropertySet("workplaceHomepage","http://xmlns.com/foaf/0.1/workplaceHomepage", foaf___Document, False)
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/Person"


	# Python class properties to wrap the PropertySet objects
	currentProject = property(fget=lambda x: x._props["currentProject"].get(), fset=lambda x,y : x._props["currentProject"].set(y), fdel=None, doc=propDocs["currentProject"])
	family_name = property(fget=lambda x: x._props["family_name"].get(), fset=lambda x,y : x._props["family_name"].set(y), fdel=None, doc=propDocs["family_name"])
	firstName = property(fget=lambda x: x._props["firstName"].get(), fset=lambda x,y : x._props["firstName"].set(y), fdel=None, doc=propDocs["firstName"])
	geekcode = property(fget=lambda x: x._props["geekcode"].get(), fset=lambda x,y : x._props["geekcode"].set(y), fdel=None, doc=propDocs["geekcode"])
	img = property(fget=lambda x: x._props["img"].get(), fset=lambda x,y : x._props["img"].set(y), fdel=None, doc=propDocs["img"])
	interest = property(fget=lambda x: x._props["interest"].get(), fset=lambda x,y : x._props["interest"].set(y), fdel=None, doc=propDocs["interest"])
	knows = property(fget=lambda x: x._props["knows"].get(), fset=lambda x,y : x._props["knows"].set(y), fdel=None, doc=propDocs["knows"])
	myersBriggs = property(fget=lambda x: x._props["myersBriggs"].get(), fset=lambda x,y : x._props["myersBriggs"].set(y), fdel=None, doc=propDocs["myersBriggs"])
	pastProject = property(fget=lambda x: x._props["pastProject"].get(), fset=lambda x,y : x._props["pastProject"].set(y), fdel=None, doc=propDocs["pastProject"])
	plan = property(fget=lambda x: x._props["plan"].get(), fset=lambda x,y : x._props["plan"].set(y), fdel=None, doc=propDocs["plan"])
	publications = property(fget=lambda x: x._props["publications"].get(), fset=lambda x,y : x._props["publications"].set(y), fdel=None, doc=propDocs["publications"])
	schoolHomepage = property(fget=lambda x: x._props["schoolHomepage"].get(), fset=lambda x,y : x._props["schoolHomepage"].set(y), fdel=None, doc=propDocs["schoolHomepage"])
	surname = property(fget=lambda x: x._props["surname"].get(), fset=lambda x,y : x._props["surname"].set(y), fdel=None, doc=propDocs["surname"])
	topic_interest = property(fget=lambda x: x._props["topic_interest"].get(), fset=lambda x,y : x._props["topic_interest"].set(y), fdel=None, doc=propDocs["topic_interest"])
	workInfoHomepage = property(fget=lambda x: x._props["workInfoHomepage"].get(), fset=lambda x,y : x._props["workInfoHomepage"].set(y), fdel=None, doc=propDocs["workInfoHomepage"])
	workplaceHomepage = property(fget=lambda x: x._props["workplaceHomepage"].get(), fset=lambda x,y : x._props["workplaceHomepage"].set(y), fdel=None, doc=propDocs["workplaceHomepage"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ns1___TemporalUnit(rdfs___Resource):
	"""
	ns1:TemporalUnit
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "TemporalUnit"
		self.URI = URI
		self._initialised = True
	classURI = "file:///Users/sefki/Desktop/Desktop/SAOcodesTestCopy/Ontologies/TemporalUnit"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Accuracy(qoi___Quality):
	"""
	qoi:Accuracy
	Category to describe the accuracy of stream data.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Quality.__init__(self)
		self._initialised = False
		self.shortname = "Accuracy"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Accuracy"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Completeness(qoi___Accuracy):
	"""
	qoi:Completeness
	Probability that provided data is within the range of precision and completeness. Completeness cannot be negative and only reach 1 (0-100%)
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Accuracy.__init__(self)
		self._initialised = False
		self.shortname = "Completeness"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Completeness"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Correctness(qoi___Accuracy):
	"""
	qoi:Correctness
	The ratio of attribute values compared to expected parameters. Correctness cannot be negative and only reach 1 (0-100%)
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Accuracy.__init__(self)
		self._initialised = False
		self.shortname = "Correctness"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Correctness"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Encryption(qoi___Security):
	"""
	qoi:Encryption
	Encryption method, authority for key management.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Security.__init__(self)
		self._initialised = False
		self.shortname = "Encryption"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Encryption"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Frequency(qoi___Timeliness):
	"""
	qoi:Frequency
	Maximum timespan between two data sets. The Frequency has to be greater 0 as it is a timespan.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Timeliness.__init__(self)
		self._initialised = False
		self.shortname = "Frequency"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Frequency"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___NetworkPerformance(qoi___Quality):
	"""
	qoi:NetworkPerformance
	Category to describe QoS values of a data stream.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Quality.__init__(self)
		self._initialised = False
		self.shortname = "NetworkPerformance"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#NetworkPerformance"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___PacketLoss(qoi___NetworkPerformance):
	"""
	qoi:PacketLoss
	The probability that a set of data / a packet will not be transported correctly from the source to its sink. PacketLoss cannot be negative and only reach 1 (0-100%)
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___NetworkPerformance.__init__(self)
		self._initialised = False
		self.shortname = "PacketLoss"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#PacketLoss"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Queuing(qoi___Quality):
	"""
	qoi:Queuing
	Describes the order of streaming information.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Quality.__init__(self)
		self._initialised = False
		self.shortname = "Queuing"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Queuing"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Signing(qoi___Security):
	"""
	qoi:Signing
	Used to describe parameters for signing.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Security.__init__(self)
		self._initialised = False
		self.shortname = "Signing"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Signing"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Volatility(qoi___Timeliness):
	"""
	qoi:Volatility
	The amount of time the information remains valid in the context of a particular activity. Volatility cannot be negative as it is a timespan.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Timeliness.__init__(self)
		self._initialised = False
		self.shortname = "Volatility"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Volatility"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class muo___BaseUnit(muo___UnitOfMeasurement):
	"""
	muo:BaseUnit
	Base units are units that have not been derived from any other unit. In turn, base units can be used to derive other measurement units. The International System of Units (SI), recognizes several base units for base physical qualities assumed to be mutually independent.
	Base units are units that have not been derived from any other unit. In turn, base units can be used to derive other measurement units.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		muo___UnitOfMeasurement.__init__(self)
		self._initialised = False
		self.shortname = "BaseUnit"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/muo/muo#BaseUnit"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class muo___DerivedUnit(muo___UnitOfMeasurement):
	"""
	muo:DerivedUnit
	Some physical qualities (such as area, acceleration, etc.), called derived physical qualities, are defined in terms of base qualities via a system of dimensional equations. The derived units for derived qualities are obtained from these equations combinated with the base units.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		muo___UnitOfMeasurement.__init__(self)
		self._initialised = False
		self.shortname = "DerivedUnit"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["derivesFrom"] = PropertySet("derivesFrom","http://purl.oclc.org/NET/muo/muo#derivesFrom", muo___UnitOfMeasurement, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/muo/muo#DerivedUnit"


	# Python class properties to wrap the PropertySet objects
	derivesFrom = property(fget=lambda x: x._props["derivesFrom"].get(), fset=lambda x,y : x._props["derivesFrom"].set(y), fdel=None, doc=propDocs["derivesFrom"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class muo___Prefix(rdfs___Resource):
	"""
	muo:Prefix
	A prefix (also known as a metric prefix) is a name or associated symbol that precedes a unit of measure (or its symbol) to form a decimal multiple or submultiple. Prefixes are used to reduce the quantity of zeroes in numerical equivalencies. For instance, 1000 meters can be written as 1 kilometer, using the prefix kilo, a symbol to represent the number 1000.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Prefix"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["altSymbol"] = PropertySet("altSymbol","http://purl.oclc.org/NET/muo/muo#altSymbol", None, False)
		self._props["factor"] = PropertySet("factor","http://purl.oclc.org/NET/muo/muo#factor", None, False)
		self._props["prefSymbol"] = PropertySet("prefSymbol","http://purl.oclc.org/NET/muo/muo#prefSymbol", None, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/muo/muo#Prefix"


	# Python class properties to wrap the PropertySet objects
	altSymbol = property(fget=lambda x: x._props["altSymbol"].get(), fset=lambda x,y : x._props["altSymbol"].set(y), fdel=None, doc=propDocs["altSymbol"])
	factor = property(fget=lambda x: x._props["factor"].get(), fset=lambda x,y : x._props["factor"].set(y), fdel=None, doc=propDocs["factor"])
	prefSymbol = property(fget=lambda x: x._props["prefSymbol"].get(), fset=lambda x,y : x._props["prefSymbol"].set(y), fdel=None, doc=propDocs["prefSymbol"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class muo___SimpleDerivedUnit(muo___DerivedUnit):
	"""
	muo:SimpleDerivedUnit
	Units that are derived from exactly one base unit. There are two main possibilities. On one hand, there are units that are derived by adding a prefix to the unit. The prefix is a name or associated symbol (e.g. kilo) that precedes a unit of measure (e.g. meter) to form a decimal multiple or submultiple (e.g. Kilometer). Derived units, obtained by the application of a prefix, measure the same physical quality as its base unit. On the other hand, there are another kind of simple derived units that are also obtained from exactly one base unit but they measure a different physical quality. They are obtained by changing the exponent of the unit in the dimensional equation. For instance, this is how square meters are derived from meters. This exponent is represented in MUO with the datatype property muo:dimensionalSize. Combining this two patterns we can represent units that are obtained from a prefix and that have a dimension size different from 1, for instance, the unit square kilometer.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		muo___DerivedUnit.__init__(self)
		self._initialised = False
		self.shortname = "SimpleDerivedUnit"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["dimensionalSize"] = PropertySet("dimensionalSize","http://purl.oclc.org/NET/muo/muo#dimensionalSize", float, False)
		self._props["modifierPrefix"] = PropertySet("modifierPrefix","http://purl.oclc.org/NET/muo/muo#modifierPrefix", muo___Prefix, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/muo/muo#SimpleDerivedUnit"


	# Python class properties to wrap the PropertySet objects
	dimensionalSize = property(fget=lambda x: x._props["dimensionalSize"].get(), fset=lambda x,y : x._props["dimensionalSize"].set(y), fdel=None, doc=propDocs["dimensionalSize"])
	modifierPrefix = property(fget=lambda x: x._props["modifierPrefix"].get(), fset=lambda x,y : x._props["modifierPrefix"].set(y), fdel=None, doc=propDocs["modifierPrefix"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___DeploymentRelatedProcess(DUL___Process):
	"""
	ssn:DeploymentRelatedProcess
	Place to group all the various Processes related to Deployment.  For example, as well as Deplyment, installation, maintenance, deployment of further sensors and the like would all be classified under DeploymentRelatedProcess.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		DUL___Process.__init__(self)
		self._initialised = False
		self.shortname = "DeploymentRelatedProcess"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["deploymentProcessPart"] = PropertySet("deploymentProcessPart","http://purl.oclc.org/NET/ssnx/ssn#deploymentProcessPart", ssn___DeploymentRelatedProcess, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#DeploymentRelatedProcess"


	# Python class properties to wrap the PropertySet objects
	deploymentProcessPart = property(fget=lambda x: x._props["deploymentProcessPart"].get(), fset=lambda x,y : x._props["deploymentProcessPart"].set(y), fdel=None, doc=propDocs["deploymentProcessPart"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___ObservationValue(DUL___Region):
	"""
	ssn:ObservationValue
	The value of the result of an Observation.  An Observation has a result which is the output of some sensor, the result is an information object that encodes some value for a Feature.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		DUL___Region.__init__(self)
		self._initialised = False
		self.shortname = "ObservationValue"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["isRegionFor"] = PropertySet("isRegionFor","http://www.loa-cnr.it/ontologies/DUL.owl#isRegionFor", ssn___SensorOutput, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#ObservationValue"


	# Python class properties to wrap the PropertySet objects
	isRegionFor = property(fget=lambda x: x._props["isRegionFor"].get(), fset=lambda x,y : x._props["isRegionFor"].set(y), fdel=None, doc=propDocs["isRegionFor"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___SensorDataSheet(DUL___InformationObject):
	"""
	ssn:SensorDataSheet
	A data sheet records properties of a sensor.  A data sheet might describe for example the accuracy in various conditions, the power use, the types of connectors that the sensor has, etc.  

Generally a sensor's properties are recorded directly (with hasMeasurementCapability, for example), but the data sheet can be used for example to record the manufacturers specifications verses observed capabilites, or if more is known than the manufacturer specifies, etc.  The data sheet is an information object about the sensor's properties, rather than a direct link to the actual properties themselves.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		DUL___InformationObject.__init__(self)
		self._initialised = False
		self.shortname = "SensorDataSheet"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#SensorDataSheet"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___SensorOutput(DUL___InformationObject):
	"""
	ssn:SensorOutput
	A sensor outputs a piece of information (an observed value), the value itself being represented by an ObservationValue.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		DUL___InformationObject.__init__(self)
		self._initialised = False
		self.shortname = "SensorOutput"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasValue"] = PropertySet("hasValue","http://purl.oclc.org/NET/ssnx/ssn#hasValue", ssn___ObservationValue, False)
		self._props["isProducedBy"] = PropertySet("isProducedBy","http://purl.oclc.org/NET/ssnx/ssn#isProducedBy", ssn___Sensor, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#SensorOutput"


	# Python class properties to wrap the PropertySet objects
	hasValue = property(fget=lambda x: x._props["hasValue"].get(), fset=lambda x,y : x._props["hasValue"].set(y), fdel=None, doc=propDocs["hasValue"])
	isProducedBy = property(fget=lambda x: x._props["isProducedBy"].get(), fset=lambda x,y : x._props["isProducedBy"].set(y), fdel=None, doc=propDocs["isProducedBy"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___AbstractInstant(tl___Instant):
	"""
	tl:AbstractInstant
	An instant defined on an abstract timeline
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tl___Instant.__init__(self)
		self._initialised = False
		self.shortname = "AbstractInstant"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#AbstractInstant"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___AbstractTimeLine(tl___TimeLine):
	"""
	tl:AbstractTimeLine
	
            Abstract time lines may be used as a backbone for Score, Works, ...
            This allows for TimeLine maps to relate works to a given
            performance (this part was played at this time).
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tl___TimeLine.__init__(self)
		self._initialised = False
		self.shortname = "AbstractTimeLine"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#AbstractTimeLine"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___DiscreteInterval(rdfs___Resource):
	"""
	tl:DiscreteInterval
	An interval defined on a discrete timeline, like the one backing a digital signal
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "DiscreteInterval"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#DiscreteInterval"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___Interval(tm___Interval):
	"""
	tl:Interval
	An interval (same as in OWL-Time). Allen's relationships are defined in OWL-Time.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tm___Interval.__init__(self)
		self._initialised = False
		self.shortname = "Interval"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["at"] = PropertySet("at","http://purl.org/NET/c4dm/timeline.owl#at", None, True)
		self._props["atDate"] = PropertySet("atDate","http://purl.org/NET/c4dm/timeline.owl#atDate", None, True)
		self._props["atDateTime"] = PropertySet("atDateTime","http://purl.org/NET/c4dm/timeline.owl#atDateTime", None, True)
		self._props["atDuration"] = PropertySet("atDuration","http://purl.org/NET/c4dm/timeline.owl#atDuration", str, True)
		self._props["atInt"] = PropertySet("atInt","http://purl.org/NET/c4dm/timeline.owl#atInt", int, True)
		self._props["atReal"] = PropertySet("atReal","http://purl.org/NET/c4dm/timeline.owl#atReal", float, True)
		self._props["atYear"] = PropertySet("atYear","http://purl.org/NET/c4dm/timeline.owl#atYear", int, True)
		self._props["atYearMonth"] = PropertySet("atYearMonth","http://purl.org/NET/c4dm/timeline.owl#atYearMonth", str, True)
		self._props["beginsAt"] = PropertySet("beginsAt","http://purl.org/NET/c4dm/timeline.owl#beginsAt", None, False)
		self._props["beginsAtDateTime"] = PropertySet("beginsAtDateTime","http://purl.org/NET/c4dm/timeline.owl#beginsAtDateTime", str, False)
		self._props["beginsAtDuration"] = PropertySet("beginsAtDuration","http://purl.org/NET/c4dm/timeline.owl#beginsAtDuration", str, False)
		self._props["beginsAtInt"] = PropertySet("beginsAtInt","http://purl.org/NET/c4dm/timeline.owl#beginsAtInt", int, False)
		self._props["duration"] = PropertySet("duration","http://purl.org/NET/c4dm/timeline.owl#duration", None, False)
		self._props["durationInt"] = PropertySet("durationInt","http://purl.org/NET/c4dm/timeline.owl#durationInt", int, False)
		self._props["durationXSD"] = PropertySet("durationXSD","http://purl.org/NET/c4dm/timeline.owl#durationXSD", str, False)
		self._props["endsAt"] = PropertySet("endsAt","http://purl.org/NET/c4dm/timeline.owl#endsAt", None, False)
		self._props["endsAtDateTime"] = PropertySet("endsAtDateTime","http://purl.org/NET/c4dm/timeline.owl#endsAtDateTime", str, False)
		self._props["endsAtDuration"] = PropertySet("endsAtDuration","http://purl.org/NET/c4dm/timeline.owl#endsAtDuration", str, False)
		self._props["endsAtInt"] = PropertySet("endsAtInt","http://purl.org/NET/c4dm/timeline.owl#endsAtInt", int, False)
		self._props["onTimeLine"] = PropertySet("onTimeLine","http://purl.org/NET/c4dm/timeline.owl#onTimeLine", tl___TimeLine, False)
		self._props["intervalAfter"] = PropertySet("intervalAfter","http://www.w3.org/2006/time#intervalAfter", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalBefore"] = PropertySet("intervalBefore","http://www.w3.org/2006/time#intervalBefore", (tm___ProperInterval,tm___TemporalEntity,tl___Interval), False)
		self._props["intervalContains"] = PropertySet("intervalContains","http://www.w3.org/2006/time#intervalContains", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalDuring"] = PropertySet("intervalDuring","http://www.w3.org/2006/time#intervalDuring", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalEquals"] = PropertySet("intervalEquals","http://www.w3.org/2006/time#intervalEquals", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalFinishedBy"] = PropertySet("intervalFinishedBy","http://www.w3.org/2006/time#intervalFinishedBy", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalFinishes"] = PropertySet("intervalFinishes","http://www.w3.org/2006/time#intervalFinishes", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalMeets"] = PropertySet("intervalMeets","http://www.w3.org/2006/time#intervalMeets", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalMetBy"] = PropertySet("intervalMetBy","http://www.w3.org/2006/time#intervalMetBy", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalOverlappedBy"] = PropertySet("intervalOverlappedBy","http://www.w3.org/2006/time#intervalOverlappedBy", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalOverlaps"] = PropertySet("intervalOverlaps","http://www.w3.org/2006/time#intervalOverlaps", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalStartedBy"] = PropertySet("intervalStartedBy","http://www.w3.org/2006/time#intervalStartedBy", (tm___ProperInterval,tl___Interval), False)
		self._props["intervalStarts"] = PropertySet("intervalStarts","http://www.w3.org/2006/time#intervalStarts", (tm___ProperInterval,tl___Interval), False)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#Interval"


	# Python class properties to wrap the PropertySet objects
	at = property(fget=lambda x: x._props["at"].get(), fset=lambda x,y : x._props["at"].set(y), fdel=None, doc=propDocs["at"])
	atDate = property(fget=lambda x: x._props["atDate"].get(), fset=lambda x,y : x._props["atDate"].set(y), fdel=None, doc=propDocs["atDate"])
	atDateTime = property(fget=lambda x: x._props["atDateTime"].get(), fset=lambda x,y : x._props["atDateTime"].set(y), fdel=None, doc=propDocs["atDateTime"])
	atDuration = property(fget=lambda x: x._props["atDuration"].get(), fset=lambda x,y : x._props["atDuration"].set(y), fdel=None, doc=propDocs["atDuration"])
	atInt = property(fget=lambda x: x._props["atInt"].get(), fset=lambda x,y : x._props["atInt"].set(y), fdel=None, doc=propDocs["atInt"])
	atReal = property(fget=lambda x: x._props["atReal"].get(), fset=lambda x,y : x._props["atReal"].set(y), fdel=None, doc=propDocs["atReal"])
	atYear = property(fget=lambda x: x._props["atYear"].get(), fset=lambda x,y : x._props["atYear"].set(y), fdel=None, doc=propDocs["atYear"])
	atYearMonth = property(fget=lambda x: x._props["atYearMonth"].get(), fset=lambda x,y : x._props["atYearMonth"].set(y), fdel=None, doc=propDocs["atYearMonth"])
	beginsAt = property(fget=lambda x: x._props["beginsAt"].get(), fset=lambda x,y : x._props["beginsAt"].set(y), fdel=None, doc=propDocs["beginsAt"])
	beginsAtDateTime = property(fget=lambda x: x._props["beginsAtDateTime"].get(), fset=lambda x,y : x._props["beginsAtDateTime"].set(y), fdel=None, doc=propDocs["beginsAtDateTime"])
	beginsAtDuration = property(fget=lambda x: x._props["beginsAtDuration"].get(), fset=lambda x,y : x._props["beginsAtDuration"].set(y), fdel=None, doc=propDocs["beginsAtDuration"])
	beginsAtInt = property(fget=lambda x: x._props["beginsAtInt"].get(), fset=lambda x,y : x._props["beginsAtInt"].set(y), fdel=None, doc=propDocs["beginsAtInt"])
	duration = property(fget=lambda x: x._props["duration"].get(), fset=lambda x,y : x._props["duration"].set(y), fdel=None, doc=propDocs["duration"])
	durationInt = property(fget=lambda x: x._props["durationInt"].get(), fset=lambda x,y : x._props["durationInt"].set(y), fdel=None, doc=propDocs["durationInt"])
	durationXSD = property(fget=lambda x: x._props["durationXSD"].get(), fset=lambda x,y : x._props["durationXSD"].set(y), fdel=None, doc=propDocs["durationXSD"])
	endsAt = property(fget=lambda x: x._props["endsAt"].get(), fset=lambda x,y : x._props["endsAt"].set(y), fdel=None, doc=propDocs["endsAt"])
	endsAtDateTime = property(fget=lambda x: x._props["endsAtDateTime"].get(), fset=lambda x,y : x._props["endsAtDateTime"].set(y), fdel=None, doc=propDocs["endsAtDateTime"])
	endsAtDuration = property(fget=lambda x: x._props["endsAtDuration"].get(), fset=lambda x,y : x._props["endsAtDuration"].set(y), fdel=None, doc=propDocs["endsAtDuration"])
	endsAtInt = property(fget=lambda x: x._props["endsAtInt"].get(), fset=lambda x,y : x._props["endsAtInt"].set(y), fdel=None, doc=propDocs["endsAtInt"])
	onTimeLine = property(fget=lambda x: x._props["onTimeLine"].get(), fset=lambda x,y : x._props["onTimeLine"].set(y), fdel=None, doc=propDocs["onTimeLine"])
	intervalAfter = property(fget=lambda x: x._props["intervalAfter"].get(), fset=lambda x,y : x._props["intervalAfter"].set(y), fdel=None, doc=propDocs["intervalAfter"])
	intervalBefore = property(fget=lambda x: x._props["intervalBefore"].get(), fset=lambda x,y : x._props["intervalBefore"].set(y), fdel=None, doc=propDocs["intervalBefore"])
	intervalContains = property(fget=lambda x: x._props["intervalContains"].get(), fset=lambda x,y : x._props["intervalContains"].set(y), fdel=None, doc=propDocs["intervalContains"])
	intervalDuring = property(fget=lambda x: x._props["intervalDuring"].get(), fset=lambda x,y : x._props["intervalDuring"].set(y), fdel=None, doc=propDocs["intervalDuring"])
	intervalEquals = property(fget=lambda x: x._props["intervalEquals"].get(), fset=lambda x,y : x._props["intervalEquals"].set(y), fdel=None, doc=propDocs["intervalEquals"])
	intervalFinishedBy = property(fget=lambda x: x._props["intervalFinishedBy"].get(), fset=lambda x,y : x._props["intervalFinishedBy"].set(y), fdel=None, doc=propDocs["intervalFinishedBy"])
	intervalFinishes = property(fget=lambda x: x._props["intervalFinishes"].get(), fset=lambda x,y : x._props["intervalFinishes"].set(y), fdel=None, doc=propDocs["intervalFinishes"])
	intervalMeets = property(fget=lambda x: x._props["intervalMeets"].get(), fset=lambda x,y : x._props["intervalMeets"].set(y), fdel=None, doc=propDocs["intervalMeets"])
	intervalMetBy = property(fget=lambda x: x._props["intervalMetBy"].get(), fset=lambda x,y : x._props["intervalMetBy"].set(y), fdel=None, doc=propDocs["intervalMetBy"])
	intervalOverlappedBy = property(fget=lambda x: x._props["intervalOverlappedBy"].get(), fset=lambda x,y : x._props["intervalOverlappedBy"].set(y), fdel=None, doc=propDocs["intervalOverlappedBy"])
	intervalOverlaps = property(fget=lambda x: x._props["intervalOverlaps"].get(), fset=lambda x,y : x._props["intervalOverlaps"].set(y), fdel=None, doc=propDocs["intervalOverlaps"])
	intervalStartedBy = property(fget=lambda x: x._props["intervalStartedBy"].get(), fset=lambda x,y : x._props["intervalStartedBy"].set(y), fdel=None, doc=propDocs["intervalStartedBy"])
	intervalStarts = property(fget=lambda x: x._props["intervalStarts"].get(), fset=lambda x,y : x._props["intervalStarts"].set(y), fdel=None, doc=propDocs["intervalStarts"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___RelativeInterval(rdfs___Resource):
	"""
	tl:RelativeInterval
	an interval defined on a relative timeline
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "RelativeInterval"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#RelativeInterval"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___TimeLineMap(rdfs___Resource):
	"""
	tl:TimeLineMap
	Allows to map two time lines together
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "TimeLineMap"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["domainTimeLine"] = PropertySet("domainTimeLine","http://purl.org/NET/c4dm/timeline.owl#domainTimeLine", tl___TimeLine, False)
		self._props["rangeTimeLine"] = PropertySet("rangeTimeLine","http://purl.org/NET/c4dm/timeline.owl#rangeTimeLine", tl___TimeLine, False)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#TimeLineMap"


	# Python class properties to wrap the PropertySet objects
	domainTimeLine = property(fget=lambda x: x._props["domainTimeLine"].get(), fset=lambda x,y : x._props["domainTimeLine"].set(y), fdel=None, doc=propDocs["domainTimeLine"])
	rangeTimeLine = property(fget=lambda x: x._props["rangeTimeLine"].get(), fset=lambda x,y : x._props["rangeTimeLine"].set(y), fdel=None, doc=propDocs["rangeTimeLine"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___UniformSamplingMap(tl___TimeLineMap):
	"""
	tl:UniformSamplingMap
	Describe the relation between a continuous time-line and its sampled equivalent
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tl___TimeLineMap.__init__(self)
		self._initialised = False
		self.shortname = "UniformSamplingMap"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["domainTimeLine"] = PropertySet("domainTimeLine","http://purl.org/NET/c4dm/timeline.owl#domainTimeLine", tl___TimeLine, False)
		self._props["rangeTimeLine"] = PropertySet("rangeTimeLine","http://purl.org/NET/c4dm/timeline.owl#rangeTimeLine", tl___TimeLine, False)
		self._props["sampleRate"] = PropertySet("sampleRate","http://purl.org/NET/c4dm/timeline.owl#sampleRate", int, False)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#UniformSamplingMap"


	# Python class properties to wrap the PropertySet objects
	domainTimeLine = property(fget=lambda x: x._props["domainTimeLine"].get(), fset=lambda x,y : x._props["domainTimeLine"].set(y), fdel=None, doc=propDocs["domainTimeLine"])
	rangeTimeLine = property(fget=lambda x: x._props["rangeTimeLine"].get(), fset=lambda x,y : x._props["rangeTimeLine"].set(y), fdel=None, doc=propDocs["rangeTimeLine"])
	sampleRate = property(fget=lambda x: x._props["sampleRate"].get(), fset=lambda x,y : x._props["sampleRate"].set(y), fdel=None, doc=propDocs["sampleRate"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class owlssp___Profile(rdfs___Resource):
	"""
	owlssp:Profile
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Profile"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.daml.org/services/owl-s/1.2/Profile.owl#Profile"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___Aggregation(ces___EventPattern):
	"""
	ces:Aggregation
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___EventPattern.__init__(self)
		self._initialised = False
		self.shortname = "Aggregation"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#Aggregation"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___ComplexEventService(ces___EventService):
	"""
	ces:ComplexEventService
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___EventService.__init__(self)
		self._initialised = False
		self.shortname = "ComplexEventService"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#ComplexEventService"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___EventPayload(rdfs___Resource):
	"""
	ces:EventPayload
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "EventPayload"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#EventPayload"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___EventRequest(ces___EventService):
	"""
	ces:EventRequest
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___EventService.__init__(self)
		self._initialised = False
		self.shortname = "EventRequest"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasConstraint"] = PropertySet("hasConstraint","http://www.insight-centre.org/ces#hasConstraint", ces___Constraint, False)
		self._props["hasPreference"] = PropertySet("hasPreference","http://www.insight-centre.org/ces#hasPreference", ces___Preference, False)
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#EventRequest"


	# Python class properties to wrap the PropertySet objects
	hasConstraint = property(fget=lambda x: x._props["hasConstraint"].get(), fset=lambda x,y : x._props["hasConstraint"].set(y), fdel=None, doc=propDocs["hasConstraint"])
	hasPreference = property(fget=lambda x: x._props["hasPreference"].get(), fset=lambda x,y : x._props["hasPreference"].set(y), fdel=None, doc=propDocs["hasPreference"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___JmsGrounding(owlsg___Grounding):
	"""
	ces:JmsGrounding
	"""
	def __init__(self,URI=None):
		# Initialise parents
		owlsg___Grounding.__init__(self)
		self._initialised = False
		self.shortname = "JmsGrounding"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["jmsService"] = PropertySet("jmsService","http://www.insight-centre.org/ces#jmsService", anyURI, False)
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#JmsGrounding"


	# Python class properties to wrap the PropertySet objects
	jmsService = property(fget=lambda x: x._props["jmsService"].get(), fset=lambda x,y : x._props["jmsService"].set(y), fdel=None, doc=propDocs["jmsService"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___Or(ces___EventPattern, rdfs___Bag):
	"""
	ces:Or
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___EventPattern.__init__(self)
		rdfs___Bag.__init__(self)
		self._initialised = False
		self.shortname = "Or"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#Or"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___Repetition(ces___EventPattern, rdfs___Seq):
	"""
	ces:Repetition
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___EventPattern.__init__(self)
		rdfs___Seq.__init__(self)
		self._initialised = False
		self.shortname = "Repetition"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasCardinality"] = PropertySet("hasCardinality","http://www.insight-centre.org/ces#hasCardinality", int, False)
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#Repetition"


	# Python class properties to wrap the PropertySet objects
	hasCardinality = property(fget=lambda x: x._props["hasCardinality"].get(), fset=lambda x,y : x._props["hasCardinality"].set(y), fdel=None, doc=propDocs["hasCardinality"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___SlidingWindow(rdfs___Resource):
	"""
	ces:SlidingWindow
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "SlidingWindow"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#SlidingWindow"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class DUL___InformationEntity(rdfs___Resource):
	"""
	DUL:InformationEntity
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "InformationEntity"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.loa-cnr.it/ontologies/DUL.owl#InformationEntity"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class DUL___PhysicalObject(rdfs___Resource):
	"""
	DUL:PhysicalObject
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "PhysicalObject"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.loa-cnr.it/ontologies/DUL.owl#PhysicalObject"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class DUL___Situation(rdfs___Resource):
	"""
	DUL:Situation
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Situation"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.loa-cnr.it/ontologies/DUL.owl#Situation"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tm___DateTimeDescription(rdfs___Resource):
	"""
	tm:DateTimeDescription
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "DateTimeDescription"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["day"] = PropertySet("day","http://www.w3.org/2006/time#day", int, False)
		self._props["dayOfWeek"] = PropertySet("dayOfWeek","http://www.w3.org/2006/time#dayOfWeek", tm___DayOfWeek, False)
		self._props["dayOfYear"] = PropertySet("dayOfYear","http://www.w3.org/2006/time#dayOfYear", int, False)
		self._props["hour"] = PropertySet("hour","http://www.w3.org/2006/time#hour", int, False)
		self._props["minute"] = PropertySet("minute","http://www.w3.org/2006/time#minute", int, False)
		self._props["month"] = PropertySet("month","http://www.w3.org/2006/time#month", int, False)
		self._props["second"] = PropertySet("second","http://www.w3.org/2006/time#second", str, False)
		self._props["timeZone"] = PropertySet("timeZone","http://www.w3.org/2006/time#timeZone", tzont___TimeZone, False)
		self._props["unitType"] = PropertySet("unitType","http://www.w3.org/2006/time#unitType", tm___TemporalUnit, False)
		self._props["week"] = PropertySet("week","http://www.w3.org/2006/time#week", int, False)
		self._props["year"] = PropertySet("year","http://www.w3.org/2006/time#year", int, False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#DateTimeDescription"


	# Python class properties to wrap the PropertySet objects
	day = property(fget=lambda x: x._props["day"].get(), fset=lambda x,y : x._props["day"].set(y), fdel=None, doc=propDocs["day"])
	dayOfWeek = property(fget=lambda x: x._props["dayOfWeek"].get(), fset=lambda x,y : x._props["dayOfWeek"].set(y), fdel=None, doc=propDocs["dayOfWeek"])
	dayOfYear = property(fget=lambda x: x._props["dayOfYear"].get(), fset=lambda x,y : x._props["dayOfYear"].set(y), fdel=None, doc=propDocs["dayOfYear"])
	hour = property(fget=lambda x: x._props["hour"].get(), fset=lambda x,y : x._props["hour"].set(y), fdel=None, doc=propDocs["hour"])
	minute = property(fget=lambda x: x._props["minute"].get(), fset=lambda x,y : x._props["minute"].set(y), fdel=None, doc=propDocs["minute"])
	month = property(fget=lambda x: x._props["month"].get(), fset=lambda x,y : x._props["month"].set(y), fdel=None, doc=propDocs["month"])
	second = property(fget=lambda x: x._props["second"].get(), fset=lambda x,y : x._props["second"].set(y), fdel=None, doc=propDocs["second"])
	timeZone = property(fget=lambda x: x._props["timeZone"].get(), fset=lambda x,y : x._props["timeZone"].set(y), fdel=None, doc=propDocs["timeZone"])
	unitType = property(fget=lambda x: x._props["unitType"].get(), fset=lambda x,y : x._props["unitType"].set(y), fdel=None, doc=propDocs["unitType"])
	week = property(fget=lambda x: x._props["week"].get(), fset=lambda x,y : x._props["week"].set(y), fdel=None, doc=propDocs["week"])
	year = property(fget=lambda x: x._props["year"].get(), fset=lambda x,y : x._props["year"].set(y), fdel=None, doc=propDocs["year"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tm___Instant(tm___TemporalEntity):
	"""
	tm:Instant
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tm___TemporalEntity.__init__(self)
		self._initialised = False
		self.shortname = "Instant"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["inDateTime"] = PropertySet("inDateTime","http://www.w3.org/2006/time#inDateTime", tm___DateTimeDescription, False)
		self._props["inXSDDateTime"] = PropertySet("inXSDDateTime","http://www.w3.org/2006/time#inXSDDateTime", str, False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#Instant"


	# Python class properties to wrap the PropertySet objects
	inDateTime = property(fget=lambda x: x._props["inDateTime"].get(), fset=lambda x,y : x._props["inDateTime"].set(y), fdel=None, doc=propDocs["inDateTime"])
	inXSDDateTime = property(fget=lambda x: x._props["inXSDDateTime"].get(), fset=lambda x,y : x._props["inXSDDateTime"].set(y), fdel=None, doc=propDocs["inXSDDateTime"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tm___TemporalUnit(rdfs___Resource):
	"""
	tm:TemporalUnit
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "TemporalUnit"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#TemporalUnit"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___AgentInfluence(prov___Influence):
	"""
	prov:AgentInfluence
	AgentInfluence provides additional descriptions of an Agent's binary influence upon any other kind of resource. Instances of AgentInfluence use the prov:agent property to cite the influencing Agent.
	It is not recommended that the type AgentInfluence be asserted without also asserting one of its more specific subclasses.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___Influence.__init__(self)
		self._initialised = False
		self.shortname = "AgentInfluence"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["agent"] = PropertySet("agent","http://www.w3.org/ns/prov#agent", (owl___Thing,prov___Agent), False)
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#AgentInfluence"


	# Python class properties to wrap the PropertySet objects
	agent = property(fget=lambda x: x._props["agent"].get(), fset=lambda x,y : x._props["agent"].set(y), fdel=None, doc=propDocs["agent"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Attribution(prov___AgentInfluence):
	"""
	prov:Attribution
	An instance of prov:Attribution provides additional descriptions about the binary prov:wasAttributedTo relation from an prov:Entity to some prov:Agent that had some responsible for it. For example, :cake prov:wasAttributedTo :baker; prov:qualifiedAttribution [ a prov:Attribution; prov:entity :baker; :foo :bar ].
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___AgentInfluence.__init__(self)
		self._initialised = False
		self.shortname = "Attribution"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Attribution"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Delegation(prov___AgentInfluence):
	"""
	prov:Delegation
	An instance of prov:Delegation provides additional descriptions about the binary prov:actedOnBehalfOf relation from a performing prov:Agent to some prov:Agent for whom it was performed. For example, :mixing prov:wasAssociatedWith :toddler . :toddler prov:actedOnBehalfOf :mother; prov:qualifiedDelegation [ a prov:Delegation; prov:entity :mother; :foo :bar ].
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___AgentInfluence.__init__(self)
		self._initialised = False
		self.shortname = "Delegation"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hadActivity"] = PropertySet("hadActivity","http://www.w3.org/ns/prov#hadActivity", prov___Activity, False)
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Delegation"


	# Python class properties to wrap the PropertySet objects
	hadActivity = property(fget=lambda x: x._props["hadActivity"].get(), fset=lambda x,y : x._props["hadActivity"].set(y), fdel=None, doc=propDocs["hadActivity"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___End(prov___EntityInfluence, prov___InstantaneousEvent):
	"""
	prov:End
	An instance of prov:End provides additional descriptions about the binary prov:wasEndedBy relation from some ended prov:Activity to an prov:Entity that ended it. For example, :ball_game prov:wasEndedBy :buzzer; prov:qualifiedEnd [ a prov:End; prov:entity :buzzer; :foo :bar; prov:atTime '2012-03-09T08:05:08-05:00'^^xsd:dateTime ].
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___EntityInfluence.__init__(self)
		prov___InstantaneousEvent.__init__(self)
		self._initialised = False
		self.shortname = "End"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hadActivity"] = PropertySet("hadActivity","http://www.w3.org/ns/prov#hadActivity", prov___Activity, False)
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#End"


	# Python class properties to wrap the PropertySet objects
	hadActivity = property(fget=lambda x: x._props["hadActivity"].get(), fset=lambda x,y : x._props["hadActivity"].set(y), fdel=None, doc=propDocs["hadActivity"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Invalidation(prov___ActivityInfluence, prov___InstantaneousEvent):
	"""
	prov:Invalidation
	An instance of prov:Invalidation provides additional descriptions about the binary prov:wasInvalidatedBy relation from an invalidated prov:Entity to the prov:Activity that invalidated it. For example, :uncracked_egg prov:wasInvalidatedBy :baking; prov:qualifiedInvalidation [ a prov:Invalidation; prov:activity :baking; :foo :bar ].
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___ActivityInfluence.__init__(self)
		prov___InstantaneousEvent.__init__(self)
		self._initialised = False
		self.shortname = "Invalidation"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Invalidation"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Start(prov___EntityInfluence, prov___InstantaneousEvent):
	"""
	prov:Start
	An instance of prov:Start provides additional descriptions about the binary prov:wasStartedBy relation from some started prov:Activity to an prov:Entity that started it. For example, :foot_race prov:wasStartedBy :bang; prov:qualifiedStart [ a prov:Start; prov:entity :bang; :foo :bar; prov:atTime '2012-03-09T08:05:08-05:00'^^xsd:dateTime ] .
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___EntityInfluence.__init__(self)
		prov___InstantaneousEvent.__init__(self)
		self._initialised = False
		self.shortname = "Start"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hadActivity"] = PropertySet("hadActivity","http://www.w3.org/ns/prov#hadActivity", prov___Activity, False)
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Start"


	# Python class properties to wrap the PropertySet objects
	hadActivity = property(fget=lambda x: x._props["hadActivity"].get(), fset=lambda x,y : x._props["hadActivity"].set(y), fdel=None, doc=propDocs["hadActivity"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___OnlineGamingAccount(foaf___OnlineAccount):
	"""
	foaf:OnlineGamingAccount
	An online gaming account.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___OnlineAccount.__init__(self)
		self._initialised = False
		self.shortname = "OnlineGamingAccount"
		self.URI = URI
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/OnlineGamingAccount"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___DistrictTrafficReportService(ces___ComplexEventService):
	"""
	ct:DistrictTrafficReportService
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___ComplexEventService.__init__(self)
		self._initialised = False
		self.shortname = "DistrictTrafficReportService"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#DistrictTrafficReportService"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___StreetTrafficReportService(ces___ComplexEventService):
	"""
	ct:StreetTrafficReportService
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___ComplexEventService.__init__(self)
		self._initialised = False
		self.shortname = "StreetTrafficReportService"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#StreetTrafficReportService"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Age(qoi___Timeliness):
	"""
	qoi:Age
	The time an information was created/measured/sensed. Has a minimum value of 0.0 and cannot be negative.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Timeliness.__init__(self)
		self._initialised = False
		self.shortname = "Age"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Age"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Bandwidth(qoi___NetworkPerformance):
	"""
	qoi:Bandwidth
	Min/Avrg/Max amount of bandwidth that is required to transport the stream. Has a minimum value of 0.0 and cannot be negative.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___NetworkPerformance.__init__(self)
		self._initialised = False
		self.shortname = "Bandwidth"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Bandwidth"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Cost(qoi___Quality):
	"""
	qoi:Cost
	Category to describe the costs of a data stream.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Quality.__init__(self)
		self._initialised = False
		self.shortname = "Cost"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Cost"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___EnergyConsumption(qoi___Cost):
	"""
	qoi:EnergyConsumption
	The amount of energy used to access the steam. The EnergyConsumption cannot be negative.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Cost.__init__(self)
		self._initialised = False
		self.shortname = "EnergyConsumption"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#EnergyConsumption"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Latency(qoi___NetworkPerformance):
	"""
	qoi:Latency
	Measure of the time delay between the stream is sent and received in the virtualisation layer. Latency cannot be negative.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___NetworkPerformance.__init__(self)
		self._initialised = False
		self.shortname = "Latency"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Latency"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___MonetaryConsumption(qoi___Cost):
	"""
	qoi:MonetaryConsumption
	Is the usage of the stream free of charge or how much does it cost. The MonetaryConsumption has to be greater or equal to 0.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Cost.__init__(self)
		self._initialised = False
		self.shortname = "MonetaryConsumption"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#MonetaryConsumption"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Ordered(qoi___Queuing):
	"""
	qoi:Ordered
	Probability that data sets arrive in the defined queuing order. Ordered cannot be negative and only reach 1 (0-100%)
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Queuing.__init__(self)
		self._initialised = False
		self.shortname = "Ordered"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Ordered"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___PublicKey(qoi___Signing):
	"""
	qoi:PublicKey
	Key to decrypt signatures.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Signing.__init__(self)
		self._initialised = False
		self.shortname = "PublicKey"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#PublicKey"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Throughput(qoi___NetworkPerformance):
	"""
	qoi:Throughput
	The amount of useful information sent by the network (e.g. sensor data), taking out the headers and protocol information sent in the network. Throughput cannot be negative.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___NetworkPerformance.__init__(self)
		self._initialised = False
		self.shortname = "Throughput"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Throughput"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class muo___ComplexDerivedUnit(muo___DerivedUnit):
	"""
	muo:ComplexDerivedUnit
	Units that are derived from two or more measurement units (i.e. a derived unit which is defined by means of more than one unit in its dimensional equation). For instance, the complex derived unit meter per second squared is defined by a dimensional equation with two units: m and s2.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		muo___DerivedUnit.__init__(self)
		self._initialised = False
		self.shortname = "ComplexDerivedUnit"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/muo/muo#ComplexDerivedUnit"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class muo___SIUnit(muo___UnitOfMeasurement):
	"""
	muo:SIUnit
	Unit belonging to the International System of Units. The SI recognizes several base and derived units for some physical qualities assumed to be mutually independent.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		muo___UnitOfMeasurement.__init__(self)
		self._initialised = False
		self.shortname = "SIUnit"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/muo/muo#SIUnit"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Deployment(ssn___DeploymentRelatedProcess):
	"""
	ssn:Deployment
	The ongoing Process of Entities (for the purposes of this ontology, mainly sensors) deployed for a particular purpose.  For example, a particular Sensor deployed on a Platform, or a whole network of Sensors deployed for an observation campaign.  The deployment may have sub processes, such as installation, maintenance, addition, and decomissioning and removal.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___DeploymentRelatedProcess.__init__(self)
		self._initialised = False
		self.shortname = "Deployment"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["deployedOnPlatform"] = PropertySet("deployedOnPlatform","http://purl.oclc.org/NET/ssnx/ssn#deployedOnPlatform", ssn___Platform, False)
		self._props["deployedSystem"] = PropertySet("deployedSystem","http://purl.oclc.org/NET/ssnx/ssn#deployedSystem", ssn___System, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Deployment"


	# Python class properties to wrap the PropertySet objects
	deployedOnPlatform = property(fget=lambda x: x._props["deployedOnPlatform"].get(), fset=lambda x,y : x._props["deployedOnPlatform"].set(y), fdel=None, doc=propDocs["deployedOnPlatform"])
	deployedSystem = property(fget=lambda x: x._props["deployedSystem"].get(), fset=lambda x,y : x._props["deployedSystem"].set(y), fdel=None, doc=propDocs["deployedSystem"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Observation(DUL___Situation):
	"""
	ssn:Observation
	An Observation is a Situation in which a Sensing method has been used to estimate or calculate a value of a Property of a FeatureOfInterest.  Links to Sensing and Sensor describe what made the Observation and how; links to Property and Feature detail what was sensed; the result is the output of a Sensor; other metadata details times etc.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		DUL___Situation.__init__(self)
		self._initialised = False
		self.shortname = "Observation"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["featureOfInterest"] = PropertySet("featureOfInterest","http://purl.oclc.org/NET/ssnx/ssn#featureOfInterest", ssn___FeatureOfInterest, False)
		self._props["observationResult"] = PropertySet("observationResult","http://purl.oclc.org/NET/ssnx/ssn#observationResult", ssn___SensorOutput, False)
		self._props["observationResultTime"] = PropertySet("observationResultTime","http://purl.oclc.org/NET/ssnx/ssn#observationResultTime", (tl___Interval,tl___Instant), False)
		self._props["observationSamplingTime"] = PropertySet("observationSamplingTime","http://purl.oclc.org/NET/ssnx/ssn#observationSamplingTime", (tl___Interval,tl___Instant), False)
		self._props["observedBy"] = PropertySet("observedBy","http://purl.oclc.org/NET/ssnx/ssn#observedBy", ssn___Sensor, False)
		self._props["observedProperty"] = PropertySet("observedProperty","http://purl.oclc.org/NET/ssnx/ssn#observedProperty", ssn___Property, False)
		self._props["qualityOfObservation"] = PropertySet("qualityOfObservation","http://purl.oclc.org/NET/ssnx/ssn#qualityOfObservation", ssn___Property, False)
		self._props["sensingMethodUsed"] = PropertySet("sensingMethodUsed","http://purl.oclc.org/NET/ssnx/ssn#sensingMethodUsed", ssn___Sensing, False)
		self._props["includesEvent"] = PropertySet("includesEvent","http://www.loa-cnr.it/ontologies/DUL.owl#includesEvent", (ssn___SensorInput,ssn___Stimulus), False)
		self._props["hadPrimarySource"] = PropertySet("hadPrimarySource","http://www.w3.org/ns/prov#hadPrimarySource", (prov___Entity,sao___StreamData,sao___StreamAnalysis), False)
		self._props["wasDerivedFrom"] = PropertySet("wasDerivedFrom","http://www.w3.org/ns/prov#wasDerivedFrom", (prov___Entity,sao___StreamData,prov___Activity,sao___StreamAnalysis,prov___Agent), False)
		self._props["wasQuotedFrom"] = PropertySet("wasQuotedFrom","http://www.w3.org/ns/prov#wasQuotedFrom", (prov___Entity,sao___StreamData,sao___StreamAnalysis), False)
		self._props["wasRevisionOf"] = PropertySet("wasRevisionOf","http://www.w3.org/ns/prov#wasRevisionOf", (prov___Entity,sao___StreamData,sao___StreamAnalysis), False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Observation"


	# Python class properties to wrap the PropertySet objects
	featureOfInterest = property(fget=lambda x: x._props["featureOfInterest"].get(), fset=lambda x,y : x._props["featureOfInterest"].set(y), fdel=None, doc=propDocs["featureOfInterest"])
	observationResult = property(fget=lambda x: x._props["observationResult"].get(), fset=lambda x,y : x._props["observationResult"].set(y), fdel=None, doc=propDocs["observationResult"])
	observationResultTime = property(fget=lambda x: x._props["observationResultTime"].get(), fset=lambda x,y : x._props["observationResultTime"].set(y), fdel=None, doc=propDocs["observationResultTime"])
	observationSamplingTime = property(fget=lambda x: x._props["observationSamplingTime"].get(), fset=lambda x,y : x._props["observationSamplingTime"].set(y), fdel=None, doc=propDocs["observationSamplingTime"])
	observedBy = property(fget=lambda x: x._props["observedBy"].get(), fset=lambda x,y : x._props["observedBy"].set(y), fdel=None, doc=propDocs["observedBy"])
	observedProperty = property(fget=lambda x: x._props["observedProperty"].get(), fset=lambda x,y : x._props["observedProperty"].set(y), fdel=None, doc=propDocs["observedProperty"])
	qualityOfObservation = property(fget=lambda x: x._props["qualityOfObservation"].get(), fset=lambda x,y : x._props["qualityOfObservation"].set(y), fdel=None, doc=propDocs["qualityOfObservation"])
	sensingMethodUsed = property(fget=lambda x: x._props["sensingMethodUsed"].get(), fset=lambda x,y : x._props["sensingMethodUsed"].set(y), fdel=None, doc=propDocs["sensingMethodUsed"])
	includesEvent = property(fget=lambda x: x._props["includesEvent"].get(), fset=lambda x,y : x._props["includesEvent"].set(y), fdel=None, doc=propDocs["includesEvent"])
	hadPrimarySource = property(fget=lambda x: x._props["hadPrimarySource"].get(), fset=lambda x,y : x._props["hadPrimarySource"].set(y), fdel=None, doc=propDocs["hadPrimarySource"])
	wasDerivedFrom = property(fget=lambda x: x._props["wasDerivedFrom"].get(), fset=lambda x,y : x._props["wasDerivedFrom"].set(y), fdel=None, doc=propDocs["wasDerivedFrom"])
	wasQuotedFrom = property(fget=lambda x: x._props["wasQuotedFrom"].get(), fset=lambda x,y : x._props["wasQuotedFrom"].set(y), fdel=None, doc=propDocs["wasQuotedFrom"])
	wasRevisionOf = property(fget=lambda x: x._props["wasRevisionOf"].get(), fset=lambda x,y : x._props["wasRevisionOf"].set(y), fdel=None, doc=propDocs["wasRevisionOf"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Platform(DUL___PhysicalObject):
	"""
	ssn:Platform
	An Entity to which other Entities can be attached - particuarly Sensors and other Platforms.  For example, a post might act as the Platform, a bouy might act as a Platform, or a fish might act as a Platform for an attached sensor.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		DUL___PhysicalObject.__init__(self)
		self._initialised = False
		self.shortname = "Platform"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["attachedSystem"] = PropertySet("attachedSystem","http://purl.oclc.org/NET/ssnx/ssn#attachedSystem", ssn___System, False)
		self._props["inDeployment"] = PropertySet("inDeployment","http://purl.oclc.org/NET/ssnx/ssn#inDeployment", ssn___Deployment, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Platform"


	# Python class properties to wrap the PropertySet objects
	attachedSystem = property(fget=lambda x: x._props["attachedSystem"].get(), fset=lambda x,y : x._props["attachedSystem"].set(y), fdel=None, doc=propDocs["attachedSystem"])
	inDeployment = property(fget=lambda x: x._props["inDeployment"].get(), fset=lambda x,y : x._props["inDeployment"].set(y), fdel=None, doc=propDocs["inDeployment"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Sensor(DUL___PhysicalObject, prov___Agent):
	"""
	ssn:Sensor
	A sensor can do (implements) sensing: that is, a sensor is any entity that can follow a sensing method and thus observe some Property of a FeatureOfInterest.  Sensors may be physical devices, computational methods, a laboratory setup with a person following a method, or any other thing that can follow a Sensing Method to observe a Property.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		DUL___PhysicalObject.__init__(self)
		prov___Agent.__init__(self)
		self._initialised = False
		self.shortname = "Sensor"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["detects"] = PropertySet("detects","http://purl.oclc.org/NET/ssnx/ssn#detects", (ssn___SensorInput,ssn___Stimulus), False)
		self._props["hasMeasurementCapability"] = PropertySet("hasMeasurementCapability","http://purl.oclc.org/NET/ssnx/ssn#hasMeasurementCapability", (ssn___Property,ssn___MeasurementCapability), False)
		self._props["implements"] = PropertySet("implements","http://purl.oclc.org/NET/ssnx/ssn#implements", ssn___Sensing, False)
		self._props["madeObservation"] = PropertySet("madeObservation","http://purl.oclc.org/NET/ssnx/ssn#madeObservation", ssn___Observation, False)
		self._props["observes"] = PropertySet("observes","http://purl.oclc.org/NET/ssnx/ssn#observes", ssn___Property, False)
		self._props["presents"] = PropertySet("presents","http://www.daml.org/services/owl-s/1.2/Service.owl#presents", ces___EventProfile, False)
		self._props["wasAttributedTo"] = PropertySet("wasAttributedTo","http://www.w3.org/ns/prov#wasAttributedTo", (ssn___Property,prov___Entity,ssn___Sensor,prov___Agent,prov___Activity), False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Sensor"


	# Python class properties to wrap the PropertySet objects
	detects = property(fget=lambda x: x._props["detects"].get(), fset=lambda x,y : x._props["detects"].set(y), fdel=None, doc=propDocs["detects"])
	hasMeasurementCapability = property(fget=lambda x: x._props["hasMeasurementCapability"].get(), fset=lambda x,y : x._props["hasMeasurementCapability"].set(y), fdel=None, doc=propDocs["hasMeasurementCapability"])
	implements = property(fget=lambda x: x._props["implements"].get(), fset=lambda x,y : x._props["implements"].set(y), fdel=None, doc=propDocs["implements"])
	madeObservation = property(fget=lambda x: x._props["madeObservation"].get(), fset=lambda x,y : x._props["madeObservation"].set(y), fdel=None, doc=propDocs["madeObservation"])
	observes = property(fget=lambda x: x._props["observes"].get(), fset=lambda x,y : x._props["observes"].set(y), fdel=None, doc=propDocs["observes"])
	presents = property(fget=lambda x: x._props["presents"].get(), fset=lambda x,y : x._props["presents"].set(y), fdel=None, doc=propDocs["presents"])
	wasAttributedTo = property(fget=lambda x: x._props["wasAttributedTo"].get(), fset=lambda x,y : x._props["wasAttributedTo"].set(y), fdel=None, doc=propDocs["wasAttributedTo"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Stimulus(DUL___Event):
	"""
	ssn:Stimulus
	An Event in the real world that 'triggers' the sensor.  The properties associated to the stimulus may be different to eventual observed property.  It is the event, not the object that triggers the sensor.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		DUL___Event.__init__(self)
		self._initialised = False
		self.shortname = "Stimulus"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Stimulus"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___System(DUL___PhysicalObject):
	"""
	ssn:System
	System is a unit of abstraction for pieces of infrastructure (and we largely care that they are) for sensing. A system has components, its subsystems, which are other systems.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		DUL___PhysicalObject.__init__(self)
		self._initialised = False
		self.shortname = "System"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasDeployment"] = PropertySet("hasDeployment","http://purl.oclc.org/NET/ssnx/ssn#hasDeployment", ssn___Deployment, False)
		self._props["hasOperatingRange"] = PropertySet("hasOperatingRange","http://purl.oclc.org/NET/ssnx/ssn#hasOperatingRange", (ssn___Property,ssn___OperatingRange), False)
		self._props["hasSubSystem"] = PropertySet("hasSubSystem","http://purl.oclc.org/NET/ssnx/ssn#hasSubSystem", ssn___System, False)
		self._props["hasSurvivalRange"] = PropertySet("hasSurvivalRange","http://purl.oclc.org/NET/ssnx/ssn#hasSurvivalRange", (ssn___Property,ssn___SurvivalRange), False)
		self._props["onPlatform"] = PropertySet("onPlatform","http://purl.oclc.org/NET/ssnx/ssn#onPlatform", ssn___Platform, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#System"


	# Python class properties to wrap the PropertySet objects
	hasDeployment = property(fget=lambda x: x._props["hasDeployment"].get(), fset=lambda x,y : x._props["hasDeployment"].set(y), fdel=None, doc=propDocs["hasDeployment"])
	hasOperatingRange = property(fget=lambda x: x._props["hasOperatingRange"].get(), fset=lambda x,y : x._props["hasOperatingRange"].set(y), fdel=None, doc=propDocs["hasOperatingRange"])
	hasSubSystem = property(fget=lambda x: x._props["hasSubSystem"].get(), fset=lambda x,y : x._props["hasSubSystem"].set(y), fdel=None, doc=propDocs["hasSubSystem"])
	hasSurvivalRange = property(fget=lambda x: x._props["hasSurvivalRange"].get(), fset=lambda x,y : x._props["hasSurvivalRange"].set(y), fdel=None, doc=propDocs["hasSurvivalRange"])
	onPlatform = property(fget=lambda x: x._props["onPlatform"].get(), fset=lambda x,y : x._props["onPlatform"].set(y), fdel=None, doc=propDocs["onPlatform"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___AbstractInterval(tl___Interval):
	"""
	tl:AbstractInterval
	
            An interval defined on an abstract time-line.
        
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tl___Interval.__init__(self)
		self._initialised = False
		self.shortname = "AbstractInterval"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#AbstractInterval"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___DiscreteTimeLine(tl___TimeLine):
	"""
	tl:DiscreteTimeLine
	A discrete time line (like the time line backing a digital signal
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tl___TimeLine.__init__(self)
		self._initialised = False
		self.shortname = "DiscreteTimeLine"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#DiscreteTimeLine"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___ShiftMap(tl___TimeLineMap):
	"""
	tl:ShiftMap
	a map just shifting one timeline to another
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tl___TimeLineMap.__init__(self)
		self._initialised = False
		self.shortname = "ShiftMap"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["delay"] = PropertySet("delay","http://purl.org/NET/c4dm/timeline.owl#delay", None, False)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#ShiftMap"


	# Python class properties to wrap the PropertySet objects
	delay = property(fget=lambda x: x._props["delay"].get(), fset=lambda x,y : x._props["delay"].set(y), fdel=None, doc=propDocs["delay"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___UniformWindowingMap(tl___TimeLineMap):
	"""
	tl:UniformWindowingMap
	Describes the relation between a discrete time line and its windowed equivalent
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tl___TimeLineMap.__init__(self)
		self._initialised = False
		self.shortname = "UniformWindowingMap"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["domainTimeLine"] = PropertySet("domainTimeLine","http://purl.org/NET/c4dm/timeline.owl#domainTimeLine", tl___TimeLine, False)
		self._props["hopSize"] = PropertySet("hopSize","http://purl.org/NET/c4dm/timeline.owl#hopSize", int, False)
		self._props["rangeTimeLine"] = PropertySet("rangeTimeLine","http://purl.org/NET/c4dm/timeline.owl#rangeTimeLine", tl___TimeLine, False)
		self._props["windowLength"] = PropertySet("windowLength","http://purl.org/NET/c4dm/timeline.owl#windowLength", int, False)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#UniformWindowingMap"


	# Python class properties to wrap the PropertySet objects
	domainTimeLine = property(fget=lambda x: x._props["domainTimeLine"].get(), fset=lambda x,y : x._props["domainTimeLine"].set(y), fdel=None, doc=propDocs["domainTimeLine"])
	hopSize = property(fget=lambda x: x._props["hopSize"].get(), fset=lambda x,y : x._props["hopSize"].set(y), fdel=None, doc=propDocs["hopSize"])
	rangeTimeLine = property(fget=lambda x: x._props["rangeTimeLine"].get(), fset=lambda x,y : x._props["rangeTimeLine"].set(y), fdel=None, doc=propDocs["rangeTimeLine"])
	windowLength = property(fget=lambda x: x._props["windowLength"].get(), fset=lambda x,y : x._props["windowLength"].set(y), fdel=None, doc=propDocs["windowLength"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___And(ces___EventPattern, rdfs___Bag):
	"""
	ces:And
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___EventPattern.__init__(self)
		rdfs___Bag.__init__(self)
		self._initialised = False
		self.shortname = "And"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#And"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___EventProfile(owlssp___Profile):
	"""
	ces:EventProfile
	"""
	def __init__(self,URI=None):
		# Initialise parents
		owlssp___Profile.__init__(self)
		self._initialised = False
		self.shortname = "EventProfile"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasTRID"] = PropertySet("hasTRID","http://ict-citypulse.eu/city#hasTRID", str, False)
		self._props["hasQuality"] = PropertySet("hasQuality","http://purl.oclc.org/NET/UASO/qoi#hasQuality", qoi___Quality, False)
		self._props["serviceCategory"] = PropertySet("serviceCategory","http://www.daml.org/services/owl-s/1.2/ServiceCategory.owl#serviceCategory", owlssc___ServiceCategory, False)
		self._props["hasAggregation"] = PropertySet("hasAggregation","http://www.insight-centre.org/ces#hasAggregation", (ces___EventPattern,ces___Aggregation), False)
		self._props["hasEventPayload"] = PropertySet("hasEventPayload","http://www.insight-centre.org/ces#hasEventPayload", ces___EventPayload, False)
		self._props["hasFilter"] = PropertySet("hasFilter","http://www.insight-centre.org/ces#hasFilter", (ces___EventPattern,ces___Filter), False)
		self._props["hasNFP"] = PropertySet("hasNFP","http://www.insight-centre.org/ces#hasNFP", qoi___Quality, False)
		self._props["hasPattern"] = PropertySet("hasPattern","http://www.insight-centre.org/ces#hasPattern", ces___EventPattern, False)
		self._props["hasSelection"] = PropertySet("hasSelection","http://www.insight-centre.org/ces#hasSelection", (ces___EventPattern,ces___Selection), False)
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#EventProfile"


	# Python class properties to wrap the PropertySet objects
	hasTRID = property(fget=lambda x: x._props["hasTRID"].get(), fset=lambda x,y : x._props["hasTRID"].set(y), fdel=None, doc=propDocs["hasTRID"])
	hasQuality = property(fget=lambda x: x._props["hasQuality"].get(), fset=lambda x,y : x._props["hasQuality"].set(y), fdel=None, doc=propDocs["hasQuality"])
	serviceCategory = property(fget=lambda x: x._props["serviceCategory"].get(), fset=lambda x,y : x._props["serviceCategory"].set(y), fdel=None, doc=propDocs["serviceCategory"])
	hasAggregation = property(fget=lambda x: x._props["hasAggregation"].get(), fset=lambda x,y : x._props["hasAggregation"].set(y), fdel=None, doc=propDocs["hasAggregation"])
	hasEventPayload = property(fget=lambda x: x._props["hasEventPayload"].get(), fset=lambda x,y : x._props["hasEventPayload"].set(y), fdel=None, doc=propDocs["hasEventPayload"])
	hasFilter = property(fget=lambda x: x._props["hasFilter"].get(), fset=lambda x,y : x._props["hasFilter"].set(y), fdel=None, doc=propDocs["hasFilter"])
	hasNFP = property(fget=lambda x: x._props["hasNFP"].get(), fset=lambda x,y : x._props["hasNFP"].set(y), fdel=None, doc=propDocs["hasNFP"])
	hasPattern = property(fget=lambda x: x._props["hasPattern"].get(), fset=lambda x,y : x._props["hasPattern"].set(y), fdel=None, doc=propDocs["hasPattern"])
	hasSelection = property(fget=lambda x: x._props["hasSelection"].get(), fset=lambda x,y : x._props["hasSelection"].set(y), fdel=None, doc=propDocs["hasSelection"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___NFP(owlssrp___ServiceParameter):
	"""
	ces:NFP
	"""
	def __init__(self,URI=None):
		# Initialise parents
		owlssrp___ServiceParameter.__init__(self)
		self._initialised = False
		self.shortname = "NFP"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#NFP"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___Sequence(ces___EventPattern, rdfs___Seq):
	"""
	ces:Sequence
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___EventPattern.__init__(self)
		rdfs___Seq.__init__(self)
		self._initialised = False
		self.shortname = "Sequence"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#Sequence"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class DUL___Method(rdfs___Resource):
	"""
	DUL:Method
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Method"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.loa-cnr.it/ontologies/DUL.owl#Method"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class rdfs___Class(rdfs___Resource):
	"""
	rdfs:Class
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Class"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["oneOf"] = PropertySet("oneOf","file:///Users/sefki/Desktop/Desktop/SAOcodesTestCopy/Ontologies/owl.rdfs#oneOf", rdf___List, False)
		self._initialised = True
	classURI = "http://www.w3.org/2000/01/rdf-schema#Class"


	# Python class properties to wrap the PropertySet objects
	oneOf = property(fget=lambda x: x._props["oneOf"].get(), fset=lambda x,y : x._props["oneOf"].set(y), fdel=None, doc=propDocs["oneOf"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tm___January(tm___DateTimeDescription):
	"""
	tm:January
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tm___DateTimeDescription.__init__(self)
		self._initialised = False
		self.shortname = "January"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["month"] = PropertySet("month","http://www.w3.org/2006/time#month", int, False)
		self._props["unitType"] = PropertySet("unitType","http://www.w3.org/2006/time#unitType", tm___TemporalUnit, False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#January"


	# Python class properties to wrap the PropertySet objects
	month = property(fget=lambda x: x._props["month"].get(), fset=lambda x,y : x._props["month"].set(y), fdel=None, doc=propDocs["month"])
	unitType = property(fget=lambda x: x._props["unitType"].get(), fset=lambda x,y : x._props["unitType"].set(y), fdel=None, doc=propDocs["unitType"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Association(prov___AgentInfluence):
	"""
	prov:Association
	An instance of prov:Association provides additional descriptions about the binary prov:wasAssociatedWith relation from an prov:Activity to some prov:Agent that had some responsiblity for it. For example, :baking prov:wasAssociatedWith :baker; prov:qualifiedAssociation [ a prov:Association; prov:agent :baker; :foo :bar ].
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___AgentInfluence.__init__(self)
		self._initialised = False
		self.shortname = "Association"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hadPlan"] = PropertySet("hadPlan","http://www.w3.org/ns/prov#hadPlan", prov___Plan, False)
		self._props["hadRole"] = PropertySet("hadRole","http://www.w3.org/ns/prov#hadRole", prov___Role, False)
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Association"


	# Python class properties to wrap the PropertySet objects
	hadPlan = property(fget=lambda x: x._props["hadPlan"].get(), fset=lambda x,y : x._props["hadPlan"].set(y), fdel=None, doc=propDocs["hadPlan"])
	hadRole = property(fget=lambda x: x._props["hadRole"].get(), fset=lambda x,y : x._props["hadRole"].set(y), fdel=None, doc=propDocs["hadRole"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Derivation(prov___EntityInfluence):
	"""
	prov:Derivation
	The more specific forms of prov:Derivation (i.e., prov:Revision, prov:Quotation, prov:PrimarySource) should be asserted if they apply.
	An instance of prov:Derivation provides additional descriptions about the binary prov:wasDerivedFrom relation from some derived prov:Entity to another prov:Entity from which it was derived. For example, :chewed_bubble_gum prov:wasDerivedFrom :unwrapped_bubble_gum; prov:qualifiedDerivation [ a prov:Derivation; prov:entity :unwrapped_bubble_gum; :foo :bar ].
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___EntityInfluence.__init__(self)
		self._initialised = False
		self.shortname = "Derivation"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hadActivity"] = PropertySet("hadActivity","http://www.w3.org/ns/prov#hadActivity", prov___Activity, False)
		self._props["hadGeneration"] = PropertySet("hadGeneration","http://www.w3.org/ns/prov#hadGeneration", prov___Generation, False)
		self._props["hadUsage"] = PropertySet("hadUsage","http://www.w3.org/ns/prov#hadUsage", prov___Usage, False)
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Derivation"


	# Python class properties to wrap the PropertySet objects
	hadActivity = property(fget=lambda x: x._props["hadActivity"].get(), fset=lambda x,y : x._props["hadActivity"].set(y), fdel=None, doc=propDocs["hadActivity"])
	hadGeneration = property(fget=lambda x: x._props["hadGeneration"].get(), fset=lambda x,y : x._props["hadGeneration"].set(y), fdel=None, doc=propDocs["hadGeneration"])
	hadUsage = property(fget=lambda x: x._props["hadUsage"].get(), fset=lambda x,y : x._props["hadUsage"].set(y), fdel=None, doc=propDocs["hadUsage"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Generation(prov___ActivityInfluence, prov___InstantaneousEvent):
	"""
	prov:Generation
	An instance of prov:Generation provides additional descriptions about the binary prov:wasGeneratedBy relation from a generated prov:Entity to the prov:Activity that generated it. For example, :cake prov:wasGeneratedBy :baking; prov:qualifiedGeneration [ a prov:Generation; prov:activity :baking; :foo :bar ].
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___ActivityInfluence.__init__(self)
		prov___InstantaneousEvent.__init__(self)
		self._initialised = False
		self.shortname = "Generation"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Generation"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___PrimarySource(prov___Derivation):
	"""
	prov:PrimarySource
	An instance of prov:PrimarySource provides additional descriptions about the binary prov:hadPrimarySource relation from some secondary prov:Entity to an earlier, primary prov:Entity. For example, :blog prov:hadPrimarySource :newsArticle; prov:qualifiedPrimarySource [ a prov:PrimarySource; prov:entity :newsArticle; :foo :bar ] .
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___Derivation.__init__(self)
		self._initialised = False
		self.shortname = "PrimarySource"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#PrimarySource"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Revision(prov___Derivation):
	"""
	prov:Revision
	An instance of prov:Revision provides additional descriptions about the binary prov:wasRevisionOf relation from some newer prov:Entity to an earlier prov:Entity. For example, :draft_2 prov:wasRevisionOf :draft_1; prov:qualifiedRevision [ a prov:Revision; prov:entity :draft_1; :foo :bar ].
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___Derivation.__init__(self)
		self._initialised = False
		self.shortname = "Revision"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Revision"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Authority(qoi___Signing):
	"""
	qoi:Authority
	Certificate authority.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Signing.__init__(self)
		self._initialised = False
		self.shortname = "Authority"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Authority"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Jitter(qoi___NetworkPerformance):
	"""
	qoi:Jitter
	Deviation from true periodicity of an assumed periodic signal.Jitter cannot be negative.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___NetworkPerformance.__init__(self)
		self._initialised = False
		self.shortname = "Jitter"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Jitter"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___NetworkConsumption(qoi___Cost):
	"""
	qoi:NetworkConsumption
	How much traffic is caused by usage of the data source. The NetworkConsumption cannot be negative.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Cost.__init__(self)
		self._initialised = False
		self.shortname = "NetworkConsumption"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#NetworkConsumption"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___QueuingType(qoi___Queuing):
	"""
	qoi:QueuingType
	Queue Type, for example FIFO, LIFO, unordered.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Queuing.__init__(self)
		self._initialised = False
		self.shortname = "QueuingType"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#QueuingType"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class sao___StreamAnalysis(prov___Entity, ssn___Observation):
	"""
	sao:StreamAnalysis
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Observation.__init__(self)
		prov___Entity.__init__(self)
		self._initialised = False
		self.shortname = "StreamAnalysis"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["Timestamp"] = PropertySet("Timestamp","http://purl.oclc.org/NET/UNIS/sao/sao#Timestamp", str, False)
		self._props["computedfrom"] = PropertySet("computedfrom","http://purl.oclc.org/NET/UNIS/sao/sao#computedfrom", sao___StreamData, False)
		self._props["hasPoint"] = PropertySet("hasPoint","http://purl.oclc.org/NET/UNIS/sao/sao#hasPoint", sao___Point, False)
		self._props["hasSegment"] = PropertySet("hasSegment","http://purl.oclc.org/NET/UNIS/sao/sao#hasSegment", sao___Segment, False)
		self._props["hasUnitOfMeasurement"] = PropertySet("hasUnitOfMeasurement","http://purl.oclc.org/NET/UNIS/sao/sao#hasUnitOfMeasurement", muo___UnitOfMeasurement, False)
		self._props["nColumns"] = PropertySet("nColumns","http://purl.oclc.org/NET/UNIS/sao/sao#nColumns", int, False)
		self._props["nRows"] = PropertySet("nRows","http://purl.oclc.org/NET/UNIS/sao/sao#nRows", int, False)
		self._props["segmentsize"] = PropertySet("segmentsize","http://purl.oclc.org/NET/UNIS/sao/sao#segmentsize", int, False)
		self._props["stepsize"] = PropertySet("stepsize","http://purl.oclc.org/NET/UNIS/sao/sao#stepsize", int, False)
		self._props["time"] = PropertySet("time","http://purl.oclc.org/NET/UNIS/sao/sao#time", (tl___Interval,tl___Instant), False)
		self._props["value"] = PropertySet("value","http://purl.oclc.org/NET/UNIS/sao/sao#value", str, False)
		self._props["wasAttributedTo"] = PropertySet("wasAttributedTo","http://www.w3.org/ns/prov#wasAttributedTo", (ssn___Property,prov___Entity,ssn___Sensor,prov___Agent,prov___Activity), False)
		self._props["wasGeneratedBy"] = PropertySet("wasGeneratedBy","http://www.w3.org/ns/prov#wasGeneratedBy", (prov___Entity,sao___StreamEvent,prov___Activity,prov___Agent), False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UNIS/sao/sao#StreamAnalysis"


	# Python class properties to wrap the PropertySet objects
	Timestamp = property(fget=lambda x: x._props["Timestamp"].get(), fset=lambda x,y : x._props["Timestamp"].set(y), fdel=None, doc=propDocs["Timestamp"])
	computedfrom = property(fget=lambda x: x._props["computedfrom"].get(), fset=lambda x,y : x._props["computedfrom"].set(y), fdel=None, doc=propDocs["computedfrom"])
	hasPoint = property(fget=lambda x: x._props["hasPoint"].get(), fset=lambda x,y : x._props["hasPoint"].set(y), fdel=None, doc=propDocs["hasPoint"])
	hasSegment = property(fget=lambda x: x._props["hasSegment"].get(), fset=lambda x,y : x._props["hasSegment"].set(y), fdel=None, doc=propDocs["hasSegment"])
	hasUnitOfMeasurement = property(fget=lambda x: x._props["hasUnitOfMeasurement"].get(), fset=lambda x,y : x._props["hasUnitOfMeasurement"].set(y), fdel=None, doc=propDocs["hasUnitOfMeasurement"])
	nColumns = property(fget=lambda x: x._props["nColumns"].get(), fset=lambda x,y : x._props["nColumns"].set(y), fdel=None, doc=propDocs["nColumns"])
	nRows = property(fget=lambda x: x._props["nRows"].get(), fset=lambda x,y : x._props["nRows"].set(y), fdel=None, doc=propDocs["nRows"])
	segmentsize = property(fget=lambda x: x._props["segmentsize"].get(), fset=lambda x,y : x._props["segmentsize"].set(y), fdel=None, doc=propDocs["segmentsize"])
	stepsize = property(fget=lambda x: x._props["stepsize"].get(), fset=lambda x,y : x._props["stepsize"].set(y), fdel=None, doc=propDocs["stepsize"])
	time = property(fget=lambda x: x._props["time"].get(), fset=lambda x,y : x._props["time"].set(y), fdel=None, doc=propDocs["time"])
	value = property(fget=lambda x: x._props["value"].get(), fset=lambda x,y : x._props["value"].set(y), fdel=None, doc=propDocs["value"])
	wasAttributedTo = property(fget=lambda x: x._props["wasAttributedTo"].get(), fset=lambda x,y : x._props["wasAttributedTo"].set(y), fdel=None, doc=propDocs["wasAttributedTo"])
	wasGeneratedBy = property(fget=lambda x: x._props["wasGeneratedBy"].get(), fset=lambda x,y : x._props["wasGeneratedBy"].set(y), fdel=None, doc=propDocs["wasGeneratedBy"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class sao___SymbolicAggregateApproximation(sao___StreamAnalysis):
	"""
	sao:SymbolicAggregateApproximation
	"""
	def __init__(self,URI=None):
		# Initialise parents
		sao___StreamAnalysis.__init__(self)
		self._initialised = False
		self.shortname = "SymbolicAggregateApproximation"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["alphabetsize"] = PropertySet("alphabetsize","http://purl.oclc.org/NET/UNIS/sao/sao#alphabetsize", int, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UNIS/sao/sao#SymbolicAggregateApproximation"


	# Python class properties to wrap the PropertySet objects
	alphabetsize = property(fget=lambda x: x._props["alphabetsize"].get(), fset=lambda x,y : x._props["alphabetsize"].set(y), fdel=None, doc=propDocs["alphabetsize"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Process(DUL___Method):
	"""
	ssn:Process
	A process has an output and possibly inputs and, for a composite process, describes the temporal and dataflow dependencies and relationships amongst its parts. [SSN XG]
	"""
	def __init__(self,URI=None):
		# Initialise parents
		DUL___Method.__init__(self)
		self._initialised = False
		self.shortname = "Process"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasInput"] = PropertySet("hasInput","http://purl.oclc.org/NET/ssnx/ssn#hasInput", ssn___Input, False)
		self._props["hasOutput"] = PropertySet("hasOutput","http://purl.oclc.org/NET/ssnx/ssn#hasOutput", ssn___Output, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Process"


	# Python class properties to wrap the PropertySet objects
	hasInput = property(fget=lambda x: x._props["hasInput"].get(), fset=lambda x,y : x._props["hasInput"].set(y), fdel=None, doc=propDocs["hasInput"])
	hasOutput = property(fget=lambda x: x._props["hasOutput"].get(), fset=lambda x,y : x._props["hasOutput"].set(y), fdel=None, doc=propDocs["hasOutput"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Sensing(ssn___Process):
	"""
	ssn:Sensing
	Sensing is a process that results in the estimation, or calculation, of the value of a phenomenon.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Process.__init__(self)
		self._initialised = False
		self.shortname = "Sensing"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["implementedBy"] = PropertySet("implementedBy","http://purl.oclc.org/NET/ssnx/ssn#implementedBy", None, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Sensing"


	# Python class properties to wrap the PropertySet objects
	implementedBy = property(fget=lambda x: x._props["implementedBy"].get(), fset=lambda x,y : x._props["implementedBy"].set(y), fdel=None, doc=propDocs["implementedBy"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___SensorInput(DUL___Event):
	"""
	ssn:SensorInput
	An Event in the real world that 'triggers' the sensor.  The properties associated to the stimulus may be different to eventual observed property.  It is the event, not the object that triggers the sensor.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		DUL___Event.__init__(self)
		self._initialised = False
		self.shortname = "SensorInput"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["isProxyFor"] = PropertySet("isProxyFor","http://purl.oclc.org/NET/ssnx/ssn#isProxyFor", ssn___Property, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#SensorInput"


	# Python class properties to wrap the PropertySet objects
	isProxyFor = property(fget=lambda x: x._props["isProxyFor"].get(), fset=lambda x,y : x._props["isProxyFor"].set(y), fdel=None, doc=propDocs["isProxyFor"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___ContinuousTimeLine(tl___TimeLine):
	"""
	tl:ContinuousTimeLine
	A continuous timeline, like the universal one, or the one backing an analog signal
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tl___TimeLine.__init__(self)
		self._initialised = False
		self.shortname = "ContinuousTimeLine"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#ContinuousTimeLine"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___PhysicalTimeLine(tl___ContinuousTimeLine):
	"""
	tl:PhysicalTimeLine
	A "physical" time-line (the universal time line (UTC)) is an instance of this class. Other time zones consists in instances of this class as well, with a "shifting" time line map relating them to the universal time line map.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tl___ContinuousTimeLine.__init__(self)
		self._initialised = False
		self.shortname = "PhysicalTimeLine"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#PhysicalTimeLine"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___UTInterval(rdfs___Resource):
	"""
	tl:UTInterval
	an interval defined on the universal time line
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "UTInterval"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#UTInterval"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___Context(ces___NFP):
	"""
	ces:Context
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___NFP.__init__(self)
		self._initialised = False
		self.shortname = "Context"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#Context"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___PrimitiveEventService(ces___EventService):
	"""
	ces:PrimitiveEventService
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___EventService.__init__(self)
		self._initialised = False
		self.shortname = "PrimitiveEventService"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["presents"] = PropertySet("presents","http://www.daml.org/services/owl-s/1.2/Service.owl#presents", ces___EventProfile, False)
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#PrimitiveEventService"


	# Python class properties to wrap the PropertySet objects
	presents = property(fget=lambda x: x._props["presents"].get(), fset=lambda x,y : x._props["presents"].set(y), fdel=None, doc=propDocs["presents"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class DUL___Quality(rdfs___Resource):
	"""
	DUL:Quality
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Quality"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.loa-cnr.it/ontologies/DUL.owl#Quality"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Activity(rdfs___Resource):
	"""
	prov:Activity
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Activity"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["actedOnBehalfOf"] = PropertySet("actedOnBehalfOf","http://www.w3.org/ns/prov#actedOnBehalfOf", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["atLocation"] = PropertySet("atLocation","http://www.w3.org/ns/prov#atLocation", prov___Location, False)
		self._props["endedAtTime"] = PropertySet("endedAtTime","http://www.w3.org/ns/prov#endedAtTime", str, False)
		self._props["generated"] = PropertySet("generated","http://www.w3.org/ns/prov#generated", (prov___Entity,sao___StreamData,sao___StreamAnalysis), False)
		self._props["hadMember"] = PropertySet("hadMember","http://www.w3.org/ns/prov#hadMember", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["hadPrimarySource"] = PropertySet("hadPrimarySource","http://www.w3.org/ns/prov#hadPrimarySource", (prov___Entity,sao___StreamData,sao___StreamAnalysis), False)
		self._props["invalidated"] = PropertySet("invalidated","http://www.w3.org/ns/prov#invalidated", prov___Entity, False)
		self._props["qualifiedAssociation"] = PropertySet("qualifiedAssociation","http://www.w3.org/ns/prov#qualifiedAssociation", (prov___Association,prov___Influence), False)
		self._props["qualifiedAttribution"] = PropertySet("qualifiedAttribution","http://www.w3.org/ns/prov#qualifiedAttribution", (prov___Influence,prov___Attribution), False)
		self._props["qualifiedCommunication"] = PropertySet("qualifiedCommunication","http://www.w3.org/ns/prov#qualifiedCommunication", (prov___Influence,prov___Communication), False)
		self._props["qualifiedDelegation"] = PropertySet("qualifiedDelegation","http://www.w3.org/ns/prov#qualifiedDelegation", (prov___Delegation,prov___Influence), False)
		self._props["qualifiedDerivation"] = PropertySet("qualifiedDerivation","http://www.w3.org/ns/prov#qualifiedDerivation", (prov___Derivation,prov___Influence), False)
		self._props["qualifiedEnd"] = PropertySet("qualifiedEnd","http://www.w3.org/ns/prov#qualifiedEnd", (prov___End,prov___Influence), False)
		self._props["qualifiedGeneration"] = PropertySet("qualifiedGeneration","http://www.w3.org/ns/prov#qualifiedGeneration", (prov___Generation,prov___Influence), False)
		self._props["qualifiedInfluence"] = PropertySet("qualifiedInfluence","http://www.w3.org/ns/prov#qualifiedInfluence", prov___Influence, False)
		self._props["qualifiedInvalidation"] = PropertySet("qualifiedInvalidation","http://www.w3.org/ns/prov#qualifiedInvalidation", (prov___Invalidation,prov___Influence), False)
		self._props["qualifiedPrimarySource"] = PropertySet("qualifiedPrimarySource","http://www.w3.org/ns/prov#qualifiedPrimarySource", (prov___PrimarySource,prov___Influence), False)
		self._props["qualifiedQuotation"] = PropertySet("qualifiedQuotation","http://www.w3.org/ns/prov#qualifiedQuotation", (prov___Quotation,prov___Influence), False)
		self._props["qualifiedRevision"] = PropertySet("qualifiedRevision","http://www.w3.org/ns/prov#qualifiedRevision", (prov___Revision,prov___Influence), False)
		self._props["qualifiedStart"] = PropertySet("qualifiedStart","http://www.w3.org/ns/prov#qualifiedStart", (prov___Influence,prov___Start), False)
		self._props["qualifiedUsage"] = PropertySet("qualifiedUsage","http://www.w3.org/ns/prov#qualifiedUsage", (prov___Influence,prov___Usage), False)
		self._props["startedAtTime"] = PropertySet("startedAtTime","http://www.w3.org/ns/prov#startedAtTime", str, False)
		self._props["used"] = PropertySet("used","http://www.w3.org/ns/prov#used", (prov___Entity,sao___StreamData,prov___Activity,sao___StreamAnalysis,prov___Agent), False)
		self._props["wasAssociatedWith"] = PropertySet("wasAssociatedWith","http://www.w3.org/ns/prov#wasAssociatedWith", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["wasAttributedTo"] = PropertySet("wasAttributedTo","http://www.w3.org/ns/prov#wasAttributedTo", (ssn___Property,prov___Entity,ssn___Sensor,prov___Agent,prov___Activity), False)
		self._props["wasDerivedFrom"] = PropertySet("wasDerivedFrom","http://www.w3.org/ns/prov#wasDerivedFrom", (prov___Entity,sao___StreamData,prov___Activity,sao___StreamAnalysis,prov___Agent), False)
		self._props["wasEndedBy"] = PropertySet("wasEndedBy","http://www.w3.org/ns/prov#wasEndedBy", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["wasGeneratedBy"] = PropertySet("wasGeneratedBy","http://www.w3.org/ns/prov#wasGeneratedBy", (prov___Entity,sao___StreamEvent,prov___Activity,prov___Agent), False)
		self._props["wasInfluencedBy"] = PropertySet("wasInfluencedBy","http://www.w3.org/ns/prov#wasInfluencedBy", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["wasInformedBy"] = PropertySet("wasInformedBy","http://www.w3.org/ns/prov#wasInformedBy", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["wasInvalidatedBy"] = PropertySet("wasInvalidatedBy","http://www.w3.org/ns/prov#wasInvalidatedBy", (prov___Entity,prov___Agent,prov___Activity), False)
		self._props["wasQuotedFrom"] = PropertySet("wasQuotedFrom","http://www.w3.org/ns/prov#wasQuotedFrom", (prov___Entity,sao___StreamData,sao___StreamAnalysis), False)
		self._props["wasRevisionOf"] = PropertySet("wasRevisionOf","http://www.w3.org/ns/prov#wasRevisionOf", (prov___Entity,sao___StreamData,sao___StreamAnalysis), False)
		self._props["wasStartedBy"] = PropertySet("wasStartedBy","http://www.w3.org/ns/prov#wasStartedBy", (prov___Entity,prov___Agent,prov___Activity), False)
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Activity"


	# Python class properties to wrap the PropertySet objects
	actedOnBehalfOf = property(fget=lambda x: x._props["actedOnBehalfOf"].get(), fset=lambda x,y : x._props["actedOnBehalfOf"].set(y), fdel=None, doc=propDocs["actedOnBehalfOf"])
	atLocation = property(fget=lambda x: x._props["atLocation"].get(), fset=lambda x,y : x._props["atLocation"].set(y), fdel=None, doc=propDocs["atLocation"])
	endedAtTime = property(fget=lambda x: x._props["endedAtTime"].get(), fset=lambda x,y : x._props["endedAtTime"].set(y), fdel=None, doc=propDocs["endedAtTime"])
	generated = property(fget=lambda x: x._props["generated"].get(), fset=lambda x,y : x._props["generated"].set(y), fdel=None, doc=propDocs["generated"])
	hadMember = property(fget=lambda x: x._props["hadMember"].get(), fset=lambda x,y : x._props["hadMember"].set(y), fdel=None, doc=propDocs["hadMember"])
	hadPrimarySource = property(fget=lambda x: x._props["hadPrimarySource"].get(), fset=lambda x,y : x._props["hadPrimarySource"].set(y), fdel=None, doc=propDocs["hadPrimarySource"])
	invalidated = property(fget=lambda x: x._props["invalidated"].get(), fset=lambda x,y : x._props["invalidated"].set(y), fdel=None, doc=propDocs["invalidated"])
	qualifiedAssociation = property(fget=lambda x: x._props["qualifiedAssociation"].get(), fset=lambda x,y : x._props["qualifiedAssociation"].set(y), fdel=None, doc=propDocs["qualifiedAssociation"])
	qualifiedAttribution = property(fget=lambda x: x._props["qualifiedAttribution"].get(), fset=lambda x,y : x._props["qualifiedAttribution"].set(y), fdel=None, doc=propDocs["qualifiedAttribution"])
	qualifiedCommunication = property(fget=lambda x: x._props["qualifiedCommunication"].get(), fset=lambda x,y : x._props["qualifiedCommunication"].set(y), fdel=None, doc=propDocs["qualifiedCommunication"])
	qualifiedDelegation = property(fget=lambda x: x._props["qualifiedDelegation"].get(), fset=lambda x,y : x._props["qualifiedDelegation"].set(y), fdel=None, doc=propDocs["qualifiedDelegation"])
	qualifiedDerivation = property(fget=lambda x: x._props["qualifiedDerivation"].get(), fset=lambda x,y : x._props["qualifiedDerivation"].set(y), fdel=None, doc=propDocs["qualifiedDerivation"])
	qualifiedEnd = property(fget=lambda x: x._props["qualifiedEnd"].get(), fset=lambda x,y : x._props["qualifiedEnd"].set(y), fdel=None, doc=propDocs["qualifiedEnd"])
	qualifiedGeneration = property(fget=lambda x: x._props["qualifiedGeneration"].get(), fset=lambda x,y : x._props["qualifiedGeneration"].set(y), fdel=None, doc=propDocs["qualifiedGeneration"])
	qualifiedInfluence = property(fget=lambda x: x._props["qualifiedInfluence"].get(), fset=lambda x,y : x._props["qualifiedInfluence"].set(y), fdel=None, doc=propDocs["qualifiedInfluence"])
	qualifiedInvalidation = property(fget=lambda x: x._props["qualifiedInvalidation"].get(), fset=lambda x,y : x._props["qualifiedInvalidation"].set(y), fdel=None, doc=propDocs["qualifiedInvalidation"])
	qualifiedPrimarySource = property(fget=lambda x: x._props["qualifiedPrimarySource"].get(), fset=lambda x,y : x._props["qualifiedPrimarySource"].set(y), fdel=None, doc=propDocs["qualifiedPrimarySource"])
	qualifiedQuotation = property(fget=lambda x: x._props["qualifiedQuotation"].get(), fset=lambda x,y : x._props["qualifiedQuotation"].set(y), fdel=None, doc=propDocs["qualifiedQuotation"])
	qualifiedRevision = property(fget=lambda x: x._props["qualifiedRevision"].get(), fset=lambda x,y : x._props["qualifiedRevision"].set(y), fdel=None, doc=propDocs["qualifiedRevision"])
	qualifiedStart = property(fget=lambda x: x._props["qualifiedStart"].get(), fset=lambda x,y : x._props["qualifiedStart"].set(y), fdel=None, doc=propDocs["qualifiedStart"])
	qualifiedUsage = property(fget=lambda x: x._props["qualifiedUsage"].get(), fset=lambda x,y : x._props["qualifiedUsage"].set(y), fdel=None, doc=propDocs["qualifiedUsage"])
	startedAtTime = property(fget=lambda x: x._props["startedAtTime"].get(), fset=lambda x,y : x._props["startedAtTime"].set(y), fdel=None, doc=propDocs["startedAtTime"])
	used = property(fget=lambda x: x._props["used"].get(), fset=lambda x,y : x._props["used"].set(y), fdel=None, doc=propDocs["used"])
	wasAssociatedWith = property(fget=lambda x: x._props["wasAssociatedWith"].get(), fset=lambda x,y : x._props["wasAssociatedWith"].set(y), fdel=None, doc=propDocs["wasAssociatedWith"])
	wasAttributedTo = property(fget=lambda x: x._props["wasAttributedTo"].get(), fset=lambda x,y : x._props["wasAttributedTo"].set(y), fdel=None, doc=propDocs["wasAttributedTo"])
	wasDerivedFrom = property(fget=lambda x: x._props["wasDerivedFrom"].get(), fset=lambda x,y : x._props["wasDerivedFrom"].set(y), fdel=None, doc=propDocs["wasDerivedFrom"])
	wasEndedBy = property(fget=lambda x: x._props["wasEndedBy"].get(), fset=lambda x,y : x._props["wasEndedBy"].set(y), fdel=None, doc=propDocs["wasEndedBy"])
	wasGeneratedBy = property(fget=lambda x: x._props["wasGeneratedBy"].get(), fset=lambda x,y : x._props["wasGeneratedBy"].set(y), fdel=None, doc=propDocs["wasGeneratedBy"])
	wasInfluencedBy = property(fget=lambda x: x._props["wasInfluencedBy"].get(), fset=lambda x,y : x._props["wasInfluencedBy"].set(y), fdel=None, doc=propDocs["wasInfluencedBy"])
	wasInformedBy = property(fget=lambda x: x._props["wasInformedBy"].get(), fset=lambda x,y : x._props["wasInformedBy"].set(y), fdel=None, doc=propDocs["wasInformedBy"])
	wasInvalidatedBy = property(fget=lambda x: x._props["wasInvalidatedBy"].get(), fset=lambda x,y : x._props["wasInvalidatedBy"].set(y), fdel=None, doc=propDocs["wasInvalidatedBy"])
	wasQuotedFrom = property(fget=lambda x: x._props["wasQuotedFrom"].get(), fset=lambda x,y : x._props["wasQuotedFrom"].set(y), fdel=None, doc=propDocs["wasQuotedFrom"])
	wasRevisionOf = property(fget=lambda x: x._props["wasRevisionOf"].get(), fset=lambda x,y : x._props["wasRevisionOf"].set(y), fdel=None, doc=propDocs["wasRevisionOf"])
	wasStartedBy = property(fget=lambda x: x._props["wasStartedBy"].get(), fset=lambda x,y : x._props["wasStartedBy"].set(y), fdel=None, doc=propDocs["wasStartedBy"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Plan(prov___Entity):
	"""
	prov:Plan
	There exist no prescriptive requirement on the nature of plans, their representation, the actions or steps they consist of, or their intended goals. Since plans may evolve over time, it may become necessary to track their provenance, so plans themselves are entities. Representing the plan explicitly in the provenance can be useful for various tasks: for example, to validate the execution as represented in the provenance record, to manage expectation failures, or to provide explanations.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___Entity.__init__(self)
		self._initialised = False
		self.shortname = "Plan"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Plan"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___Document(rdfs___Resource):
	"""
	foaf:Document
	A document.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Document"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["primaryTopic"] = PropertySet("primaryTopic","http://xmlns.com/foaf/0.1/primaryTopic", owl___Thing, False)
		self._props["sha1"] = PropertySet("sha1","http://xmlns.com/foaf/0.1/sha1", None, False)
		self._props["topic"] = PropertySet("topic","http://xmlns.com/foaf/0.1/topic", owl___Thing, False)
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/Document"


	# Python class properties to wrap the PropertySet objects
	primaryTopic = property(fget=lambda x: x._props["primaryTopic"].get(), fset=lambda x,y : x._props["primaryTopic"].set(y), fdel=None, doc=propDocs["primaryTopic"])
	sha1 = property(fget=lambda x: x._props["sha1"].get(), fset=lambda x,y : x._props["sha1"].set(y), fdel=None, doc=propDocs["sha1"])
	topic = property(fget=lambda x: x._props["topic"].get(), fset=lambda x,y : x._props["topic"].set(y), fdel=None, doc=propDocs["topic"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___Distance(ces___Context):
	"""
	ct:Distance
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___Context.__init__(self)
		self._initialised = False
		self.shortname = "Distance"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#Distance"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___Place(ces___Context):
	"""
	ct:Place
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___Context.__init__(self)
		self._initialised = False
		self.shortname = "Place"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["locatesIn"] = PropertySet("locatesIn","http://ict-citypulse.eu/city#locatesIn", ct___Place, False)
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#Place"


	# Python class properties to wrap the PropertySet objects
	locatesIn = property(fget=lambda x: x._props["locatesIn"].get(), fset=lambda x,y : x._props["locatesIn"].set(y), fdel=None, doc=propDocs["locatesIn"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___SegTrafficReportService(ces___PrimitiveEventService):
	"""
	ct:SegTrafficReportService
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___PrimitiveEventService.__init__(self)
		self._initialised = False
		self.shortname = "SegTrafficReportService"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#SegTrafficReportService"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___Street(ct___Place):
	"""
	ct:Street
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ct___Place.__init__(self)
		self._initialised = False
		self.shortname = "Street"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#Street"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Confidentiality(qoi___Security):
	"""
	qoi:Confidentiality
	The degree to which information has attributes that ensure that it is only accessible and interpretable by authorized users in a specific context of use.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Security.__init__(self)
		self._initialised = False
		self.shortname = "Confidentiality"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Confidentiality"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___LicenceDefinition(qoi___Confidentiality):
	"""
	qoi:LicenceDefinition
	Reference to license class.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Confidentiality.__init__(self)
		self._initialised = False
		self.shortname = "LicenceDefinition"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#LicenceDefinition"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___MayBeUsed(qoi___Confidentiality):
	"""
	qoi:MayBeUsed
	Reference to permission class.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Confidentiality.__init__(self)
		self._initialised = False
		self.shortname = "MayBeUsed"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#MayBeUsed"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class sao___DiscreteCosineTransform(sao___StreamAnalysis):
	"""
	sao:DiscreteCosineTransform
	"""
	def __init__(self,URI=None):
		# Initialise parents
		sao___StreamAnalysis.__init__(self)
		self._initialised = False
		self.shortname = "DiscreteCosineTransform"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UNIS/sao/sao#DiscreteCosineTransform"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class sao___DiscreteWaveletTransform(sao___StreamAnalysis):
	"""
	sao:DiscreteWaveletTransform
	"""
	def __init__(self,URI=None):
		# Initialise parents
		sao___StreamAnalysis.__init__(self)
		self._initialised = False
		self.shortname = "DiscreteWaveletTransform"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UNIS/sao/sao#DiscreteWaveletTransform"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class sao___Median(sao___StreamAnalysis):
	"""
	sao:Median
	"""
	def __init__(self,URI=None):
		# Initialise parents
		sao___StreamAnalysis.__init__(self)
		self._initialised = False
		self.shortname = "Median"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UNIS/sao/sao#Median"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class sao___SensorSAX(sao___StreamAnalysis):
	"""
	sao:SensorSAX
	"""
	def __init__(self,URI=None):
		# Initialise parents
		sao___StreamAnalysis.__init__(self)
		self._initialised = False
		self.shortname = "SensorSAX"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["alphabetsize"] = PropertySet("alphabetsize","http://purl.oclc.org/NET/UNIS/sao/sao#alphabetsize", int, False)
		self._props["minwindowsize"] = PropertySet("minwindowsize","http://purl.oclc.org/NET/UNIS/sao/sao#minwindowsize", int, False)
		self._props["sensitivity"] = PropertySet("sensitivity","http://purl.oclc.org/NET/UNIS/sao/sao#sensitivity", float, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UNIS/sao/sao#SensorSAX"


	# Python class properties to wrap the PropertySet objects
	alphabetsize = property(fget=lambda x: x._props["alphabetsize"].get(), fset=lambda x,y : x._props["alphabetsize"].set(y), fdel=None, doc=propDocs["alphabetsize"])
	minwindowsize = property(fget=lambda x: x._props["minwindowsize"].get(), fset=lambda x,y : x._props["minwindowsize"].set(y), fdel=None, doc=propDocs["minwindowsize"])
	sensitivity = property(fget=lambda x: x._props["sensitivity"].get(), fset=lambda x,y : x._props["sensitivity"].set(y), fdel=None, doc=propDocs["sensitivity"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class sao___StreamEvent(prov___Activity):
	"""
	sao:StreamEvent
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___Activity.__init__(self)
		self._initialised = False
		self.shortname = "StreamEvent"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["Timestamp"] = PropertySet("Timestamp","http://purl.oclc.org/NET/UNIS/sao/sao#Timestamp", str, False)
		self._props["time"] = PropertySet("time","http://purl.oclc.org/NET/UNIS/sao/sao#time", (tl___Interval,tl___Instant), False)
		self._props["observationResultTime"] = PropertySet("observationResultTime","http://purl.oclc.org/NET/ssnx/ssn#observationResultTime", (tl___Interval,tl___Instant), False)
		self._props["observationSamplingTime"] = PropertySet("observationSamplingTime","http://purl.oclc.org/NET/ssnx/ssn#observationSamplingTime", (tl___Interval,tl___Instant), False)
		self._props["generated"] = PropertySet("generated","http://www.w3.org/ns/prov#generated", (prov___Entity,sao___StreamData,sao___StreamAnalysis), False)
		self._props["used"] = PropertySet("used","http://www.w3.org/ns/prov#used", (prov___Entity,sao___StreamData,prov___Activity,sao___StreamAnalysis,prov___Agent), False)
		self._props["wasAssociatedWith"] = PropertySet("wasAssociatedWith","http://www.w3.org/ns/prov#wasAssociatedWith", (prov___Entity,prov___Agent,prov___Activity), False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UNIS/sao/sao#StreamEvent"


	# Python class properties to wrap the PropertySet objects
	Timestamp = property(fget=lambda x: x._props["Timestamp"].get(), fset=lambda x,y : x._props["Timestamp"].set(y), fdel=None, doc=propDocs["Timestamp"])
	time = property(fget=lambda x: x._props["time"].get(), fset=lambda x,y : x._props["time"].set(y), fdel=None, doc=propDocs["time"])
	observationResultTime = property(fget=lambda x: x._props["observationResultTime"].get(), fset=lambda x,y : x._props["observationResultTime"].set(y), fdel=None, doc=propDocs["observationResultTime"])
	observationSamplingTime = property(fget=lambda x: x._props["observationSamplingTime"].get(), fset=lambda x,y : x._props["observationSamplingTime"].set(y), fdel=None, doc=propDocs["observationSamplingTime"])
	generated = property(fget=lambda x: x._props["generated"].get(), fset=lambda x,y : x._props["generated"].set(y), fdel=None, doc=propDocs["generated"])
	used = property(fget=lambda x: x._props["used"].get(), fset=lambda x,y : x._props["used"].set(y), fdel=None, doc=propDocs["used"])
	wasAssociatedWith = property(fget=lambda x: x._props["wasAssociatedWith"].get(), fset=lambda x,y : x._props["wasAssociatedWith"].set(y), fdel=None, doc=propDocs["wasAssociatedWith"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Property(DUL___Quality, prov___Agent):
	"""
	ssn:Property
	An observable Quality of an Event or Object.  That is, not a quality of an abstract entity as is also allowed by DUL's Quality, but rather an aspect of an entity that is intrinsic to and cannot exist without the entity and is observable by a sensor.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		DUL___Quality.__init__(self)
		prov___Agent.__init__(self)
		self._initialised = False
		self.shortname = "Property"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasMeasurementCapability"] = PropertySet("hasMeasurementCapability","http://purl.oclc.org/NET/ssnx/ssn#hasMeasurementCapability", (ssn___Property,ssn___MeasurementCapability), False)
		self._props["hasMeasurementProperty"] = PropertySet("hasMeasurementProperty","http://purl.oclc.org/NET/ssnx/ssn#hasMeasurementProperty", (ssn___Property,ssn___MeasurementProperty), False)
		self._props["hasOperatingProperty"] = PropertySet("hasOperatingProperty","http://purl.oclc.org/NET/ssnx/ssn#hasOperatingProperty", (ssn___Property,ssn___OperatingProperty), False)
		self._props["hasOperatingRange"] = PropertySet("hasOperatingRange","http://purl.oclc.org/NET/ssnx/ssn#hasOperatingRange", (ssn___Property,ssn___OperatingRange), False)
		self._props["hasProperty"] = PropertySet("hasProperty","http://purl.oclc.org/NET/ssnx/ssn#hasProperty", (ssn___Property,ssn___FeatureOfInterest), False)
		self._props["hasSurvivalProperty"] = PropertySet("hasSurvivalProperty","http://purl.oclc.org/NET/ssnx/ssn#hasSurvivalProperty", (ssn___Property,ssn___SurvivalProperty), False)
		self._props["hasSurvivalRange"] = PropertySet("hasSurvivalRange","http://purl.oclc.org/NET/ssnx/ssn#hasSurvivalRange", (ssn___Property,ssn___SurvivalRange), False)
		self._props["isPropertyOf"] = PropertySet("isPropertyOf","http://purl.oclc.org/NET/ssnx/ssn#isPropertyOf", (ssn___Property,ssn___FeatureOfInterest), False)
		self._props["qualityOfObservation"] = PropertySet("qualityOfObservation","http://purl.oclc.org/NET/ssnx/ssn#qualityOfObservation", ssn___Property, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Property"


	# Python class properties to wrap the PropertySet objects
	hasMeasurementCapability = property(fget=lambda x: x._props["hasMeasurementCapability"].get(), fset=lambda x,y : x._props["hasMeasurementCapability"].set(y), fdel=None, doc=propDocs["hasMeasurementCapability"])
	hasMeasurementProperty = property(fget=lambda x: x._props["hasMeasurementProperty"].get(), fset=lambda x,y : x._props["hasMeasurementProperty"].set(y), fdel=None, doc=propDocs["hasMeasurementProperty"])
	hasOperatingProperty = property(fget=lambda x: x._props["hasOperatingProperty"].get(), fset=lambda x,y : x._props["hasOperatingProperty"].set(y), fdel=None, doc=propDocs["hasOperatingProperty"])
	hasOperatingRange = property(fget=lambda x: x._props["hasOperatingRange"].get(), fset=lambda x,y : x._props["hasOperatingRange"].set(y), fdel=None, doc=propDocs["hasOperatingRange"])
	hasProperty = property(fget=lambda x: x._props["hasProperty"].get(), fset=lambda x,y : x._props["hasProperty"].set(y), fdel=None, doc=propDocs["hasProperty"])
	hasSurvivalProperty = property(fget=lambda x: x._props["hasSurvivalProperty"].get(), fset=lambda x,y : x._props["hasSurvivalProperty"].set(y), fdel=None, doc=propDocs["hasSurvivalProperty"])
	hasSurvivalRange = property(fget=lambda x: x._props["hasSurvivalRange"].get(), fset=lambda x,y : x._props["hasSurvivalRange"].set(y), fdel=None, doc=propDocs["hasSurvivalRange"])
	isPropertyOf = property(fget=lambda x: x._props["isPropertyOf"].get(), fset=lambda x,y : x._props["isPropertyOf"].set(y), fdel=None, doc=propDocs["isPropertyOf"])
	qualityOfObservation = property(fget=lambda x: x._props["qualityOfObservation"].get(), fset=lambda x,y : x._props["qualityOfObservation"].set(y), fdel=None, doc=propDocs["qualityOfObservation"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___SurvivalProperty(ssn___Property):
	"""
	ssn:SurvivalProperty
	An identifiable characteristic that represents the extent of the sensors useful life.  Might include for example total battery life or number of recharges, or, for sensors that are used only a fixed number of times, the number of observations that can be made before the sensing capability is depleted.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "SurvivalProperty"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#SurvivalProperty"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___SystemLifetime(ssn___SurvivalProperty):
	"""
	ssn:SystemLifetime
	Total useful life of a sensor/system (expressed as total life since manufacture, time in use, number of operations, etc.).
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___SurvivalProperty.__init__(self)
		self._initialised = False
		self.shortname = "SystemLifetime"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#SystemLifetime"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___RelativeTimeLine(tl___ContinuousTimeLine):
	"""
	tl:RelativeTimeLine
	Semi infinite time line...canonical coordinate system --> adressed through xsd:duration since the instant 0.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tl___ContinuousTimeLine.__init__(self)
		self._initialised = False
		self.shortname = "RelativeTimeLine"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#RelativeTimeLine"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ces___Filter(ces___EventPattern):
	"""
	ces:Filter
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ces___EventPattern.__init__(self)
		self._initialised = False
		self.shortname = "Filter"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["onEvent"] = PropertySet("onEvent","http://www.insight-centre.org/ces#onEvent", ces___EventService, False)
		self._props["onPayload"] = PropertySet("onPayload","http://www.insight-centre.org/ces#onPayload", ces___EventPayload, False)
		self._initialised = True
	classURI = "http://www.insight-centre.org/ces#Filter"


	# Python class properties to wrap the PropertySet objects
	onEvent = property(fget=lambda x: x._props["onEvent"].get(), fset=lambda x,y : x._props["onEvent"].set(y), fdel=None, doc=propDocs["onEvent"])
	onPayload = property(fget=lambda x: x._props["onPayload"].get(), fset=lambda x,y : x._props["onPayload"].set(y), fdel=None, doc=propDocs["onPayload"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tm___DateTimeInterval(tm___ProperInterval):
	"""
	tm:DateTimeInterval
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tm___ProperInterval.__init__(self)
		self._initialised = False
		self.shortname = "DateTimeInterval"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasDateTimeDescription"] = PropertySet("hasDateTimeDescription","http://www.w3.org/2006/time#hasDateTimeDescription", tm___DateTimeDescription, False)
		self._props["xsdDateTime"] = PropertySet("xsdDateTime","http://www.w3.org/2006/time#xsdDateTime", str, False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#DateTimeInterval"


	# Python class properties to wrap the PropertySet objects
	hasDateTimeDescription = property(fget=lambda x: x._props["hasDateTimeDescription"].get(), fset=lambda x,y : x._props["hasDateTimeDescription"].set(y), fdel=None, doc=propDocs["hasDateTimeDescription"])
	xsdDateTime = property(fget=lambda x: x._props["xsdDateTime"].get(), fset=lambda x,y : x._props["xsdDateTime"].set(y), fdel=None, doc=propDocs["xsdDateTime"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Quotation(prov___Derivation):
	"""
	prov:Quotation
	An instance of prov:Quotation provides additional descriptions about the binary prov:wasQuotedFrom relation from some taken prov:Entity from an earlier, larger prov:Entity. For example, :here_is_looking_at_you_kid prov:wasQuotedFrom :casablanca_script; prov:qualifiedQuotation [ a prov:Quotation; prov:entity :casablanca_script; :foo :bar ].
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___Derivation.__init__(self)
		self._initialised = False
		self.shortname = "Quotation"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Quotation"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___AirPollutionIndex(ssn___Property):
	"""
	ct:AirPollutionIndex
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "AirPollutionIndex"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#AirPollutionIndex"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___AverageSpeed(ssn___Property):
	"""
	ct:AverageSpeed
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "AverageSpeed"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#AverageSpeed"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___CauseArea(ssn___Property):
	"""
	ct:CauseArea
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "CauseArea"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#CauseArea"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___CurrentUpdate(ssn___Property):
	"""
	ct:CurrentUpdate
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "CurrentUpdate"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#CurrentUpdate"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___District(ct___Place):
	"""
	ct:District
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ct___Place.__init__(self)
		self._initialised = False
		self.shortname = "District"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#District"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___LevelOfInterest(ssn___Property):
	"""
	ct:LevelOfInterest
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "LevelOfInterest"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#LevelOfInterest"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___Node(ct___Place):
	"""
	ct:Node
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ct___Place.__init__(self)
		self._initialised = False
		self.shortname = "Node"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#Node"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___ParkingVacancy(ssn___Property):
	"""
	ct:ParkingVacancy
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "ParkingVacancy"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#ParkingVacancy"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___Rain(ssn___Property):
	"""
	ct:Rain
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "Rain"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#Rain"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___StreetVehicleCount(ssn___Property):
	"""
	ct:StreetVehicleCount
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "StreetVehicleCount"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#StreetVehicleCount"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___Temperature(ssn___Property):
	"""
	ct:Temperature
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "Temperature"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#Temperature"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___MayBePublished(qoi___Confidentiality):
	"""
	qoi:MayBePublished
	Reference to permission class.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Confidentiality.__init__(self)
		self._initialised = False
		self.shortname = "MayBePublished"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#MayBePublished"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class sao___DiscreteFourierTransform(sao___StreamAnalysis):
	"""
	sao:DiscreteFourierTransform
	"""
	def __init__(self,URI=None):
		# Initialise parents
		sao___StreamAnalysis.__init__(self)
		self._initialised = False
		self.shortname = "DiscreteFourierTransform"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UNIS/sao/sao#DiscreteFourierTransform"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class sao___PiecewiseAggregateApproximation(sao___StreamAnalysis):
	"""
	sao:PiecewiseAggregateApproximation
	"""
	def __init__(self,URI=None):
		# Initialise parents
		sao___StreamAnalysis.__init__(self)
		self._initialised = False
		self.shortname = "PiecewiseAggregateApproximation"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UNIS/sao/sao#PiecewiseAggregateApproximation"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class sao___StreamData(prov___Entity, ssn___Observation):
	"""
	sao:StreamData
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Observation.__init__(self)
		prov___Entity.__init__(self)
		self._initialised = False
		self.shortname = "StreamData"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasProvenance"] = PropertySet("hasProvenance","http://purl.oclc.org/NET/UASO/qoi#hasProvenance", prov___Agent, False)
		self._props["hasQuality"] = PropertySet("hasQuality","http://purl.oclc.org/NET/UASO/qoi#hasQuality", qoi___Quality, False)
		self._props["Timestamp"] = PropertySet("Timestamp","http://purl.oclc.org/NET/UNIS/sao/sao#Timestamp", str, False)
		self._props["computeby"] = PropertySet("computeby","http://purl.oclc.org/NET/UNIS/sao/sao#computeby", sao___StreamAnalysis, False)
		self._props["hasPoint"] = PropertySet("hasPoint","http://purl.oclc.org/NET/UNIS/sao/sao#hasPoint", sao___Point, False)
		self._props["hasSegment"] = PropertySet("hasSegment","http://purl.oclc.org/NET/UNIS/sao/sao#hasSegment", sao___Segment, False)
		self._props["hasUnitOfMeasurement"] = PropertySet("hasUnitOfMeasurement","http://purl.oclc.org/NET/UNIS/sao/sao#hasUnitOfMeasurement", muo___UnitOfMeasurement, False)
		self._props["nColumns"] = PropertySet("nColumns","http://purl.oclc.org/NET/UNIS/sao/sao#nColumns", int, False)
		self._props["nRows"] = PropertySet("nRows","http://purl.oclc.org/NET/UNIS/sao/sao#nRows", int, False)
		self._props["quality"] = PropertySet("quality","http://purl.oclc.org/NET/UNIS/sao/sao#quality", DUL___InformationEntity, False)
		self._props["samplesize"] = PropertySet("samplesize","http://purl.oclc.org/NET/UNIS/sao/sao#samplesize", int, False)
		self._props["samplingrate"] = PropertySet("samplingrate","http://purl.oclc.org/NET/UNIS/sao/sao#samplingrate", int, False)
		self._props["time"] = PropertySet("time","http://purl.oclc.org/NET/UNIS/sao/sao#time", (tl___Interval,tl___Instant), False)
		self._props["value"] = PropertySet("value","http://purl.oclc.org/NET/UNIS/sao/sao#value", str, False)
		self._props["observationResultTime"] = PropertySet("observationResultTime","http://purl.oclc.org/NET/ssnx/ssn#observationResultTime", (tl___Interval,tl___Instant), False)
		self._props["observationSamplingTime"] = PropertySet("observationSamplingTime","http://purl.oclc.org/NET/ssnx/ssn#observationSamplingTime", (tl___Interval,tl___Instant), False)
		self._props["wasAttributedTo"] = PropertySet("wasAttributedTo","http://www.w3.org/ns/prov#wasAttributedTo", (ssn___Property,prov___Entity,ssn___Sensor,prov___Agent,prov___Activity), False)
		self._props["wasGeneratedBy"] = PropertySet("wasGeneratedBy","http://www.w3.org/ns/prov#wasGeneratedBy", (prov___Entity,sao___StreamEvent,prov___Activity,prov___Agent), False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UNIS/sao/sao#StreamData"


	# Python class properties to wrap the PropertySet objects
	hasProvenance = property(fget=lambda x: x._props["hasProvenance"].get(), fset=lambda x,y : x._props["hasProvenance"].set(y), fdel=None, doc=propDocs["hasProvenance"])
	hasQuality = property(fget=lambda x: x._props["hasQuality"].get(), fset=lambda x,y : x._props["hasQuality"].set(y), fdel=None, doc=propDocs["hasQuality"])
	Timestamp = property(fget=lambda x: x._props["Timestamp"].get(), fset=lambda x,y : x._props["Timestamp"].set(y), fdel=None, doc=propDocs["Timestamp"])
	computeby = property(fget=lambda x: x._props["computeby"].get(), fset=lambda x,y : x._props["computeby"].set(y), fdel=None, doc=propDocs["computeby"])
	hasPoint = property(fget=lambda x: x._props["hasPoint"].get(), fset=lambda x,y : x._props["hasPoint"].set(y), fdel=None, doc=propDocs["hasPoint"])
	hasSegment = property(fget=lambda x: x._props["hasSegment"].get(), fset=lambda x,y : x._props["hasSegment"].set(y), fdel=None, doc=propDocs["hasSegment"])
	hasUnitOfMeasurement = property(fget=lambda x: x._props["hasUnitOfMeasurement"].get(), fset=lambda x,y : x._props["hasUnitOfMeasurement"].set(y), fdel=None, doc=propDocs["hasUnitOfMeasurement"])
	nColumns = property(fget=lambda x: x._props["nColumns"].get(), fset=lambda x,y : x._props["nColumns"].set(y), fdel=None, doc=propDocs["nColumns"])
	nRows = property(fget=lambda x: x._props["nRows"].get(), fset=lambda x,y : x._props["nRows"].set(y), fdel=None, doc=propDocs["nRows"])
	quality = property(fget=lambda x: x._props["quality"].get(), fset=lambda x,y : x._props["quality"].set(y), fdel=None, doc=propDocs["quality"])
	samplesize = property(fget=lambda x: x._props["samplesize"].get(), fset=lambda x,y : x._props["samplesize"].set(y), fdel=None, doc=propDocs["samplesize"])
	samplingrate = property(fget=lambda x: x._props["samplingrate"].get(), fset=lambda x,y : x._props["samplingrate"].set(y), fdel=None, doc=propDocs["samplingrate"])
	time = property(fget=lambda x: x._props["time"].get(), fset=lambda x,y : x._props["time"].set(y), fdel=None, doc=propDocs["time"])
	value = property(fget=lambda x: x._props["value"].get(), fset=lambda x,y : x._props["value"].set(y), fdel=None, doc=propDocs["value"])
	observationResultTime = property(fget=lambda x: x._props["observationResultTime"].get(), fset=lambda x,y : x._props["observationResultTime"].set(y), fdel=None, doc=propDocs["observationResultTime"])
	observationSamplingTime = property(fget=lambda x: x._props["observationSamplingTime"].get(), fset=lambda x,y : x._props["observationSamplingTime"].set(y), fdel=None, doc=propDocs["observationSamplingTime"])
	wasAttributedTo = property(fget=lambda x: x._props["wasAttributedTo"].get(), fset=lambda x,y : x._props["wasAttributedTo"].set(y), fdel=None, doc=propDocs["wasAttributedTo"])
	wasGeneratedBy = property(fget=lambda x: x._props["wasGeneratedBy"].get(), fset=lambda x,y : x._props["wasGeneratedBy"].set(y), fdel=None, doc=propDocs["wasGeneratedBy"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___BatteryLifetime(ssn___SurvivalProperty):
	"""
	ssn:BatteryLifetime
	Total useful life of a battery.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___SurvivalProperty.__init__(self)
		self._initialised = False
		self.shortname = "BatteryLifetime"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#BatteryLifetime"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___MeasurementCapability(ssn___Property):
	"""
	ssn:MeasurementCapability
	Collects together measurement properties (accuracy, range, precision, etc) and the environmental conditions in which those properties hold, representing a specification of a sensor's capability in those conditions.

The conditions specified here are those that affect the measurement properties, while those in OperatingRange represent the sensor's standard operating conditions, including conditions that don't affect the observations.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "MeasurementCapability"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["forProperty"] = PropertySet("forProperty","http://purl.oclc.org/NET/ssnx/ssn#forProperty", ssn___Property, False)
		self._props["hasMeasurementProperty"] = PropertySet("hasMeasurementProperty","http://purl.oclc.org/NET/ssnx/ssn#hasMeasurementProperty", (ssn___Property,ssn___MeasurementProperty), False)
		self._props["inCondition"] = PropertySet("inCondition","http://purl.oclc.org/NET/ssnx/ssn#inCondition", ssn___Condition, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#MeasurementCapability"


	# Python class properties to wrap the PropertySet objects
	forProperty = property(fget=lambda x: x._props["forProperty"].get(), fset=lambda x,y : x._props["forProperty"].set(y), fdel=None, doc=propDocs["forProperty"])
	hasMeasurementProperty = property(fget=lambda x: x._props["hasMeasurementProperty"].get(), fset=lambda x,y : x._props["hasMeasurementProperty"].set(y), fdel=None, doc=propDocs["hasMeasurementProperty"])
	inCondition = property(fget=lambda x: x._props["inCondition"].get(), fset=lambda x,y : x._props["inCondition"].set(y), fdel=None, doc=propDocs["inCondition"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___OperatingProperty(ssn___Property):
	"""
	ssn:OperatingProperty
	An identifiable characteristic of the environmental and other conditions in which the sensor is intended to operate.  May include power ranges, power sources, standard configurations, attachments and the like.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "OperatingProperty"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#OperatingProperty"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___SurvivalRange(ssn___Property):
	"""
	ssn:SurvivalRange
	The conditions a sensor can be exposed to without damage: i.e., the sensor continues to operate as defined using MeasurementCapability.  If, however, the SurvivalRange is exceeded, the sensor is 'damaged' and MeasurementCapability specifications may no longer hold.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "SurvivalRange"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasSurvivalProperty"] = PropertySet("hasSurvivalProperty","http://purl.oclc.org/NET/ssnx/ssn#hasSurvivalProperty", (ssn___Property,ssn___SurvivalProperty), False)
		self._props["inCondition"] = PropertySet("inCondition","http://purl.oclc.org/NET/ssnx/ssn#inCondition", ssn___Condition, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#SurvivalRange"


	# Python class properties to wrap the PropertySet objects
	hasSurvivalProperty = property(fget=lambda x: x._props["hasSurvivalProperty"].get(), fset=lambda x,y : x._props["hasSurvivalProperty"].set(y), fdel=None, doc=propDocs["hasSurvivalProperty"])
	inCondition = property(fget=lambda x: x._props["inCondition"].get(), fset=lambda x,y : x._props["inCondition"].set(y), fdel=None, doc=propDocs["inCondition"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class owlssc___ServiceCategory(rdfs___Resource):
	"""
	owlssc:ServiceCategory
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "ServiceCategory"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["serviceCategoryName"] = PropertySet("serviceCategoryName","http://www.daml.org/services/owl-s/1.2/ServiceCategory.owl#serviceCategoryName", str, False)
		self._initialised = True
	classURI = "http://www.daml.org/services/owl-s/1.2/ServiceCategory.owl#ServiceCategory"


	# Python class properties to wrap the PropertySet objects
	serviceCategoryName = property(fget=lambda x: x._props["serviceCategoryName"].get(), fset=lambda x,y : x._props["serviceCategoryName"].set(y), fdel=None, doc=propDocs["serviceCategoryName"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___Collection(prov___Entity):
	"""
	prov:Collection
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___Entity.__init__(self)
		self._initialised = False
		self.shortname = "Collection"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hadMember"] = PropertySet("hadMember","http://www.w3.org/ns/prov#hadMember", (prov___Entity,prov___Agent,prov___Activity), False)
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#Collection"


	# Python class properties to wrap the PropertySet objects
	hadMember = property(fget=lambda x: x._props["hadMember"].get(), fset=lambda x,y : x._props["hadMember"].set(y), fdel=None, doc=propDocs["hadMember"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___PersonalProfileDocument(foaf___Document):
	"""
	foaf:PersonalProfileDocument
	A personal profile RDF document.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___Document.__init__(self)
		self._initialised = False
		self.shortname = "PersonalProfileDocument"
		self.URI = URI
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/PersonalProfileDocument"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___AirPollutionLevel(ssn___Property):
	"""
	ct:AirPollutionLevel
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "AirPollutionLevel"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#AirPollutionLevel"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___City(ct___Place):
	"""
	ct:City
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ct___Place.__init__(self)
		self._initialised = False
		self.shortname = "City"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#City"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___EstimatedTime(ssn___Property):
	"""
	ct:EstimatedTime
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "EstimatedTime"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#EstimatedTime"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___ParkingCapacity(ssn___Property):
	"""
	ct:ParkingCapacity
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "ParkingCapacity"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#ParkingCapacity"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___Status(ssn___Property):
	"""
	ct:Status
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "Status"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#Status"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___WindSpeed(ssn___Property):
	"""
	ct:WindSpeed
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "WindSpeed"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#WindSpeed"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Precision(qoi___Accuracy):
	"""
	qoi:Precision
	Category for parameters describing the precision.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Accuracy.__init__(self)
		self._initialised = False
		self.shortname = "Precision"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Precision"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class sao___Mean(sao___StreamAnalysis):
	"""
	sao:Mean
	"""
	def __init__(self,URI=None):
		# Initialise parents
		sao___StreamAnalysis.__init__(self)
		self._initialised = False
		self.shortname = "Mean"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UNIS/sao/sao#Mean"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class sao___Segment(sao___StreamData):
	"""
	sao:Segment
	"""
	def __init__(self,URI=None):
		# Initialise parents
		sao___StreamData.__init__(self)
		self._initialised = False
		self.shortname = "Segment"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["value"] = PropertySet("value","http://purl.oclc.org/NET/UNIS/sao/sao#value", str, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UNIS/sao/sao#Segment"


	# Python class properties to wrap the PropertySet objects
	value = property(fget=lambda x: x._props["value"].get(), fset=lambda x,y : x._props["value"].set(y), fdel=None, doc=propDocs["value"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Condition(ssn___Property):
	"""
	ssn:Condition
	Used to specify ranges for qualities that act as conditions on a system/sensor's operation.  For example, wind speed of 10-60m/s is expressed as a condition linking a quality, wind speed, a unit of measurement, metres per second, and a set of values, 10-60, and may be used as the condition on a MeasurementProperty, for example, to state that a sensor has a particular accuracy in that condition.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "Condition"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Condition"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___MaintenanceSchedule(ssn___OperatingProperty):
	"""
	ssn:MaintenanceSchedule
	Schedule of maintenance for a system/sensor in the specified conditions.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___OperatingProperty.__init__(self)
		self._initialised = False
		self.shortname = "MaintenanceSchedule"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#MaintenanceSchedule"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___OperatingPowerRange(ssn___OperatingProperty):
	"""
	ssn:OperatingPowerRange
	Power range in which system/sensor is expected to operate.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___OperatingProperty.__init__(self)
		self._initialised = False
		self.shortname = "OperatingPowerRange"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#OperatingPowerRange"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tl___OriginMap(tl___TimeLineMap):
	"""
	tl:OriginMap
	A timeline map linking a physical timeline to a relative one (originating at some point on the physical timeline)
	"""
	def __init__(self,URI=None):
		# Initialise parents
		tl___TimeLineMap.__init__(self)
		self._initialised = False
		self.shortname = "OriginMap"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["domainTimeLine"] = PropertySet("domainTimeLine","http://purl.org/NET/c4dm/timeline.owl#domainTimeLine", tl___TimeLine, False)
		self._props["origin"] = PropertySet("origin","http://purl.org/NET/c4dm/timeline.owl#origin", str, False)
		self._props["rangeTimeLine"] = PropertySet("rangeTimeLine","http://purl.org/NET/c4dm/timeline.owl#rangeTimeLine", tl___TimeLine, False)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#OriginMap"


	# Python class properties to wrap the PropertySet objects
	domainTimeLine = property(fget=lambda x: x._props["domainTimeLine"].get(), fset=lambda x,y : x._props["domainTimeLine"].set(y), fdel=None, doc=propDocs["domainTimeLine"])
	origin = property(fget=lambda x: x._props["origin"].get(), fset=lambda x,y : x._props["origin"].set(y), fdel=None, doc=propDocs["origin"])
	rangeTimeLine = property(fget=lambda x: x._props["rangeTimeLine"].get(), fset=lambda x,y : x._props["rangeTimeLine"].set(y), fdel=None, doc=propDocs["rangeTimeLine"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class prov___EmptyCollection(prov___Collection):
	"""
	prov:EmptyCollection
	"""
	def __init__(self,URI=None):
		# Initialise parents
		prov___Collection.__init__(self)
		self._initialised = False
		self.shortname = "EmptyCollection"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/ns/prov#EmptyCollection"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___Category(ssn___Property):
	"""
	ct:Category
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "Category"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#Category"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___MeasuredTime(ssn___Property):
	"""
	ct:MeasuredTime
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "MeasuredTime"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#MeasuredTime"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___SubCategory(ssn___Property):
	"""
	ct:SubCategory
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "SubCategory"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#SubCategory"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Resolution(qoi___Precision):
	"""
	qoi:Resolution
	Resolution detail for the measured value. The Resoultion cannot be negative.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Precision.__init__(self)
		self._initialised = False
		self.shortname = "Resolution"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Resolution"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class muo___MetricUnit(muo___UnitOfMeasurement):
	"""
	muo:MetricUnit
	FIX
	"""
	def __init__(self,URI=None):
		# Initialise parents
		muo___UnitOfMeasurement.__init__(self)
		self._initialised = False
		self.shortname = "MetricUnit"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/muo/muo#MetricUnit"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___MeasurementProperty(ssn___Property):
	"""
	ssn:MeasurementProperty
	An identifiable and observable characteristic of a sensor's observations or ability to make observations.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "MeasurementProperty"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#MeasurementProperty"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___OperatingRange(ssn___Property):
	"""
	ssn:OperatingRange
	The environmental conditions and characteristics of a system/sensor's normal operating environment.  Can be used to specify for example the standard environmental conditions in which the sensor is expected to operate (a Condition with no OperatingProperty), or how the environmental and other operating properties relate: i.e., that the maintenance schedule or power requirements differ according to the conditions.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "OperatingRange"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasOperatingProperty"] = PropertySet("hasOperatingProperty","http://purl.oclc.org/NET/ssnx/ssn#hasOperatingProperty", (ssn___Property,ssn___OperatingProperty), False)
		self._props["inCondition"] = PropertySet("inCondition","http://purl.oclc.org/NET/ssnx/ssn#inCondition", ssn___Condition, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#OperatingRange"


	# Python class properties to wrap the PropertySet objects
	hasOperatingProperty = property(fget=lambda x: x._props["hasOperatingProperty"].get(), fset=lambda x,y : x._props["hasOperatingProperty"].set(y), fdel=None, doc=propDocs["hasOperatingProperty"])
	inCondition = property(fget=lambda x: x._props["inCondition"].get(), fset=lambda x,y : x._props["inCondition"].set(y), fdel=None, doc=propDocs["inCondition"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Resolution(ssn___MeasurementProperty):
	"""
	ssn:Resolution
	The smallest difference in the value of a quality being observed that would result in perceptably different values of observation results.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___MeasurementProperty.__init__(self)
		self._initialised = False
		self.shortname = "Resolution"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Resolution"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Selectivity(ssn___MeasurementProperty):
	"""
	ssn:Selectivity
	Selectivity is a property of a sensor whereby it provides observed values for one or more qualities such that the values of each quality are independent of other qualities in the phenomenon, body, or substance being investigated.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___MeasurementProperty.__init__(self)
		self._initialised = False
		self.shortname = "Selectivity"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Selectivity"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Sensitivity(ssn___MeasurementProperty):
	"""
	ssn:Sensitivity
	Sensitivity is the quotient of the change in a result of sensor and the corresponding change in a value of a quality being observed.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___MeasurementProperty.__init__(self)
		self._initialised = False
		self.shortname = "Sensitivity"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Sensitivity"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___DisruptionID(ssn___Property):
	"""
	ct:DisruptionID
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "DisruptionID"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#DisruptionID"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class qoi___Deviation(qoi___Precision):
	"""
	qoi:Deviation
	The maximum percentage of deviation from the real value. Deviation cannot be negative and only reach 1 (0-100%)
	"""
	def __init__(self,URI=None):
		# Initialise parents
		qoi___Precision.__init__(self)
		self._initialised = False
		self.shortname = "Deviation"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UASO/qoi#Deviation"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Accuracy(ssn___MeasurementProperty):
	"""
	ssn:Accuracy
	The closeness of agreement between the value of an observation and the true value of the observed quality.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___MeasurementProperty.__init__(self)
		self._initialised = False
		self.shortname = "Accuracy"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Accuracy"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Drift(ssn___MeasurementProperty):
	"""
	ssn:Drift
	A, continuous or incremental, change in the reported values of observations over time for an unchanging quality.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___MeasurementProperty.__init__(self)
		self._initialised = False
		self.shortname = "Drift"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Drift"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Latency(ssn___MeasurementProperty):
	"""
	ssn:Latency
	The time between a request for an observation and the sensor providing a result.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___MeasurementProperty.__init__(self)
		self._initialised = False
		self.shortname = "Latency"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Latency"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Precision(ssn___MeasurementProperty):
	"""
	ssn:Precision
	The closeness of agreement between replicate observations on an unchanged or similar quality value: i.e., a measure of a sensor's ability to consitently reproduce an observation.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___MeasurementProperty.__init__(self)
		self._initialised = False
		self.shortname = "Precision"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Precision"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class DUL___DesignedArtifact(rdfs___Resource):
	"""
	DUL:DesignedArtifact
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "DesignedArtifact"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.loa-cnr.it/ontologies/DUL.owl#DesignedArtifact"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ct___ParkingVehicleCount(ssn___Property):
	"""
	ct:ParkingVehicleCount
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Property.__init__(self)
		self._initialised = False
		self.shortname = "ParkingVehicleCount"
		self.URI = URI
		self._initialised = True
	classURI = "http://ict-citypulse.eu/city#ParkingVehicleCount"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___DetectionLimit(ssn___MeasurementProperty):
	"""
	ssn:DetectionLimit
	An observed value for which the probability of falsely claiming the absence of a component in a material is , given a probability of falsely claiming its presence.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___MeasurementProperty.__init__(self)
		self._initialised = False
		self.shortname = "DetectionLimit"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#DetectionLimit"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Frequency(ssn___MeasurementProperty):
	"""
	ssn:Frequency
	The smallest possible time between one observation and the next.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___MeasurementProperty.__init__(self)
		self._initialised = False
		self.shortname = "Frequency"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Frequency"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___ResponseTime(ssn___MeasurementProperty):
	"""
	ssn:ResponseTime
	The time between a (step) change inthe value of an observed quality and a sensor (possibly with specified error) 'settling' on an observed value.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___MeasurementProperty.__init__(self)
		self._initialised = False
		self.shortname = "ResponseTime"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#ResponseTime"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class sao___Point(sao___StreamData):
	"""
	sao:Point
	"""
	def __init__(self,URI=None):
		# Initialise parents
		sao___StreamData.__init__(self)
		self._initialised = False
		self.shortname = "Point"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["value"] = PropertySet("value","http://purl.oclc.org/NET/UNIS/sao/sao#value", str, False)
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/UNIS/sao/sao#Point"


	# Python class properties to wrap the PropertySet objects
	value = property(fget=lambda x: x._props["value"].get(), fset=lambda x,y : x._props["value"].set(y), fdel=None, doc=propDocs["value"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___MeasurementRange(ssn___MeasurementProperty):
	"""
	ssn:MeasurementRange
	The set of values that the sensor can return as the result of an observation under the defined conditions with the defined measurement properties.  (If no conditions are specified or the conditions do not specify a range for the observed qualities, the measurement range is to be taken as the condition for the observed qualities.)
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___MeasurementProperty.__init__(self)
		self._initialised = False
		self.shortname = "MeasurementRange"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#MeasurementRange"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___Device(DUL___DesignedArtifact, ssn___System):
	"""
	ssn:Device
	A device is a physical piece of technology - a system in a box. Devices may of course be built of smaller devices and software components (i.e. systems have components).
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___System.__init__(self)
		DUL___DesignedArtifact.__init__(self)
		self._initialised = False
		self.shortname = "Device"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#Device"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class ssn___SensingDevice(ssn___Device, ssn___Sensor):
	"""
	ssn:SensingDevice
	A sensing device is a device that implements sensing.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		ssn___Device.__init__(self)
		ssn___Sensor.__init__(self)
		self._initialised = False
		self.shortname = "SensingDevice"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.oclc.org/NET/ssnx/ssn#SensingDevice"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr


# ======================= Instance Definitions ======================= 

tm___Friday = ns1___DayOfWeek("http://www.w3.org/2006/time#Friday")
tm___Monday = ns1___DayOfWeek("http://www.w3.org/2006/time#Monday")
tm___Saturday = ns1___DayOfWeek("http://www.w3.org/2006/time#Saturday")
tm___Sunday = ns1___DayOfWeek("http://www.w3.org/2006/time#Sunday")
tm___Thursday = ns1___DayOfWeek("http://www.w3.org/2006/time#Thursday")
tm___Tuesday = ns1___DayOfWeek("http://www.w3.org/2006/time#Tuesday")
tm___Wednesday = ns1___DayOfWeek("http://www.w3.org/2006/time#Wednesday")

tm___unitDay = ns1___TemporalUnit("http://www.w3.org/2006/time#unitDay")
tm___unitHour = ns1___TemporalUnit("http://www.w3.org/2006/time#unitHour")
tm___unitMinute = ns1___TemporalUnit("http://www.w3.org/2006/time#unitMinute")
tm___unitMonth = ns1___TemporalUnit("http://www.w3.org/2006/time#unitMonth")
tm___unitSecond = ns1___TemporalUnit("http://www.w3.org/2006/time#unitSecond")
tm___unitWeek = ns1___TemporalUnit("http://www.w3.org/2006/time#unitWeek")
tm___unitYear = ns1___TemporalUnit("http://www.w3.org/2006/time#unitYear")

tl___universaltimeline = tl___PhysicalTimeLine("http://purl.org/NET/c4dm/timeline.owl#universaltimeline")
tl___universaltimeline.description = \
"""The timeline one can addresss "the 1st of July, 2007"."""



namespaceBindings = {"owl":"http://www.w3.org/2002/07/owl#","sao":"http://purl.oclc.org/NET/UNIS/sao/sao#","vs":"http://www.w3.org/2003/06/sw-vocab-status/ns#","skos":"http://www.w3.org/2004/02/skos/core#","qoi":"http://purl.oclc.org/NET/UASO/qoi#","ct":"http://ict-citypulse.eu/city#","xml":"http://www.w3.org/XML/1998/namespace","owlssc":"http://www.daml.org/services/owl-s/1.2/ServiceCategory.owl#","dc":"http://purl.org/dc/terms/","rdfs":"http://www.w3.org/2000/01/rdf-schema#","wot":"http://xmlns.com/wot/0.1/","owlssp":"http://www.daml.org/services/owl-s/1.2/Profile.owl#","tl":"http://purl.org/NET/c4dm/timeline.owl#","daml":"http://www.daml.org/2001/03/daml+oil#","muo":"http://purl.oclc.org/NET/muo/muo#","foaf":"http://xmlns.com/foaf/0.1/","DUL":"http://www.loa-cnr.it/ontologies/DUL.owl#","time":"http://www.w3.org/2006/time#","dc":"http://purl.org/dc/elements/1.1/","ssn":"http://purl.oclc.org/NET/ssnx/ssn#","ces":"http://www.insight-centre.org/ces#","owlssrp":"http://www.daml.org/services/owl-s/1.2/ServiceParameter.owl#","tzont":"http://www.w3.org/2006/timezone#","geo":"http://www.w3.org/2003/01/geo/wgs84_pos#","owlss":"http://www.daml.org/services/owl-s/1.2/Service.owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","xsd":"http://www.w3.org/2001/XMLSchema#","prov":"http://www.w3.org/ns/prov#","owlsg":"http://www.daml.org/services/owl-s/1.2/Grounding.owl#"}



# =======================       Clean Up       ======================= 
del objToStr, propDocs
