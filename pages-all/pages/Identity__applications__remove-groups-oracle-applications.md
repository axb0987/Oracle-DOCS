# Removing Groups from Oracle Applications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/remove-groups-oracle-applications.htm
- Fetched: 2026-09-05 02:19 CDT

# Removing Groups from Oracle Applications

You can remove groups from Oracle applications from the Application Roles tab. You can remove groups from Oracle applications only after you activate the applications.

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/../domains/to-view-identity-domains.htm).
- On the details page, select Integrated applications . A list of applications in the domain is displayed.
- Select the application that you want to modify.
- Select Application roles .
- Select the checkbox for the application role of the Oracle application from which you want to remove groups.

Tip  
  
You can see which application roles have groups assigned to them by the group icon and the Groups assigned link that appears in the application role.
- Select the Actions menu, and then select Revoke groups .
- In the Revoke groups window, select the checkbox for each group that you want to remove from the application role.

Note  
  
The All tenant users group is a default group that's created by IAM. All IAM users are assigned to this group, by default. If you remove the All tenant users group from your applications, then access rights to these applications are revoked for every IAM user.
-
