# Modifying an AD Bridge Between IAM and Microsoft Active Directory
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/modify-microsoft-active-directory-ad-bridge.htm
- Fetched: 2026-09-05 02:24 CDT

# Modifying an AD Bridge Between IAM and Microsoft Active Directory

Modify details of bridge between IAM and Microsoft Active Directory.

You can change the following items for a Microsoft Active Directory (AD) bridge:
- The Microsoft Active Directory users and groups that you want IAM to import using the AD bridge.
- Whether, after a user or group is synchronized from Microsoft Active Directory to IAM, if you activate or deactivate a user, modify the user's attribute values, or change the group memberships for the user in IAM, these changes are propagated to Microsoft Active Directory.
- How often you want IAM to use the AD bridge to import users and groups from Microsoft Active Directory.
- The predefined and custom attribute mappings defined between Microsoft Active Directory and IAM.
- Whether users can use their Microsoft Active Directory or their IAM passwords, or their federated accounts, to sign in to IAM to access resources protected by IAM, such as the My Profile Console, IAM Console, and apps assigned to the users.

Note  
  

You can upgrade the client for the AD bridge. By doing this, you can install the latest client without removing the existing client that's installed.

To upgrade the client, download it and follow the instructions in[Create a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/create-microsoft-active-directory-ad-bridge.htm). When you see the Specify Oracle Identity Cloud Service Credentials or the Specify Microsoft Active Directory Credentials dialog boxes, use the credentials you provided in the previous installation. For this reason, the values are unavailable to edit.

## Modifying an AD Bridge

- On the Directory integrations list page, select the AD bridge you want to work with. If you need help finding the directory integrations page, see[Listing Active Directory Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/list-ad-bridges.htm).
- To edit configuration information about the bridge, select Configuration .
- In the Select organizational units (OUs) for users and Select organizational units (OUs) for groups panes, select or clear checkboxes to enable or prevent IAM from importing users and groups using the bridge.
See[Configure a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/configure-microsoft-active-directory-ad-bridge.htm)for more information about the Select organizational units (OUs) for users and Select organizational units (OUs) for groups panes.
- In the Supported operations area, select or clear checkboxes to enable or prevent IAM from propagating changes for a user's activation status, attribute values, or group memberships to To edit configuration information about the bridge.
See[Configure a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/configure-microsoft-active-directory-ad-bridge.htm)for more information about the Supportedoperations area.
- In the Set import frequency area, change how often you want IAM to use the bridge to import users and groups from To edit configuration information about the bridge.
- In the Configure attribute mappings area, select Edit attribute mappings . The Edit attribute mappings window opens and two tabs appear:

- Microsoft Active Directory to Identity cloud: In this tab, you can modify inbound attribute mappings from Microsoft Active Directory to IAM.
- Identity cloud to Microsoft Active Directory: Use this tab to modify outbound attribute mappings from IAM to Microsoft Active Directory.
- 

Select the Microsoft Active Directory to Identity cloud or Identity cloud to Microsoft Active Directory tab.
- 

In the Directory User Attributes and IAM User Attributes columns, change the Microsoft Active Directory or IAM attribute used for the predefined or custom attribute mapping.
- 

To remove an attribute mapping, select the X button to the right of the mapping.
Note  
  
Inbound attribute mappings with asterisks in the Microsoft Active Directory to Identity cloud tab are required by the bridge to pass values associated with Microsoft Active Directory user accounts into IAM so that the accounts can be created in IAM. You can't delete these mappings.
- 

Select Save to close the Edit Attribute Mappings window.
See[Define Attribute Mappings for a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/define-custom-attribute-mappings-microsoft-active-directory-ad-bridge.htm)for more information about the Directory User Attributes and IAM User Attributes columns of the Microsoft Active Directory to IAM and IAM to Microsoft Active Directory tabs of the Edit Attribute Mappings window.
- In the Authentication Settings area, select the Enable local authentication option if you want users to use their IAM or their Microsoft Active Directory passwords to sign in to IAM to access IAM-protected resources.

If you select this option, then configure delegated authentication for the bridge. See[Configure a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/configure-microsoft-active-directory-ad-bridge.htm).

If you select Enable local authentication , then select or clear Don't send Welcome Notifications to enable or prevent IAM from notifying users by email that they must activate the IAM accounts that are created for them.

Otherwise, select Enable federated authentication to have users use their federated accounts to sign in to IAM.
- Select Save .
- In the Confirmation window, select OK .
See[Configure a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/configure-microsoft-active-directory-ad-bridge.htm)
