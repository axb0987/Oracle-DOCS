# Testing an Identity Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/test-identity-provider.htm
- Fetched: 2026-09-05 02:22 CDT

# Testing an Identity Provider

After adding and activating an identity provider, you can test it. You can verify that you can use your federated SSO credentials to sign in to the identity domain through an external website.

- If you assigned the identity provider to an identity provider policy, then go to step 2. Otherwise, assign the identity provider to an identity provider policy. See[Assign Identity Providers to the Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/assign-identity-providers-policy.htm).
- Sign out of the identity domain.
- In the Sign In page, verify that you see a link called &lt;Identity_Provider_Name&gt; .

The &lt;Identity_Provider_Name&gt; placeholder represents the name you entered for the identity provider that you created.

If, for example, you created an identity provider called Google, then the link appears as Google .
- Select the &lt;Identity_Provider_Name&gt; link.
- Sign in to the external website with your federated SSO credentials.
The identity provider evaluates the user's sign-on credentials, verifies that the user is an authorized user, and returns this information to the identity domain.

Tip  
  
If you no longer want to display the link to the identity provider in the Sign In page, then remove the identity provider from all identity provider policies and deactivate the identity provider. See[Removing Identity Providers from the Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/../idppolicies/remove-identity-providers-policy.htm)and[Deleting an Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/delete-identity-provider.htm)
