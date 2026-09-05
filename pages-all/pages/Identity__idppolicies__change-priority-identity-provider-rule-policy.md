# Changing the Priority of an Identity Provider Rule for a Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/idppolicies/change-priority-identity-provider-rule-policy.htm
- Fetched: 2026-09-05 02:22 CDT

# Changing the Priority of an Identity Provider Rule for a Policy

You can change the priority of an identity provider rule for an identity provider policy to change the order that the identity domain evaluates it.

- On the Identity provider (IdP) policies list page, select the policy to change. If you need help finding the list page, see[Listing Identity Provider Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/idppolicies/list-idp-policies.htm#console).
- Perform one of the following actions depending on the options that you see:
- Select Identity provider rules .
- Under Resources , select Identity provider rules .
- Perform one of the following actions depending on the options that you see:
- Select Actions , and then select Edit IdP rules priority . In the Priority field, enter a number to indicate the order in which you want the rule evaluated relative to other rules.

For example, if the identity provider rule has a priority of 4, and you want it to be evaluated first, enter a 1 in the Priority field. This rule will now be evaluated first, and the rule previously on top now has a priority of 2.
- Select Edit priority . In the Priority column, select the up or down arrow next to the rule that you want to move. Set the rule at the position in the list that indicates the order in which you want it evaluated relative to the other rules.

For example, if the identity provider rule has a priority of 4, and you want it to be evaluated first, select the up arrow until it's at the top of the list. This rule will now be evaluated first, and the rule previously on top now has a priority of 2.
-
