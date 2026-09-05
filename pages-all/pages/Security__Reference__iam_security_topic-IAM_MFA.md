# IAM MFA
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-IAM_MFA.htm
- Fetched: 2026-09-05 03:04 CDT

# IAM MFA

Multifactor authentication (MFA) is a method of authentication that requires the use of more than one factor to verify a user's identity.

With MFA enabled, when a user signs in to an application, they're prompted for their username and password, which is the first factor – something that they know. The user is then required to provide a second type of verification. The two factors work together to add an additional layer of security by using either additional information or a second device to verify the user's identity and complete the sign-in process.
Note  
  
If you have configured MFA in a 3rd-party identity provider (IdP), such as Microsoft Azure Active Directory (Azure AD) or Okta, you don't need to configure MFA using IAM or Oracle Identity Cloud Service.

## MFA Enablement Plan

To enhance security, we've started seeding the "Security Policy For OCI Console" sign-on policy in all tenancies. As soon as an identity domain or an Identity Cloud Service stripe has been seeded with the policy, you should activate it to enable multifactor authentication (MFA) for users with administrative privileges.
Note  
  

The "Security Policy For OCI Console" policy applies to:
- Tenancies with identity domains in IAM, to the Default domain and all secondary domains. We will automatically activate this policy after the 17th of July 2023 , unless you meet one of the conditions below.
- All Identity Cloud Service stripes for tenancies which use Identity Cloud Service. We will automatically activate this policy after 24th July 2023 , unless you meet one of the conditions below.

## Find Out Your Tenancy Type

To find out which tenancy type you have, see[Determining the Tenancy Type](https://docs.oracle.com/iaas/Content/Security/Reference/determining_the_tenancy_type.htm).

## What the "Security Policy for OCI Console" Does

The "Security Policy for OCI Console" sign-on policy only affects access to the OCI Console.

After the policy is activated, all local users must use MFA to sign in to the Console. Users who don't log in to the Console will not be affected by this policy

## When We Won't Automatically Activate the Policy

We will not automatically activate the policy:
- If you have modified the default sign-on policy
- If you already have a sign-on policy and the OCI Console is explicitly assigned to it.
- If an active external IDP (SAML/Social or X.509) is configured in the IAM domain. This means that federated users are excluded from the impact of this policy.
- If you delete the "Security Policy for OCI Console" using an API, we won't re-create it. To delete the policy using REST APIs, see[Delete a Policy](https://docs.oracle.com/en/cloud/paas/identity-cloud/rest-api/op-admin-v1-policies-id-delete.html).

## Best Practices for IAM MFA

To configure IAM MFA using best practices:
- Find out which tenancy type you have. See[Determining the Tenancy Type](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/determining_the_tenancy_type.htm).
- Configure MFA best practices for that tenancy type using one of the following sets of instructions.
- [Identity Domains Without the "Security Policy for OCI Console" Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_with_identity_domains.htm)

For tenancies which use identity domains, but which haven't been seeded with the "Security Policy For OCI Console" sign-on policy.
- [Identity Domains With the "Security Policy for OCI Console" Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_identity_domains_signon_policy.htm)

For tenancies which use identity domains, but which have been seeded with the "Security Policy For OCI Console" sign-on policy.
- [Tenancies Without Identity Domains and Without the "Security Policy for OCI Console" Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_no_identity_domains_no_policy.htm)

For tenancies which use Identity Cloud Service, but which haven't been seeded with the "Security Policy For OCI Console" sign-on policy.
- [Tenancies Without Identity Domains and With the "Security Policy for OCI Console" Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_no_identity_domains.htm)

For tenancies which use Identity Cloud Service, but which have been seeded with the "Security Policy For OCI Console" sign-on policy.
- [Use Cloud Guard](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-using_cloud-guard.htm)
