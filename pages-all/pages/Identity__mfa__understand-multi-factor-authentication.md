# Managing Multifactor Authentication
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/understand-multi-factor-authentication.htm
- Fetched: 2026-09-05 02:24 CDT

# Managing Multifactor Authentication

Multifactor Authentication (MFA) is a method of authentication that requires the use of more than one factor to verify a user's identity to access an identity domain in IAM.
Note  
  
The tasks in this section are for an administrator that needs to set up MFA for an identity domain in IAM. If you're a user that needs to set up 2-step verification for yourself, see[Setting Up Account Recovery and 2-Step Verification](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/../usersettings/manage_security_and_2_step_verification.htm).

With MFA enabled in an identity domain, when a user signs in to an application, they're prompted for their username and password, which is the first factor – something that they know. The user is then required to provide a second type of verification. The two factors work together to add an additional layer of security by using either additional information or a second device to verify the user's identity and complete the sign in process.

MFA may include any two of the following:

- 

Something that you know , such as a passcode.
- 

Something that you have , such as a device.
- 

Something that you are , such as a fingerprint.

Users are increasingly connected, accessing their accounts and applications from anywhere. As an administrator, when you add MFA on top of the traditional username and password, you reduce the likelihood of online identity theft and fraud, which secures your business applications even if an account password is compromised.

This section contains the following topics:
- [Securing IAM MFA with Oracle Best Practices](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/understand-multi-factor-authentication.htm#understand-multi-factor-authentication__iam-domains-mfa-best-practice)
- [Using MFA in Restricted Realms](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/understand-multi-factor-authentication.htm#understand-multi-factor-authentication__mfa-restr-realms)
- [Default MFA Security for Identity Domains My Profile and My Apps Pages](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/default_mfa_access_for_identity_domains_my_profile.htm)
- [Using Mobile Authenticator Apps with MFA](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/learn-using-mobile-authenticator-app-mfa.htm)
- [Multifactor Authentication Authorization Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/multi-factor-authentication-authorization-flows.htm)
- [Registering a Client Application](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/register-client-app.htm)
- [Configuring Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm)
- [Configuring Authentication Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-authentication-factors.htm)

## Securing IAM MFA with Oracle Best Practices

If you're using MFA with identity domains in IAM, we recommend that you set up MFA using Oracle best practices. See[IAM MFA](https://docs.oracle.com/iaas/Content/Security/Reference/iam_security_topic-IAM_MFA.htm)in the Security guide.

## Using MFA in Restricted Realms
