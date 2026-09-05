# Regenerating a Client Secret for Confidential Applications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/regenerate-client-secret-confidential-applications.htm
- Fetched: 2026-09-05 02:19 CDT

# Regenerating a Client Secret for Confidential Applications

When you create a confidential application, you use a Client ID and a Client Secret as part of your connection settings. You can regenerate your Client Secret at any time for a confidential application using the identity domains console.

Before You Begin:

Create an confidential application and activate it. See[Adding a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-confidential-application.htm).

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/../domains/to-view-identity-domains.htm).
- On the details page, select Integrated applications . A list of applications in the domain is displayed.
- Select the confidential application for which you want to regenerate a client secret.
- Depending on the options you see, do one of the following:

- Select the OAuth configuration tab and then select Regenerate secret , or
- in the General information section of the application detail page, select Regenerate .
- Confirm your choice to regenerate the secret. The new Client Secret appears in the New client secret dialog box.
- Copy the Client Secret if necessary.
-
