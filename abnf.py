"""
ABNF specification according to RFC 5234.
http://tools.ietf.org/html/rfc5234
"""

import math

class SyntaxError(Exception):
	pass

class Rules(object):
	def __init__(self, abnf):
		# rulelist
		repeat(
			lambda:
				alt(
					rule(i),
					group(
						repeat(lambda: c_wsp(i)),
						c_nl(i)
					)
				),
			1
		)
		# rule
		def rule(i):
			
			for f in (rulename, defined_as, elements, c_nl):
				n
				if not n: return False
		# rulename
		def rulename(i):
			pass
		def defined_as(i):
			pass
		def elements(i):
			pass
		def c_wsp(i):
			pass
		def c_nl(i):
			pass
		def comment(i):
			pass
		def alternation(i):
			pass
		def repetition(i):
			pass
		def repeat(i):
			pass
		def element(i):
			pass
		def group(i):
			pass
		def option(i):
			pass
		def char_val(i):
			pass
		def num_val(i):
			pass
		def bin_val(i):
			pass
		def dec_val(i):
			pass
		def hex_val(i):
			pass
		def prose_val(i):
			pass
		# Operator precedence
		#	rule_name, prose_val, terminal
		#	comment
		#	val_range
		#	repeat
		#	group, option
		#	concat
		#	alt
		def terminal():
			pass
		def comment(arg):
			if arg[0] == ";":
				end = arg.find("\n")
				return arg[1:end+1].strip()
			return False
		def val_range(begin, end, arg):
			if arg >= begin and arg <= end:
				return arg
			return False
		# elem should be a closure
		def repeat(elem, a=0, b=-1):
			i = 0
			v = ""
			while True:
				e = elem()
				if e != False and (i < b or b < 0):
					v += e
					i++
				else:
					break
			if i >= a: return v
			else: return False
		def group(*args):
			return concat(*args)
		def option(elem):
			return repeat(elem, 0, 1)
		def concat(*args):
			if False in args: return False
			return "".join(args)
		def alt(*args):
			for a in args:
				if a != False:
					return a
			return False
