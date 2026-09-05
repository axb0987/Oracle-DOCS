# Removing Groups from Custom Applications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/remove-groups-custom-applications.htm
- Fetched: 2026-09-05 02:19 CDT

# Removing Groups from Custom Applications

You can modify custom applications by removing groups from them. Users who are members of these groups can no longer view these applications through the My Apps page.
Activate the application.

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/../domains/to-view-identity-domains.htm).
- On the details page, select Integrated applications . A list of applications in the domain is displayed.
- Select the application that you want to modify.
- Select Groups .
- Select the checkbox for each group that you want to remove from the application.

The All tenant users group is a default group that's created by IAM. All IAM users are assigned to this group, by default. If you remove the All tenant users group from your applications, then access rights to these applications are revoked for every IAM user.
-
