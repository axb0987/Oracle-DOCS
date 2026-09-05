# Error Code 400 for Deploy Button
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/deploy-button.htm
- Fetched: 2026-09-05 02:57 CDT

# Error Code 400 for Deploy Button

Troubleshoot error code 400 when using the Deploy to Oracle Cloud button.

When you attempt to create a stack from the linked[Deploy to Oracle Cloud button , the error message`Error code: InvalidParameter(400)`appears.

Possible causes:
- The URL isn't a valid zip file.
- The URL isn't accessible by Resource Manager.

To resolve this error, ensure that the URL points to a valid zip file, and that the URL is accessible without authentication.
- GitHub: To get a URL that points to the downloaded zip file, select the Code button and then right-click the Download ZIP option.
- GitLab: To get a URL that points to the downloaded zip file, select the Download button and then right-click the zip option.
- Object Storage ([pre-authenticated request URL](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)
