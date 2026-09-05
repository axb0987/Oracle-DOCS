# Deleting an Identity Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/delete-identity-provider.htm
- Fetched: 2026-09-05 02:22 CDT

# Deleting an Identity Provider

Delete an identity provider (IdP) for an identity domain in IAM.
Remove an IdP from all policies before deactivating or deleting an IdP.
Note  
  
Deleting a social IdP removes the user profiles that are linked to that IdP. Consider deactivating a social IdP (which doesn't remove the user profiles) rather than deleting it, so that users can still see the accounts in My profile but can't use them to sign in.

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/../domains/to-view-identity-domains.htm).
- On the details page, depending on the options you see, do one of the following:

- select Federation , or
- select Security and then select Identity providers . A list of identity providers in the domain is displayed.
- Select the name of the IdP that you want to delete.
- Select More actions , and then select Delete IdP .
-
