# JIT Provisioning from Okta to OCI IAM
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/jit_okta/okta_jit.htm
- Fetched: 2026-09-05 02:29 CDT

# JIT Provisioning from Okta to OCI IAM

In this tutorial, you configure Just-In-Time (JIT) provisioning between the OCI Console and Okta, using Okta as the identity provider (IdP).

You can set up JIT provisioning so that identities can be created in the target system at the time that they make a request to access the target system. This can be easier to set up than having all users created in advance.

This tutorial covers the following steps:

- Configure SAML attributes sent by Okta.
- Configure JIT attributes in OCI IAM.
- Test JIT provisioning between OCI IAM and Okta.
Note  
  
This tutorial is specific to IAM with Identity Domains.

[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/jit_okta/okta_jit.htm#)

To perform this tutorial, you must have the following:
- 

A paid Oracle Cloud Infrastructure (OCI) account, or an OCI trial account. See[Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm).
- Identity domain administrator role for the OCI IAM identity domain. See[Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/jit_okta/../../../roles/understand-administrator-roles.htm).
- An Okta account with one of the following Okta roles:
- Global Administrator
- Cloud Application Administrator
- Application Administrator

In addition, you must have completed the tutorial[SSO With OCI and Okta](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/jit_okta/../sso_okta/sso_okta.htm), and collected the object ID of the groups which you are going to use for JIT Provisioning.

[1. Configure SAML Attributes Sent by Okta](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/jit_okta/okta_jit.htm#)

In OCI IAM, update the Okta IdP for JIT.

- 

Open a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm)and enter the Console URL:

`[](https://cloud.oracle.com)https://cloud.oracle.com`
- Enter your Cloud Account Name , also referred to as your tenancy name, and select Next .
- Select the identity domain which will be used to configure SSO.
- Sign in with your username and password.
- Open the navigation menu and select Identity &amp; Security .
- Under Identity , select Domains .
- Select the identity domain in which you had configured Okta as IdP.
- Select Security in the left menu, and then Identity providers .
- Select the Okta IdP.
- Select Configure JIT.

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
- familyName:`familyName`
- primaryEmailAddress:`email`
- Select Add Row and enter:`firstName`.

For the identity domain user attribute, choose`First name`.
Note  
  
If you configured additional user attributes to be sent as part of the user assertion from Okta, you can map them to identity domain user attributes by adding additional rows.
- Select Assign group mapping .
- Enter the Group membership attribute name . In this tutorial, use`groups`.
Note  
  
Make a note of the group membership attribute name, because you'll use it in the next section.
- Select Define explicit group membership mappings .
- Under IdP group name maps to identity domain group name, do the following:
- In IdP Group name , provide name of the group in Okta.
- In Identity domain group name , and select the group in OCI IAM to map the Okta group to.

[
Note  
  
Additional groups can be mapped by selecting Add Row .

This diagram shows the attributes configured in Okta on the left, and attributes mapped in OCI IAM on the right.

[
- Under Assignment rules, select the following:
- When assigning group memberships: Merge with existing group memberships
- When a group is not found: Ignore the missing group

[
Note  
  
Select options based on your organization's requirements.
- Select Save changes .

[2. Configure JIT attributes for OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/jit_okta/okta_jit.htm#)

In Okta, update the OCI IAM app configuration to send user attributes and the group name in the SAML assertion.

- In Okta, in the enterprise application you created for OCI IAM, select the Sign On tab.
- Select Edit next to Settings.
- Under Saml 2.0, select &gt; next to Attributes (Optional) .
- Provide the following values:

Name Name format Value
`firstName``Unspecified``user.firstName`
`familyName``Unspecified``user.lastName`
`email``Unspecified``user.email`

You can add additional attributes to suit your business requirements, but you only need these for this tutorial.

[
- Under Group Attribute Statements, enter these value.
Note  
  
Okta provides a mechanism for filtering groups which can be sent in SAML Assertion. The filter has options including`Starts with`,`Equals`,`Contains`, and`Matches regex`.In this tutorial, we use the`Contains`filter, which means that Okta only sends those groups which are associated with the user and which contain the specified string. In this example, we have specified`Admin`as the string, so all the groups which contain the string`Admin`and are associated with the user, are sent in the SAML Assertion.

Name Name format Filter Value
`groups``Unspecified``Contains``Admin`

[
- Select Save .

[3. Test JIT Provisioning Between Okta and OCI](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/jit_okta/okta_jit.htm#)

In this section, you can test that JIT provisioning works between Okta and OCI IAM.
- In the Okta console, create a new user with an email Id which is not present in OCI IAM.
- Assign the user to the required groups, for example,`Administrators and Admins`.
- Log out of Okta.
- Assign the user to the OCI IAM app in Okta.

[
- In the browser, open the OCI Console.
- Select the identity domain in which JIT configuration has been enabled.
- From the sign in options, select Okta .
- On the Okta login page, provide the newly created user id.
- On successful authentication from Okta:
- The user account is created in OCI IAM.
- The user is logged into the OCI Console.

[
- In the navigation menu , select the Profile menu and then select User settings . Check the user properties such as email id, first name, last name, and associated groups.

[

[What's Next](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/jit_okta/okta_jit.htm#)

Congratulations! You have successfully set up JIT provisioning between Okta and IAM.

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developers Portal](https://developer.oracle.com/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
