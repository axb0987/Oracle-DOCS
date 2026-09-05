# Assigning Applications to a User
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/users/assign-applications-users.htm
- Fetched: 2026-09-05 02:30 CDT

# Assigning Applications to a User

Assign applications to a user in an OCI IAM identity domain.

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/users/../domains/to-view-identity-domains.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the User management tab, and then go to the User section of the tab.
- Under Identity domain on the left side of the page, select Users .
- Select a person's username to see their details.
- Select Integrated applications .
- Select Assign applications .
- In the Assign applications window, select the Actions menu (three dots) and select Assign for each application that you want to assign to the user account.
- If you're assigning a managed application to the user account, then an Assign Application window appears, containing a form for the application. To populate this form:
- Enter the required values for the form.
- If the form contains multi valued attributes, then an Add button appears to the right of each attribute. Select Add , and then in the Allowed Values window, select the values for the attribute, and select OK .

Tip  
  
To remove an existing value from the attribute, select the X button to the right of the value.
- Select Save .

Note  
  

The Active icon for each application in the Access tab represents the active status of the user account and not the application status. The status remains active as long as the user account is active, regardless of whether the application is active or inactive.
- Select Finish .

Note  
  

If you assigned a managed application to the user account, then you can modify the values of the application form. To do this, select the Actions menu (three dots) then select Edit , change the appropriate values, and then select Save .

Also, if you have enabled and configured synchronization for an App Catalog app, and assigned the app to a user account, then you can activate or deactivate the user's account with the app. To do so:
- 

Select the Actions menu (three dots) for the App Catalog app that you assigned to the user.
- 

Select Activate or Deactivate .
-
