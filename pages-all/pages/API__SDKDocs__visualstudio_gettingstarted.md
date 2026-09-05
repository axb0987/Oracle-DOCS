# Getting Started with Oracle Developer Tools for Visual Studio
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/visualstudio_gettingstarted.htm
- Fetched: 2026-09-05 01:37 CDT

# Getting Started with Oracle Developer Tools for Visual Studio

This topic describes how to install, configure, and uninstall the Oracle Developer Tools for Visual Studio.

## Installing the Extension

The Oracle Developer Tools for Visual Studio is available in the Visual Studio Marketplace.
- From the Visual Studio menu, select Extensions-&gt;Manage Extensions
- From the list on the left side of the dialog, select Online and then Visual Studio Marketplace
- Find the "Oracle Developer Tools for Visual Studio 2019" extension.
- Click on the Download button next to the extension.
- 

A browser window opens with instructions to download the installer.

## Configuring the Toolkit

### Oracle Developer Tools for Visual Studio Preferences

Before you can use the developer tools, you must configure the Oracle Cloud Infrastructure Preferences. This process will provide the necessary identifiers and credentials so the developer tools can connect to your Oracle Cloud Infrastructure account. For more information, see[Required Keys and OCIDs](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/apisigningkey.htm).
- The deployment wizard requires an Oracle Cloud Infrastructure user credentials configuration file. For more information, see[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm).
- Run the "docker desktop" app, and ensure it has the Linux Containers option selected.
- If behind a proxy, set the proxy values http_proxy and https_proxy in the environment variables for Windows and in the Docker Desktop settings (see the Resources-&gt;Proxies menu).

## Uninstalling the Toolkit

- From the Visual Studio menu, select Extensions , then Manage Extensions .
- From the list on the left side of the dialog, select Installed .
- Select "Oracle Developer Tools for Visual Studio 2019" from the middle menu and click on the Uninstall button that appears next to it.
Note
