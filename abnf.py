"""
ABNF specification according to RFC 5234.
http://tools.ietf.org/html/rfc5234
"""

class rule(object):
	def __init__(self, text):
		stream = bytes(text)
		for i in range(len(stream)):
			i = parse(stream[i])
		def parse(char):
			pass

