# Assigning a Provisioning Bridge to Apps
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/assign-provisioning-bridge-apps.htm
- Fetched: 2026-09-05 02:27 CDT

# Assigning a Provisioning Bridge to Apps

After creating a provisioning bridge for an identity domain in IAM, you can assign it to on-premises apps in the App Catalog. Because this bridge serves as a provisioning and synchronizing agent between the identity domain and your apps, the bridge can poll for changes to users or groups in the apps and synchronize those changes into the identity domain.

- On the Integrated applications list page, select the application to activate. If you need help finding the list page, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/../applications/listing-apps.htm).

Tip  
  
To search for applications, enter all or part of the beginning of the application name that you want to locate in the search field, and then press Enter . To fine-tune your search, select the search field again, and then select a status.
- Select the name of the App Catalog app to which you want to assign a bridge.
- On the app details page, select Deactivate .
- In the Deactivate application dialog box, select Deactivate application .

Note  
  
You must deactivate the app so that you can modify it by assigning a provisioning bridge to it.
- Under Resources , select Provisioning , and then select Edit provisioning .
- Turn on the Enable Provisioning switch.
- If prompted, confirm that you want to enable provisioning, and then select Save changes .
- From the Associate with Provisioning Bridge list, select the bridge that you want to assign to this app.

Note  
  
If the provisioning bridge has an inactive status, then activate it.
- Select Save .
- Select Activate .
- In the Activate provisioning bridge window, select Activate application .

Note  
  
By activating this app, the provisioning bridge that you assigned to it can be used either to poll the app for changes to users and groups in the app, and synchronize these changes into the identity domain, or to provision users to the app.
- To assign the provisioning bridge to another app, repeat the preceeding steps.
- Navigate back to the identity domain by selecting its link in the breadcrumb at the top of the page.
- Select Settings , and then select Provisioning Bridges .
- Select the name of the bridge that you assigned to apps, and then select Apps .
-
