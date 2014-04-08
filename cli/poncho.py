# CLI to scrape Poncho forecast & display in terminal
# requires BeautifulSoup & lxml parser & textwrap
# recommend shell alias: p = "~/path/to/poncho.py <refcode>"

## usage: 
##   python po.py [ref] [-d]
##
## options: 
##   <ref>	referral code	from "view in browser" url, e.g XXXX from (http://poncho.is/s/XXXX) defaults to RW5pQ (NYC)
##   -d			suppress detail description - just headline/temps.

import urllib2
import sys
import textwrap
from StringIO import StringIO   
from bs4 import BeautifulSoup, Comment

if (len(sys.argv)>1):
	ref = sys.argv[1]
else: 
	print "No referral code set, defaulting to NYC"
	ref = 'RW5pQ'

url = 'http://poncho.is/s/'+ref
r = urllib2.urlopen(url)
h = r.read()
p = BeautifulSoup(h, "lxml")

# strip out comments & head tag
comments = p.findAll(text=lambda text:isinstance(text, Comment))
[comment.extract() for comment in comments]
p.head.extract()

# Use element & class name to find matching elements and extract the target value strings
head = p.find("td", class_ = "content w612").h3.string
det = p.find("td", class_ = "content w612").p.string
tt = p.find_all("td",class_ = "w33")
unit = p.find("div", class_="unit").string

time1 = tt[0].h4.string
temp1 = tt[0].h3.string
time2 = tt[1].h4.string
temp2 = tt[1].h3.string
time3 = tt[2].h4.string
temp3 = tt[2].h3.string

# Output
print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
print head

# if flag set, print blurb.
if '-d' not in str(sys.argv):
	x = textwrap.wrap(det)
	for l in x:
		print l

print "\n"+str(time1).upper()+': '+str(temp1)+unit, " | ", str(time2).upper()+': '+str(temp2)+unit, " | ", str(time3)+': '+str(temp3)+unit+"\n"

print "Poncho: The World's BEST Personalized Weather Service (poncho.is)\n"
print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
