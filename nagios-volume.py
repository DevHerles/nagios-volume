import alsaaudio
import sys

from optparse import OptionParser

usage = "usage: %prog [options] arg1 arg2 arg3"
parser = OptionParser(usage=usage)
parser.add_option("-a", "--allowed", dest="Allowed level",
                  help="Set allowed volume level", metavar="VOLUME")
parser.add_option("-w", "--warning", dest="Warnig level",
                  help="Set warning volume level", metavar="VOLUME")
parser.add_option("-c", "--critical", dest="Critical level",
                  help="Set critical volume level", metavar="VOLUME")

(options, args) = parser.parse_args()
mixer = alsaaudio.Mixer()
volume = int(mixer.getvolume()[0])

allowed_volume, warning_volume, critical_volume = 40, 60, 80

a_volume, w_volume, c_volume = 0, 0, 0

if len(sys.argv) != 4:
    a_volume, w_volume, c_volume = allowed_volume, warning_volume, critical_volume
else:
    a_volume, w_volume, c_volume = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

if volume < a_volume:
    print(f"OK - Volume level is {volume}%")
    sys.exit(0)
if a_volume <= volume < c_volume:
    print(f"WARNING - Volume level is {volume}%")
    sys.exit(1)
if volume >= c_volume:
    print(f"CRITICAL - Volume level is {volume}%")
    sys.exit(2)

print(f"UNKNOWN - Volume level is UNKNOWN")
sys.exit(3)

