# Determining the Tenancy Type
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/determining_the_tenancy_type.htm
- Fetched: 2026-09-05 03:04 CDT

# Determining the Tenancy Type

The steps to configure multifactor authentication (MFA) best practices depends on your tenancy type.

There are two types of tenancies:
- Tenancies with IAM identity domains. In these services you will see a Default domain and possibly secondary domains. These can be new tenancies or migrated tenancies.
- Tenancies without IAM identity domains. In these services you will see an auto-federated Identity Cloud Service stripe and optional secondary stripes. These services use Identity Cloud Service as an auto-federated identity provider (IdP).

## Does Your Tenancy Have Identity Domains?

Complete the following steps find the documentation that's right for you.

- Sign in to the Oracle Cloud Console.
- In the navigation menu, click Identity &amp; Security .
- Under Identity , check for Domains .
- 

If you don't see Domains , go to[Tenancies Without Identity Domains and With the "Security Policy for OCI Console" Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_no_identity_domains.htm)to learn how to enable MFA and create a sign-on policy according to Oracle security best practices.
- 

If you see Domains , go to the next step.
- 

Click Domains . Click the name of your identity domain, click Security and then Sign-on policies . Look for the Security Policy for OCI Console sign-on policy.

[Security Policy for OCI Console example](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/determining_the_tenancy_type.htm#)

[
- If you don't see the Security Policy for OCI Console sign-on policy then you enable MFA and create a sign-on policy according to Oracle security best practices. Go to[Identity Domains Without the "Security Policy for OCI Console" Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_with_identity_domains.htm).
- If you do see the Security Policy for OCI Console sign-on policy, then MFA is activated in your domain using Oracle security best practices. All users are required to enroll in and use MFA. To learn more about this preconfigured policy as well as changes you should make to the policy to customize it for your organization, see[Identity Domains With the "Security Policy for OCI Console" Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_identity_domains_signon_policy.htm)
