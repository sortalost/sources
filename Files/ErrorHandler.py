# Author: @v1s1t0r999
# [28-05-2021 @ 15:02]
#########################################################
# THIS AN ERROR HANDLING FILE FOR A FRIEND
# USAGE:
"""
import LogError

try:
    ...
    An Error Takes Place Here
    ...

except Exception as VarE:
    logError.handle(file="FileName.log",error=VarE)   
"""

########################################################

import datetime
import smtplib

now = datetime.datetime.now()

class RequiredArgument(Exception):
	pass
class SmtpException(Exception):
	pass

def handle(file,error):
	try:	
		
		if not file:
			raise RequiredArgument("Missing Required Argument: 'file'")
		if not error:
			raise RequiredArgument("Missing Required Argument: 'error'")
		date = now.strftime(f"[%d-%m-%Y @ %H:%M]->")
		F = open("Error.log","a")
		F.write(f"\n{str(date)}: {str(error)}")
		F.close()
	except Exception as e:
		print(e)

def MailAuthor(email,password,content):
	f"""Email The Author (PLEASE!!! NO SPAMMING)

	-> You need to enable "Allow Less Secure Apps" in your GMAIL Account.
	---> How to do this?? <https://myaccount.google.com/lesssecureapps>
	***
	-> Only GMAIL Accounts Are allowed!!!"""

	chk = email.endswith("@gmail.com")
	if chk==True:

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		try:
			server.login(email, password)
		except Exception as e:
			raise SmtpException(e)
		finally:
			server.sendmail(email,'aditya.funs.11@gmail.com', content)
			server.close()
	else:
		raise SmtpException("Only GMAIL.COM accounts are permitted")
