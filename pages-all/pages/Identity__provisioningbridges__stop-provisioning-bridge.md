# Stopping a Provisioning Bridge
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/stop-provisioning-bridge.htm
- Fetched: 2026-09-05 02:27 CDT

# Stopping a Provisioning Bridge

Stop a provisioning bridges in an OCI IAM identity domain.

If you stop a provisioning bridge that's running on a Windows or generic machine, then you must wait three minutes to restart the bridge. Also, before you stop a provisioning bridge, you must deactivate it. See[Deactivate Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/deactivate-provisioning-bridges.htm).

Use the following table to guide you on how to stop a provisioning bridge.

Machine Mode Action
Generic`normal`Close the Terminal window or press`Ctrl + C`.
Generic`background`At the prompt of the Terminal window, stop the process by entering`kill -9 [Process_ID]`.

Note: Because you started the provisioning bridge in`background`mode, even if you close the Terminal window, the bridge continues to run. For this reason, you must stop the process to stop the provisioning bridge.
Tip: If you don't know the process ID, then run the following command:
```

```

Windows N/A Close the Command window.

- On the Provisioning bridges list page, select the provisioning bridge you want to work with. If you need help finding the list page or the recipe, see[Listing Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/list-provisioning-bridges.htm).
- Verify that the provisioning bridge that you stopped has a status of Stopped .
