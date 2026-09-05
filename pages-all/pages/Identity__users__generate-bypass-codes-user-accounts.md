# Generating a Bypass Code for a User
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/users/generate-bypass-codes-user-accounts.htm
- Fetched: 2026-09-05 02:30 CDT

# Generating a Bypass Code for a User

Generate a bypass code for a user in an OCI IAM identity domain. The code can be used as a one-time 2-Step Verification method to sign in.

You can increase security for user accounts by using Multi Factor Authentication (MFA) capabilities provided by IAM. MFA adds an extra layer of identity verification to the sign-on process by requiring a user to provide a second verification method, such as a one-time passcode (OTP) for the device associated with the user's account, notification, short message service (SMS), also known as a text message, or security questions.

The ability to generate a bypass code is available to the user after the user enrolls in 2-Step Verification. The user can generate a bypass code and store it for later use or request that an administrator generate a bypass code for the user. For example, when a user has forgotten their phone, doesn't have cell service, or can't access their computer, at the 2-Step Verification page, the user can contact the help desk to have an administrator generate a bypass code.

As a result, the user can use this bypass code as a one-time 2-Step Verification method to sign in.

In addition, the administrator can set when the bypass code expires, and how often the bypass code can be used for the user account.
Note  
  
The user must already be enrolled in MFA to use a bypass code or request that one is generated for the user.

- On the Users list page, select the user for which you want to generate a bypass code. If you need help finding the list page, see[Listing Users](https://docs.oracle.com/en-us/iaas/Content/Identity/users/list-user-accounts.htm).
- On the user details page, select More Actions and then select Generate bypass code .
- In the Bypass Code expiration region of the Generate bypass code window, set when the bypass code expires.
- Set the time (in days, hours, and minutes) that the bypass code will expire. After this time elapses, the user can't use the bypass code.
- If you don't want the bypass code to expire, then select Never Expires .
- In the Bypass Code use region of the Generate Bypass Code window, specify how often the bypass code can be used.
- If the bypass code can be used only one time, then select Once .
- If the bypass code can be used for a finite number of times, then select the button to the left of the text box. Enter a number in the text box that represents how many times the bypass code can be used.
- If the bypass code can be used for an unlimited number of times, then select Unlimited .
- Select Generate .
-
