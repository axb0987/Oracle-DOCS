# Adding a Datastore in vSphere using VMware Solution Management Appliance
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvs-management-app-adding-datastore.htm
- Fetched: 2026-09-05 03:08 CDT

# Adding a Datastore in vSphere using VMware Solution Management Appliance

Add a datastore in vSphere using VMware Solution Management Appliance.

- Sign in to the vSphere web console.
If you need information about how to sign in, see the[SDDC's details](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-get.htm)page.
- Select Inventory , and then select the Storage tab.
- Right-click a storage cluster, go to OCI Integration , and then select Add datastore .
- Enter the following information:

- Datastore name : Enter a name for the new datastore.
- OCI datastore compartment : The compartment containing the storage cluster.
- Datastore cluster : Select one of the following options:
- Use existing datastore cluster : Select to place the new datastore in the existing datastore cluster.
- Create new datastore cluster : Complete the following items to create a new datastore cluster for the datastore:
- Datastore cluster name : Enter a name for the new datastore cluster.
- OCI datastore cluster compartment : Select the compartment containing the new datastore cluster.
- vCenter host cluster : Enter the vCenter host cluster associated with the new datastore cluster.
- Select Next .
- Enter the block volume configuration:

- Block volume size and units : Enter the size of the datastore and select the units that represent the size.
- Encryption : Select one of the following options:
- Encrypt using Oracle-managed keys : Select to have Oracle handle all encryption-related matters to Oracle.
- Encrypt using customer-managed keys : Select to specify the vault and key the datastore uses for encryption yourself.
- Select Next .
- Customize the block volume parameters:

- Volume performance : Select the default option, or customize the block volume performance.
- Backup policy : Select backup policy for the block volume.

For more information, see[Block Volume](https://docs.oracle.com/iaas/Content/Block/home.htm).
- Select Next .
- (Optional) Apply tagging. For more information, see[Tagging](https://docs.oracle.com/iaas/Content/Tagging/home.htm).
- Select Next .
- Review the configuration summary.
- Select Create .
- Sign in to OCI.

Note  
  
The Management Appliance requires user authentication for this operation. If you're not sure what OCI sign-in credentials to use, contact your administrator.
The Management Appliance starts a job that adds the datastore. You can monitor the job and its steps. See[Monitoring VMware Solution Management Appliance Jobs in vSphere](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvs-management-app-jobs.htm)
