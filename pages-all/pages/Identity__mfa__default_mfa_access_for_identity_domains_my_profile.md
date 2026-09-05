# Default MFA Security for Identity Domains My Profile and My Apps Pages
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/default_mfa_access_for_identity_domains_my_profile.htm
- Fetched: 2026-09-05 02:23 CDT

# Default MFA Security for Identity Domains My Profile and My Apps Pages

MFA enrollment and authentication is enabled by default for My Profile and My Apps access for all users.

Default MFA security means that:
- The following phishing resistant MFA factors are enabled in the identity domain MFA settings:
- Mobile app push notification
- Mobile app passcode
- 

Fast ID Online (FIDO)

Important : At least one of these phishing resistant factors must be enabled. To review the MFA factors that are enabled in an identity domain, see[Configuring Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm).
- Users accessing My Profile and My Apps pages will be challenged for MFA, even if they've already authenticated with MFA during their current session.
- Any users who aren't enrolled in MFA, will be forced to enroll.
My Profile and My Apps example URL:
```

```

## Changing MFA Factor Settings

Review and change MFA factor settings in the security section of the domain.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- On the domain details page, select Security in the leftmost navigation area to access security options.
- Select MFA under Security in the leftmost navigation area to display the MFA settings page.
- Set MFA preferences by enabling or disabling MFA factors.

Remember : At least one phishing resistant factor must be enabled.

## Disabling Default MFA Access

Disabling the default MFA security feature isn't recommended. Oracle support must disable it for you. See[Support Requests](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm)
