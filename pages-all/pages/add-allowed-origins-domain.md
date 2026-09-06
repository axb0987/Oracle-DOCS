# Allow Other Domains Access to Services
- Source: https://docs.oracle.com/iaas/visual-builder/doc/add-allowed-origins-domain.html
- Fetched: 2026-09-05 18:59 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/visual-builder/doc/add-allowed-origins-domain.html#dcoc-content-body)

# Allow Other Domains Access to Services

Use the Global Settings page to specify the domains that are permitted to interact with services in your instance.

Cross-Origin Resource Sharing (CORS) is a mechanism that enables you to specify the domains that are allowed to exchange data with applications in your instance. By default, incoming requests from domains not on your instance’s list of allowed origins are blocked from accessing application resources.

To add a domain to the list of allowed origins:
- In the upper-left corner of the Visual Builder title bar, click Navigation Menu .
- Click Settings in the navigation menu to open Tenant Settings.
  

  
[Description of the illustration admin-menu-settings.png](https://docs.oracle.com/iaas/visual-builder/doc/img_text/admin-menu-settings.html)  

- In the Allowed Origins panel, click New Origin and type the URL of the domain that you want to allow. Click Submit .

The URL must be a fully-qualified domain, meaning it must contain`http://`or`https://`, for example,`https://myoracle.cloud.service`. You must explicitly enter each fully-qualified domain that you want to allow. To allow both`http://`and`https://`connections from a domain, you would need to add both domains (`https://myoracle.cloud.service`and`http://myoracle.cloud.service`).  
  
[Description of the illustration admin-settings-origins.png](https://docs.oracle.com/iaas/visual-builder/doc/img_text/admin-settings-origins.html)  

The Allowed Origins panel lists all origins that are permitted to retrieve information from the instance.

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
