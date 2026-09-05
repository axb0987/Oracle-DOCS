# Setting Up Account Recovery and 2-Step Verification
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/manage_security_and_2_step_verification.htm
- Fetched: 2026-09-05 02:30 CDT

# Setting Up Account Recovery and 2-Step Verification

Set up and manage account recovery, 2-step verification, and generate bypass codes to ensure that you always have secure access to your account.
Important  
  

The tasks in this section are for users to perform to set up account recovery and 2-step verification using the options configured by an administrator. If you're an administrator that needs to set up account recovery or 2-step verification for an identity domain, see[Managing Account Recovery](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/../accountrecovery/understand-account-recovery.htm)and[Managing Multifactor Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/../mfa/understand-multi-factor-authentication.htm).

If your administrator has enabled bypass codes, we recommend that you create a bypass code and store it in a secure location, for example, write it down in a notebook. If you lose your bypass code, you also have the option to contact an administrator to obtain a bypass code for access.

Users, to learn how to generate a bypass code for yourself, see[Generating a Bypass Code](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/generate-bypass-code.htm).

Administrators, to learn how to generate a bypass code for another user, see[Generating a Bypass Code for a User](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/../users/generate-bypass-codes-user-accounts.htm).

## How Account Recovery and 2-Step Verification Work
- Administrators set up account recovery and 2-step verification for users in an identity domain by:
- choosing the recovery and verification factors available to users and
- specifying whether users must enroll.
- 
You, as a user , set up account recovery and 2-step verification using the recovery and verification factors the administrator set up either
- during your first sign in to an identity domain or
- after your first sign to an identity domain by using the self-service My profile console.

## Account Recovery

Account recovery is an automated process designed to help you regain access to you account if you have trouble signing in, if you're locked out, or you forget your password.

Note  
  
The account recovery factors that are available for you to set are dependent upon the selections your identity domain administrator or security administrator made when they set up account recovery for your identity domain. For example, if your administrator disabled mobile number as an account recovery factor, then you can't use mobile number to recover your account. Account recovery factors that aren't enabled don't appear in the Security tab of the My profile console.

You must set at least one account recovery factor. In addition to having one account recovery factor, if the option is available, always generate a bypass code and store it in a safe place. See[Generating a Bypass Code](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/generate-bypass-code.htm).

## 2-Step Verification

2-Step verification is an authentication method that requires you to use more than one way of verifying your identity, providing a second layer of security to your account.
Note  
  

The 2-step verification factors that are available for you to set are dependent upon the selections your identity domain administrator or security administrator made when they set up 2-factor verification for your identity domain. For example, if your administrator disabled email as a 2-factor verification factor, then you can't use email . 2-step verification factors that aren't enabled don't appear in the Security tab of the My profile console.

This section contains the following topics:
- [Setting Account Recovery Options](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/set-your-account-recovery-options.htm)
- [Activating 2-Step Verification](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/../mfa/enroll-2-step-verification-first-login.htm)
- [Managing 2-Step Verification](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/../mfa/manage-2-step-verification.htm)
- [Generating a Bypass Code](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/generate-bypass-code.htm)
- [Signing In to an Identity Domain Using an Alternative Login Method](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/sign-in-identity-domain-alternative-login-method.htm)
