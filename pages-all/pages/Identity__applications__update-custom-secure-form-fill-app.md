# Updating a Custom Secure Form Fill App
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/update-custom-secure-form-fill-app.htm
- Fetched: 2026-09-05 02:19 CDT

# Updating a Custom Secure Form Fill App

To update a custom secure form fill app, you first update the Web app using the Secure Form Fill App, export the configuration file in (*.ini), and then update the custom secure form fill app in the identity domain.

Before you begin:
- 

Create a Web app in the Secure Form Fill Admin Client. See[Installing the Secure Form Fill Admin Client](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/install-secure-form-fill-admin-client.htm).
- 

Create a custom secure form fill app created in the identity domain.
To update a custom secure form fill app, complete the following steps:

- If you need to update the Web app and configuration file created in Secure Form Fill Admin Client, update the Web app first, and then save and export the file. See[Create a Secure Form Fill Configuration File](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/create-secure-form-fill-configuration-file.htm).
- To change the custom secure form fill app, access the application as an Identity domain administrator, make any necessary changes, import the new configuration file (if necessary), and then save the app. See[Create a Secure Form Fill App in IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/create-secure-form-fill-app-oci-iam.htm).
What to do next: Test your new configuration. See[Test a Custom Secure Form Fill App](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/test-custom-secure-form-fill-app.htm)
