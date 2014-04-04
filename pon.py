# script to scrape poncho forecast & display via CLI

import pycurl
import sys
from StringIO import StringIO   
from bs4 import BeautifulSoup

# check for refid - if none found, use NYC default
if (sys.argv[1]):
	ref_code = sys.argv[1]
else: 
	print "No referral code found, defaulting to NYC"
	ref_code = 'RW5pQ'

url = ['http://poncho.is/s/'+ref_code]

# Download html via cURL

s = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEFUNCTION, s.write)
c.perform()
c.close()
h = s.getvalue()

# debug line.
print h

# Parse html with BeautifulSoup
p = BeautifulSoup(h, "lxml")

# Use element & class name to find matching elements and extract the target value strings

head = 
blurb = 
now = 
later = 
tom = 

# Output
print "headline:", head
print "blurb:", blurb
print "Now:", now
print "Later:", later
print "Tomorrow:", tom
