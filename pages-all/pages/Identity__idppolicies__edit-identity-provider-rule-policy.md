# Updating an Identity Provider Rule for the Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/idppolicies/edit-identity-provider-rule-policy.htm
- Fetched: 2026-09-05 02:22 CDT

# Updating an Identity Provider Rule for the Policy

Update configuration settings for an identity provider rule of an identity provider policy.

- On the Identity provider (IdP) policies list page, find and open the policy to edit. If you need help finding the list page, see[Listing Identity Provider Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/idppolicies/list-idp-policies.htm#console).
- Under Resources , select Identity provider rules .
- Select the Actions menu (three dots) for the identity provider rule that you want to edit.
- Select Edit IdP rule . A window that displays configuration settings for the identity provider rule opens.
- Enter a Rule name for the identity provider rule.
- Use the Assign identity providers menu to select the identity providers to assign to this rule.
- Use the following table to configure rule Conditions :

- 

Expression placement : There are two options associated with this field: Starts with expression and Ends with expression . If you select Starts with expression , then the rule evaluates the start of the username in the user account. If you select Ends with expression , then the rule evaluates the end of the username in the user account.
- 

Enter user name expression : Specify information about usernames to evaluate and decide whether they meet the criteria of the rule. For example, you might want the rule to be applicable only to those users that have usernames that end with`@example.com`. Select Ends with expression from the menu, and enter @example.com in the Enter user name expression text box.
- 

(Optional) Exclude users : Enter or select the users to exclude from the rule.
- 

(Optional) Group membership : Enter or select the groups to exclude from the rule.
- 

Filter by client IP address : There are two options associated with this field: Anywhere and Restrict to the following network perimeters . If you select Anywhere , then the identity providers that you specify in this rule will be available to users that sign in from any IP address. If you select Restrict to the following network perimeters , then a text box appears. In this text box, enter or select network perimeters that you defined. For more information, see[Creating a Network Perimeter](https://docs.oracle.com/en-us/iaas/Content/Identity/idppolicies/../networkperimeters/add-network-perimeter.htm). The identity providers that you specify in this rule will be available to users that sign in using only IP addresses that are contained in the defined network perimeters.
-
