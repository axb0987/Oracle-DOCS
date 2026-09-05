# Managing Sign-On Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/managingsignonpolicies.htm
- Fetched: 2026-09-05 02:29 CDT

# Managing Sign-On Policies

Use the topics in this section describe how to create, activate, update, deactivate, and delete a sign-on policies for an identity domain.
- [About Sign-On Policies and Sign-On Rules](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/managingsignonpolicies.htm#understand-sign-policies)
- [Required Policy or Role](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/managingsignonpolicies.htm#signon_iam_role)
- [Listing Sign-On Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/list-signon-policy.htm)
- [Creating a Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/add-sign-policy.htm)
- [Activating a Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/activate-sign-policies.htm)
- [Updating a Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/modify-sign-policy.htm)
- [Deactivating a Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/deactivate-sign-policies.htm)
- [Deleting a Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/delete-sign-policies.htm)

## About Sign-On Policies and Sign-On Rules

A sign-on policy uses sign-on rules to define criteria that determine whether to allow a user to sign in to an identity domain or an application.

All identity domains come with a Default Sign-On Policy . If your identity domain has been preconfigured with the Security Policy for OCI Console sign-on policy, then we recommend that you used that policy. You can add additional sign-on policies as needed. Prioritize sign-on rules for a sign-on policy to specify the order in which the rules are to be evaluated.

### The "Default" Sign-On Policy

All identity domain include an active Default Sign-On Policy that contains a Default Sign-On Rule .

By default, this Default Sign-On Rule allows all users to sign in to the identity domain with a username and password. You can build upon this policy by adding other sign-on rules to it. By adding these rules, you can prevent some of your users from signing in to the identity domain. Or, you can allow them to sign in, but prompt them for an additional factor to access resources that are protected by the identity domain, such as the Oracle Cloud Infrastructure Console.

For example, you can create two sign-on rules for the Default Sign-On Policy . The first rule prevents any users from signing in to the identity domain if they're using an IP address that falls within the range of a network perimeter that you defined named: Denied Network Perimeters . The second rule requires users who belong to a particular group (for example, the UA Developers Group ) to be prompted for a second factor as part of the 2-Step Verification process named: UA Developers Group . All other users will be able to sign in without being prompted for a second factor.

Important  
  
For the Default Sign-On Rule , never set access for all of your users to be denied. If users don't meet the criteria of any other rules you define that allow them to sign in to the identity domain, they will be prevented from accessing identity domain-protected resources. Also, configure the identity domain to evaluate this sign-on rule last because, by default, it allows all users to sign in to the identity domain.

### The "Security Policy for OCI Console" Sign-On Policy

The Security Policy for OCI Console sign-on policy is activated by default and preconfigured with Oracle security best practices.

- The following factors needed for this sign-on policy are already enabled: Mobile app passcode , Mobile app notification , Bypass code , and Fast ID Online (FIDO) authenticator .
- The OCI Console application has been added to the policy.
- The sign-on policy comes with two active sign-on rules:

[
- MFA for administrators : The rule is first in priority order. This preconfigured rule requires that all users in the Administrators group and all users with an administrator role must enroll in MFA and must supply an additional factor every time they sign in.
Note  
  
You can remove this rule and use the MFA for all users rule to require all users (including administrators) to enroll in MFA. Or you can leave this rule in place and all users (including administrators) will still be required to enroll in MFA when the MFA for all users rule is evaluated.
- MFA for all users : The rule is second in priority order. This preconfigured rule requires that all users must enroll in MFA and must supply an additional factor every time they sign in.
Note  
  
If you don't want to require MFA for all users at this time, you can make this rule optional and users will have the option to enroll into MFA. Or you can remove this rule and keep the MFA for administrators so that only administrators must enroll in MFA.

Important  
  
Whichever rule you decide to keep, exclude at least one administrator from the rule. If you keep both rules, make the change to both rules. See[Creating a Sign-On Policy](https://docs.oracle.com/iaas/Content/Identity/signonpolicies/add-sign-policy.htm)to learn how to exclude users from a sign-on rule.

To set up MFA using the Security Policy for OCI Console sign-on policy see the best practices at[Identity Domains With the "Security Policy for OCI Console" Sign-On Policy](https://docs.oracle.com/iaas/Content/Security/Reference/iam_security_topic-iam_mfa_identity_domains_signon_policy.htm).

### Additional Sign-On Policies

You can create sign-on policies and associate them with specific apps. When a user uses one of these apps to attempt to sign in to the identity domain, the identity domain checks to see if the app has any sign-on policies associated with it. If so, then the identity domain evaluates the criteria of the sign-on rules assigned to the policy. If there are no sign-on policies for the app, then the Default Sign-On Policy is evaluated.

### The Priority of Sign-On Rules for a Policy

Because you can define multiple sign-on rules for a sign-on policy, the identity domain must know the order in which the rules are to be evaluated. To do this, you can set the priority of the rules.

Using the sign-on rules from the Default Sign-On Policy example above, you can have the Denied Network Perimeters sign-on rule evaluated first, and the UA Developers Group sign-on rule evaluated next. If a user meets the criteria of the Denied Network Perimeters sign-on rule (that is, the IP address used to attempt to sign in to the identity domain falls within the IP range that you defined in the network perimeter), the user is prevented from accessing identity domain-protected resources. If the user doesn't match the criteria for this rule, then the rule with the next highest priority is evaluated. For this example, this is the UA Developers Group rule. If the user is a member of the UA Developers Group , they will be prompted for an additional factor to sign in to the identity domain. If the user is not a member of the UA Developers Group , the rule with the next highest priority is evaluated. For this example, this is the Default Sign-On Rule . Because this rule, by default, allows all users to sign in to the identity domain, the user will be able to sign in without being prompted for a second factor.

## Required Policy or Role

Required policy or role.
To manage sign-on policies, you must have one of the following access grants:
- Be a member of the Administrators group
- Be granted the identity domain administrator, security administrator, or application administrator role
- Be a member of a group granted`manage identity-domains`

To understand more about policies and roles, see[The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/../getstarted/identity-domains.htm#The),[Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/../roles/understand-administrator-roles.htm), and[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/../policieshow/Policy_Basics.htm)
