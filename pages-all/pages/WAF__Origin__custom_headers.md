# Custom Headers
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/custom_headers.htm
- Fetched: 2026-09-05 03:10 CDT

# Custom Headers

Describes how to configure custom headers for the origins for an edge policy.

Use custom headers to help validate that the requests made to your origin were sent from the edge. Custom headers let you configure your origin to only allow requests that contain the custom header values that you specify.

## Using the Console

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.
All the edge policies in that compartment are listed in a table.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:

- State
- Name
- Policy Type : Select Edge Policy .
- Select the name of the edge policy where you want to configure custom headers for the origins.
The edge policy's details page opens.
- Select Settings under WAF Policy .
The Settings list appears.
- Select the Origin Settings tab.
- Select Edit .
The Origin Management Settings panel opens.
Note  
  
The Edit option is available when the policy status is ACTIVE, and isn't available when the status is UPDATING.
- Scroll to the bottom of the dialog box and select Show Advanced Options .
The Custom Headers section opens.
- Enter the Header Name and Header Value .

Select + Additional Header to add another custom header row for you to complete. Select X to remove an associated header row.
- Select Save Changes .
Publish your changes for them to take effect. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/../Bot/publishing_changes.htm#PublishChanges)
