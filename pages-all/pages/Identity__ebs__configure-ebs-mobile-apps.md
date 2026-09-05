# Configuring E-Business Suite for Mobile Applications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/configure-ebs-mobile-apps.htm
- Fetched: 2026-09-05 02:21 CDT

# Configuring E-Business Suite for Mobile Applications

Configure Oracle E-Business Suite to enable E-Business Suite mobile applications to authenticate with IAM.

- Access the drawer icon (E-Business Suite version 12.2.8) or navigator icon (E-Business Suite version 12.1/12.2), select Mobile Applications Manager , and then select Applications .
- Search for Application Name . For example,`EBS Approvals`.
- In the results list, select the Configure icon for the application. For example, EBS Approvals .
- In the Configure Mobile Application page, expand the Connection Settings .
- Select Sub Category as`AppsSSO Login`.
- Expand the Connection Settings category, and then update the parameters as follows:
- LoginURL :`%APPS_AUTH_AGENT%/login/sso`
- LogoutURL :`%APPS_AUTH_AGENT%/logout/sso`
- LoginSuccessURL :`%APPS_AUTH_AGENT%/login/sso`
- APPS_SESSION_SERVICE :`%APPS_AUTH_AGENT%/login/apps`
- Select Apply .
