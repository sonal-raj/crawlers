# ********************************************************************************************
# Date: 05-09-2015
# Author: Deltawave
# Script Purpose: This script can browse the entire directory structure of a static or dynamic 
#		  website, and based on the inputs of the user it will download all the files 
#		  based on the following parameters:
#		  1. File Type
#		  2. Name String 
#		  3. Regular Expression
#
# ********************************************************************************************

import urllib
import re
import sys

# The Arguments with power to rip the website

url = "http://www.sonalraj.com/"
depth = 2
Regex = ""
Filetype = ""

# The actual processing

PageOne = urllib.urlopen( url )
Content = PageOne.read()

# Parse the contents recursively on the page upto given levels

print Content

