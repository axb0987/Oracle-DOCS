# Assigning Users to Custom Applications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/assign-users-custom-applications.htm
- Fetched: 2026-09-05 02:19 CDT

# Assigning Users to Custom Applications

Custom applications are non Oracle Public Cloud (OPC) services. You can modify custom applications by assigning users to them. Users can access the My Apps page to view these applications.

- 

The application must be activated.
- 

The application must be assigned to the current user who is accessing the My Apps page
- 

The Display in My Apps checkbox must be selected in the Details tab in the applications.

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/../domains/to-view-identity-domains.htm).
- On the details page, select Integrated applications . A list of applications in the domain is displayed.
- Select the application that you want to modify.
- Select Users .
- Select Assign users .
- In the Assign users window, do one of the following:
- Select the checkbox for each user that you want to assign to the application.
- For a provisioned application, select Assign next to the user that you want to assign to the application. Enter the required values for the form, and then select Save .

Note  
  
If the form contains multi-valued attributes, then an Add button appears to the right of each attribute. Select Add , and then in the Allowed values window, select the values for the attribute, and select OK .
- Select Assign .

Note  
  

If you assigned a provisioned application to the user, then you can modify the values of the application form. To do this, select the Actions menu, select Edit , change the appropriate values, and then select Save .

You can activate or deactivate a user's account assigned to a synchronized app that's created from the App Catalog. To do so:
- 

Select the Actions menu to the right of the user account that you assigned to the application.
- 

Select Activate or Deactivate .
- 

In the Activate account? or Deactivate account? window, select OK .

See[Enabling Provisioning for an App Catalog Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/enable-provisioning-app-catalog-application.htm)
