def send_email(email:str, car_name,number_of_days,_amount_payable):
    """EMAIL SENDING USING GMAIL"""
    template = f"""
        <!DOCTYPE html>
        <html>

        <head>
            <title></title>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        </head>

        <body style="background-color: #f4f4f4; margin: 0 !important; padding: 0 !important;">
            <!-- HIDDEN PREHEADER TEXT -->
            <div style="display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: 'Lato', Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;"> We're thrilled to have you here! Get ready to dive into your new account.
            </div>
            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                <!-- LOGO -->
                <tr>
                    <td bgcolor="#2a60B7" align="center">
                        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                            <tr>
                                <td align="center" valign="top" style="padding: 40px 10px 40px 10px;"> </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td bgcolor="#2a60B7" align="center" style="padding: 0px 10px 0px 10px;">
                        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                            <tr>
                                <td bgcolor="#ffffff" align="center" valign="top" style="padding: 40px 20px 20px 20px; border-radius: 4px 4px 0px 0px; color: #111111; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; letter-spacing: 4px; line-height: 48px;">
                                    <img src="https://img.icons8.com/?size=512&id=YbPqIO0gOrT3&format=png" width="125" height="120" style="display: block; border: 0px;" />
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
                        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                            <tr>
                                <td bgcolor="#ffffff" align="left" style="padding: 20px 30px 40px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                                    <p style="margin: 0;">Dear {email}</p>
                                    <b style="margin: 0;">Thanks for patronage!</b>
                                    <p></p>
                                    <p style="margin: 0;">Your Bookings Breakdown.</p>
                                    <table>
                                      <tr>
                                        <th>Car name</th>
                                        <th>No of Days</th>
                                        <th>Total Amount</th>
                                      </tr>
                                      <tr>
                                        <td>{car_name}</td>
                                        <td>{number_of_days}</td>
                                        <td>{_amount_payable}</td>
                                      </tr>
                                    </table>
                                    <p>Cheers,</p>
                                    <p>The Monrent Rental Team</p>
                                    <i>You will be required to tender a copy of this email before and after the ride is collected</i>
                                    <i>Extra Days after booking will incure more charges</i>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
                        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                            <tr>
                                <td bgcolor="#f4f4f4" align="left" style="padding: 0px 30px 30px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 400; line-height: 18px;"> <br>
                                    <p style="text-align: center;">&copy;Monrent Rental Service</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
    """
    from email.mime.text import MIMEText
    import smtplib


    fromaddr = "davidisaac081@gmail.com"
    toaddr = email


    html = template
    msg = MIMEText(template, 'html')
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "MONRENT Receipt"

    debug = False
    if debug:
        print(msg.as_string())
    else:
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login("connect2arabeautylounge@gmail.com", "kscoszxuaxwfqmam")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()


def send_receipt(email:str,invoice_url:str):
    """EMAIL SENDING USING GMAIL"""
    template = f"""
       <!DOCTYPE html>
<html>

<head>
    <title></title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
</head>

<body style="background-color: #f4f4f4; margin: 0 !important; padding: 0 !important;">
    <!-- HIDDEN PREHEADER TEXT -->
    <div style="display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: 'Lato', Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;"> We're thrilled to have you here! Get ready to dive into your new account.
    </div>
    <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <!-- LOGO -->
        <tr>
            <td bgcolor="#FF1919" align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td align="center" valign="top" style="padding: 40px 10px 40px 10px;"> </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor="#FF1919" align="center" style="padding: 0px 10px 0px 10px;">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td bgcolor="#ffffff" align="center" valign="top" style="padding: 40px 20px 20px 20px; border-radius: 4px 4px 0px 0px; color: #111111; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; letter-spacing: 4px; line-height: 48px;"> 
                          <img src="https://img.icons8.com/?size=512&id=XeXDyAe766PV&format=png" width="230"  style="display: block; border: 0px;" />
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td bgcolor="#ffffff" align="left" style="padding: 20px 30px 40px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                            <p style="margin: 0;">Dear {email}</p>
                            <b>Thank You for your purchase</b>
                            <p>Please view your receipt <a href={invoice_url}>here</a> </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td bgcolor="#f4f4f4" align="left" style="padding: 0px 30px 30px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 400; line-height: 18px;"> <br>
                            <p style="text-align: center;">&copy;ArabeautyLounge</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
    """
    from email.mime.text import MIMEText
    import smtplib


    fromaddr = "davidisaac081@gmail.com"
    toaddr = email


    html = template
    msg = MIMEText(template, 'html')
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Payment Receipt"
    debug = False
    if debug:
        print(msg.as_string())
    else:
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login("connect2arabeautylounge@gmail.com", "kscoszxuaxwfqmam")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()