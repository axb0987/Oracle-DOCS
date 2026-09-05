# Using Identity Verification Providers
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/securing/identity_verification_providers.htm
- Fetched: 2026-09-05 02:28 CDT

# Using Identity Verification Providers

Learn the tasks that you can perform using Identity Verification Providers.

## Creating an Identity Verification Provider

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/securing/../domains/to-view-identity-domains.htm).
- In the Console, open the navigation menu and select Identity &amp; Security .
- On the Domain's page, select the Security tab, and then select Identity verification providers .
- Select Create verification provider .
- In the Details section:
- Select a Verification provider from the drop down list.
- Enter a unique Name and a Description for this provider configuration.
- In the Configure section, enter the credentials you obtained from your third-party provider:
- Client ID
- Client secret
- Discovery URL
- Token endpoint
- User endpoint
- In the Supported claims retrieved section, map the claims returned by the provider to attributes in your identity domain. This ensures that the data from the ID document is correctly associated with the user's profile.
- Select a Verified Claim (for example, First name).
- Select the corresponding Identity Domain User Attribute to map it to.
- Select Add another claim to map additional attributes.
- Select Create .

Note  
  
The identity verification provider is created in a deactivated state. You must first activate an identity provider to use the provider in an Identity Assurance policy.

## Getting an Identity Verification Provider's Details

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/securing/../domains/to-view-identity-domains.htm).
- Go to Security , and then select Identity verification providers .
- Select one of the identity verification providers to view the details.

## Updating an Identity Verification Provider

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/securing/../domains/to-view-identity-domains.htm).
- Go to Security , and then Identity verification providers .
- Select one of the identity verification providers to view the details.
- (Optional) Make any necessary updates to the Details page.
- Select Save .

## Deleting an Identity Verification Provider

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/securing/../domains/to-view-identity-domains.htm).
- Go to Domain , Security , and then Identity verification providers .
- Select one of the identity verification providers to delete.
- Confirm the deletion.

## Activate an Identity Verification Provider

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/securing/../domains/to-view-identity-domains.htm).
- Go to Domain , Security , and then Identity verification providers .
- From the Actions menu (three dots) of the identity verification provider you want to activate, select Activate verification provider .
- Confirm the activation.

## Deactivating an Identity Verification Provider

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/securing/../domains/to-view-identity-domains.htm).
- From the Actions menu (three dots), of the identity verification provider you want to deactivate, select Deactivate verification provider .
-
