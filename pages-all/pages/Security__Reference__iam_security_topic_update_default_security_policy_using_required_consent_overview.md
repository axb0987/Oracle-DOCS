# Modifying and Restoring Oracle Security Defaults Using the Required Consents
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic_update_default_security_policy_using_required_consent_overview.htm
- Fetched: 2026-09-05 03:04 CDT

# Modifying and Restoring Oracle Security Defaults Using the Required Consents

You can modify the Oracle security defaults for the "Security Policy for OCI Console" sign-on policy for an identity domain after providing explicit modification consent . You can also restore the Oracle security defaults after providing restoration consent .

Oracle has implemented the "Security Policy for OCI Console" sign-on policy for all domains to safeguard the Console. This policy enforces multifactor authentication with phishing-resistant factors to be prompted for each sign-in attempt to the Console, protecting its resources.

To guarantee that the identity domain's Oracle security defaults is always maintained, explicit consent must be recorded whenever you modify the Oracle security defaults provided by Oracle. The system sends an email notification to all identity domain administrators alerting them of any modifications.
Note  
  
A maximum of 50 identity domain administrators receive the email notification.

To understand more about policies and roles, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm),[Understanding Administrator Roles](https://docs.oracle.com/iaas/Content/Identity/roles/understand-administrator-roles.htm), and[Understanding Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm#understand_policies.htm).

The following changes to the Oracle security defaults of the "Security Policy for OCI Console" sign-on policy require explicit consent:
- Adding new rules
- Deleting any Oracle default security rules
- Resequencing any Oracle default security rules
- Modifying any Conditions (including Group membership) or Actions in the Oracle default security rules
- Restoring the "Security Policy for OCI Console" to the Oracle security defaults

Important  
  
Oracle sends three email reminders to all tenancy and domain administrators, reminding them to review the "Security Policy for OCI Console" sign-on policy for each of their domains and to either keep any customizations to the policy or restore the policy to the Oracle security defaults. After three email reminders, at least one administrator must provide consent before you can continue working in the Console.

This section contains the following topics:
- [Modifying the Domain's Oracle Security Defaults](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic_update_default_security_policy_using_required_consent_overview.htm#iam_security_topic_change_security_policy_for_oci_console)
- [Deleting Resources That Belong to the Domain's Oracle Security Defaults](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic_update_default_security_policy_using_required_consent_overview.htm#iam_security_topic_delete_resources_security_policy_for_oci_console)
- [Restoring the Domain's Oracle Security Defaults](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic_update_default_security_policy_using_required_consent_overview.htm#iam_security_topic_restore_security_policy_for_oci_console_defaults)
- [Recording Consent for Changes to the Oracle Security Defaults That Were Made Without Recorded Consent](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic_update_default_security_policy_using_required_consent_overview.htm#untitled1)
- [Viewing the "Security Policy for OCI Console" Sign-On Policy Consents](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic_update_default_security_policy_using_required_consent_overview.htm#iam_security_topic_view_security_policy_for_oci_console_consents)
- [Security Policy for OCI Console Consent FAQs](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic_update_default_security_policy_using_required_consent_overview.htm#identity_security_policy_for_oci_console_consent_faqs)

## Modifying the Domain's Oracle Security Defaults

Modifying the "Security Policy for OCI Console" sign-on policy, either through the Console or through the API, requires explicit consent from the identity domain administrators. An email will then be sent to other identity domain administrators with details of the change.

To manage sign-on policies, you must have one of the following access grants:
- Be a member of the Administrators group
- Be granted the identity domain administrator role
- Be a member of a group granted`manage identity-domains`

Note  
  

- 
Important  
  
If you're using Oracle Identity Cloud Service (IDCS) stripes that haven't been migrated to IAM identity domains, you can't modify the "Security Policy for OCI Console" using the Admin Console. To make changes to this policy, you must use the API instead. Note that the Admin Console UI doesn't support modifications to the "Security Policy for OCI Console"
- After the modification consent is provided, you can make changes to the policy without any additional consents. After the "Security Policy for OCI Console" sign-on policy is restored to the Oracle security defaults, any subsequent change will require consent.
Important  
  
To restore the Oracle security defaults, you must click Restore defaults . Don't manually revert the changes to the Oracle security defaults.
- Consent emails can be sent to a maximum of 50 identity domain administrators.
- Identity domain administrators can restore a modified "Security Policy for OCI Console" sign-on policy to the Oracle security defaults at any time. See[Restoring the Domain's Oracle Security Defaults](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic_update_default_security_policy_using_required_consent_overview.htm#iam_security_topic_restore_security_policy_for_oci_console_defaults).

### Modifying the Oracle Security Defaults Using the Console

To modify the Oracle security defaults in the sign-on policy, you must provide explicit consent and a justification.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- Click Security , and then click Sign-on policies .
- In the Sign-on policies page, click the "Security Policy for OCI Console" sign-on policy.
- Make your changes ans record consent. Click Predefined Category or click Other to enter the supporting justification. See[Updating a Sign-On Policy](https://docs.oracle.com/iaas/Content/Identity/signonpolicies/modify-sign-policy.htm)for more details about modifying sign-on policies in the Console.

### Modifying Oracle Security Defaults Using the API
To modify the "Security Policy for OCI Console" sign-on policy, use the following API operations:
Note  
  
For information about accessing the REST API, see[Using OAuth 2 to Access the REST API](https://docs.oracle.com/iaas/Content/Identity/api-getstarted/OATOAuthClientWebApp.htm).
- `/Policies`
- `/Rules`
- `/ConditionGroups`
- `/Conditions`

Note  
  

- All these APIs accept consent , justification , and reason similar to the Console.
- The API operation is blocked if no explicit consent is provided. The consent, justification, or reason only apply to the "Security Policy for OCI Console" sign-on policy.

Example Request Body
```

```

Example Response Body
```

```

### Deleting Resources That Belong to the Domain's Oracle Security Defaults

To delete the resources that belong to the "Security Policy for OCI Console" sign-on policy, they must be dereferenced from their parent object.

Rules, Conditions and Condition Groups are part of the Policy object. See the following list of the parent-child references for the objects:
- Rule is referenced in Policy
- Condition Group is referenced in Rule
- Condition is referenced in Rule or Condition Groups

#### Deleting Resources Using the Console

To remove a sign-on rule from the "Security Policy for OCI Console" sign-on policy:
- On the sign-on policy details page, select the checkbox for each sign-on rule that you want to delete from the policy.
- Click Remove sign-on rule .
- Click the Consent checkbox and enter a justification.
- In the confirmation window, click Remove sign-on rule .

#### Deleting Resources Using the API

Dereferencing must be done using a PUT or PATCH operation on the corresponding parent object before removing the required child object.

Example Request Body
```

```

Example Response Body
```

```

## Restoring the Domain's Oracle Security Defaults

You can restore the "Security Policy for OCI Console" sign-on policy to the Oracle security defaults after providing restoration consent .

To restore the default security settings for the "Security Policy for OCI Console" sign-on policy, you must provide explicit consent and a justification. An email will then be sent to other identity domain administrators with details of the restoration.
Note  
  

- Restoration emails can be sent to a maximum of 50 identity domain administrators.
- Identity domain administrators can restore a changed "Security Policy for OCI Console" sign-on policy sign-on policy to the Oracle security defaults at any time.

During restoration of the "Security Policy for OCI Console" sign-on policy, the following actions are performed:
- If any of the phishing-resistant factors aren't enabled for the policy, then restoration enables the following factors:
- Mobile app push notification
- Mobile app passcode
- Fast ID Online (FIDO)
- Only the rules seeded by Oracle are restored, even if the rule was deleted. Any custom rules are removed from the policy.
- If an administrator's group is deleted or renamed, during restoration, a new administrator's group is created without any members or roles and assigned to the MFA for administrators sign-on rule. The administrator's group name differs depending on the identity domain. Use the following list to find the correct group name:
- Administrators group: In default identity domains.
- Domain_Administrators group: In secondary identity domains.
- IDCS_Administrators group: For IDCS stripes migrated to OCI identity domains.
- If a custom policy has been attached or no policy has been attached to the OCI Console application, on restoration this policy is attached to the "Security Policy for OCI Console" sign-on policy.

### Restoring the Oracle Security Defaults Using the Console

To restore the "Security Policy for OCI Console" sign-on policy to the Oracle security defaults, access the sign-on policy details page and click Restore defaults and provide the consent.
Important  
  
To restore the Oracle security defaults, you must click Restore defaults . Don't manually revert the changes to the Oracle security defaults.

See[Updating a Sign-On Policy](https://docs.oracle.com/iaas/Content/Identity/signonpolicies/modify-sign-policy.htm)for more details about modifying sign-on policies in the Console.

### Restoring the Oracle Security Defaults Using the API

To restore a policy to Oracle security defaults, make a POST call using the`/RestoreOciConsolePolicy`API operation.

Example Request Body
```

```

Example Response Body
```

```

## Recording Consent for Changes to the Oracle Security Defaults That Were Made Without Recorded Consent

Oracle requires explicit consent for changes to the "Security Policy for OCI Console" sign-on policy. If you've made changes without consent, you must provide it now.
Note  
  

If you haven't made any changes to the "Security Policy for OCI Console" and are still prompted for consent, complete the following steps:
- On the Review sign-on policy changes page, select the option Restore to default security posture .
- Enter the Reason as "Default Domain Henosis Migration."
- Select Save Changes .

### Recording Consent for Changes If You Haven't Done So

If you've modified the "Security Policy for OCI Console" sign-on policy without providing consent, Oracle now requires it. You'll be prompted to review and address any deviations from the Oracle security defaults.

Any of the following changes alert Oracle that the "Security Policy for OCI Console" sign-on policy has deviated from the Oracle security defaults:
- The sign-on policy hasn't been attached to the "OCI Console Application."
- The sign-on policy is deactivated.
- Adding new rules.
- Deleting any Oracle default security rules.
- Resequencing any Oracle default security rules. The policy should only contain 2 sign-on rules:
- 1. MFA for administrators and
- 2. MFA for all users which have been created by Oracle in the same preferential order.
- Modifying any Oracle default security rules.

If the "Security Policy for OCI Console" sign-on policy has deviated from the Oracle security defaults, you must provide explicit consent to either retain the current state of the policy or restore it to the Oracle security defaults. To review the sign-on policy, sign in to the Console as a tenancy administrator or domain administrator. Once signed in, the "Review sign-on policy changes" page will be displayed, where you can make one of the following choices and then save the change:
- Keep changes : Select this option if the sign-on policy changes meet your custom requirements and you want to keep them. By accepting consent, you acknowledge the risks of deviating from Oracle's security defaults. We will record your consent and notify the identity domain administrators in an email.
Note  
  
A maximum of 50 identity domain administrators receive the email notification. See[Modifying the Oracle Security Defaults Using the Console](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic_update_default_security_policy_using_required_consent_overview.htm#iam_security_topic_change_security_policy_for_oci_console__change-default-security-posture_console)for more details.
- Restore to default policy : Select this option to revert to the Oracle security defaults. By accepting consent, you agree to restore all elements of the "Security Policy for OCI Console" sign-on policy, including phishing-resistant factors, to the Oracle security defaults. Restoration consent is recorded, and email notifications are sent to the identity domain administrators of the respective domain.
Note  
  
A maximum of 50 identity domain administrators receive the email notification. See[Restoring the Domain's Oracle Security Defaults](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic_update_default_security_policy_using_required_consent_overview.htm#iam_security_topic_restore_security_policy_for_oci_console_defaults)for more details.

After consent is recorded, you'll not be prompted again when signing in.

## Viewing the "Security Policy for OCI Console" Sign-On Policy Consents

Use the identity domains API to view the recorded modification consents and restoration consents for an identity domain.

To view the consents in an identity domain, make a GET call using the`/OciConsoleSignOnPolicyConsents`API operation.

The`changeType`of the consent indicates the current consent status of the identity domain and can be one of the following types:
- No entry: No consent has ever been recorded for the identity domain.
- MODIFIED: Modification consent has been recorded for the identity domain and the "Security Policy for OCI Console" sign-on policy has been modified from the Oracle security defaults.
- RESTORED_TO_FACTORY_DEFAULTS: Restoration consent has been recorded for the identity domain and the "Security Policy for OCI Console" sign-on policy is configured to the Oracle security defaults.

[Viewing Consents Using the Console](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic_update_default_security_policy_using_required_consent_overview.htm#)

You can't perform this action in the Console.

[Viewing All Consents Using the API](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic_update_default_security_policy_using_required_consent_overview.htm#)

Example Response Body (view all consents)
```

```

Example Response Body (view all consents)
```

```

[Viewing the Latest Consent Using the API](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic_update_default_security_policy_using_required_consent_overview.htm#)

Example Request Body (view latest consent)
```

```

Example Response Body (view latest consent)
```

```

## Security Policy for OCI Console Consent FAQs

Read about the frequently asked questions when providing consent for the Oracle-seeded Security Policy for OCI Console sign-on policy.

1. When is the consent screen displayed?

The consent screen is displayed when customers have modified the Oracle-seeded Security Policy for OCI Console or if the Security Policy for OCI Console isn't active.

2. Is consent mandatory?

Yes, consent is mandatory per Oracle security guidelines. Any customer who deviates from the Oracle-seeded Security Policy for OCI Console must either provide explicit consent or restore to the Oracle-seeded Security Policy for OCI Console to Oracle's default security posture.

3. How do you know if the Security Policy for OCI Console has changed?
If the Security Policy for OCI Console has been modified from the Oracle-seeded version, the system detects the deviations and flags them for review.
Note  
  
The sign-on policy information can be checked using the following steps:
- Sign in to the Console.
- Select Security , and then select Sign-in policies .
- In the Sign-on policies page, find the Security Policy for OCI Console sign-on policy and select it.
- On the Sign-on policy details page, in the Sign-on policy information tab, confirm the consent information.

4. What happens if the policy hasn't changed but you see the consent screen?

If you haven't made any modifications but still see the consent request, verify whether the policy is active.
- If the policy is inactive , you must either activate it or provide consent to proceed. See[Activating a Sign-On Policy](https://docs.oracle.com/iaas/Content/Identity/signonpolicies/activate-sign-policies.htm).
- If the policy is active , complete the steps in the note[here](https://docs.oracle.com/iaas/Content/Security/Reference/iam_security_topic_update_default_security_policy_using_required_consent_overview.htm#:~:text=provide%20it%20now.-,Note,-If%20you%20haven%27t).

5. What if I'm never prompted for consent and there's a change in the default OCI Console Sign-on Policy?

If you're not being prompted for consent, record the complete`har`file of the OCI Console access and contact support.

6. Who needs to provide consent?

Any customer who has modified the Oracle-seeded Security Policy for OCI Console or is using an external identity provider (IdP) with a custom security policy must provide explicit consent to continue using their customized settings.

7. What happens if I've configured MFA in an external IdP or modified the policy to meet my security requirements?

If you're using an external identity provider (IdP) for multifactor authentication (MFA) or have customized the policy, you must provide consent acknowledging the deviation from the Oracle-seeded Security Policy for OCI Console. This will ensure that your custom security settings remain in place.

8. Will providing consent change the current security posture?

No, providing consent only records the acknowledgment and doesn't alter the existing security posture. There will be no change in the user sign-on experience.

9. If I restore the Security Policy for OCI Console, what will happen?

Restoring the policy overrides any custom-configured policy. This might lead to changes in the user sign-on experience.

10. Why do I keep getting notifications to provide consent despite already accepting it multiple times?

Oracle sends multiple consent notifications to ensure they're not missed. If you've already provided consent for the Security Policy for OCI Console sign-on policy, then you can ignore the additional notifications.

11. What happens if I try to restore the Security Policy for OCI Console to Oracle's default security posture? Will current users must reauthenticate and register new MFA factors?
- This depends on your current policy configuration and the multifactor authentication (MFA) factors it supports. The Oracle-seeded Security Policy for OCI Console only supports FIDO, OMA Push, and TOTP .
-
