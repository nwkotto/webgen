#!/usr/bin/env python

import os
import sys

def confirmOverwrites(filenames):
	confirmation = ""
	overwrites = []
	for filename in filenames:
		if os.path.isfile(filename):
			overwrites.append(filename)
	for filename in overwrites:
		while 1:
			confirmation = raw_input( filename + " file already exists.  Are you sure you want to overwrite it (y/n)?" )
			if len(confirmation) > 0:
				if confirmation[0] == 'y':
					break
				elif confirmation[0] == 'n':
					sys.exit()
				else:
					print "An incorrect value was entered.  Once again..."
			else:
				print "No value entered.  Once again..."

def createHTML():
	code = """<!DOCTYPE html>
<html>
	<head>
		<title>Sample</title>
		<link rel="stylesheet" type="text/css" href="css/index.css" />
	</head>
	<body>
		<!-- Insert markup here -->

		<script type="text/javascript" src="js/index.js"></script>
	</body>
</html>
"""	
	f = open("index.html", "w")
	f.write(code)

def createCSS():
	code = """body {
	color: black;
	background-color: white;
}
"""
	if not os.path.exists("css"):
		os.makedirs("css")
	f = open("css/index.css", "w")
	f.write(code)

def createJS():
	code = """window.onload = function() {
}
"""
	if not os.path.exists("js"):
		os.makedirs("js")
	f = open("js/index.js", "w")
	f.write(code)

def main():
	filenames = ["index.html", "css/index.css", "js/index.js"]
	confirmOverwrites(filenames)
	createHTML()
	createCSS()
	createJS()

if __name__ == "__main__":
    main()