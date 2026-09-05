# Importing Users from a SaaS Application
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/import-user-accounts-software-service-application.htm
- Fetched: 2026-09-05 02:19 CDT

# Importing Users from a SaaS Application

After enabling provisioning and synchronization for your App Catalog app, you might want to import the existing users from your Software as a Service (SaaS) applications and link them to IAM users.

Before You Begin:

Before you import your SaaS users, verify that:
- 

The app is activated. To activate your app, see[Activating Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/activate-applications.htm).
- 

Provisioning is enabled. See[Enabling Provisioning for an App Catalog Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/enable-provisioning-app-catalog-application.htm).
- 

Synchronization is enabled. See[Enabling Synchronization for an App Catalog Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/enable-synchronization-app-catalog-application.htm).

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/../domains/to-view-identity-domains.htm).
- On the details page, select Integrated applications . A list of applications in the domain is displayed.
- Select the name of the app that you want to configure.
- Verify that the app is activated.
- Select Import .
The page lists the result of the last import if any and the actions you need to perform. See[Synchronizing User Accounts](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/synchronize-user-accounts.htm).
- If you want to invoke an on-demand synchronization, select the Import icon. If the icon is unavailable, select the Provisioning tab and verify that Provisioning and Synchronization are enabled, and the app is activated.
- A message confirms that the job for importing users is running successfully.
