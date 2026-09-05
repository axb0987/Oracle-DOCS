# Identity Domains With the "Security Policy for OCI Console" Sign-On Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_identity_domains_signon_policy.htm
- Fetched: 2026-09-05 03:04 CDT

# Identity Domains With the "Security Policy for OCI Console" Sign-On Policy

If you're using multifactor authentication (MFA) in tenancies with identity domains with the "Security Policy for OCI Console" sign-on policy, then we recommend that you set up MFA using this sign-on policy.

## MFA Enablement Plan

To enhance security, we've started seeding the "Security Policy For OCI Console" sign-on policy in all tenancies. As soon as an identity domain has been seeded with the policy, you should activate it to enable multifactor authentication (MFA) for users with administrative privileges.

The following flowchart outlines the complete process from policy rollout, where Oracle initiates the seeding of the policy, to the policy enforcement stage, during which Oracle will activate the policy except under specific circumstances.

[

- The "Security Policy for OCI Console" sign-on policy only affects access to the OCI Console. After the policy is activated, all local users must use MFA to sign in to the Console.
- The policy applies to the Default domain and all secondary domains.

We will not automatically activate the policy:
- If you have modified the default sign-on policy
- If you already have a sign-on policy and the OCI Console is explicitly assigned to it.
- If an active external IDP (SAML/Social or X.509) is configured in the IAM domain. This means that federated users are excluded from the impact of this policy.
- If you delete the "Security Policy for OCI Console" using an API, we won't re-create it. To delete the policy using REST APIs, see[Delete a Policy](https://docs.oracle.com/en/cloud/paas/identity-cloud/rest-api/op-admin-v1-policies-id-delete.html).

For you to activate the policy in an identity domain, see[Activating a Sign-On Policy](https://docs.oracle.com/iaas/Content/Identity/signonpolicies/activate-sign-policies.htm).

When it's been activated, it'll look like this in the Sign-on policies page in the Console.

[

To learn more about the policy, see[About the "Security Policy for OCI Console" Sign-On Policy](https://docs.oracle.com/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_identity_domains_signon_policy.htm#iam_security_topic-iam_mfa_identity_domains_signon_policy__about-identity-domains-sign-on-policy).

## Enforcement Rules for "Security Policy for OCI Console" for Identity Domains in IAM

Sign-on Policy "Security Policy For OCI Console" status You have modified the Default Sign-on Policy Sign-on Policy "Security Policy For OCI Console" status after forcing enablement
Present and Enabled Not applicable (you can't have another active sign-on policy for the OCI Console) No change
Present and Disabled No The policy is changed to Present and Enabled
Present and Disabled Yes No change. We won't overwrite your policy.
Deleted Not applicable No change

## Setting Up the "Security Policy for OCI Console" Sign-On Policy

To set up the "Security Policy for OCI Console" sign-on policy:
- Read[Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_identity_domains_signon_policy.htm#iam_security_topic-iam_mfa_identity_domains_signon_policy__prereq-identity-domains-sign-on-policy).
- Read[About the "Security Policy for OCI Console" Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_identity_domains_signon_policy.htm#iam_security_topic-iam_mfa_identity_domains_signon_policy__about-identity-domains-sign-on-policy).
- Optionally and only during the roll out period, exclude an administrator from the policy. When you're confident that your users have set up MFA for their accounts, add that account back in to the "Security Policy for OCI Console". See[Temporarily Exclude an Administrator From the "Security Policy for OCI Console" Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_identity_domains_signon_policy.htm#exclude-admins-users-sign-on-policy).
Note  
  
It is a security risk to have a user able to sign in without MFA, so if you choose to do this do it for as short a time as possible.
- Learn how to enroll in MFA using a mobile app passcode or a mobile app notification. See[Completing MFA Enrollment](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_no_identity_domains.htm#enroll-mobile-app-passcodes-notifications).

## Prerequisites

Before you begin: Before you configure MFA, complete the following prerequisites. Skip any prerequisites that you have already completed.
- Review the MFA factors. The MFA factors available to you depend on the identity domain type you have. The Domain type shows in the Domains page of the tenancy. See[Feature Availability for Identity Domain Types](https://docs.oracle.com/iaas/Content/Identity/sku/overview.htm#features)for more information about MFA and domain types.
- Review the documentation for[Using the Oracle Mobile Authenticator App](https://docs.oracle.com/iaas/Content/Identity/mobileauthapp/use-oracle-mobile-authenticator-app.htm)to learn how to use Mobile app notification and Mobile app passcode in the Oracle Mobile Authenticator app.
- Optionally, and only during the roll out period, exclude an identity domain administrator from the "Security Policy for OCI Console" policy, so if you make any mistakes during roll out you have not locked yourself out of the Console.

As soon as roll out is complete, and you are confident that your users have all set up MFA and can access the Console, you can remove this user account.
- Identify any Identity Cloud Service groups mapped to OCI IAM groups. ( Note: Migrated tenancies only.)
- Register a client application with an identity domain administrator role to enable access to your identity domain using the REST API in case your Sign-On Policy configuration locks you out. If you don't register this client application and a Sign-On Policy configuration restricts access to everyone, then all users are locked out of the identity domain until you contact Oracle Support. For information about registering a Client Application, see[Registering a Client Application](https://docs.oracle.com/iaas/Content/Identity/mfa/register-client-app.htm).
- Create a bypass code and store that code in a secure location. See[Generating a Bypass Code](https://docs.oracle.com/iaas/Content/Identity/usersettings/generate-bypass-code.htm).

## About the "Security Policy for OCI Console" Sign-On Policy

The Security Policy for OCI Console sign-on policy is activated by default and preconfigured with Oracle security best practices.

If you modify the rules in this policy, you are no longer following Oracle security best practice.

- The following factors needed for this sign-on policy are already enabled: Mobile app passcode , Mobile app notification , Bypass code , and Fast ID Online (FIDO) authenticator .
- The Console application has been added to the policy.
- The sign-on policy comes with two active sign-on rules:

[
- MFA for administrators : The rule is first in priority order. This preconfigured rule requires that all users in the Administrators group and all users with an administrator role must enroll in MFA and must supply an additional factor every time they sign in to the OCI Console.
- MFA for all users : The rule is second in priority order. This preconfigured rule requires that all users must enroll in MFA and must supply an additional factor every time they sign in to the Console.

## Temporarily Exclude an Administrator From the "Security Policy for OCI Console" Sign-On Policy

As best practice, don't modify the "Security Policy for OCI Console" Sign-On Policy. However, you may want to do this during roll out. You can temporarily exclude an administrator account in case you make changes which lock you out of the OCI Console. After roll out is complete, and users have MFA configured so that they can access the OCI Console, change this back.
- Decide which admin user you are going to temporarily exclude from "Security Policy for OCI Console", create a new group and assign the user to it.
- Create a new rule which doesn't use MFA, and assign the group to it.
- Make that rule the first rule in the "Security Policy for OCI Console" policy.
Note  
  
Once roll out is complete, all users have configured MFA, and there are fewer chances of making a mistake which could lock you out of the OCI Console, revert these steps and restore the "Security Policy for OCI Console" policy to its unmodified state.

- Create a new group and assign the user you want to exclude to it. See[Creating a Group](https://docs.oracle.com/iaas/Content/Identity/groups/create-groups.htm)and[Adding Users to a Group](https://docs.oracle.com/iaas/Content/Identity/groups/add-users-to-groups.htm).
- Create a new sign-on rule.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
-   

Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- In the list of sign-on policies, click Security Policy for OCI Console .
- Click Add sign-on rule .
- Give the rule a name.
- For Group Membership , select the new group you've just created.
- Click Add sign-on rule .
The new rule is added to the list of rules for the "Security Policy for OCI Console" policy.
- Make the new rule the first in the "Security Policy for OCI Console" policy.
- On the policy details page, click Edit priority .
- Use the arrows to change the sign-on rules priority.
- Click Save changes .
When this user signs in, the first rule is applied and they don't have to use MFA to authenticate.

As soon as you're confident that all users have set up MFA, and that there's no chance of accidentally locking yourself out of the OCI Console, delete the new rule so that the "Security Policy for OCI Console" policy reverts to its unmodified state.

To delete the rule:
- In the Sign-on policies page, click Security Policy for OCI Console .
- Click the checkbox for the new rule, and click Remove sign-on rule .

Now, all users must use MFA to sign-in to the OCI Console.

## Completing MFA Enrollment

After "Security Policy for OCI Console" sign-on policy has been activated, anyone signing in to the OCI Console will be prompted to complete MFA enrollment using the Oracle Mobile Authenticator (OMA).

You, and any other users who sign in to the OCI Console, will see a screen similar to this example.

Click Enable Secure Verification , and follow the instructions in[Using the Oracle Mobile Authenticator App](https://docs.oracle.com/iaas/Content/Identity/mobileauthapp/use-oracle-mobile-authenticator-app.htm).

[
