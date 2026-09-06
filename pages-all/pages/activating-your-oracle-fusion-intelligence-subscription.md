# About Activating Your Oracle Fusion Data Intelligence Subscription
- Source: https://docs.oracle.com/iaas/analytics-for-applications/doc/activating-your-oracle-fusion-intelligence-subscription.html
- Fetched: 2026-09-05 18:59 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/analytics-for-applications/doc/activating-your-oracle-fusion-intelligence-subscription.html#dcoc-content-body)

# About Activating Your Oracle Fusion Data Intelligence Subscription

After Oracle processes your subscription, you receive a Welcome email confirming your subscription.

In the body of this Welcome email for your Oracle Fusion Data Intelligence subscription, the name of the service is "Oracle Fusion &lt;pillar-name&gt; Analytics," where &lt;pillar-name&gt; represents the Oracle Fusion Data Intelligence application you subscribed to such as Fusion HCM Analytics and Fusion ERP Analytics.

To start using Oracle Fusion Data Intelligence, you must activate your subscription. You can activate multiple Oracle Fusion Data Intelligence subscriptions in a single tenancy, but you can’t split one subscription and activate the split parts into multiple tenancies. You can create multiple development, test, and production instances in one tenancy using the multiple subscription IDs. However, note that you can create one instance per one subscription; you can’t split a subscription and provision the split parts across instances. If a subscription has expired and you bought a new one to replace it, then at the time of updating the offering, you can update that instance to use the new subscription ID.
On receiving the Welcome email, follow these steps:
- Review the[Important – Read Before Activating](https://docs.oracle.com/iaas/analytics-for-applications/doc/activating-your-oracle-fusion-intelligence-subscription.html#GUID-0DD88318-4441-4227-A423-A15EA16526A8__GUID-227FE2A1-4335-4750-B468-6DCFE6572043)section.
- Write down the name of your Oracle Fusion Cloud Applications account or tenancy.
Note  
  
A Cloud account is also known as a tenancy.
- Ensure that you're a cloud administrator in your Oracle Fusion Cloud Applications account and have been granted the OCI_Administrator role or added to the Administrators group, whichever is available. See the[Role Needed to Activate](https://docs.oracle.com/iaas/analytics-for-applications/doc/activating-your-oracle-fusion-intelligence-subscription.html#GUID-0DD88318-4441-4227-A423-A15EA16526A8__GUID-1AE0B737-35CE-4DA4-B1E3-C13D80BD09A2)section.
- Use your Oracle Fusion Cloud Applications credentials to sign into your cloud account.
- Activate the Oracle Fusion Data Intelligence subscription into the same existing Oracle Fusion Cloud Applications account.
- Wait until you receive a confirmation email from Oracle Cloud stating that your services are ready before signing back into your Oracle Fusion Cloud Applications account and verifying that your Oracle Fusion Data Intelligence entitlements appear and that the "Create Instance" button is enabled.
- It's also feasible to activate your Oracle Fusion Data Intelligence subscription into a non-Oracle Fusion Cloud Applications account but this is discouraged. See[Important – Read Before Activating](https://docs.oracle.com/iaas/analytics-for-applications/doc/activating-your-oracle-fusion-intelligence-subscription.html#GUID-0DD88318-4441-4227-A423-A15EA16526A8__GUID-227FE2A1-4335-4750-B468-6DCFE6572043)for further details.

Important – Read Before Activating
- Best practice is to always activate Oracle Fusion Data Intelligence into your Oracle Fusion Cloud Applications account. Doing so saves you time, cost, and complexity when setting up your security integration between Oracle Fusion Data Intelligence and your Oracle Fusion Cloud Applications, as well as improved ongoing synchronization performance.
- Activating the Oracle Fusion Data Intelligence subscription into a non-Oracle Fusion Cloud Applications account goes against best practices. It will cost you additional time, money, and complexity when setting up your security integration between Oracle Fusion Data Intelligence and your Oracle Fusion Cloud Applications, and reduced performance in its ongoing synchronization.
- From Release Platform 25.R1.P2, Universal Credits (UCC) are no longer a prerequisite for activating Oracle Fusion Data Intelligence. You can activate Oracle Fusion Data Intelligence without relying on UCC. However, you may require UCC in specific scenarios to access or scale Oracle Cloud Infrastructure services that support Oracle Fusion Data Intelligence and for enhanced performance. Ensure that you have an UCC subscription in these scenarios to pay for additional charges:
- When you want to add OCPUs in the associated Oracle Analytics Cloud for enhanced processing power and analytics. Use the Change Capacity capability to increase the OCPU count. See[Change Oracle Analytics Cloud Capacity](https://docs.oracle.com/iaas/analytics-for-applications/doc/change-oracle-analytics-cloud-capacity.html#GUID-DA856E08-D298-4D44-9D6A-10B1E2B68F05).
- When you want to add ECPUs in the associated Oracle Autonomous AI Lakehouse for compute resources and increase storage capacity for long-term backups and database tools. Use the Manage Scaling capability. See[Scale Up Oracle Autonomous Data Warehouse](https://docs.oracle.com/iaas/analytics-for-applications/doc/scale-oracle-autonomous-ai-lakehouse.html#GUID-9C0AE161-2EED-4729-A947-600B3A2C19D0).
- If you plan on extending Oracle Fusion Data Intelligence with more than 50GB of non-Oracle Fusion Cloud Applications data.
- When you want to use these additional Oracle Cloud Infrastructure services:
- Key Management - for example, if you opt for customer-managed encryption keys, you need to use Oracle Key Management and you can use universal credits to pay for:
- Additional key versions beyond the first free 20 key versions
- Key creation and storage
- Key rotation and API requests
- AI/ML Services for advanced analytics and automation.
- Object Storage Service (OSS) for scalable data storage.
- For the specific scenarios that may require universal credits, note these:
- If an UCC subscription exists in your Oracle Fusion Cloud Applications account, then you don’t need another UCC subscription.
- Activate a new UCC subscription in your Oracle Fusion Cloud Applications account. See[Activate the Universal Credits Subscription](https://docs.oracle.com/iaas/analytics-for-applications/doc/activate-universal-credits-subscription.html#GUID-2B124221-25B5-4288-A71A-DD1F924BFA42).
- UCC Pay As You Go (PAYG) subscriptions expire within 30 days of receiving the UCC Welcome email. It's very important that you activate UCC into your Oracle Fusion Cloud Applications account within 30 days of receiving it. If the UCC PAYG subscription expires, then UCC activation will fail and you'll need to submit a service request.

Role Needed to Activate
You must be a cloud administrator with the OCI_Administrator role or be in the OCI_Administrators group for the Oracle Cloud account that you’re trying to activate your subscriptions into to activate successfully both UCC and Oracle Fusion Data Intelligence subscriptions. If you aren’t a cloud administrator with this role, then follow either of these options:
- Ask the current cloud administrator of the cloud account to add you as a cloud administrator and assign the OCI_Administrator role or add you to the Administrators group before you try to activate. However, be mindful of your account’s location when asking:
- If you've an account in an Oracle Cloud Infrastructure Identity and Access Management default or local domain, then a user with the Oracle Cloud Infrastructure administrator privileges needs to add you to the Administrators group.
Note  
  
The prebuilt read-only Tenant Admin Policy grants administration privileges to the prebuilt Administrators group.
- If you've an account in an Oracle Identity Cloud Service stripe, then a user with the Oracle Cloud Infrastructure administrator privileges needs to ensure that the Oracle Identity Cloud Service OCI_Administrators group is mapped to the Identity and Access Management Administrators group, and then add you to the Oracle Identity Cloud Service OCI_Administrators group.
Note  
  
The prebuilt OCI_Administrators group in an Oracle Identity Cloud Service stripe is mapped to the Administrators group in the Identity and Access Management local domain.
- If you've an account in a migrated Oracle Identity Cloud Service identity domain, then a user with the Oracle Cloud Infrastructure administrator privileges needs to add you to the OCI_Administrators group and create the following policy rule:
```

```

Note  
  
A migrated OCI_Administrators group doesn't have administrative privileges immediately after a migration.
- If you've an account in any other identity domain, then a user with the Oracle Cloud Infrastructure administrator privileges needs to add you to the Domain_Administrators group and create the following policy rule:
```

```

- Forward the activation emails to a person who has the OCI_Administrator role or is in the Administrators group and have them follow the activation instructions.
Note these:
- If this Oracle Cloud account uses identity domains, then see the Creating Users section in[Using the Console](https://docs.oracle.com/iaas/Content/Identity/users/about-managing-users.htm#managingusers_usingconsole)to create a user and assign the OCI_Administrators or Administrators group, whichever is available.

To add this group to an existing user in an identity domain, see the Adding Users to Groups section in[Using the Console](https://docs.oracle.com/iaas/Content/Identity/users/about-managing-users.htm#managingusers_usingconsole).
- If this Oracle Cloud account uses Oracle Identity Cloud Service to manage users, then see[Create User Accounts](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/create-user-accounts.html)to create a user and assign the OCI_Administrator role or Administrators group, whichever is available.

To add this group to an existing user in Oracle Identity Cloud Service, see[Assign Groups to the User Account](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/assign-groups-user-account.html).
- To know if your tenancy uses identity domains or Oracle Identity Cloud Service, see[Do You Have Access to Identity Domains?](https://docs.oracle.com/iaas/Content/Identity/getstarted/identity-domains.htm#identity_documentation__updated-identity-domains)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
