"""
ABNF specification according to RFC 5234.
http://tools.ietf.org/html/rfc5234
"""

import math, re

class SyntaxError(Exception):
	pass

class Rules(object):
	def __init__(self, abnf):
#		# rulelist
#		index = 0	# Tried using a closure to get rid of this global, but I'm
#					# not really sure there is a point to that.
#		repeat(line, 1)
#		def line():
#			if index < len(abnf):
#				alt(
#					rule(index),
#					group(
#						repeat(lambda: c_wsp(index)),
#						c_nl(index)
#					)
#				)
#			else:
#				return False
#		# rule
#		def rule(i):
#			v = ""
#			for f in (rulename, defined_as, elements, c_nl):
#				n = f(i)
#				if n == False: return False
#				i += len(n)
#				v += n
#			index = i + 1
#			return v
#		# rulename
#		def rulename(i):
#			pass
#		def defined_as(i):
#			pass
#		def elements(i):
#			pass
#		def c_wsp(i):
#			pass
#		def c_nl(i):
#			pass
#		def comment(i):
#			pass
#		def alternation(i):
#			pass
#		def repetition(i):
#			pass
#		def repeat(i):
#			pass
#		def element(i):
#			pass
#		def group(i):
#			pass
#		def option(i):
#			pass
#		def char_val(i):
#			pass
#		def num_val(i):
#			pass
#		def bin_val(i):
#			pass
#		def dec_val(i):
#			pass
#		def hex_val(i):
#			pass
#		def prose_val(i):
#			pass
		def comment(arg):
			if arg[0] == ";":
				end = arg.find("\n")
				return arg[1:end+1].strip()
			return False
		# Operator precedence
		#	rule_name, prose_val, terminal
		#	comment
		#	val_range
		#	repeat
		#	group, option
		#	concat
		#	alt
		def terminal(num, arg):
			if ord(arg) == num: return arg
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
					i += 1
				else:
					break
			if i >= a: return v
			else: return False
		def group(*args):
			return concat(*args)
		# elem should be a closure
		def option(elem):
			return repeat(elem, 0, 1)
		def concat(*rules, arg):
			v = ""
			for r in rules:
				e = r(arg)
				if e == False: return False
				arg = arg[len(e)-1:]
			return v
		def alt(*args):
			for a in args:
				if a != False:
					return a
			return False
		# Core rules from Appendix B
		self.ALPHA	= lambda a: alt(val_range(0x41, 0x5a, a), val_range(0x61, 0x7a, a))
		self.BIT	= lambda a: val_range(0x30, 0x31, a)
		self.CHAR	= lambda a:	val_range(0x01, 0x7f, a)
		self.CR		= lambda a:	terminal(0x0d, a)
		self.CRLF	= lambda a:	concat(CR, LF)
		self.CTL	= lambda a:	alt(val_range(0, 0x1f, a), terminal(0x7f, a))
		self.DIGIT	= lambda a: val_range(0x30, 0x39, a)
		self.DQUOTE	= lambda a: terminal(0x22, a)
		self.HEXDIG	= lambda a: alt(self.DIGIT(a), val_range(0x41, 0x46, a), val_range(0x61, 0x66, a))
		self.HTAB	= lambda a: terminal(0x09, a)
		self.LF		= lambda a: terminal(0x0a, a)
		self.LWSP	= lambda a: repeat(
