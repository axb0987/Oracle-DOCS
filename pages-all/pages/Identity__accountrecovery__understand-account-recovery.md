# Managing Account Recovery
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/accountrecovery/understand-account-recovery.htm
- Fetched: 2026-09-05 02:16 CDT

# Managing Account Recovery

Account recovery is an automated process that allows users regain access to an identity domain in IAM if they have trouble signing in, if they're locked out, or they forget their passwords.
Note  
  
These tasks are for an administrator that needs to set up account recovery for an identity domain. If you're a user that needs to set up account recovery for yourself, see[Setting Up Account Recovery and 2-Step Verification](https://docs.oracle.com/en-us/iaas/Content/Identity/accountrecovery/../usersettings/manage_security_and_2_step_verification.htm).

Identity domain administrators and security administrators can configure the following account recovery options for users:
- Security questions: Users select and answer security questions, and provide hints for answers to these questions to verify their identity. A user must answer these questions correctly to regain access.
- Email: By default, a user's primary email address has been set as the email address that IAM uses to help the user recover their account. IAM sends a notification to this email address and the user follows the instructions in the notification to recover their account.

Note  
  
Instead of their primary email address, you can allow the user to specify an alternate (recovery) email address to regain access to their account.
- Text message (SMS): Users provide a mobile number that IAM uses to help them recover access to their account. IAM sends a passcode in a text message (SMS) to this mobile number and the user enters this passcode to recover their account.

In addition to setting account recovery factors, identity domain administrators and security administrators can specify:
- How many consecutive, unsuccessful account recovery attempts a user can make before the user's account recovery is locked.
- How long the user's account recovery is locked before they can attempt to recover their account again.

To find out how users can recover their account, see[Recovering Your Account](https://docs.oracle.com/en-us/iaas/Content/Identity/accountrecovery/../usersettings/recover-your-account.htm)
