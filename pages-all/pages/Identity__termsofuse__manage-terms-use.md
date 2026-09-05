# Managing Terms of Use Documents
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/termsofuse/manage-terms-use.htm
- Fetched: 2026-09-05 02:29 CDT

# Managing Terms of Use Documents

This feature lets you present disclaimers and acceptable use policies, also known as terms of use , to users in an identity domain. You can configure terms of use for each application and collect consent from users before allowing them to access the application.

## Required Policy or Role
To manage terms of use settings, you must have one of the following access grants:
- Be a member of the Administrators group
- Be granted the Identity Domain Administrator role or the Security Administrator role
- Be a member of a group granted`manage identity-domains`

To understand more about policies and roles, see[The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/termsofuse/../getstarted/identity-domains.htm#The),[Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/termsofuse/../roles/understand-administrator-roles.htm), and[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/termsofuse/../policieshow/Policy_Basics.htm).

## About Terms of Use Documents

About terms of use documents.

The terms of use feature lets you to set the terms and conditions to access the Console or a target application, based on the user's consent. This feature lets the identity domain administrator set relevant disclaimers for legal or compliance requirements and enforce the terms by refusing the service unless consent is received.

In an identity domain, you can optionally grant or deny access to applications based on the consent provided by the user. When the user sign in for the first time, the disclaimers for legal or compliance requirements are displayed. The user has the option of either consenting or denying consent. If the user doesn't provide consent by accepting the terms of use, they are not allowed to access the application.

When you create a terms of use, you add the customized content and language that you want to display and select the applications that use the terms. You can also set an expiration date for the consent to require users to provide consent again after a set period of time.
