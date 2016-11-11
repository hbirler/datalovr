from flask import jsonify

class CQuery:
	def __init__(self, mid = "", title = "", text = "", opts = []):
		self.id = mid
		self.title = title
		self.text = text
		self.opts = opts
	
	def get_json(self):
		return jsonify({"id":self.id, "title":self.title, "text":self.text, "opts": self.opts})


def sample_query():
	return CQuery("123","Topkek","Ayy lmaoo",["Laufen","Tanzen","Oww yeah"])