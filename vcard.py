
"""
A vCard implementation complying with the 4.0 specification in RFC 6350.
http://tools.ietf.org/html/rfc6350
"""

import pyparsing as pp

version="4.0"

pp.ParserElement.setDefaultWhitespaceChars("")

class vCard(object):
	def __init__(self, stream):
		self.vcard = []

		crlf = pp.Literal("\r\n").suppress()
		begin = pp.Literal("BEGIN:VCARD").suppress()
		begin.setParseAction(lambda: self.vcard.append([]))
		ver = pp.Literal("VERSION:" + version).suppress()
		end = pp.Literal("END:VCARD").suppress()
		folded = ~end + pp.Combine(pp.OneOrMore(pp.Word(pp.printables + " \t") \
				| pp.Suppress(pp.Literal("\r\n ") | pp.Literal("\r\n\t")))) + \
				crlf
		vcard = begin + crlf + ver + crlf + pp.OneOrMore(folded) + end + crlf
		vcard_entity = pp.OneOrMore(pp.Group(vcard))
#		vcard_entity.setDebug()

		identifier = lambda: pp.Word(pp.alphanums + "-").copy()
		group = identifier().setResultsName("group")
		name = identifier().setResultsName("name")
		param_value = pp.CharsNotIn('":;') | pp.QuotedString('"')
		param = identifier() + pp.Literal("=").suppress() + param_value + \
				pp.ZeroOrMore(pp.Literal(",") + param_value)
		params = pp.ZeroOrMore(pp.Group(pp.Literal(";").suppress() + \
				param)).setResultsName("parameters")
		value = pp.Word(pp.printables + " \t").setResultsName("property value")
		contentline = pp.Optional(group + pp.Literal(".").suppress()) + name + \
				params + pp.Literal(":").suppress() + value

		def propertyAction(tok):
			v = contentline.parseString(tok[0]).asDict()
			self.vcard[-1].append(v)
			return v
		#folded.setParseAction(propertyAction)
		print(vcard_entity.parseString(stream).asList())
	def dump(self):
		return self.vcard
	def _iterate(self, action, name=None, group=None, params=tuple()):
		ret = None
		for v in self.vcard:
			for p in v:
				if name != None and p["name"].upper() != name.upper():
					continue
				if group != None and p["group"] != group.upper():
					continue
				if len(params) > 0:
					for k in params:
						pass
				a = action(p, v)
				if a != None:
					ret = a
		return ret
	def listProperty(self, name, group=None, params=tuple()):
		properties = []
		def action(p, v):
			properties.append(p)
			return properties
		return self._iterate(action, name, group, params)
	def findByProperty(self, name, value, group=None, params=tuple()):
		def action(p, v):
			if p["property value"] == value:
				return v
		return self._iterate(action, name, group, params)
	def findByFN(self, fn):
		return self.findByProperty("FN", fn)

example = """BEGIN:VCARD\r
VERSION:4.0\r
FN:Simon Perreault\r
N:Perreault;Simon;;;ing. jr,M.Sc.\r
BDAY:--0203\r
ANNIVERSARY:20090808T1430-0500\r
GENDER:M\r
LANG;PREF=1:fr\r
LANG;PREF=2:en\r
ORG;TYPE=work:Viagenie\r
ADR;TYPE=work:;Suite D2-630;2875 Laurier;\r
 Quebec;QC;G1V 2M2;Canada\r
TEL;VALUE=uri;TYPE="work,voice";PREF=1:tel:+1-418-656-9254;ext=102\r
TEL;VALUE=uri;TYPE="work,cell,voice,video,text":tel:+1-418-262-6501\r
EMAIL;TYPE=work:simon.perreault@viagenie.ca\r
GEO;TYPE=work:geo:46.772673,-71.282945\r
KEY;TYPE=work;VALUE=uri:\r
 http://www.viagenie.ca/simon.perreault/simon.asc\r
TZ:-0500\r
URL;TYPE=home:http://nomis80.org\r
END:VCARD\r
BEGIN:VCARD\r
VERSION:4.0\r
UID:urn:uuid:4fbe8971-0bc3-424c-9c26-36c3e1eff6b1\r
FN;PID=1.1:J. Doe\r
N:Doe;J.;;;\r
EMAIL;PID=1.1:jdoe@example.com\r
CLIENTPIDMAP:1;urn:uuid:53e374d9-337e-4727-8803-a1e9c14e0556\r
END:VCARD\r
"""

test = vCard(example)
#print(test.findByFN("Simon Perreault"))
print(test.listProperty("TEL"))
