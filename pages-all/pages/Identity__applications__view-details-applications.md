# Viewing Details About Applications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/view-details-applications.htm
- Fetched: 2026-09-05 02:20 CDT

# Viewing Details About Applications

By default, you can see the name and description for each application in IAM.
By selecting an application name, you can view high-level and configuration information about the application. For Oracle applications, you can also see the roles associated with the application, and the IAM groups and users assigned to the application.

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/../domains/to-view-identity-domains.htm).
- On the details page, select Integrated applications . A list of applications in the domain is displayed.
- Select the application name for which you want additional information. If you need help finding the list page, see[Listing Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/listing-apps.htm).

Tip  
  
To search for applications, enter all or part of the beginning of the application name that you want to locate in the search field, and then press Enter . To fine-tune your search, select the search field again, and then select a status.
- To view high-level information about the application, such as the application type, name, description, icon, URL, links, and whether the application will appear on the My Apps page, select Edit application .
- To view configuration information about the application, select Configuration . For custom SAML applications, this tab is labeled SSO configuration because, by granting SAML applications to users, they can single sign-on (SSO) into SaaS applications that support SAML for SSO. See[Add a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-confidential-application.htm),[Add a Mobile Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-mobile-application.htm), and[Add a SAML Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-saml-application.htm).
- For Oracle applications, to view roles associated with the application, select Application roles . You can assign users and groups to an application role or remove users and groups from the application role. See[Editing an Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/modify-applications.htm).
- For Oracle applications, to view the names and descriptions of any groups assigned to the application, select Groups .
- For Oracle applications, to view the names, email addresses, and phone numbers of any users assigned to the application, select Users . You can filter and sort this list of users.
- To display only those users who are assigned to a particular application role, select Show , and then select the application role.
- To display users who are assigned to any application role, select Show , and then select All role members .
-
