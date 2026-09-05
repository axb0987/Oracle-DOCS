# OTP in SMS Text Messages
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/0tp-texts.htm
- Fetched: 2026-09-05 02:23 CDT

# OTP in SMS Text Messages

MFA notification messages in SMS are in a standardized format for all identity domains.

SMS MFA notification messages are in the format " Your`${companyName}`one time authentication code is:`${OTP}`".

The company name field in SMS messages is populated based on the value defined in Branding settings for an identity domain.
Note  
  

A company name longer than 30 characters will be truncated in the message body. If you leave the Company name field empty, the IAM IdP tenancy name will be populated as the company name in the notification message. Please note that the tenancy name will be truncated beyond 30 characters.
