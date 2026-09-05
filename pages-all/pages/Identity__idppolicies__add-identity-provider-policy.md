# Creating an Identity Provider Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/idppolicies/add-identity-provider-policy.htm
- Fetched: 2026-09-05 02:22 CDT

# Creating an Identity Provider Policy

Create an identity provider policy for an identity domain.

You can define the following criteria in an IdP policy:
- The username of the user
- The IP address that the user is using to sign in to the identity domain
- The IdPs that will be available to the user to access the identity domain

- On the Identity provider (IdP) policies list page, select Create IdP policy . If you need help finding the list page, see[Listing Identity Provider Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/idppolicies/list-idp-policies.htm#console).
- On the Add policy page, enter a name and then select Add policy . The policy is added.
- On the Add identity provider rules page, select Add IdP rule to define rules for this policy.
- Enter a Rule name for the identity provider rule.
- Use the Assign identity providers menu to select the IdPs to assign to this rule.
- Configure the following Conditions :

- Expression placement : The following options are associated with this field:
- If you select Starts with expression , then the rule evaluates the start of the username in the user account.
- If you select Ends with expression , then the rule evaluates the end of the username in the user account.
- Enter user name expression : Specify information about users' usernames to evaluate whether they meet the criteria of the rule. For example, if you want the rule to be applicable only to those users who have usernames that end with @example.com , then select Ends with expression from the preceding menu, and then enter @example.com in this text box.
- Exclude users : Optionally, enter or select the users to exclude from the rule.
- Group membership : Optionally, enter or select the groups to exclude from the rule.
- Filter by client IP address : The following options are associated with this field:
- If you select Anywhere , then the IdPs that you specify in this rule will be available to users that sign in from any IP address.
-  If you select Restrict to the following network perimeters , then you enter or select network perimeters that you have defined. For more information, see[Creating a Network Perimeter](https://docs.oracle.com/en-us/iaas/Content/Identity/idppolicies/../networkperimeters/add-network-perimeter.htm). The IdPs that you specify in this rule will be available to users that sign in using only IP addresses that are contained in the defined network perimeters.
- Select Add IdP rule .
- To add another identity provider rule to this policy, repeat the preceding steps.

Note: If you have added multiple identity provider rules to this policy, you can change the order in which they're evaluated. Select Edit priority and then change the priority order.
- When you're finished adding rules, select Next .
- Add apps to the policy. For more information see[Adding Apps to the Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/idppolicies/add-apps-idp-policy.htm).
-
