# Deleting a VCN
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_vcn.htm
- Fetched: 2026-09-05 02:43 CDT

# Deleting a VCN

Delete a Virtual Cloud Network (VCN) from OCI.

The Console has an easy "Delete all" process that scans the chosen compartments and then deletes a VCN and its related Networking resources (subnets, route tables, security lists, sets of DHCP options, internet gateway, and so on). If the VCN is attached to a Dynamic Routing Gateway (DRG), the process deletes the attachment, but the DRG remains.

The "Delete All" process deletes one resource at a time. A VCN with many compartments and resources takes longer to delete than a VCN with only a few. A progress report is displayed to show the results of both the scan for resources and the deletion of those resources.
Note  
  

Before using the "Delete All" process, verify that no resources such as Compute instances,[load balancers](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm), OCI database systems, or orphaned mount targets are present in any of the subnets. If any of these are present, the deletion process stalls when trying to delete the resource's subnet. Deleted VCN resources are irretrievable. For more information, see[Subnet or VCN Deletion](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Troubleshoot/vcn_troubleshooting.htm#Subnet_or_VCN_Deletion).

If any subnet still contains resources, or if you don't have permission to delete a particular Networking resource, the "Delete All" process stops and returns an error message that includes the OCIDs of the blocking resources and subnets, which link to the details page for that resource. Sometimes, you might need to contact the tenancy administrator to help you delete any remaining resources if you don't have the needed permissions.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_vcn.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_vcn.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete_vcn.htm#)
- 

- On the Virtual Cloud Networks list page, find the VCN that you want to delete. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- From the Actions menu (three dots) for the VCN, select Delete .
- In the Delete Virtual Cloud Network dialog box, select Search compartments for resources associated with this VCN .

When you select this option, the process scans for active resources in the VCN. If the process finds any active resources (subnets and route tables, for example) it deletes them if possible, then deletes the VCN. If the process finds a VNIC on a Compute instance, a Load Balancer, a database system, or a mount target, you must manually delete those resources and then restart the process.

We recommend selecting this option unless you're certain the VCN and its subnets are already empty. If you select this option, you can also select which compartments to search:
- All n compartments : This option searches all compartments in the same region as this VCN for resources associated with the VCN.
- Specific compartments : This option lets you select specific compartments and searches only the chosen compartments for resources associated with the VCN.

Searching more compartments takes more time, but is more thorough and has a smaller chance of failure.
- Select Scan .

The scan begins. Progress is displayed in the completion bar when the process identifies associated resources. The scan lists associated VCN resource types such as subnets, DRG attachments, internet or NAT gateways, and so on.
- Select Delete All to delete associated resources in the order listed.

If you don't have the necessary permissions to delete an associated resource or some other error occurs, the deletion process stops. Deleted VCN resources are irretrievable. Resolve the error and restart the process to delete the VCN.

If a subnet still contains Compute instances, Load Balancers, and so on, deleting the subnet fails. The resulting error message displays the OCID of the subnet and the blocking item in that subnet. Select the OCID to go to the details page for that item and either delete it or move it to a subnet in a different VCN.
- Select Close when the deletion of the VCN and all associated resources finishes.
If the VCN is empty, its state changes to Terminating and then Terminated temporarily until the VCN is removed. After a deleted VCN is removed it no longer appears in the list of VCNs in that compartment.
- 

Use the[network vcn delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/delete.html)command and required parameters to delete a VCN:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/DeleteVcn)operation to delete a VCN.

Be aware this deletes only the VCN and not its related resources. If there are any resources in the VCN, the deletion attempt will not succeed. For more information, see[Subnet or VCN Deletion](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Troubleshoot/vcn_troubleshooting.htm#Subnet_or_VCN_Deletion)
