# IAM Credentials
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-IAM_Credentials.htm
- Fetched: 2026-09-05 03:04 CDT

# IAM Credentials

IAM user credentials (Console password, API signing key, auth tokens, and customer secret keys) grant access to resources. It is important to secure these credentials to prevent unauthorized access to Oracle Cloud Infrastructure resources.

General guidelines for handling credentials include:
- 

Create a strong Console password for each IAM user, with sufficient complexity. Oracle recommends the following for a complex password:
- Password has a minimum length of 12 characters
- Password contains at least one uppercase letter
- Password contains at least one lowercase letter
- Password contains at least one symbol
- Password contains at least one number
- Rotate IAM passwords and API keys regularly, every 90 days or less. In addition to a security engineering best practice, this is also a compliance requirement. For example, PCI-DSS Section 3.6.4 states, "Verify that key-management procedures include a defined cryptoperiod for each key type in use and define a process for key changes at the end of the defined crypto period(s)."
- Do not hard code sensitive IAM credentials directly in software or documents accessible to a wide audience. Examples include code uploaded to GitHub, presentations, or documents available on the internet. There have been known, highly publicized cases of hackers breaching customer cloud accounts, using credentials inadvertently disclosed on public sites. When software applications need to access Oracle Cloud Infrastructure resources, Oracle recommends that you use instance principals. If it is not feasible to use instance principals, other recommendations include using user environment variables to store credentials, and using locally stored credential files with API keys to be used by the Oracle Cloud Infrastructure SDK or CLI.
- Do not share IAM credentials between multiple users.
- By federating the Console login through Oracle Identity Cloud Service, customers can use multifactor authentication (MFA) for IAM users, especially administrators.

When rotating API keys, verify that the rotated keys work as expected before disabling older keys. For information about generating and uploading IAM API keys, see[Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm). The high-level steps in rotating an API key are:
- Generate and upload a new API key.
- Update the SDK and CLI configuration files with the new API key.
- Verify that the SDK and CLI calls are working correctly with the new key.
- Disable the old API key. Use[ListApiKeys](https://docs.oracle.com/iaas/api/#/en/identity/latest/ApiKey/ListApiKeys)
