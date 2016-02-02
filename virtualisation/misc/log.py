import chardet
import logging
import sys
import datetime


__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'


class Log(object):
    logger = None
    DEBUG_2_LVL = 5
    no_enc = (int, float, long, datetime.datetime)

    def __init__(self, level):
        level = level.upper()
        possible_lvls = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "DEBUG2", "NOTSET"]
        if not Log.logger:
            logging.addLevelName(Log.DEBUG_2_LVL, "DEBUG2")
            Log.logger = logging.getLogger("virtualisation")
            hdlr = logging.FileHandler('./virtualisation.log')
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            hdlr.setFormatter(formatter)
            Log.logger.addHandler(hdlr)
            hdlr = logging.StreamHandler(sys.stdout)
            hdlr.setFormatter(formatter)
            Log.logger.addHandler(hdlr)
            if level in possible_lvls:
                if hasattr(logging, level):
                    Log.logger.setLevel(getattr(logging, level))
                else:
                    Log.logger.setLevel(Log.DEBUG_2_LVL)
                
            Log.logger.propagate = False
            self.logger = Log.logger
        else:
            self.logger = Log.logger

    @classmethod
    def c(cls, *args):
        Log.log(logging.CRITICAL, args)

    @classmethod
    def d(cls, *args):
        Log.log(logging.DEBUG, args)

    @classmethod
    def d2(cls, *args):
        Log.log(Log.DEBUG_2_LVL, args)

    @classmethod
    def e(cls, *args):
        Log.log(logging.ERROR, args)

    @classmethod
    def w(cls, *args):
        Log.log(logging.WARNING, args)

    @classmethod
    def i(cls, *args):
        Log.log(logging.INFO, args)

    @classmethod
    def log(cls, lvl, args):
        args = map(Log.enc, args)
        try:
            #Log.logger.log(lvl, " ".join(map(unicode, args)).decode('ascii', 'ignore'))
            Log.logger.log(lvl, " ".join(args))
        except:
            print "Logging error!"
            
    @classmethod
    def enc(cls, arg):
        if isinstance(arg, unicode):
            return arg
        if isinstance(arg, Log.no_enc):
            return str(arg)
        try:
            #find encoding
            encoding = chardet.detect(arg)['encoding']
            return arg.decode(encoding, 'ignore')
        except:
            return ""