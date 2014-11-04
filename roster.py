import urllib2, json

'''
API details: https://classes.cornell.edu/content/SP15/api-details
'''



def getClasses(term,varl):
	'''
	vars:
	{subj:'subject'
	,level:'level'}

	From each class, want:
	(the ['classes'][0] will need to loop through all relevant classes, 
		possibly only show so many on a page)
	(sections will need to be properly parsed)

	{'classId':data['data']['classes'][0]['catalogNbr']
	,'title':data['data']['classes'][0]['titleLong']
	,'description':data['data']['classes'][0]['description']
	,'semester':data['data']['classes'][0]['catalogWhenOffered']
	,'forbiddenOver':data['data']['classes'][0]['catalogForbiddenOverlaps']
	,'prereq':data['data']['classes'][0]['catalogPrereqCoreq']
	,'sections':data['data']['classes'][0]['classSections']}
	'''

	
	url = "https://classes.cornell.edu/api/2.0/search/classes.json?roster=%s&subject=%s&classLevels[]=%s"%(term,varl['subj'],varl['level'])
	data = json.loads(urllib2.urlopen(url).read())
	'''
	This gets the sections for an individual class
	output = {'classId':data['data']['classes'][0]['catalogNbr']

	,'title':data['data']['classes'][0]['titleLong']
	,'description':data['data']['classes'][0]['description']
	,'semester':data['data']['classes'][0]['catalogWhenOffered']
	,'forbiddenOver':data['data']['classes'][0]['catalogForbiddenOverlaps']
	,'prereq':data['data']['classes'][0]['catalogPrereqCoreq']
	,'sections':data['data']['classes'][0]['enrollGroups'][0]['classSections']}

	classes = data['data']['classes'][0]['enrollGroups'][0]['classSections'][0]
	'''

	output = data['data']['classes']

	return output

