# Getting Started with Toolkit for Eclipse
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/eclipsegettingstarted.htm
- Fetched: 2026-09-05 01:36 CDT

# Getting Started with Toolkit for Eclipse

This topic describes how to install, configure, and uninstall the OCI Toolkit for Eclipse.

## Downloading the Toolkit

You can download the`com.oracle.oci.eclipse.zip`toolkit from[the releases section on GitHub](https://github.com/oracle/oci-toolkit-eclipse/releases).

## Installing the Toolkit

After downloading the toolkit, launch the Eclipse IDE.
- From the top navigation bar, select Help &gt; Install New Software...
- In Install dialog, click Add...
- In the Add Repository dialog, click Archive...
- In the right pane of the Repository Archive window, select the zip file containing the toolkit. Click Open .
- In the Add Repository dialog click Add .
- In the Available Software dialog, select Oracle Cloud Infrastructure Toolkit for Eclipse , then click Next .
- In the Install Details dialog, click Finish .

## Configuring the Toolkit

### Oracle Cloud Infrastructure Preferences

Before you can use the toolkit, you must configure the Oracle Cloud Infrastructure Preferences in the Eclipse IDE. This process will provide the necessary identifiers and credentials so the toolkit can connect to your Oracle Cloud Infrastructure account. For more information, see[Required Keys and OCIDs](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/apisigningkey.htm).
- From the top navigation bar, select Preferences &gt; Oracle Cloud Infrastructure Preferences .
- For Profile Name , provide a short descriptive name.
- 

From the Region dropdown, select your region.
- Enter your User OCID and Tenancy OCID . For information on how to locate this information, see[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/apisigningkey.htm#five).
- For Key File , click Browse and select the appropriate file. For more information, see[How to Generate an API Signing Key](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/apisigningkey.htm#two).
- Enter the Fingerprint for the Key File. For more information, see[How to Get the Key's Fingerprint](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/apisigningkey.htm#four).
- 

Enter the Passphrase , if you created one for the key pair. If not, leave this field blank.
- Click Save Profile .
- Click Apply and Close .

### Proxy Settings

If you are on a network that uses a proxy to connect to the internet, you must configure Eclipse proxy settings. For more information, see Network Connections in the[Eclipse IDE Documentation](https://help.eclipse.org/2018-12/index.jsp).

## Uninstalling the Toolkit

Launch the Eclipse IDE.
- From the top navigation bar, select Help &gt; About Eclipse IDE
- Click Installation Details .
- In the Installation Details window, select the Installed Software tab.
- Select Oracle Cloud Infrastructure Toolkit for Eclipse and click Uninstall...
- In the Uninstall dialog, confirm the items to be uninstalled then click Finish .
-
