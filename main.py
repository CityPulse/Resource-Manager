

import argparse
import sys
import os
import subprocess
from virtualisation.resourcemanagement.resourcemanagement import ResourceManagement

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-replay', help="start in replay mode", dest='replay', action="store_true")
    parser.add_argument('-test', help="for development purposes", dest='test', action="store_true")
    parser.add_argument('-messagebus', help="messages are sent through the message bus", dest='messagebus', action="store_true")
    parser.add_argument('-triplestore', help="save annotated data into the triplestore", dest='triplestore', action="store_true")
    parser.add_argument('-aggregate', help="Aggregate the incoming data. Requires triplestore to be activated", dest='aggregate', action="store_true")
    parser.add_argument('-gentle', help="Reduces the CPU load but slower. Only effective in replay mode", dest='gentle', action="store_true")
    parser.add_argument('-eventannotation', help="listen for new events on the message bus, annotate them and send them into the triplestore.", dest='eventannotation', action="store_true")
    parser.add_argument('-from', help="in replay mode determines the beginning date", dest='start', required=False)
    parser.add_argument('-to', help="in replay mode determines the end date", dest='end', required=False)
    parser.add_argument('-speed', help="Speed of the clock in replay mode [1, 1000]", dest='speed', type=int, required=False)
    parser.add_argument('-continuelive', help="Continue in live mode after replay end time is reached", dest="continuelive", action="store_true")
    parser.add_argument('-gdi', help="Store newly registered wrappers into the GDI Database", dest="gdi", action="store_true")
    parser.add_argument('-cleartriplestore', help="Deletes all graphs in the triplestore (may take up to 300s per wrapper!)", dest="cleartriplestore", action="store_true")
    parser.add_argument('-log', help="Specify the log level. Accepted values are: 'CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG' or 'DEBUG2'. Default is INFO.", dest="log")
    parser.add_argument('-pt', help="Performance Test, print the number of processed observations/s in replay mode", dest="pt", action="store_true")
    parser.add_argument('-noQuality', help="Disables the QoI calculation", dest="noQuality", action="store_true")
    parser.add_argument('-nofr', help="Disables the Fault Recovery", dest="nofr", action="store_true")
    parser.add_argument('-restart', help="Restarts the resource management with the same arguments as last time.", dest="restart", action="store_true")
    parser.add_argument('-sql', help="Use a SQL database", dest="sql", action="store_true")
    parser.set_defaults(replay=False, test=False, messagebus=False, speed=999, aggregate=False, gentle=False, eventannotation=False, continuelive=False, gdi=False, log="INFO", pt=False, nofr=False, restart=False, sql=False)
    args = parser.parse_args()

    if args.restart:
        if os.path.exists("last"):
            f = open("last", "r")
            pid = f.readline().strip()
            _arg = (sys.executable + " " + f.readline()).strip().split(" ")
            f.close()
            try:
                os.kill(int(pid), 9)
            except OSError:
                # no matching process
                print "No proccess with pid", pid, "found."
            # print _arg
            # print os.path.dirname(os.path.abspath(__file__))
            FNULL = open(os.devnull, 'w')
            wd = os.path.dirname(os.path.abspath(__file__))
            print "Starting", _arg, "in working directoy", wd
            p = subprocess.Popen(_arg, stderr=subprocess.STDOUT, stdout=FNULL, cwd=wd)
            print "resource management restarted with pid", p.pid
            sys.exit(0)
        else:
            print "Impossible to restart. No information about previous session found."
    else:
        f = open("last", "w")
        f.write(str(os.getpid()))
        f.write('\n')
        for a in sys.argv:
            f.write(a)
            f.write(' ')
        f.close()

        rm = ResourceManagement(args)

        # setup resource management component

        if args.test:
            rm.test()

        if args.replay:
            rm.startReplay()
        else:
            rm.start()
