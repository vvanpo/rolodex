"""
Attempted implementation of extended BNF parser
http://standards.iso.org/ittf/PubliclyAvailableStandards/s026153_ISO_IEC_14977_1996(E).zip
"""

class SyntaxError(Exception):
	pass

class Rules(object):
	def __init__(self, stream):
		# Operator precedence

