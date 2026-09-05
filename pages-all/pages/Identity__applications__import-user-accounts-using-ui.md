# Importing Users into Applications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/import-user-accounts-using-ui.htm
- Fetched: 2026-09-05 02:19 CDT

# Importing Users into Applications

You can perform a full sync import of the users of third-party Cloud applications using a flat file. In a full sync import, the imported user in the CSV file replaces any existing user who is already assigned to the application.

- Create a CSV file for import in the following format or download the CSV file along with user data from the target system apps:

```

```

This table provides a description of the attributes in the CSV format file:

Attribute Name

Description

Sample Value

ID

The unique identifier of the account in the target.

hercule.poirot@sampleapp.com

NAME

The name of the account.

NAME is the primary input that is matched with the username of a particular user in IAM&gt;.

hercule.poirot@sampleapp.com

ACTIVE

The status of the account on the target. The possible values are`true`and`false`.

If the value is`true`, the user account is imported and activated. If the value is`false`, the user is imported in a deactivated state.

true
- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/../domains/to-view-identity-domains.htm).
- On the details page, select Integrated applications . A list of applications in the domain is displayed.
- Select the application to change.
- Depending on the options you see, do one of the following:

- select the Import tab, then under the Actions menu (three dots) , select Import , or
- on the application detail page, select Import .
- Browse for the CSV file, and import it.

Note  
  
Import from CSV file is enabled for applications that support flat file synchronization.
- Refresh the page to view the import result. If the import succeeds, then the users present in the CSV file displays.
- Select Users to view the imported users.

Note  
  
Refresh the Users tab to view the imported users.
- Observe that the users with a`true`value for ACTIVE attribute are activated. However, if a user account has`false`value for ACTIVE attribute, the user account is imported in a deactivated state.

Note  
  
The Users tab displays only the matched and confirmed users.
- Synchronize the imported users. See[Synchronizing Imported User Accounts](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/synchronize-imported-user-accounts.htm)
