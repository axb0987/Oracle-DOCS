# Managing Provisioning Bridges
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/managing-provisioning-bridge.htm
- Fetched: 2026-09-05 02:27 CDT

# Managing Provisioning Bridges

The provisioning bridge provides a link between your on-premises apps and IAM. Through synchronization, account data that's created and updated directly on the apps is pulled into an identity domain and stored for the corresponding identity domain users and groups. As a result, any changes to these records are transferred into an identity domain. So, if a user is deleted in one of your apps, then this change is propagated into the identity domain. Because of this, the state of each record is synchronized between your apps and the identity domain.

Suppose you're using an on-premises app such Oracle Internet Directory as an authoritative source for your company's users and groups. This app lies within your company's firewall. For a provisioning bridge to communicate with on-premises apps such as Oracle Internet Directory, it must use Identity Connector Framework (ICF) connectors to access the associated apps. As a result, the provisioning bridge can poll the on-premises apps for changes to users and groups in the apps, and synchronize these changes with the identity domain. You can configure a provisioning bridge so that IAM can synchronize users and groups from one or multiple apps.

The following image shows directory synchronization:

[

Both the provisioning bridges and your on-premises apps are in your Microsoft Windows or generic environment. A generic environment consists of any machine that has Java 8 installed on it and supports Bash shell.

Each provisioning bridge uses a client network to access the on-premises apps with which you want to synchronize identity domain users and groups. Because IAM is in a different environment, a bridge is needed to span the networks.

The following image shows provisioning bridge security:P

[

To manage provisioning bridges, you must have one of the following access grants:
- Be a member of the Administrators group
- Be granted the Identity Domain Administrator role or the Security Administrator role
- Be a member of a group granted`manage`domains

To understand more about policies and roles, see[The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/../getstarted/identity-domains.htm#The),[Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/../roles/understand-administrator-roles.htm), and[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/../policieshow/Policy_Basics.htm).

## Statuses
A provisioning bridge client has two statuses:
- 

Started: The provisioning bridge started successfully.
- 

Stopped: The provisioning bridge stopped unexpectedly or the identity domain administrator or security administrator stopped it. See[Stop a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/stop-provisioning-bridge.htm).
A provisioning bridge has two statuses:
- 

Active: The provisioning bridge is installed, started, and activated. It's available to poll the apps to which the provisioning bridge is assigned for changes to users and groups in the apps, and synchronize these changes with the identity domain. See[Activate Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/activate-provisioning-bridges.htm).
- 

Inactive: The provisioning bridge is installed and configured, but it's deactivated. It's not available to retrieve users and groups from the apps to which the provisioning bridge is assigned. For performance reasons, this is done. See[Deactivate Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/deactivate-provisioning-bridges.htm).

- [Listing Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/list-provisioning-bridges.htm)
- [Creating a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/create-provisioning-bridge.htm)
- [Removing Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/remove-provisioning-bridges.htm)
- [Starting a Provisioning Bridge on a Generic Machine](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/start-provisioning-bridge-generic-machine.htm)
- [Starting a Provisioning Bridge on a Windows Machine](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/start-provisioning-bridge-windows-machine.htm)
- [Stopping a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/stop-provisioning-bridge.htm)
- [Activating Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/activate-provisioning-bridges.htm)
- [Deactivating Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/deactivate-provisioning-bridges.htm)
- [Viewing Details about a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/view-details-provisioning-bridge.htm)
- [Modifying a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/modify-provisioning-bridge.htm)
- [Assigning a Provisioning Bridge to Apps](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/assign-provisioning-bridge-apps.htm)
- [Changing the Provisioning Bridge Assigned to Apps](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/change-provisioning-bridge-assigned-apps.htm)
- [Managing Log Files for a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/manage-log-files-provisioning-bridge.htm)
