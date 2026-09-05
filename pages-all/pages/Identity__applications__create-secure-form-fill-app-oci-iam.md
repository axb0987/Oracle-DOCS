# Creating a Secure Form Fill App
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/create-secure-form-fill-app-oci-iam.htm
- Fetched: 2026-09-05 02:19 CDT

# Creating a Secure Form Fill App

After you create a configuration file in the Oracle Enterprise Single Sign-On (ESSO) Administrative Console, the next step is to create a secure form fill app.

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/../domains/to-view-identity-domains.htm).
- On the details page, select Integrated applications . A list of applications in the domain is displayed.
- Select Add application .
- In the Add application window, select Application catalog and then Launch workflow .
- Enable the Secure form fill filter Type .
- Search for and select Generic Secure FormFill App Template .
- Complete the application details by entering a Name , Description , and Application URL .

Important  
  

The application name must match the file name of the`.ini`file created in the ESSO Administrative Console.
- In the URLs section, add any necessary URLs.
- In the Display settings section, select Display in My Apps .

Important  
  
If you do not select Display in My Apps , the application does not display in the My Apps page for users.

When you select the Display in My Apps checkbox in applications, the app is then visible in the My Apps page, but selecting this checkbox doesn't enable or disable SSO to the app.
- Select the User can request access checkbox, if you want the app to be listed in the Catalog . This option allows end users to request access to applications from their My Apps page by selecting Add and then selecting the app from the Catalog .
- Select User can view their credentials if you want users to view their credentials in User settings .
- Select Create application .
- Select Import to import the secure form fill configuration file that you created in the ESSO Administrative Console.
The application has been added in deactivate state. To activate your application, select Activate next to the app name.
- To assign users to the application, select Users .

Tip  
  
Assign the application to yourself or a test user. This saves you time when testing the secure form fill app.
- To assign groups to the application, select Groups .
