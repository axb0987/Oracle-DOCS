# Configuring Account Recovery
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/accountrecovery/configuring-account-recovery.htm
- Fetched: 2026-09-05 02:16 CDT

# Configuring Account Recovery

Configure account recovery an identity domain in IAM so that users can regain access to an identity domain.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- On the domain details page, select Security .
- On the Security page, select Account recovery .
- Choose at least one factor to be used for account recovery.

- To allow users to answer security questions before they can recover their password, select Security Questions and then select Configure to define the settings for the security questions.
- To allow users to specify an email address to recover their password, select Email and then select Configure to define the email settings for the notifications sent to the user.

If this option is already selected and you clear the checkbox, then select Deactivate Email in the Deactivate Email? dialog box
- To allow users to specify a mobile number to recover their password, select Text Message (SMS) and then select Configure to define the settings for sending a passcode as a text message (SMS) to the user.

If this option is already selected and you clear the checkbox, select Deactivate SMS in the Deactivate SMS? dialog box.
- For Maximum consecutive unsuccessful recovery attempts , specify the number of consecutive, unsuccessful account recovery attempts after which the user's account recovery is locked. Enter a number between 1 and 99.
- For Lockout duration (minutes) , specify (in minutes) how long the user's account recovery is locked (because they exceeded the setting in Maximum consecutive unsuccessful recovery attempts ) before the user can try to recover their account again. Enter a number between 5 and 9,999.
-
