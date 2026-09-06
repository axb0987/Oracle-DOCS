# Add a Connection to Oracle Cloud Applications
- Source: https://docs.oracle.com/iaas/visual-builder/doc/add-connection-applications.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/visual-builder/doc/add-connection-applications.html#dcoc-content-body)

# Add a Connection to Oracle Cloud Applications

The list of REST services in the service catalog of a visual application is retrieved from an Oracle Cloud Applications backend service. Specify the instance URL of the Oracle Cloud Applications backend service in the Tenant Settings page.

All visual applications in the tenant will use the Oracle Cloud Applications instance URL specified in Tenant Settings, but a visual application can be configured to use a different Oracle Cloud Applications backend service by specifying a different instance URL in the Backends tab (which you access from the Navigator's Services tab). The tenant-level backend configuration is ignored if you or a visual application developer configures a different Oracle Cloud Applications backend service in a visual application’s Backends tab.
The authentication choices available to configure a tenant-level Oracle Cloud Applications backend are:
- Basic Auth: Uses a fixed username and password for authentication.
- Oracle Cloud Account: Needs federation between Oracle Cloud Applications and Visual Builder.
- Delegate Authentication (previously called Propagate Current User Identity): Same as Oracle Cloud Applications. That is, it needs federation between Oracle Cloud Applications and Visual Builder.
- None: This assumes your Oracle Cloud Applications REST API can be called without any authentication, which is not usually the case.

See[About Authentication and Connection Type](https://docs.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/app-builder-cloud/visual-builder-oci-admin&id=VBCDG-GUID-132602A0-6ADE-417C-B249-5F1744E08D35)in Developing Applications with Oracle Visual Builder .

If the necessary prerequisites for setting a tenant-level Oracle Cloud Applications backend service are not available, then a visual application developer can set up a backend service at the visual application level where more options are available. Another option is for you (the service administrator) to configure the Oracle Cloud Applications backend with`None`and let the visual application developer override the authentication setting at the visual application level.

To specify an Oracle Cloud Applications service for the tenant:
- Open the instance’s Tenant Settings page.
- In the Services tab, click Create Backend , then choose Oracle Cloud Applications in the Create Backend dialog.
  
  
[Description of the illustration admin-settings-fa-url.png](https://docs.oracle.com/iaas/visual-builder/doc/img_text/admin-settings-fa-url.html)  

When specifying the URL in the Tenant Settings, you (the service administrator) only need to provide the instance URL of the Oracle Cloud Applications backend service to retrieve the list of services.
- In the dialog, type the Server URL of the backend service, and configure other settings, such as security, as needed.
- (Optional) After you configure settings for the backend, add headers to the backend.
Backend headers that you add will be applicable for any service connection to this backend, irrespective of the server or application profile that is used.
- Click Create .

Visual Builder automatically discovers the interfaceCatalogs endpoint of the Oracle Cloud Applications backend, which retrieves the list of services and their metadata. This endpoint is typically in the form:

```

```

This endpoint is publicly accessible without any authentication.

If there is a problem creating the connection, verify the instance URL of the Oracle Cloud Applications instance.

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
