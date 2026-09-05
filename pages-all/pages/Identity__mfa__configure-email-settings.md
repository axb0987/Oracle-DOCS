# Configuring Email Settings
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-email-settings.htm
- Fetched: 2026-09-05 02:23 CDT

# Configuring Email Settings

Configure settings in an identity domain in IAM to send a one-time passcode (OTP) to a user's primary email address.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- On the domain details page, select Authentication .
- On the Authentication page, in the Email row, select Edit .
- Under Configure the email settings for MFA , enter the following values:

- Passcode length: The number of characters in the passcode.
- Passcode validity: The number of minutes for which the passcode will be valid, after the passcode was sent.
- Under Configure the email settings for account recovery and account activation , enter the following values:

- Activation email validity: The number of days that the activation email remains valid. Enter a value between 1 and 30.
- Password reset email validity: The number of minutes that the password reset email remains valid. Enter a value between 1 and 43,200. This corresponds to 1 minute through 720 hours.
- To allow the user to add an alternate email address for account recovery, select the checkbox.
- Select Save changes .
- Confirm the changes when prompted.
- To access the email template that's sent to the user's primary email account and edit it as needed, follow these steps:
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- On the domain details page, select Notifications .
- On the Notifications page, go to Email templates .
- The template name is 2-Step email one-time passcode verification .
-
