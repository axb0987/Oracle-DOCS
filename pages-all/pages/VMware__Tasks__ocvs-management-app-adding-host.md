# Adding an ESXi Host in vSphere using VMware Solution Management Appliance
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvs-management-app-adding-host.htm
- Fetched: 2026-09-05 03:08 CDT

# Adding an ESXi Host in vSphere using VMware Solution Management Appliance

Add an ESXi host in vSphere for use with VMware Solution Management Appliance.

- Sign in to the vSphere web console.
You can get the link to the vSphere web console from the[SDDC Details page](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-get.htm).
- Select Inventory .
- Right-click a data center or a cluster, go to OCI Integration , and then select Add ESXi host .
- Select the name of the cluster you want to add the ESXi host to. If you navigated from a cluster, the cluster is already selected.

Important  
  
The selected cluster must correspond to a cluster in OCI. If the Management Appliance finds a cluster with a matching name, it automatically appears in the Cluster Name in OCI list. If the matching OCI cluster isn't found, you can manually select a matching cluster in the list. Be sure you have selected the correct cluster before proceeding.
- Select Next .
- Enter the following information:

- Host name : Enter a name for the new host that helps to identify it later. The name must be from 1 to 22 characters long, must start with a letter, and can contain only alphanumeric characters and hyphens (-). Hyphens can't be next to each other. Avoid entering confidential information.
Important  
  
ESXi host names can have a maximum of 22 characters including any optional SDDC prefix you might have configured. Host FQDNs can have a maximum of 64 characters total.
- Release name : Select the software version for the host. For more information, see[About the VMware Software](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/ocvsoverview.htm#about-vmware)for more information.
- Shape name : Select a shape and number of cores for the ESXi host. For more information, see[Supported Shapes](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/ocvsoverview.htm#supported-shapes).
- OCPU cores : Select the number of cores enabled for the ESXi host. For more information, see[Core Disabling](https://docs.oracle.com/iaas/Content/Compute/References/bios-settings.htm#disable-cores)for more information.
- Select Next .
- Select the capacity type you want to use for the host:

- On-demand capacity : Select to specify Compute capacity required to create the host is provisioned at the time of the request. You start paying for the capacity when it's provisioned.
- Capacity reservation : Select to reserve instances in advance so that the capacity is available for workloads when you need it. For more information, see[Using Reserved Capacity](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/ocvsoverview.htm#using-reserved-capacity). Select the compartment and capacity reservation name.
- Select Next .
- Select the pricing you want to use for the host:

- Pricing interval commitment : The pricing interval to apply to the ESXi hosts. For more information about available pricing intervals, see[Billing Options](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/ocvsoverview.htm#billing-options).
- Select a deleted host for billing continuation : (Optional) When you create a host, you can reuse the leftover billing commitment from a deleted host. Only deleted hosts with the same shape, CPU, and SKU as you selected for the new host are available for use. Select a compartment and a deleted ESXi host. For more information, see[Transferring VMware Solution Billing Commitments](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/swap-billing.htm).
- Select Next .
- (Optional) Apply tagging. For more information, see[Tagging](https://docs.oracle.com/iaas/Content/Tagging/home.htm).
- Select Next .
- Review the configuration summary.
- Select Create .
- Sign in to OCI.

Note  
  
The Management Appliance requires user authentication for this operation. If you're not sure what OCI sign-in credentials to use, contact your administrator.
The Management Appliance starts a job that adds the ESXi host. To monitor the job and its steps, see[Monitoring VMware Solution Management Appliance Jobs in vSphere](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvs-management-app-jobs.htm)
