
"""
A vCard implementation complying with the 4.0 specification in RFC 6350.
http://tools.ietf.org/html/rfc6350
"""

import pyparsing as pp

version="4.0"

class vCard(object):
	def load(self, stream):
		# "Core" ABNF from rfc5234
		CRLF = pp.Literal("\r\n")
	#	VCHAR = 
		WSP = pp.Word(" \t", exact=1)
		NON_ASCII = 
		vcard = pp.Literal("BEGIN:VCARD") + CRLF + pp.Literal("VERSION:" + \
				version) + CRLF + pp.OneOrMore(contentline) + \
				pp.Literal("END:VCARD") + CRLF
		contentline = pp.Optional(group + pp.Literal(".")) + name + \
				pp.ZeroOrMore(pp.Literal(";") + param) + pp.Literal(":") + \
				value + CRLF
		group = pp.Word(alphanums + "-")
		name = pp.oneOf("SOURCE KIND FN N NICKNAME PHOTO BDAY ANNIVERSARY \
				GENDER ADR TEL EMAIL IMPP LANG TZ GEO TITLE ROLE LOGO ORG \
				MEMBER RELATED CATEGORIES NOTE PRODID REV SOUND UID \
				CLIENTPIDMAP URL KEY FBURL CALADRURI CALURI XML".split(), \
				caseless=True) | iana-token | x-name
		iana-token = group
		x-name = pp.oneOf(["x-", "X-"]) + group
		param = language_param | value_param | pref_param | pid_param | \
				type_param | geo_parameter | tz_parameter | sort_as_param | \
				calscale_param | any_param
		param_value = pp.CharsNotIn('"') | pp.QuotedString('"')
		any_param = (iana-token | x-name) + pp.Literal("=") + param_value + \
				pp.ZeroOrMore(pp.Literal(",") + param_value)
		value = 


		vcard_entity = pp.OneOrMore(vcard).leaveWhitespace()
	def dump(self):
		pass


