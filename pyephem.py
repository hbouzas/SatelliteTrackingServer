#!/usr/bin/python 
import math
import time
import ftplib
import sys
import json
from datetime import datetime
import ephem
import urllib2

def get_sec(time_str):
    h, m, s = time_str.split(':')
    return float(h) + float(m)/60  + float(s)/3600

print sys.argv[1] #key
print sys.argv[2] #name

if sys.argv[2] == 'list':
   data={}
   data['name1'] = 'ao07'
   data['name2'] = 'ao73'
   data['name3'] = 'ao85'
   data['name4'] = 'ao91'
   data['name5'] = 'ao92'
   data['name6'] = 'cas4a'
   data['name7'] = 'cas4b'
   data['name8'] = 'cubebug-1'
   data['name9'] = 'co57'
   data['name10'] = 'co55'
   data['name11'] = 'eo79'
   data['name12'] = 'eo80'
   data['name13'] = 'eo88'
   data['name14'] = 'fo29'
   data['name15'] = 'lilacsat-2'
   data['name16'] = 'lo87'
   data['name17'] = 'no44'
   data['name18'] = 'no84'
   data['name19'] = 'so50'
   data['name20'] = 'technosat'
   data['name21'] = 'ukube-1'
   data['name22'] = 'xw2a'
   data['name23'] = 'xw2b'
   data['name24'] = 'xw2c'
   data['name25'] = 'xw2d'
   data['name26'] = 'xw2f'
   data['name27'] = 'iss'
   data['name28'] = 'moon'
   data['name29'] = 'sun'
   data['name30'] = 'none'
   data['name31'] = 'test'
   data['name32'] = 'fixed'

   json_data = json.dumps(data)
   print(json_data)
   quit()

print sys.argv[3] #lat
print sys.argv[4] #lon
print sys.argv[5] #elev

sleep_time = 60
degrees_per_radian = 180.0 / math.pi

home = ephem.Observer()
# home.lon = '-114.052654'   # +E
# home.lat = '51.073063'      # +N
home.lon = sys.argv[4]     # +E
home.lat = sys.argv[3]      # +N
#home.elevation = 1050 # meters
elevation = float(sys.argv[5])    # meters
home.date = datetime.utcnow()
print str(datetime.now())

# Always get the latest ISS TLE data from:
# http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
if sys.argv[2] == 'ao07':
# AO-07 Norad 7530
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=7530')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   ao07 = ephem.readtle('AO07',TLE1,TLE2)
   ao07.compute(home)
   data={}
   data['name']='ao07'
   data['azi']=str(get_sec(str(ao07.az)))
   data['alt']=str(get_sec(str(ao07.alt)))
   json_data = json.dumps(data)
   print json_data

elif sys.argv[2] == 'ao73':
#AO-73 Norad 39444
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=39444')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   ao73 = ephem.readtle('AO73',TLE1,TLE2)
   ao73.compute(home)
   data={}
   data['name']='ao73'
   data['azi']=str(get_sec(str(ao73.az)))
   data['alt']=str(get_sec(str(ao73.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'ao85':
#AO-85 Norad 40967
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=40967')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   ao85 = ephem.readtle('AO85',TLE1,TLE2)
   ao85.compute(home)
   data={}
   data['name']='ao85'
   data['azi']=str(get_sec(str(ao85.az)))
   data['alt']=str(get_sec(str(ao85.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'ao91':
#AO-91 Norad 43017
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=43017')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   ao91 = ephem.readtle('AO91',TLE1,TLE2)
   ao91.compute(home)
   data={}
   data['name']='ao91'
   data['azi']=str(get_sec(str(ao91.az)))
   data['alt']=str(get_sec(str(ao91.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'ao92':
#AO-92 Norad 43137
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=43137')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   ao92 = ephem.readtle('AO92',TLE1,TLE2)
   ao92.compute(home)
   data={}
   data['name']='ao92'
   data['azi']=str(get_sec(str(ao92.az)))
   data['alt']=str(get_sec(str(ao92.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'eo79':
#EO-79 Norad 40025
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=40025')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   eo79 = ephem.readtle('EO79',TLE1,TLE2)
   eo79.compute(home)
   data={}
   data['name']='eo79'
   data['azi']=str(get_sec(str(eo79.az)))
   data['alt']=str(get_sec(str(eo79.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'eo80':
#EO-80 Norad 40032
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=40032')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   eo80 = ephem.readtle('EO80',TLE1,TLE2)
   eo80.compute(home)
   data={}
   data['name']='eo80'
   data['azi']=str(get_sec(str(eo80.az)))
   data['alt']=str(get_sec(str(eo80.alt)))
   json_data = json.dumps(data)
   print json_data

elif sys.argv[2] == 'eo88':
#EO-88 Norad 42017
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=42017')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   eo88 = ephem.readtle('EO88',TLE1,TLE2)
   eo88.compute(home)
   data={}
   data['name']='eo88'
   data['azi']=str(get_sec(str(eo88.az)))
   data['alt']=str(get_sec(str(eo88.alt)))
   json_data = json.dumps(data)
   print json_data   
elif sys.argv[2] == 'cas4a':
#CAS 4A
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=42761')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   cas4a = ephem.readtle('CAS4A',TLE1,TLE2)
   cas4a.compute(home)
   data={}
   data['name']='cas4a'
   data['azi']=str(get_sec(str(cas4a.az)))
   data['alt']=str(get_sec(str(cas4a.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'cas4b':
#CAS 4B
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=42759')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   cas4b = ephem.readtle('CAS4B',TLE1,TLE2)
   cas4b.compute(home)
   data={}
   data['name']='cas4b'
   data['azi']=str(get_sec(str(cas4b.az)))
   data['alt']=str(get_sec(str(cas4b.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'cubebug-1':
#CUBEBUG-1 Norad 39153
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=39153')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   cubebug1 = ephem.readtle('CUBEBUG-1',TLE1,TLE2)
   cubebug1.compute(home)
   data={}
   data['name']='cubebug1'
   data['azi']=str(get_sec(str(cubebug1.az)))
   data['alt']=str(get_sec(str(cubebug1.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'co57':
#CO57 Norad 27848
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=27848')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   co57 = ephem.readtle('CO57',TLE1,TLE2)
   co57.compute(home)
   data={}
   data['name']='co57'
   data['azi']=str(get_sec(str(co57.az)))
   data['alt']=str(get_sec(str(co57.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'co55':
#CO55 Norad 27844
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=27844')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   co55 = ephem.readtle('CO55',TLE1,TLE2)
   co55.compute(home)
   data={}
   data['name']='co55'
   data['azi']=str(get_sec(str(co55.az)))
   data['alt']=str(get_sec(str(co55.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'fo29':
#FO29 Norad 24278
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=24278')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   fo29 = ephem.readtle('FO29',TLE1,TLE2)
   fo29.compute(home)
   data={}
   data['name']='fo29'
   data['azi']=str(get_sec(str(fo29.az)))
   data['alt']=str(get_sec(str(fo29.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'lilacsat-2':
   #Lilacsat-2 Norad 40908
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=40908')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   lilacsat2 = ephem.readtle('LILACSAT2',TLE1,TLE2)
   lilacsat2.compute(home)
   data={}
   data['name']='lilacsat-2'
   data['azi']=str(get_sec(str(lilacsat2.az)))
   data['alt']=str(get_sec(str(lilacsat2.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'lo87':
#ELO-87 Nusat
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=41557')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   lo87 = ephem.readtle('LO87',TLE1,TLE2)
   lo87.compute(home)
   data={}
   data['name']='lo87'
   data['azi']=str(get_sec(str(lo87.az)))
   data['alt']=str(get_sec(str(lo87.alt)))
   json_data = json.dumps(data)
   print json_data
      
elif sys.argv[2] == 'no44':
#NO-44 40654
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=26931')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   no44 = ephem.readtle('NO44',TLE1,TLE2)
   no44.compute(home)
   data={}
   data['name']='no44'
   data['azi']=str(get_sec(str(no44.az)))
   data['alt']=str(get_sec(str(no44.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'no84':
#NO-84 40654
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=40654')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   no84 = ephem.readtle('NO84',TLE1,TLE2)
   no84.compute(home)
   data={}
   data['name']='no84'
   data['azi']=str(get_sec(str(no84.az)))
   data['alt']=str(get_sec(str(no84.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'so50':
#SO-50 27607
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=27607')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   so50 = ephem.readtle('SO50',TLE1,TLE2)
   so50.compute(home)
   data={}
   data['name']='so50'
   data['azi']=str(get_sec(str(so50.az)))
   data['alt']=str(get_sec(str(so50.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'technosat':
#TECHNOSAT 42829
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=42829')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   technosat = ephem.readtle('TECHNOSAT',TLE1,TLE2)
   technosat.compute(home)
   data={}
   data['name']='technosat'
   data['azi']=str(get_sec(str(technosat.az)))
   data['alt']=str(get_sec(str(technosat.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'ukube-1':
#UKUBE-1 40074
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=40074')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   ukube1 = ephem.readtle('UKUBE-1',TLE1,TLE2)
   ukube1.compute(home)
   data={}
   data['name']='ukube-1'
   data['azi']=str(get_sec(str(ukube1.az)))
   data['alt']=str(get_sec(str(ukube1.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'xw2a':
#XW2A Norad 40903
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=40903')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   xw2a = ephem.readtle('XW2A',TLE1,TLE2)
   xw2a.compute(home)
   data={}
   data['name']='xw2a'
   data['azi']=str(get_sec(str(xw2a.az)))
   data['alt']=str(get_sec(str(xw2a.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'xw2b':
#XW2B Norad 40911
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=40911')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   xw2b = ephem.readtle('XW2B',TLE1,TLE2)
   xw2b.compute(home)
   data={}
   data['name']='xw2b'
   data['azi']=str(get_sec(str(xw2b.az)))
   data['alt']=str(get_sec(str(xw2b.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'xw2c':
#XW2C Norad 40906
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=40906')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   xw2c = ephem.readtle('XW2C',TLE1,TLE2)
   xw2c.compute(home)
   data={}
   data['name']='xw2c'
   data['azi']=str(get_sec(str(xw2c.az)))
   data['alt']=str(get_sec(str(xw2c.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'xw2d':
#XW2D Norad 40907
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=40907')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   xw2d = ephem.readtle('XW2D',TLE1,TLE2)
   xw2d.compute(home)
   data={}
   data['name']='xw2d'
   data['azi']=str(get_sec(str(xw2d.az)))
   data['alt']=str(get_sec(str(xw2d.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'xw2f':
#XW2F Norad 40910
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=40910')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   xw2f = ephem.readtle('XW2F',TLE1,TLE2)
   xw2f.compute(home)
   data={}
   data['name']='xw2f'
   data['azi']=str(get_sec(str(xw2f.az)))
   data['alt']=str(get_sec(str(xw2f.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'iss':
#ISS Norad 25544
   response = urllib2.urlopen('http://www.n2yo.com/satellite/?s=25544')
   html = response.read()
   ind_sat=html.find('Two Line Element Set (TLE):')
   ind_TLE1=html.find('1 ', ind_sat)
   ind_end_TLE1=html.find('\n',ind_TLE1)
   ind_end_TLE1=ind_end_TLE1-1
   TLE1=html[ind_TLE1:ind_end_TLE1]
   ind_TLE2=html.find('2 ',ind_end_TLE1)
   ind_end_TLE2=html.find('\n',ind_TLE2)
   TLE2=html[ind_TLE2:ind_end_TLE2]
   iss = ephem.readtle('ISS',TLE1,TLE2)
   iss.compute(home)
   data={}
   data['name']='iss'
   data['azi']=str(get_sec(str(iss.az)))
   data['alt']=str(get_sec(str(iss.alt)))
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'moon':
   moon = ephem.Moon()
   moon.compute(home)
   data={}
   data['name']='moon'
   data['azi']=str(get_sec(str(moon.az)))
   data['alt']=str(get_sec(str(moon.alt)))
   print(moon.az)
   print(moon.alt)
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'sun':
   sun = ephem.Sun()
   sun.compute(home)
   data={}
   data['name']='sun'
   data['azi']=str(get_sec(str(sun.az)))
   data['alt']=str(get_sec(str(sun.alt)))
   print(sun.az)
   print(sun.alt)
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'none':
   data={}
   data['name']='none'
   data['azi']=str(-999.000)
   data['alt']=str(-999.000)
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'test':
   data={}
   data['name']='test'
   data['azi']=str(105.000)
   data['alt']=str(45.000)
   json_data = json.dumps(data)
   print json_data
elif sys.argv[2] == 'fixed':
   data={}
   data['name']='fixed'
   data['azi']=str(180.000)
   data['alt']=str(90.000)
   json_data = json.dumps(data)
   print json_data
else:
   data={}
   data['error'] = 'invalid name'
   json_data = json.dumps(data)
   print(json_data)

