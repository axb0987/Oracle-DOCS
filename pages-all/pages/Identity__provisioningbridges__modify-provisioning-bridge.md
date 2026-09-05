# Modifying a Provisioning Bridge
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/modify-provisioning-bridge.htm
- Fetched: 2026-09-05 02:27 CDT

# Modifying a Provisioning Bridge

Modify the name, description, or client secret of a provisioning bridge in an IAM identity domain.

To change the apps to which the bridge is assigned, see[Changing the Provisioning Bridge Assigned to Apps](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/change-provisioning-bridge-assigned-apps.htm).

To change the folder where all log files for the provisioning bridge are stored and the log level for these log files, see[Manage Log Files for a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/manage-log-files-provisioning-bridge.htm).

- On the Provisioning bridges list page, select the provisioning bridge that you want to work with. If you need help finding the list page or the recipe, see[Listing Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/list-provisioning-bridges.htm).
- To edit the name or descriptive information about the bridge, select Edit provisioning bridge , change the values as needed, and then select Save changes .
- To regenerate the Client Secret for this bridge, select Regenerate .

- If the bridge is in the Activated state, then you can't regenerate a client secret for it because the bridge is using this secret to access the identity domain as an administrator.
- To regenerate a secret for this bridge, you must first deactivate the bridge, and then stop it. See[Deactivate Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/deactivate-provisioning-bridges.htm)and[Stop a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/stop-provisioning-bridge.htm).
- If you regenerate the secret for a provisioning bridge, then you must delete the`wallet`folder and recreate the Oracle Wallet that you made in[Create a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/create-provisioning-bridge.htm)so that the wallet contains the regenerated secret.
- In the New client secret window, select Copy to copy the client secret to the clipboard.
-
