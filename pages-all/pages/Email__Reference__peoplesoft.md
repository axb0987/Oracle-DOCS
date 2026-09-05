# Integrating PeopleSoft with Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/peoplesoft.htm
- Fetched: 2026-09-05 02:01 CDT

# Integrating PeopleSoft with Email Delivery

Use PeopleSoft to send emails through the Email Delivery service.

## Configure PeopleSoft to Send Email Through Email Delivery

You can use PeopleSoft to send emails through Email Delivery. Before you use PeopleSoft, you must configure Oracle Cloud Infrastructure Email Delivery in your PeopleSoft application.

Important  
  
These instructions contain sample code for your convenience and should be used as a reference. For client support, you must contact Oracle PeopleSoft customer support.
Note  
  

The following steps require familiarity with[PeopleSoft documentation](https://docs.oracle.com/cd/F13640_01/pt857pbr2/eng/pt/index.html?focusnode=home). These steps were tested on an Oracle Linux Server release 7.9 compute instance and PeopleTools version 8.53.06. Please refer to the documentation for your specific PeopleTools version.

To enable PeopleSoft to integrate with Email Delivery:
- Make sure Email Delivery is configured to send email. See[Getting Started](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted.htm).
Note  
  

SMTP credentials are required to configure PeopleSoft to use Email Delivery. Be sure to note the user name and password when you generate the SMTP credentials.
- Run the following command to view the certificate chain:
```

```
Example output:
```

```

- Extract the certificate that signed your domain. In this example, this is the last certificate (`2 s:/C=US/O=DigiCert Inc/OU=www.digicert.com/CN=DigiCert Global Root G2`). Copy and paste the certificate into a separate`DigiCert.pem`file, including the`BEGIN CERTFICATE`and`END CERTIFICATE`fields.
For example:
```

```

- Add the certificates to the PeopleSoft application.

Log into the Pure Internet Architecture (PIA) as user "PS" and import the certificates into the target environment. See[Installing Application Server-Based Digital Certificates](https://docs.oracle.com/cd/F13640_01/pt857pbr2/eng/pt/tsec/task_InstallingApplicationServer-BasedDigitalCertificates-fe7e95.html?pli=ul_d169e153_tsec)and refer to the Adding CA Authorities and Installing Root Certificates section.
- Encrypt the SMTP password in the config file.

You can encrypt the SMTP password using the PIA or the PSCipher utility.

Using the PIA
- Open the navigation menu on the PeopleSoft dashboard. Go to PeopleTools , and then select Integration Broker .
- Select Configuration , and then click Gateways . Select the default LOCAL gateway.
- Click Gateway Setup Properties . The default user ID is administrator and the default password is the password selected during setup.
- Click the Advanced Properties Page link.
- Click Password Encryption at the bottom of the page. This is where you will encrypt your password.

Using PSCipher

The PSCipher utility can be found under`$PS_CFG_HOME/webserv/<DOMAIN>/piabin`where`<DOMAIN>`is your web server domain.

Run the following command:
```

```

Note  
  

The password can have special characters so you will need to enclose the password in single quotes. For example:`./PSCipher.sh '#rpassword$){'`
- Update the SMTP settings on the PeopleSoft Application server. For more information, see[SMTP Settings](https://docs.oracle.com/cd/F13640_01/pt857pbr2/eng/pt/tsvt/concept_SMTPSettings-c07f2b.html)in the PeopleSoft documentation.

Establish an ssh connection to the PeopleSoft Application server machine (as username "opc") and do the following:
- Switch user to`psadm2`(for example,`sudo su - psadm2`).
Note  
  
`psadm2`is the PeopleTools domain user who creates and configures the Application Server domain.
- Navigate to the Appserver configuration directory.

Run the following command:
```

```

- Back up the original`psappsrv.cfg`file.
- Add the following information to the`psappsrv.cfg`file:
```

```

Note  
  

Do not include a space between the "=" and the values because the space could be counted in the value for the password, causing an authentication failure.
- Add the primary email address for the PeopleSoft application user who is trying to send notification from within the application. In this example, the user is "PS".

Log in as "PS" and do the following:
- Open the navigation menu on the PeopleSoft dashboard. Go to PeopleTools , and then select Security .
- Select User Profiles , and then click user Profiles . Find the profile for "PS".
- On the General tab, click Edit Email Addresses .
- Enter the approved sender email address as the primary email address.
- Log out of the PeopleSoft application.
- Reboot the application server using the`PSADMIN`utility. See[Using the Application Server Administration Menu](https://docs.oracle.com/cd/F13640_01/pt857pbr2/eng/pt/tsvt/task_UsingtheApplicationServerAdministrationMenu-c07e84.html?pli=ul_d173e77_tsvt).
- Test the email notification delivery.

Log into the PIA as "PS", and select Notify anywhere in the console. For example, you can do the following:
- Go to Peopletools , and then select Web Profile .
- Select Web Profile Configuration .
- Click Search , and then click PROD in the search results.
- Click Notify , enter the notification details, and then click OK .

Confirm receipt of the test email.

To debug SMTP errors (optional):
- You can add the following parameter to help with SMTP debugging:`SMTPTrace=1`

LogFence should be set to 5 to use this parameter. The system writes the log information to`SMTP<DDMM>.log`in`%PS_SERVDIR%/LOGS`by default, or the custom value set for Log Directory.

For example:
```

```

- After you set this parameter, you will need to reboot the Application server. Once this parameter is set, you can monitor the SMTP log.
- Type`ls`and find the SMTP file for the date you sent the email.
- Run the following command:
```

```

For example,
```

```

Search for any errors in the output.

## Troubleshooting

535 authentication required error occurs when sending email

To troubleshoot this issue, complete the following steps:

- Use the following method to re-encrypt the SMTP user password, and enter it in the PeopleSoft application server or process scheduler configuration file's SMTP settings.
- Open any Integration Broker node by navigating to PeopleTools , Integration Broker , Integration Setup , and then click Nodes .
- Click on the Connectors tab. Ensure it is using the HTTPTARGET Connector.
- Expand the encryption section and encrypt the SMTP user password again.
- Enter the new encrypted password in the SMTPUserPassword settings.
- Verify that the optional parameters below are set in the SMTP settings section of the configuration file even if they are not being used.
```

```

## More Information

- [SMTP Settings (PeopleSoft)](https://docs.oracle.com/cd/F13640_01/pt857pbr2/eng/pt/tsvt/concept_SMTPSettings-c07f2b.html)
- [Encrypting Passwords in the PeopleSoft Pure Internet Architecture](https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/tiba/task_EncryptingPasswords-497d0e.html)
- 

My Oracle Support:[Is There a Way to Both Authenticate And Secure Emails From PeopleSoft?](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=481254804754673&parent=SrDetailText&sourceId=3-21009447511&id=2351637.1&_afrWindowMode=0&_adf.ctrl-state=ky4avd2b6_53)
