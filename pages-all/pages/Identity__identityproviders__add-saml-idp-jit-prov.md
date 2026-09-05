# Adding a SAML Just-in-Time Identity Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/add-saml-idp-jit-prov.htm
- Fetched: 2026-09-05 02:22 CDT

# Adding a SAML Just-in-Time Identity Provider

Set up a SAML identity provider (IdP) that uses just-in-time (JIT) provisioning for an identity domain in IAM.

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/../domains/to-view-identity-domains.htm).
- On the details page, depending on the options you see, do one of the following:

- select Federation , or
- select Security and then select Identity providers . A list of identity providers in the domain is displayed.
- Select the name of an identity provider.
- On the details page, select Configure JIT .
- Select Enable Just-in-Time (JIT) provisioning .
- Select one of the following options:

- Create a new identity domain user : Create an identity user in the identity domain, if the user doesn't exist when sign in with the identity provider.
- Update the existing identity domain user : Merge and overwrite identity domain user account data from the mapped IdP. The existing data is overwritten by the user data from the IdP.
Note  
  
To enable JIT, you must select one of these options.
- In the Map user attributes area, map a user account from the IdP to a user account from the identity domain.
- Select a value in the IdP user attribute type row.

- If you select Attribute , then enter the IdP user attribute name.
- If you select NameID , you don't need to enter the IdP user attribute name.
- (Optional) Select the identity domain user attribute.
- (Optional) Add more identity domain attributes.
- To enable group mapping, select Assign group mapping .

Note  
  
If you enable group mapping, proceed to the next step. If not, skip to step 10.
- For Group membership attribute name enter the IdP attribute name that contains group memberships.
- To import the group settings, select one of the following options:

- Define explicit group mapping : This option requires you to provide the group name to map between the IdP and identity domain. If you select this option, enter the IdP group name and select an available identity domain group name.
- Assign implicit group mapping : This option maps an IdP group to an identity domain group that has the same name. No other action is required.
- (Optional) To assign group memberships from the identity domain, select Assign domain group memberships and then perform the following steps:
- Select Add group .
- Select the groups that you want to add, and then select Add groups .
- Under Assignment rules , specify actions to take when assigning group memberships:

- If users are assigned to existing groups, select whether to merge with existing group memberships or replace existing group memberships.
- When a group isn't found, select to take one of the following actions:

- Ignore the missing group : The user successfully signs in.
- Fail the entire request : The sign-in attempt fails.
- Select Save Changes .
- (Optional) Activate the IdP before adding it to any policies. For more information, see[Activating or Deactivating an Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/activate-identity-provider.htm)
