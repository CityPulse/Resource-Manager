#!/bin/bash
sudo /etc/init.d/virtuoso-opensource-7 stop
sudo rm /var/lib/virtuoso-opensource-7/db/virtuoso*
sudo cp /var/lib/virtuoso-opensource-7/db/backup/* /var/lib/virtuoso-opensource-7/db/
sudo /etc/init.d/virtuoso-opensource-7 start
echo "Finished Virtuoso Reset"
echo "Now restart Resource Management to restore graphs"
su citypulse
cd /home/citypulse/virtualisation2/
python main.py -restart
exit
echo "Finished, CP framework should now run smoothly"
