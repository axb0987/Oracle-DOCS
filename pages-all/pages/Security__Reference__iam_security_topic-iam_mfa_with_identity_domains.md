# Identity Domains Without the "Security Policy for OCI Console" Sign-On Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_with_identity_domains.htm
- Fetched: 2026-09-05 03:04 CDT

# Identity Domains Without the "Security Policy for OCI Console" Sign-On Policy

If you're using multifactor authentication (MFA) in tenancies with identity domains but without the "Security Policy for OCI Console" sign-on policy, we recommend that you set up MFA using the following Oracle best practices.

To set up MFA without the "Security Policy for OCI Console" sign-on policy:
- Read the[Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_with_identity_domains.htm#iam_security_topic-iam_mfa_with_identity_domains__prereq-identity-domains-no-sign-on-policy).
- Enable MFA. See[Step 1: Enable MFA in Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_with_identity_domains.htm#iam_security_topic-step_1_enable_mfa).
- Create a sign-on policy. See[Step 2: Create a New Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_with_identity_domains.htm#iam_security_topic-step_2__sign_on_policy).

## Prerequisites

Before you begin: Before you configure MFA, complete the following prerequisites. Skip any prerequisites that you have already completed.
- Review the MFA factors. The MFA factors available to you depend on the identity domain type you have. The Domain type shows in the Domains page of the tenancy. See[Feature Availability for Identity Domain Types](https://docs.oracle.com/iaas/Content/Identity/sku/overview.htm#features)for more information about MFA and domain types.
- Review the documentation for[Using the Oracle Mobile Authenticator App](https://docs.oracle.com/iaas/Content/Identity/mobileauthapp/use-oracle-mobile-authenticator-app.htm)to learn how to use Mobile app notification and Mobile app passcode in the Oracle Mobile Authenticator app.
- Optionally, and only during the roll out period, exclude an identity domain administrator from the "Security Policy for OCI Console" policy, so if you make any mistakes during roll out you have not locked yourself out of the Console.

As soon as roll out is complete, and you are confident that your users have all set up MFA and can access the Console, you can remove this user account.
- Identify any Identity Cloud Service groups mapped to OCI IAM groups. ( Note: Migrated tenancies only.)
- Register a client application with an identity domain administrator role to enable access to your identity domain using the REST API in case your Sign-On Policy configuration locks you out. If you don't register this client application and a Sign-On Policy configuration restricts access to everyone, then all users are locked out of the identity domain until you contact Oracle Support. For information about registering a Client Application, see[Registering a Client Application](https://docs.oracle.com/iaas/Content/Identity/mfa/register-client-app.htm).
- Create a bypass code and store that code in a secure location. See[Generating a Bypass Code](https://docs.oracle.com/iaas/Content/Identity/usersettings/generate-bypass-code.htm).

[Step 1: Enable MFA in Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_with_identity_domains.htm#)

Enable multifactor authentication (MFA) settings and compliance policies that define which authentication factors that you want to allow, and then configure the MFA factors.
Note  
  

Enable MFA for the Default identity domain as well as any secondary identity domains.
- Sign in to a tenancy with identity domains using your identity domain administrator credentials.
- Open the navigation menu and click Identity &amp; Security . Under Identity , click Domains . Locate the Default identity domain.
Note  
  
If you don't see the Default identity domain, under Compartment , choose the root compartment from the list.
- Select the Default identity domain and click Security and then MFA .
- In the Factors section, select each of the factors that you want users to be able to select.
Note  
  

The MFA factors available to you depend on the identity domain type you have. The Domain type shows in the Domains page of the tenancy. See[Feature Availability for Identity Domain Types](https://docs.oracle.com/iaas/Content/Identity/sku/overview.htm#features)for more information about MFA and domain types.
Note  
  

We recommend that you use these phishing-resistant MFA authenticators:
- 

Mobile app passcode and Mobile app notification
Note  
  
See[Using the Oracle Mobile Authenticator App](https://docs.oracle.com/iaas/Content/Identity/mobileauthapp/use-oracle-mobile-authenticator-app.htm)to learn how to use Mobile app notification and Mobile app passcode in the Oracle Mobile Authenticator app.
- 

Fast ID Online (FIDO)

For more information about MFA authenticators, see[Configuring Authentication Factors](https://docs.oracle.com/iaas/Content/Identity/passwordless/configure-auth-factors.htm).
- (Required) Always enable Bypass Code so that administrators can generate a one-time passcode as a second factor if users lose their external authenticator such as their mobile app or their FIDO key.
- (Optional) Set the Maximum number of enrolled factors that users can configure.
- (Optional) Use the Trusted devices section to configure trusted device settings.
Note  
  
Similar to "remember my computer," trusted devices don't require the user to provide secondary authentication each time that they sign in (for a defined period).
- (Optional) In the Sign-in rules section, set the Maximum unsuccessful MFA attempts that you want to allow a user to incorrectly provide MFA verification before being locked out.

[MFA factors example](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_with_identity_domains.htm#)

[
- Click Save changes , and then confirm the change.
- (Optional) Click Configure for the MFA factors that you have selected to configure them individually.

What to do next: Create a new Sign-on Policy. See[Step 2: Create a New Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_with_identity_domains.htm#iam_security_topic-step_2__sign_on_policy).

[Step 2: Create a New Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_with_identity_domains.htm#)

Create a new sign-on policy, add a rule for MFA, prioritize that rule to be the first rule that the identity domain evaluates, add the Console app to the new policy, activate the policy, and test the policy.
- Open the navigation menu and click Identity &amp; Security . Under Identity , click Domains . Select the Default identity domain and click Security and then Sign-on policies . The Default Sign-On Policy and any other sign-on policies you've defined are listed.
- Click Create sign-on policy .
- Enter the following information:
- Name : Enter OCIConsole SignOn Policy .
- Description : Enter a description for the policy.
- Click Add policy .
Note  
  

After you click Add policy , the sign-on policy is saved in a deactivated state. You must activate the policy to use it.
- In the Add sign-on rules screen, click Add sign-on rule to add a sign-on rule to this policy.
- Use the following table to configure the new MFA rule.
Note  
  

You can create more sign-on rules as you need them and then prioritize them to specify which rules are processed first. Evaluation stops at the first matching rule. If there is no matching rule, access is denied.

Field Description
Rule name

Enter a name. Enter the name of the sign-on rule. For example name it, MFA for OCI Console to enable MFA for all users. Or name it MFA for OCI Console Administrators to enable MFA for administrators.
Authenticating identity provider (Optional) Enter or select all identity providers used to authenticate the user accounts evaluated by this rule. If you leave this empty, the other conditions are used for authentication.
Group membership

Enable MFA for all users by entering or selecting the groups that users must be a member of to meet the criteria of this rule.

Best practice. Enable MFA for all users using Group membership .

If you can't enable MFA for all users at this time, we recommend that you enable MFA for following groups which grant administrative privileges to users in the Console:
- All groups through which OCI permissions are granted in an IAM policy.
- The Administrators group in the Default identity domain.
- Any Identity Cloud Service groups mapped to OCI IAM groups. ( Note: Migrated tenancies only.)

Important: If you leave Group membership empty and uncheck Administrator , all users are included in this rule.
Administrator

Users assigned to the Administrator roles in the identity domain are included in this rule.

Best practice. Use Group membership to enable MFA for all users or, at the least, all administrators. If you can't enable MFA for all users or administrators at this time using group membership, select Administrator to include administrators in this rule.

Important: If you create a rule for Administrators only, you must create a second rule without MFA for non-administrators to sign in. If the second rule is not created, Console access is blocked for non-administrators.
Exclude users

Best practice. Best practice is not to exclude any users. However, when you are setting up MFA, you can temporarily exclude an administrator account in case you make changes which lock you out of the OCI Console. After roll out is complete, and your users have MFA configured so that they can access the OCI Console, change this back so that no users are excluded from the rule.

See[Identity Domains Without the "Security Policy for OCI Console" Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_with_identity_domains.htm)for a list of prerequisites.
Filter by client IP address There are two options associated with this field: Anywhere and Restrict to the following network perimeters .
- 

If you select Anywhere , then users can sign in to the identity domain using any IP address.
- 

If you select Restrict to the following network perimeters , then the Network perimeters text box appears. In this text box, enter or select network perimeters that you defined. For more information, see[Creating a network perimeter](https://docs.oracle.com/iaas/Content/Identity/networkperimeters/add-network-perimeter.htm). Users can sign in to the identity domain using only IP addresses that are contained in the defined network perimeters.
Allow access or Deny access

Select whether a user will be allowed to access the Console if the user account meets the criteria of this rule. When you select Allow access , the following additional options are presented.

Best practice. Choose Allow access .
Prompt for reauthentication

Select this checkbox to force the user to re-enter credentials to access the assigned application even when there's an existing identity domain session.

When selected, this option prevents Single Sign On for the applications assigned to the Sign On policy. For example, an authenticated user must sign on to a new application.

If not selected, and the user has previously authenticated, they can access the application using their existing Single Sign On session without needing to enter credentials.

Best practice. Turn off Prompt for reauthentication .
Prompt for an additional factor

Select this checkbox to prompt the user for an additional factor to sign in to the identity domain.

If you select this checkbox, then you must specify whether the user is required to enroll in multifactor authentication (MFA) and how often this additional factor is to be used to sign in.

Select Any factor to prompt the user to enroll and verify any factor enabled in the MFA tenant level settings.

Select Specified factors only to prompt the user to enroll and verify a subset of factors enabled in the MFA tenant level settings. After you select Specified factors only , you can select factors that must be enforced by this rule.

Best practice. Choose Specified factors only and then choose any factors except Email or Phone Call .

Always enable Bypass Code .
Frequency

Best practice. Choose Every time .
- 

Select Once per session or trusted device , so that for each session that the user has opened from an authoritative device, they must use both their user names and passwords, and a second factor.
- 

Select Every time , so that each time users sign in from a trusted device, they must use their user names and passwords, and a second factor. Best practice. Choose Every time .
- 

Select Custom interval , and then specify how often users must provide a second factor to sign in. For example, if you want users to use this additional factor every two weeks, then click Number , enter 14 in the text field, and then click the Interval drop-down menu to select Days . If you configured multifactor authentication (MFA), then this number must be less than or equal to the number of days a device can be trusted according to MFA settings. For more information, see[Managing Multifactor Authentication](https://docs.oracle.com/iaas/Content/Identity/mfa/understand-multi-factor-authentication.htm).
Enrollment

This menu contains two options: Required and Optional .
- 

Select Required to force the user to enroll in MFA.
- 

Select Optional to give users the option of skipping enrolling in MFA. Users see the inline enrollment setup process after they enter their user name and password, but can click Skip . Users can then enable MFA later from the 2–Step Verification setting in the Security settings of My Profile. Users aren't prompted to set up a factor the next time that they sign in.

Note: If you set Enrollment to Required , and later change it to Optional , the change only affects new users. Users already enrolled in MFA will not see the inline enrollment process and will not be able to click Skip when signing in.

[MFA sign-on rule example](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_with_identity_domains.htm#)

[
- Click Add sign-on rule .
Note  
  
If you create an MFA rule for Administrators only, you must create a second rule without MFA for non-administrators to sign in. If the second rule is not created, Console access is blocked for non-administrators.
- Add the Console app to the OCIConsole SignOn Policy policy. Important: To ensure that your policy applies to Console access only and that it doesn't apply to any other applications, only add the Console app.
- On the sign-on policy details page, click Apps . The list of applications already added to the policy is displayed.
- Click Add app .
- In the Add app window, locate Console app, and select the checkbox for the app. Then, click Add app .
Note  
  
If you don't see the Console app, it is already assigned to a policy.

[OCI Console app added to a sign-on policy example](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_with_identity_domains.htm#)

[
- 
- Activate the sign-on policy and MFA is enabled. Users will be prompted to enroll in MFA the next time they sign in.
- In the Sign-On Policies page, click OCIConsole SignOn Policy .
- Click Activate sign-on policy .
- Sign out of identity domains.
- Sign in to identity domains. You should be prompted for MFA enrollment. Complete MFA enrollment using the Oracle Mobile Authenticator (OMA). See[Using the Oracle Mobile Authenticator App](https://docs.oracle.com/iaas/Content/Identity/mobileauthapp/use-oracle-mobile-authenticator-app.htm).

[MFA enrollment screen example](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_with_identity_domains.htm#)

[
