#!/usr/bin/python

# PyShoutOut by Joey C. (http://www.joeyjwc.x3fusion.com)
# Writes the recieved information to the data file.
import cgi
from  psogen import process_form 

print "Content-type:text/html\r\n\r\n"

values = cgi.FieldStorage()
if values.has_key("name"):
  rawname = values["name"].value
else:
  rawname = "&nbsp;"
if values.has_key("data"):
  rawdata = values["data"].value
else:
  rawdata = "&nbsp;"

color = values["color"].value
timestamp = float(values["timestamp"].value)

process_form(rawname, rawdata, color, timestamp)

print """<html><body>ok</body></html>"""
