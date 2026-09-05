# Tenancies Without Identity Domains and With the "Security Policy for OCI Console" Sign-On Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_no_identity_domains.htm
- Fetched: 2026-09-05 03:04 CDT

# Tenancies Without Identity Domains and With the "Security Policy for OCI Console" Sign-On Policy

If you're using multifactor authentication (MFA) in tenancies without identity domains, and Oracle Identity Cloud Service as an auto-federated identity provider (IdP) in IAM and with with the "Security Policy for OCI Console" sign-on policy, then we recommend that you set up MFA using this sign-on policy

## MFA Enablement Plan

To enhance security, we've started seeding the "Security Policy For OCI Console" sign-on policy in all tenancies. As soon as an Identity Cloud Service stripe has been seeded with the policy, you should activate it to enable multifactor authentication (MFA) for users with administrative privileges.

The following flowchart outlines the complete process from policy rollout, where Oracle initiates the seeding of the policy, to the policy enforcement stage, during which Oracle will activate the policy except under specific circumstances.

[

- The "Security Policy for OCI Console" sign-on policy only affects access to the OCI Console. After the policy is activated, all local users must use MFA to sign in.
- The policy applies to to all Identity Cloud Service stripes.
Note  
  
In tenancies with Identity Cloud Service stripes, we will automatically activate this policy after 24th July 2023 .

We will not automatically activate the policy:
- If you have modified the default sign-on policy
- If an active external IDP (SAML/Social or X.509) is configured in the IAM domain. This means that federated users are excluded from the impact of this policy.
- If you already have a sign-on policy and the OCI Console is explicitly assigned to it.
- If you delete the "Security Policy for OCI Console" using an API, we won't re-create it. To delete the policy using REST APIs, see[Delete a Policy](https://docs.oracle.com/en/cloud/paas/identity-cloud/rest-api/op-admin-v1-policies-id-delete.html).

For you to activate the policy in an Identity Cloud Service stripe, see[Activate Sign-On Policies](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/activate-sign-policies.html#GUID-25FCDFB1-C5B5-458E-8F6E-C59FAE4CCAF9).

When it's been activated, the policy will look like this in the Sign-On Policies page in the Identity Cloud Service Admin Console.

[

To learn more about the policy, see[About the "Security Policy for OCI Console" Sign-On Policy](https://docs.oracle.com/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_identity_domains_signon_policy.htm#iam_security_topic-iam_mfa_identity_domains_signon_policy__about-identity-domains-sign-on-policy).

## Enforcement Rules for "Security Policy for OCI Console" for Identity Cloud Service Stripes

Sign-on Policy "Security PolicyFor OCI Console" Status You have modified the Default Sign-on Policy Sign-on Policy "Security Policy For OCI Console" Status after forcing enablement
Present and Enabled Not applicable (you can't have another active sign-on policy for OCI Console) No change
Present and Disabled No The policy is changed to Present and Enabled
Present and Disabled Yes No change. We won't overwrite your policy.
Deleted Not applicable No change

## Setting Up the "Security Policy for OCI Console" Sign-On Policy

To set up the "Security Policy for OCI Console" sign-on policy:
- Read[Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_no_identity_domains.htm#iam_security_topic-iam_mfa_with_identity_domains__prereq-no-idc-sign-on-policy).
- Read[About the "Security Policy for OCI Console" Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_no_identity_domains.htm#iam_security_topic-iam_mfa_with_identity_domains__about-idc-sign-on-policy).
- Optionally and only during the roll out period, exclude an administrator from the policy. When you're confident that your users have set up MFA for their accounts, add that account back in to the "Security Policy for OCI Console". See[Temporarily Exclude an Administrator From the "Security Policy for OCI Console" Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_identity_domains_signon_policy.htm#exclude-admins-users-sign-on-policy).
Note  
  
It is a security risk to have a user able to sign in without MFA, so if you choose to do this do it for as short a time as possible.
- Learn how to enroll in MFA using a mobile app passcode or a mobile app notification. See[Completing MFA Enrollment](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_no_identity_domains.htm#enroll-mobile-app-passcodes-notifications).

## Prerequisites

Before you begin: Before you configure MFA, complete the following prerequisites.
- Review the MFA factors. The MFA factors available to you depend on the License Type you have. The License Type shows in the top right of the Identity Cloud Service console. See[About Oracle Identity Cloud Service Pricing Models](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/oracle-identity-cloud-service-pricing-models.html#GUID-05F56DF0-0F71-436C-A103-3A10AEB38650)for more information about MFA and license types.
- Review the documentation for[Use the Oracle Mobile Authenticator App as an Authentication Method](https://docs.oracle.com/en/cloud/paas/identity-cloud/usids/use-oracle-mobile-authenticator-app-authentication-method.html)to learn how to use Mobile app notification and Mobile app passcode in the Oracle Mobile Authenticator app.
- Optionally, and only during the roll out period, exclude an identity domain administrator from the "Security Policy for OCI Console" policy, so if you make any mistakes during roll out you have not locked yourself out of the Console.

As soon as roll out is complete, and you are confident that your users have all set up MFA and can access the Console, you can remove this user account.
- Identify any Identity Cloud Service groups mapped to OCI IAM groups.
- Register a client application with an Identity Domain Administrator role to enable access to your identity domain using the REST API in case your Sign-On Policy configuration locks you out. If you don't register this client application and a Sign-On Policy configuration restricts access to everyone, then all users are locked out of the identity domain until you contact Oracle Support. For information about registering a Client Application, see[Register a Client Application](https://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/idcs/idcs_rest_postman_obe/rest_postman.html#RegisteraClientApplication)in Using the Oracle Identity Cloud Service REST APIs with Postman .
- Create a bypass code and store that code in a secure location. See[Generate and Use the Bypass Code](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/generate-and-use-bypass-code.html).

## About the "Security Policy for OCI Console" Sign-On Policy

The Security Policy for OCI Console sign-on policy is activated by default and preconfigured with Oracle security best practices.

- The following factors needed for this sign-on policy are already enabled: Mobile app passcode , Mobile app notification , Bypass code , and Fast ID Online (FIDO) authenticator .
- The OCI Console application has been added to the policy.
- The sign-on policy comes with two active sign-on rules:

[
- MFA for administrators : The rule is first in priority order. This preconfigured rule requires that all users in the Administrators group and all users with an administrator role must enroll in MFA and must supply an additional factor every time they sign in.
- MFA for all users : The rule is second in priority order. This preconfigured rule requires that all users must enroll in MFA and must supply an additional factor every time they sign in.

## Temporarily Exclude an Administrator From the "Security Policy for OCI Console" Sign-On Policy

As best practice, don't modify the "Security Policy for OCI Console" Sign-On Policy. However, you may want to do this during roll out. You can temporarily exclude an administrator account in case you make changes which lock you out of the OCI Console. After roll out is complete, and users have MFA configured so that they can access the OCI Console, change this back.
- Decide which admin user you are going to temporarily exclude from "Security Policy for OCI Console", create a new group and assign the user to it.
- Create a new rule which doesn't use MFA, and assign the group to it.
- Make that rule the first rule in the "Security Policy for OCI Console" policy.
Note  
  
Once roll out is complete, all users have configured MFA, and there are fewer chances of making a mistake which could lock you out of the OCI Console, revert these steps and restore the "Security Policy for OCI Console" policy to its unmodified state.

- Create a new group and assign the user you want to exclude to it. See[Create Groups](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/create-groups.html)and[Assign User Accounts to the Group](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/assign-user-accounts-group.html).
- Create a new rule and add the group you've just created.
- In the Identity Cloud Service console, expand the Navigation Drawer , click Security , and then click Sign-On Policies . You should see the Security Policy for OCI Console policy.
- Click the Sign-On Rules tab.
- Click Add , and give the new rule a name.
- Add the new group to And is a member of these groups .
- Click Save .
The new rule is added to the list of rules for the "Security Policy for OCI Console" policy.
- Make the new rule the first in the "Security Policy for OCI Console" policy.
- On the policy details page, click the action icon to the left of the new rule.
- Drag the new rule to be the first rule in the policy.
- Click Save .
When this user signs in, the first rule is applied and they don't have to use MFA to authenticate.

As soon as you're confident that all users have set up MFA, and that there's no chance of accidentally locking yourself out of the OCI Console, delete the new rule so that the "Security Policy for OCI Console" policy reverts to its unmodified state.

To delete the rule:
- In the Sign-on policies page, click Security Policy for OCI Console .
- Click the checkbox for the new rule, and click Remove .

Now, all users must use MFA to sign-in to the OCI Console.

## Completing MFA Enrollment

After "Security Policy for OCI Console" sign-on policy has been activated, anyone signing in to the OCI Console will be prompted to complete MFA enrollment using the Oracle Mobile Authenticator (OMA).

You, and any other users who sign in to the OCI Console, will see a screen similar to this example.

Click Enable Secure Verification , and follow the instructions in[Using the Oracle Mobile Authenticator App](https://docs.oracle.com/iaas/Content/Identity/mobileauthapp/use-oracle-mobile-authenticator-app.htm).

[
