# Enabling Synchronization for an App Catalog Application
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/enable-synchronization-app-catalog-application.htm
- Fetched: 2026-09-05 02:19 CDT

# Enabling Synchronization for an App Catalog Application

User provisioning and synchronization is an important aspect of application management. After enabling provisioning, synchronization allows you to control how operations like creating and deleting accounts in Software as a Service (SaaS) applications are reflected in IAM.
You can enable and configure synchronization for App Catalog applications either when adding the app or later when modifying it. You can only enable synchronization after enabling provisioning. To enable provisioning, see[Enabling Provisioning for an App Catalog Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/enable-provisioning-app-catalog-application.htm). Follow the application catalog instructions for your specific SaaS app to enable and configure synchronization.

- On the Domains list page, select the domain for which you want to create a user. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/../domains/to-view-identity-domains.htm).
- On the details page, select Integrated applications . A list of applications in the domain is displayed.
- Select the name of the app that you want to configure.
- Select Provisioning .
- Depending on the options you see, select either the Actions menu (three dots) or Edit provisioning , then select Enable provisioning .
- Confirm your choice and then on the Enable provisioning page, find and select Enable synchronization .
- In the Configure synchronization section, modify the attributes following the application catalog instructions for your specific SaaS application.
- Select Save changes .

Enable synchronization to import users from your SaaS app.
Note  
  
If the number of created objects (users) and deleted recorded objects (synced users) exceeds the maximum number allowed, the sync job quits. The maximum number of objects created or recorded objects deleted is an approximate maximum limit, not a precise limit because of the parallel processing of synced objects.

See[Importing User Accounts from a Software as a Service Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/import-user-accounts-software-service-application.htm)
