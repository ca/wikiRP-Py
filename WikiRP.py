import urllib2
import ast

class WikiRP(object):
	def __init__(self):
		self.thesis = raw_input("Enter a thesis statement: ")

	def makeRequest(self, method):
		body = "http://en.wikipedia.org/w/api.php?format=json&action=query"

		if method == "search":
			params = "&list=search&srprop=timestamp&srsearch="+self.thesis
		else:
			params = "&prop=revisions&rvprop=content&titles="+self.thesis

		url = body + params
		response = urllib2.urlopen(url)
		json = response.read()
		out = ast.literal_eval(json)
		# Below qould be useful but idk not right now
		# print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

		# Oops! Obviously this below will be different if it's search vs pages req
		# Make this all functional (ie. create a parse method)
		pageid = out["query"]["pages"].keys()[0]
		content = out["query"]["pages"][pageid]["revisions"][0]["*"]
		print content
		self.content = content

	def errors(self):
		if "#Redirect" in self.content:
			redirect = self.content.split("]]")[0].split("[[")[1]
			print redirect
			return True
		else:
			return False

researchPaper = WikiRP()
# This all goes in a "main" method
researchPaper.makeRequest("pages")
if researchPaper.errors():
	researchPaper.makeRequest("search")