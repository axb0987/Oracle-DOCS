# Configuring Multifactor Authentication Settings
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm
- Fetched: 2026-09-05 02:23 CDT

# Configuring Multifactor Authentication Settings

Configure multifactor authentication (MFA) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.

Note  
  
The tasks in this section are for an administrator that needs to set up MFA for an identity domain in IAM. If you're a user that needs to set up 2-step verification for yourself, see[Setting Up Account Recovery and 2-Step Verification](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/../usersettings/manage_security_and_2_step_verification.htm). Before you begin:
- Create a test user in a test identity domain. Use that identity domain to set up MFA for the first time. See[Creating an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/../domains/to-create-new-identity-domain.htm)and[Creating a User](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/../users/create-user-accounts.htm).
- Set up a client application to enable access to an identity domain using the REST API in case your Sign-On Policy configuration locks you out. If you don't set up this client application and a sign-on policy configuration restricts access to everyone, then all users are locked out of the identity domain until you contact Oracle Support. For information about setting up the client application, see[Registering a Client Application](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/register-client-app.htm).

To define MFA settings, you must be assigned to either the identity domain administrator role or the security administrator role.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- On the domain details page, select Authentication .
- On the Authentication page, select Enable or Disable factors . A settings panel opens.
- In the Enable or Disable factors settings panel, select each of the factors that you want to be required to access an identity domain.
For an explanation of each factor, see[Configuring Authentication Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-authentication-factors.htm).
- (Optional) Set the Maximum number of enrolled factors that users can configure.
- (Optional) Use the Trusted devices section to configure trusted device settings.
Similar to "remember my computer," trusted devices don't require the user to provide secondary authentication each time that they sign in.
- (Optional) Under Sign-in rules , set the maximum number of unsuccessful MFA attempts that you want to allow a user to incorrectly provide MFA verification before being locked out.
- Select Save changes , and then confirm the change.
- (Optional) Select Edit next to the MFA factors that you have selected to configure them individually.
For instructions for each factor, see[Configuring Authentication Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-authentication-factors.htm).
- Ensure that any sign-on policies that are active allow two-step authentication:
- Select the Domain policies tab.
- On the Sign-on policies page, select Default Sign-On Policy .
- On the Default Sign-On Policy page, select Sign-on rules .
- In the Default Sign-On Rule row, select the Actions menu (three dots) and select Edit sign-on rule .
- In the Edit sign-on rule dialog box, under Exclude users , exclude yourself or another identity domain administrator from this rule until testing is complete. This ensures that at least one administrator always has access to the identity domain should issues arise.
- Under Actions , select Prompt for an additional factor and ensure that Allow access is selected.
- Select Save changes .
- If other sign-on policies have been added, follow the preceding steps for each of those policies to ensure that MFA is enabled under all conditions where you want it to be enabled.

Note  
  

The settings for the default sign-on rule enable MFA globally. Settings for other sign-on rules might override the default sign-on rule for users and groups specified by conditions for those rules. See[Managing Password Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/../passwordpolicies/Managing-Password-Policies.htm).

Important  
  

Ensure you exclude one Identity Domain Administrator from each policy. This ensures that at least one administrator always has access to the identity domain should issues arise.

Set Enrollment as Optional until you're finished testing the sign-on policy.
- (Optional) Enable separate lock thresholds for MFA validation failure and MFA notification attempts. To enable this, ensure you know how to make REST API calls.

Note  
  
There are two new attributes in the user MFA schema:

- mfaIncorrectValidationAttempts —Tracks incorrect MFA validation attempts by a user.
- mfaNotificationAttempts —Tracks MFA notification attempts by a user.

Also there are two new attributes added to AuthenticationFactorSettings:
- maxMfaIncorrectValidationAttempts —The maximum number of incorrect MFA validation that can be tried before an account is locked. If a value is set for this attribute, there must also be a value set for maxMfaNotificationAttempts. If this attribute is not set, the MFA locking behavior is determined by maxIncorrectAttempts. If mfaIncorrectValidationAttempts reaches maxMfaIncorrectValidationAttempts, the user is locked immediately.
- maxMfaNotificationAttempts —The maximum number of MFA notifications that can be tried before an account is locked. If a value is set for this attribute, there must also be a value set for maxMfaIncorrectValidationAttempts. If this attribute is not set, the MFA locking behavior is determined by maxIncorrectAttempts. If the mfaNotificationAttempts reaches maxMfaNotificationAttempts, the user is locked the next time they try to initiate a notification, to allow the user to authenticate using the last MFA notification.

Update AuthenticationFactorSettings to set both`maxMfaIncorrectValidationAttempts`and`maxMfaNotificationAttempts`by doing a`PATCH`call on`< IDENTITY_DOMAIN_URL >/admin/v1/AuthenticationFactorSettings/AuthenticationFactorSettings`endpoint with following payload:

```

```

The value for both can vary from a minimum of 3 to a maximum of 10.
- To test the configuration, sign out of the Console and then sign in as the test user.
