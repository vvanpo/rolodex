"""
ABNF specification according to RFC 5234.
http://tools.ietf.org/html/rfc5234
"""

import math

class SyntaxError(Exception):
	def __init__(self):
		pass

class rule(object):
	def __init__(self, stream):
		for i in range(len(stream)):
			i = element(stream[i])
		def whitespace(i):
			if stream[i] == " " or stream[i] == "\t":
				whitespace(i+1)
			else:
				return i
		def element(i):
			pass
		def terminal(i):
			def char(i, base):
				string = ""
				for j in range(i, i+(math.log(256, base))):
					if stream[j] not in range(str(base)):
						if j == i: raise SyntaxError()
						else:
							return = (j, int(string, base))
					else:
						string.append(stream[j])
				raise SyntaxError()
			if stream[i] != "%": raise SyntaxError()
			i++
			if stream[i] == "b":
				c = char(i+1, 2)
			elif stream[i] == "d":
				c = char(i+1, 10)
			elif stream[i] == "x":
				c = char(i+1, 16)
			else: raise SyntaxError()
			i = c[0]
			if stream[i] == ".":
				pass
			elif stream[i] == "-":
				pass
			else:
				whitespace(i)
