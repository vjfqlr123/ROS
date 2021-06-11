#!/usr/bin/env python
# license removed for brevity

import rospy
import actionlib
import os, sys
import subprocess
from datetime import datetime
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

now = datetime.now()

print(now.year, now.month, now.day, now.hour, now.minute, now.second)

#NEWCODE = "roscore &"
#os.system(NEWCODE)


subprocess.check_call('gnome-terminal')
subprocess.check_call('ls', shell=True)

subprocess.check_output(['gnome-terminal', 'ls'])
