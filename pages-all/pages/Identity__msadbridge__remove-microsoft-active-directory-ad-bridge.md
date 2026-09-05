# Removing an AD Bridge
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/remove-microsoft-active-directory-ad-bridge.htm
- Fetched: 2026-09-05 02:24 CDT

# Removing an AD Bridge

Remove an AD bridge from an IAM identity domain.

- On the Directory integrations list page, select the AD bridge that you want to remove. If you need help finding the directory integrations page, see[Listing Active Directory Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/list-ad-bridges.htm).
- From the Actions menu (three dots) select Remove .
- When prompted, confirm the deletion.
By removing the domain, you're removing the bridge associated with the domain. To ensure that the bridge is deleted cleanly and completely, you must delete the client associated with the bridge.
- Double-click the`ad-id-bridge.exe`file.
The IAM Microsoft Active Directory Bridge Installer appears.
- In the Welcome dialog box, select Next .
- In the Removal completed dialog box, select Close .

Important  
  
If you can't remove the client for the AD bridge or the bridge still appears in the Directory integrations page, then complete the following steps:

- Run the following cURL command to obtain the client ID that you used to install the client for the AD bridge:
```

```

`<Identity_Cloud_Service_URL>`is a placeholder for the identity domain URL that you used to install the client for the bridge, and`<access_token>`is a placeholder for the access token that contains the authorization credentials that are required to obtain the client ID.

See the[IAM: First REST API Call](https://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/idcs/idcs_rest_1stcall_obe/rest_1stcall.html)tutorial to learn how to get this access token.

A list of bridge clients that are installed for your identity domain appears.
- From this list, find the client ID of the bridge that you want to remove.
- Run the following cURL command to remove the client for the bridge:

```

```

`<Client_ID>`represents the ID of the client for the bridge that you want to remove.

A`204 (No Content)`
