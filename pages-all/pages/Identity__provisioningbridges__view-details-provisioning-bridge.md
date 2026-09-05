# Viewing Details about a Provisioning Bridge
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/view-details-provisioning-bridge.htm
- Fetched: 2026-09-05 02:27 CDT

# Viewing Details about a Provisioning Bridge

View the details of a provisioning bridge in an IAM identity domain.

On the provisioning bridges list page, you can see the name, description, and connection status for each bridge.

On a bridge's details page, Yyou can also see other information about a provisioning bridge, such as its identity domain URL, version number, client ID, and client secret, any apps assigned to the bridge, and any connectors that are used by the bridge to communicate between the apps and the identity domain.

- On the Provisioning bridges list page, select the provisioning bridge that you want to work with. If you need help finding the list page or the recipe, see[Listing Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/list-provisioning-bridges.htm).
On the details page, the Provisioning bridge Information tab displays information about the provisioning bridge, including its name, description, identity domain URL, version number, and client ID. By selecting Show secret , you can see the client secret for the provisioning bridge in clear text. By selecting Regenerate , you can regenerate the secret for this bridge.
- Select Details .
In this tab, you see information about the provisioning bridge, including its name, description, identity domain URL, version number, and Client ID. By selecting Show Secret , you can see the Client Secret for the provisioning bridge in clear text. By selecting Regenerate , you can regenerate the Secret for this bridge.
- Under Resources , select Apps .
The Apps section displays a list of apps assigned to the provisioning bridge. You can assign more apps to this bridge or change the bridge associated with the apps. See[Assign a Provisioning Bridge to Apps](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/assign-provisioning-bridge-apps.htm)and[Change the Provisioning Bridge Assigned to Apps](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/change-provisioning-bridge-assigned-apps.htm).
Note  
  
For load-balancing purposes, Oracle suggests that you don't assign more than 10 apps to a provisioning bridge. To maintain more apps, create another provisioning bridge.
- Under Resources , select Connectors .
