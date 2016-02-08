import chardet
import copy


__author__ = 'Thorben Iggena (t.iggena@hs-osnabrueck.de)'

 
def getType(strType):
    if "." in strType:
        splittedType = strType.split(".")
        moduleName = ".".join(splittedType[:-1])
        importedModule = __import__(moduleName)
        return getattr(importedModule, splittedType[1])
    else:
        import __builtin__
        return getattr(__builtin__, strType)

def nice_filename(org):
    """
    Converts a string to a valid filename by removing any special characters
    :param org: the original string
    :return: a string usable as filename
    """
    return "".join([c for c in org if c.isalpha() or c.isdigit() or c == ' ']).rstrip()

def unicode2ascii(string):
    if not isinstance(string, str) and not isinstance(string, unicode):
        # not a string, nothing to do
        return string
    try:
        string = string.encode('ascii', 'xmlcharrefreplace')
    except UnicodeDecodeError:
        #find endocing
        encoding = chardet.detect(string)['encoding']
        string = string.decode(encoding).encode('ascii', 'xmlcharrefreplace')
    return string

def str2Type(stringValue, strType):
    # print "str2Type:", stringValue, "to", strType
    valueType = getType(strType)
    try:
        return valueType(stringValue)
    except UnicodeEncodeError:
        try:
            return strType.encode("ascii", "ignore")
        except UnicodeEncodeError:
            return "Encoding error"


def cast(value, strType):
    return str2Type(value, strType)

def formatSensorID(sensordescription):
    return "".join([sensordescription.namespace + "SensorID-" + sensordescription.uuid])

def dictdeepcopy(aDict):
    return copy.deepcopy(aDict)

def valueToBoolean(value):
    if value:
        if value == "True":
            return True
    return False