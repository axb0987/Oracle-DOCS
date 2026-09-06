# Add a Connection to a Custom Backend
- Source: https://docs.oracle.com/iaas/visual-builder/doc/add-connection-custom-backend.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/visual-builder/doc/add-connection-custom-backend.html#dcoc-content-body)

# Add a Connection to a Custom Backend

You can create your own backend to map to a custom server other than the Oracle Integration, Process, and Oracle Cloud Applications backend services. You can create a custom backend with a free-form URL, or create a custom ADF backend when you know the Describe URL that points to an ADF Describe service.

To add a connection to a custom backend:
- Open the instance’s Tenant Settings page.
- In the Services tab, click Create Backend .
  

  
[Description of the illustration admin-settings-custom.png](https://docs.oracle.com/iaas/visual-builder/doc/img_text/admin-settings-custom.html)  

- In the Create Backend wizard, select the type of backend you want to create:
- To create a backend with a free-form URL, click Custom .
- To create a backend with the Describe URL of an ADF service, click Custom ADF Describe . Use this option only when your custom ADF Describe endpoint does not have any child backends.
- In the Name field, enter a name and description for the custom backend.
- Add headers to the backend. Backend headers that you add will be applicable for any service connection to this backend, irrespective of the server or application profile that is used.
- Click Next .
- Enter the instance URL for the custom backend, configure other settings, such as security, and click Create .

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
