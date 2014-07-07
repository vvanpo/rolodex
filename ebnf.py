"""
Attempted implementation of extended BNF parser.  Roughly:
http://standards.iso.org/ittf/PubliclyAvailableStandards/s026153_ISO_IEC_14977_1996(E).zip
"""

class SyntaxError(Exception):
	pass

# Operator Precedence:
#	*	repeat
#	-	except
#	,	concat
#	|	alt
#	=	define
#	;	terminate
# Overriding precedence:
#	'	single_quote	'
#	"	double_quote	"
#	(*	comment			*)
#	(	group			)
#	[	option			]
#	{	start_repeat	}
#	?	special			?
class Rules(object):
	def __init__(self, stream):
		while stream != "":
			stream = add_rule(stream)
	def add_rule(s):
		name = identifier(s)
		self.__dict__[name] = rhs(s)
		def rhs(s):
			id = identifier(s)
			if id != False: return id
			t = terminal(s)
			if t != False: return t
		def identifier(s):
			id = False
			if s[0] in letter:
				for i, c in enumerate(s[1:]):
					if c not in letter or c not in digit or c != "_":
						id = self.__dict__[s[0:i]]
			return id
		def terminal(s)
			t = False
			if s[0].isprintable():
				t = s[0]
				for i in s[1:]:
					if i.isprintable():
						t += i
					else: return t
