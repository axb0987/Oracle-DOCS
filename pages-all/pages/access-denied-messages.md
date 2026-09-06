# Set Page Messages for Access Denied Errors
- Source: https://docs.oracle.com/iaas/visual-builder/doc/access-denied-messages.html
- Fetched: 2026-09-05 18:58 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/visual-builder/doc/access-denied-messages.html#dcoc-content-body)

# Set Page Messages for Access Denied Errors

Administrators can use the instance’s settings page to specify a URL that users are navigated to when they are denied access to an application or page.

Authenticated users might see an Access Denied page or message when they attempt to access an application or page in an application that their user role is not permitted to access. Administrators can set the default page or message that users see when they are denied access to an application or page. Access Denied messages that are set at the application level in the General Settings of an application will override messages set in the instance’s settings page. The default Access Denied page and message is used if the message options in this panel are not set.

To specify an Access Denied page or message for applications in the instance:
- In the upper-left corner of the Visual Builder title bar, click Navigation Menu .
- Click Settings in the navigation menu to open Tenant Settings.
  

  
[Description of the illustration admin-menu-settings.png](https://docs.oracle.com/iaas/visual-builder/doc/img_text/admin-menu-settings.html)  

- In the Security panel, type a URL that users are directed to when denied access to an application.

The URL that you specify is used as the Access Denied page for all applications in the instance and should be accessible to users who are not logged in.  
  
[Description of the illustration admin-settings-messages.png](https://docs.oracle.com/iaas/visual-builder/doc/img_text/admin-settings-messages.html)  

Note  
  
If you are configuring settings for classic applications, the Access Denied settings are set in the Messages panel.
- Type the message that you want users to see when they are denied access to a page.

The message that you enter will be displayed in the Access Denied page for all applications in the instance except for those where a message was set at the application level in the application’s General Settings page.

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
