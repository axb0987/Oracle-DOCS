# Changing the Priority of a Rule for a Sign-On Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/change-priority-sign-rule-policy.htm
- Fetched: 2026-09-05 02:29 CDT

# Changing the Priority of a Rule for a Sign-On Policy

If you have more than one sign-on rule for a sign-on policy, you can change the priority of a rule to change the order in which the identity domain evaluates it.

- On the Sign-on policies list page, select the sign-on policy that you want to work with. If you need help finding the list page, see[Listing Sign-On Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/list-signon-policy.htm).
- Perform one of the following actions depending on the option that you see:

- From Actions select Edit sign-on rules priority and confirm that you want to proceed. Then set the priority for each rule.
- Under Resources , select Sign-on rules . Select Edit priority and confirm you want to continue. Select the up or down arrow next to the rule to move it to the position in the listed order that you want the rule applied.

For example, if the sign-on rule is currently listed fourth, and you want the identity domain to evaluate it first, select the up arrow next to the rule until it's at the top of the list. That sign-on rule now has a priority of 1, and the rule that was listed first now has a priority of 2.
-
