# Adding a Network Perimeter to an Application
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/add-network-perimeter-to-an-application.htm
- Fetched: 2026-09-05 02:24 CDT

# Adding a Network Perimeter to an Application

Configure OAuth client IP restrictions for an integrated application
Before you begin:
- Ensure that you're an Identity Domain Administrator or Application Administrator with permissions for the target application.
- Create a network perimeter.
- Ensure that you have access to the OCI Console and to the correct identity domain.
To add a Network Perimeter to an Application:

- On the Domains list page, select the domain in which you want to make changes.
If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/../domains/to-view-identity-domains.htm).
- On the Details page, select Integrated applications .
A list of applications in the domain is displayed.
- Select the application to open a detailed view.
- In the application settings, select OAuth configuration and then Edit OAuth configuration .
- If not already selected, under Client configuration , select Configure this application as a client now .
- In the Client IP address section, select Restrict by network perimeter .
- Enter or select one or more Network Perimeters .
-
