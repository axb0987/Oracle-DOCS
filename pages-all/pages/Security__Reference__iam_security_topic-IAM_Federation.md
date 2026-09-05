# IAM Federation
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-IAM_Federation.htm
- Fetched: 2026-09-05 03:04 CDT

# IAM Federation

Oracle recommends that you use federation to manage logins into the Console.
- Identity federation supports SAML 2.0 compliant identity providers, and can be used to federate on-premises users and groups to IAM users and groups. The enterprise administrator needs to set up a federation trust between the on-premises identity provider (IdP) and IAM, in addition to creating mapping between on-premises groups and IAM groups. Then, on-premises users can single sign-on (SSO) into the Console, and access resources based on authorization of IAM groups they belong to. For more information about federating to the Console, see[Federating with Identity Providers](https://docs.oracle.com/iaas/Content/Identity/Concepts/federation.htm). Federation is especially important for enterprises using custom policies for user authentication (for example, multifactor authentication) . For more information about managing users and groups under federation, see[Federating with Identity Providers](https://docs.oracle.com/iaas/Content/Identity/Concepts/federation.htm).
- When using federation, Oracle recommends that you create a federation administrators group that maps to the federated IdP administrator group. The federation administrators group will have administrative privileges to manage customer tenancy, while being governed by the same security policies as the federated IdP administrator group. In this scenario, it is a good idea to have access to the local tenancy administrator user (that is, member of the default tenancy administrator IAM group), to handle any break-glass type scenarios (for example, inability to access resources through federation). However, you must prevent any unauthorized use of this highly privileged local tenancy administrator user. Oracle recommends the following approach to securely managing the tenancy administrator user:
- Create a local user belonging to the default tenancy administrator group.
- Create a highly complex Console password or passphrase (18 characters or more, with at least one lowercase letter, one uppercase letter, one number, and one special character) for the local tenancy administrator user.
- Securely escrow the local tenancy administrator user password in an on-premises location (for example, place the password in a sealed envelope in an on-premises physical safe).
- Create security policies for accessing the escrowed password only under specific "break-glass" scenarios.
- Have IAM security policy to prevent the federated administrators IAM group from adding or modifying membership of the default tenancy administrator group to prevent security by-passes.
- Monitor audit logs for accesses by default tenancy administrator and changes to the administrator group, to alert on any unauthorized actions. For additional security, the local tenancy administrator user password can be rotated after every login, or periodically, based on a password policy.

For an example that shows the way various IAM components fit together, see[Details for Health Checks](https://docs.oracle.com/iaas/Content/Identity/Reference/healthcheckpolicyreference.htm)
