# Configuring OTP Phone Calls
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-otp-phone-call.htm
- Fetched: 2026-09-05 02:23 CDT

# Configuring OTP Phone Calls

Configure passcode settings to send users in an identity domain in IAM a one-time passcode (OTP) as a phone call. Use a phone call template to configure the phone call.
Before you can configure phone call settings, you must first set up a[Vonage](https://www.vonage.com/)provider.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- On the domain details page, select Authentication .
- On the Authentication page, in the Phone call row, select Edit .
- Make any necessary changes to the Passcode length and Passcode validity duration (minutes) . These settings apply to one-time passcodes sent in phone calls.

- Passcode length: The number of characters in the passcode.
- Passcode validity duration (minutes): The number of minutes for which the passcode will be valid, after the passcode was sent.
- Configure a phone call.
- If you haven't already done so, set up your[Vonage](https://www.vonage.com/)provider. When you are ready, turn on Click here to proceed if the Vonage provider is already configured.
You can enter the Vonage provider settings only after you turn on the setting.
- Enter the Vonage provider settings .

Important  
  
You must base64 encode the Vonage private key before you upload it.
- Under Text message template , select the language for the message.

Note that IAM provides a fixed list of message variables. Select Message variables to view the available variables and variable definitions.
Note  
  

Add your company name to the Company name field on the Branding page in Settings . A company name longer than 30 characters are truncated in the message body. If you leave the Company name field, your company details don't appear in notifications such as Oracle Mobile Authenticator (OMA) when a user completes MFA enrollment.
- Select Save changes .
-
