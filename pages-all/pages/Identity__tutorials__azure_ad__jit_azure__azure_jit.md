# JIT Provisioning from Entra ID to OCI IAM
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/azure_jit.htm
- Fetched: 2026-09-05 02:29 CDT

# JIT Provisioning from Entra ID to OCI IAM

In this tutorial, you configure Just-In-Time (JIT) Provisioning between between the OCI Console and Entra ID, using Entra ID as the IdP.

You can set up JIT provisioning so that identities can be created in the target system during run time, as and when they make a request to access the target system.

This tutorial covers the following steps:

- Configure the Entra ID IdP in OCI IAM for JIT.
- Update the OCI IAM app configuration in Entra ID.
- Test that you can provision from Entra ID to OCI IAM.
Note  
  
This tutorial is specific to IAM with Identity Domains.

[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/azure_jit.htm#)

To perform this tutorial, you must have the following:
- 

A paid Oracle Cloud Infrastructure (OCI) account, or an OCI trial account. See[Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm).
- Identity domain administrator role for the OCI IAM identity domain. See[Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/../../../roles/understand-administrator-roles.htm).
- An Entra ID account with one of the following Entra ID roles:
- Global Administrator
- Cloud Application Administrator
- Application Administrator

In addition, you must have completed the tutorial[SSO Between OCI and Microsoft Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/../sso_azure/azure_sso.htm), and collected the object ID of the groups which you are going to used for JIT Provisioning.

[1. Configure SAML Attributes Sent by Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/azure_jit.htm#)

In order to JIT Provisioning to work, appropriate and required SAML attributes have to be configured, which will be sent in SAML Assertion to OCI IAM by Entra ID.
- In the browser, sign in to Microsoft Entra ID using the URL:
```

```

- Navigate to Enterprise Applications .
- Select the Oracle Cloud Infrastructure Console application.
Note  
  
This is the app you created as part of[SSO Between OCI and Microsoft Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/../sso_azure/azure_sso.htm).
- In the left menu, select Single sign-on .
- In the Attributes and Claims section, select Edit .
- Verify that the attributes are properly configured:
- `NameID`
- `Email Address`
- `First Name`
- `Last Name`

If you require new claims, add them.
- Make a note of all the configured claim names. For example

`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname`

is the claim name for`First Name`.

[
- Navigate to Groups . You'll see all the groups available in Entra ID.
- Make a note of Object ids of the groups want to make part of SAML to send to OCI IAM.

[

Additional Entra ID Configurations

In Entra ID, you can filter groups based on the group name, or`sAMAccountName`, attribute.

For example, suppose only the`Administrators`group needs to be sent over using SAML:

- Select the group claim.
- In Group Claims, expand Advanced options .
- Select Filter Groups .
- For Attribute to match , select`Display Name`.
- For Match with , select`contains`.
- For String , provide the name of the group, for example,`Administrators`.

[
Using this option, even if the user in the administrator group is part of other groups, Entra ID only sends the Administrators group in SAML.
Note  
  
This helps organisations to send only the required groups to OCI IAM from Entra ID.

[2. Configure JIT Attributes in OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/azure_jit.htm#)

In OCI IAM, update the Entra ID IdP for JIT.

- 

Open a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm)and enter the Console URL:

`[](https://cloud.oracle.com)https://cloud.oracle.com`
- Enter your Cloud Account Name , also referred to as your tenancy name, and select Next .
- Select the identity domain which will be used to configure SSO.
- Sign in with your username and password.
- Open the navigation menu and select Identity &amp; Security .
- Under Identity , select Domains .
- Select the identity domain in which you have already configured Entra ID as IdP.
- Select Security from menu on the left, and then Identity providers .
- Select the Entra ID IdP.
Note  
  
This is the Entra ID IdP you created as part of[SSO Between OCI and Microsoft Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/../sso_azure/azure_sso.htm).
- On the Entra ID IdP page, select Configure JIT.

[
- On the Configure Just-in-time (JIT) provisioning page:
- Select Just-In-Time (JIT) provisioning .
- Select Create a new identity domain user .
- Select Update the existing identity domain user .

[
- Under Map User attributes:
- Leave the first row for`NameID`unchanged.
- For other attributes, under IdP user attribute select`Attribute`.
- Provide the IdP user attribute name as follows
- familyName:`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname`
- primaryEmailAddress:`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`
- Select Add Row and enter:`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname`.

For the identity domain user attribute, choose`First name`.
Note  
  
The fully qualified display name (FQDN) is from[1. Configure SAML Attributes Sent by Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/azure_jit.htm#jit-config-iam).

This diagram shows what the user attributes in OCI IAM should look like (on the right), and the mapping of user attributes between Entra ID and OCI IAM.

[
- Select Assign group mapping .
- Enter the Group membership attribute name :`http://schemas.microsoft.com/ws/2008/06/identity/claims/groups`.
- Select Define explicit group membership mappings .
- In IdP Group name , provide the Object ID of the group in Entra ID from the previous step.
- In Identity domain group name , and select the group in OCI IAM to map the Entra ID group to.

[

This diagram shows what the group attributes in OCI IAM should look like (on the right), and the mapping of group attributes between Entra ID and OCI IAM.

[
- Under Assignment rules, select the following:
- When assigning group memberships : Merge with existing group memberships
- When a group is not found : Ignore the missing group

[
Note  
  
Select options based on your organization's requirements.
- Select Save changes .

[3. Test JIT Provisioning Between Entra ID and OCI](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/azure_jit.htm#)

In this section, you can test that JIT provisioning works between Entra ID and OCI IAM.
- In Entra ID console, create a new user with an email Id which is not present in OCI IAM.
- 

Assign the user to the required groups.

[
- In the browser, open the OCI Console.
- Select the identity domain in which JIT configuration has been enabled.
- Select Next .
- From the sign on options, select Entra ID .
- On the Microsoft login page, enter the newly created user id.

[
- On successful authentication from Microsoft:
- The user account is created in OCI IAM.
- The user is logged into the OCI Console.

[
- In the navigation menu , select the Profile menu and then select User settings . Check the user properties such as email id, first name, last name, and associated groups.

[

[What's Next](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/jit_azure/azure_jit.htm#)

Congratulations! You have successfully set up JIT provisioning between Entra ID and OCI IAM.

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developers Portal](https://developer.oracle.com/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
