#'''@author: Saikat Dey'''

#############Install Below Command If Libs Not Available#################

#pip install smtplib email pybase64


##############Importation Libs#####################
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email_with_attachments(smtp_server, smtp_port, smtp_username, smtp_password, from_email, to_email, cc_email, subject, html_body, attachments=[]):
    try:
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Cc'] = ', '.join(cc_email) if cc_email else ''  # Include CC if provided
        message['Subject'] = subject

        ######### Create an HTML message part#########
        html_message = MIMEText(html_body, 'html')
        message.attach(html_message)

        ###########Attach files###########
        for attachment_path in attachments:
            with open(attachment_path, 'rb') as file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="{attachment_path}"')
                message.attach(part)

        ###########Combine TO and CC recipients into a single list###########
        all_recipients = [to_email] + (cc_email or [])

        #####Connect to the Inotes server#########
        server = smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=30)
        server.login(smtp_username, smtp_password)

        ########Send the email to all recipients##########
        server.sendmail(from_email, all_recipients, message.as_string())
        print('Email sent successfully')

    except Exception as e:
        print(f'Error: {str(e)}')

    finally:
        if server:
            server.quit()
            
#######################Example Variable##############
"""
smtp_server = '199999.1678.69.108'
smtp_port = 777
smtp_username = 'Secrets'
smtp_password = 'Debo Na'

# Sender and recipient email addresses
from_email = 'your_email@gmail.com'
to_email = 'saikat.dey@test.ai'
cc_email = ['test@gmail.com']
# Email subject
subject = 'Inotes Automated Mail Sending'

# HTML-formatted email body
html_body = '''<!DOCTYPE html>
<html lang="en">
<head>
	<title></title>
	<script type="text/javascript" src="https://gc.kis.v2.scr.kaspersky-labs.com/FD126C42-EBFA-4E12-B309-BB3FDD723AC1/main.js?attr=zz1JFUgzilcSz524M30TapF2e2xA6g_C2ShSQqStHbUtuIQhvfs_RJ9zFL_mHTBxRHE1SCGXFdObfUo59U4RFcQ9IdivoWgIdqZBWmVyPhcijlnqTACtzQeL_fZoSbjyrOYcPsmZjTMVsqJ08g3vcmyhc91kF2IwE9i4Vy4-wimAtkS6rKsN25NjlkfyXDYaQubFKc6C9ERtZPtY0icsKeQiVi7YKULGz2L4oFHEH9CbwYzrq_vwNnM1HXp2dvMp3cv8KQ3A9u5MWrSPenehdKzCVTrWD_LnwmLze7a-rzMKLFOkCRIBsB4Srz2nOzjfuP-6YiCj93sA5qlKTiO_xMsvWRpKnFtgbs9nxL2-Pi0lwoi6FX6kXoEKruIugSLoRRqNksgy3dikH4xIsBJzgGuh_3tsRTfRvFh6v1T1ZR_fMX6FXvUMYCIUSwop0BcHKA3pHDUE0nkPRl9kt-Prjz2psc3gbAoa0ozE-w1sduLDhFolsTHMkuEjDoLAVgm9dU5B0Npgb6FjF16XZ-R2KpTl8ySmqwpCFyhZIKK4r-Y0-UGtFVZYR8fcxa3K1srZAfdYVgM-cRJH_33DD4wFPaDwESiIvaXsmFsTJy9Y3S9nSupfYx8OE_jeilGVzOWFGrvIxJAYNhYzeTyMFyw9m5IAE49djJxCNKn_mh0nX4vLgvdadqNlVPazA3uppyMfTmFfY0D3GNUMfq4KEgdPXhkAq72qhFnefQy77lKeMFKR1M6IvXrY8PsonqtRQRsi0gN4NLfhQ0v8AQutSt4N9v5bfT9h__oDi4MfxHmql-WAG9ud2ATU5b_junDbSuzClYrRLLXCTxXOsRfe1suHHvyBlhg_jadk8xIyO9R0akS3ShVkEm8GiMY8hivydT7Nf0h48aqHQj29qrXtlHmr1raxFhdbCm8d2JpIdpPpJ6hwZ9y6eqBtMnMfEaMlknxZh38MLbKIyrNw_yQfDBOT5QCzey3qlUUlB_jRaoy9jRTfqfZQmRoqrjztrgQGKJAKyQzISuZWzekGLC6xOsSG8cmlG7Ib0HmDC8TGSTPjFtVl8mjll_YtrKGzpCbyDvMkC7Y3Ko5QFTLWbTqyFdKIs068NCg1rOtvmKoOCWr1fFchYfMhLisCpIVg-DZQYf-Kn98p3lsefzjaoc6OStl0ecXkqSTpO9cZQcTh2D41xxYYdPqsNXJJd-z2VMw4b36b-YcSips1loLk3nu9_0kgsMPSVwUbORYTzr32RyyXjyDvQeEyzuBZhkcly2mOAkRUBsWW91awAFFqU77_jgWPRL482UX2_wtwgqaS622c3BbWx-e34w16r2P8KgllYSnmYM854-ndwkhNNGtiJFKZRBmgfWnH5M9mf2E71A0AXZLyGJOo4miVq1xhpsSBdNBfSs-ryfpsXgdHVuiGFaYsaRRFi6mIxwXeBrF1dDkgZe7gVrlu5drUMxrxY_4t6G3oYJb8bmHZNJIz_PXhHhaPvokRWuo6gCT43RASMCZyVWlfk-gCrXepJoQ6s9mmSR9EH3Apy1TCB7QfwjXVnjWn4BB6n5q2TY1vcQxV8bwpQFGja11QtjZcF2IrFufCT7vHVnHadEIkCp9NXxqHpKavmMAeknU5MIufR4IqBn3-X8itjD-7yGIy_j7qOfX8_0ySmruFVluVYVf0l6oCfoBTm7aEL5BAu4Gq8vdcAFTFDDdpks4hDk70mjqQcybzZZo-LklXodwgcsb-qS7me2DtKJm4R8H4u8xqKABsy2QYstJOUwT75-oNCjvLhrSyUngozmgkV6I9WOvDVVjR7YfoSmyN73lIEmlBMDzDlaUrJF1faOjbw6q3aZVx1tDG4WCXoSE6wvDi9nfsmcd4lPT5ICkDe0AXz0QJ-_5nWf29QDR6LI1CqNjmLvOiasKdRUc4-9VTmuHcj-lWp_HYRf4RWViSYGMGrYtQGfhYSAmEYjvRkRdS0id7KFkmcNujJAWCkfFlcdcUW7AJTdO60TjB4TBex2P2ePyGoHr9MZzGLsjCOOQos6u6hrFw1GuoB2KX" charset="UTF-8"></script><style type="text/css">
		.data_charts {
			margin: auto;
		}
		.data_graph{
			height: 100px;
			width: 100px;
		}
		h3 {
			color: #100039;
		}
	</style>
</head>
<body style="font-size:110%; font-family:calibri; height: 100%; width: 100%; margin: 3px; padding: 2px">
<div id="greetings_text"><p>Hello,</p></div>
<div class="msg_body">Please be informed that DCB Inotes Mail Task completed on <span id="run_date_time">20/09/2023</span>. Please message me for Script</div>

<h5>Mail Automation Info</h5>
</body>
</html>'''
attachments = ['open_me.txt']
# Call the send_email function with the HTML-formatted body
send_email(smtp_server, smtp_port, smtp_username, smtp_password, from_email, to_email, subject, html_body)
"""
