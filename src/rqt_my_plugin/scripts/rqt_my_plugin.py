#!/usr/bin/env python
 
import sys
 
from rqt_my_plugin.my_module import MyPlugin
from rqt_gui.main import Main
 
plugin = 'rqt_my_plugin'
main = Main(filename=plugin)
sys.exit(main.main(standalone=plugin))
