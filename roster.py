import urllib2, json

'''
API details: https://classes.cornell.edu/content/SP15/api-details
'''



def getClasses(term,varl):
	url = "https://classes.cornell.edu/api/2.0/search/classes.json?roster=%s&subject=%s&classLevels[]=%s"%(term,varl['subj'],varl['level'])
	data = json.loads(urllib2.urlopen(url).read())
	classes = data['data']['classes'][0]['enrollGroups'][0]['classSections'][0]
	return classes

