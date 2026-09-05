# Enabling MFA to Authenticate into Linux
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/enable-mfa-authenticate-linux.htm
- Fetched: 2026-09-05 02:23 CDT

# Enabling MFA to Authenticate into Linux

Learn how to set up Multi Factor Authentication (MFA) so Linux users can authenticate using multiple factors.

- Enable the MFA factors for your requirements. See[Configuring Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/../mfa/configure-multi-factor-authentication-settings.htm)and[Configuring Authentication Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/../mfa/configure-authentication-factors.htm)
- Create a group for MFA, and add the POSIX Users to this group.
- Navigate to Groups &gt; Create group.
- Enter the Name of the group.
- Search for the POSIX users you want to enable for MFA.
- Select the users and select Create .
- Create a Sign-On rule.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- Select the Default Sign-On Policy .
- Select Add sign-on rule .
- Enter a Rule name , and under Conditions in the field Group membership type and select the group that you created above. Under Actions ensure that Allow access and Prompt for an additional factor is checked. Change the Enrollment to Optional and select Add sign-on rule .

Note  
  
The only sign on policy that the Linux Pluggable Authentication Module (PAM) supports, is the Default Sign-On Policy .
- Move the newly created sign-on rule to the top by selecting the sign-on rule and dragging it to the top of the list. Select Save . This ensures that this rule gets evaluated first so that users belonging to the chosen group are prompted for MFA when they sign in.
- Sign in to IAM as a user in the MFA Group, for example via`https://identity-cloud-service-instance-url/ui/v1/myconsole`
- Enroll the user in MFA and select the factors to enroll in.

Note  
  
Backup factors aren't currently supported with the IAM Linux PAM.
- After the user is enrolled in MFA, test authentication on Linux:
- SSH into your Linux environment where the IAM Linux PAM is installed.
- When prompted enter the password for the IAM user.
- Enter the second factor with which to authenticate.
