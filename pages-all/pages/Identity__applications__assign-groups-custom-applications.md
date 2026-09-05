# Assigning Groups to Custom Applications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/assign-groups-custom-applications.htm
- Fetched: 2026-09-05 02:19 CDT

# Assigning Groups to Custom Applications

You can modify custom applications by assigning groups to them. Users who are members of these groups can access the My Apps page to view these applications.
Prerequisite : The application must be activated.

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/../domains/to-view-identity-domains.htm).
- On the details page, select Integrated applications . A list of applications in the domain is displayed.
- Select the application that you want to modify.
- Select Groups .
- Select Assign groups .
- In the Assign groups window, do one of the following.
- Select the checkbox for each group that you want to assign to the application.
- For a provisioned application, select Assign next to the group that you want to assign to the application. Enter the required values for the form, and then select Save .

Note  
  

If the form contains multi-valued attributes, then an Add button appears to the right of each attribute. Select Add , and then in the Allowed values window, select the values for the attribute, and select OK .

The All tenant users group is a default group that's created by IAM. All IAM users are assigned to this group, by default. If you assign this group to any of your applications, then all users are assigned to these applications indirectly.
- Select Assign .

Note
