# Configuring the IdP Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/passwordless/configure-idp-policy.htm
- Fetched: 2026-09-05 02:25 CDT

# Configuring the IdP Policy

Configure the identity provider (IdP) policy to include a new rule for passwordless authentication.
You can create a new IdP Policy, or edit an existing IdP policy.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Under Federation go to Identity provider policies .
- In the Identity provider policies section, select the policy that you want to update.
- Select Identity provider rules .
- Select Add IdP rule , and on the Add identity provider rule page, add a rule name and in Assign identity providers select the authentication factor or factors that you enabled. For example,`Email`or`Mobile App Passcode`.
Add all the authentication factors that you enabled in the previous step.
- Optionally, select one or more groups that this rule applies to.
- Select Add IdP rule .
- On the Identity provider rules page, if there is more than one IdP rule, ensure that the passwordless authentication rule is the first by selecting Edit priority .
