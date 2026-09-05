# Migrating to VCN-Native Clusters
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingclusters.htm
- Fetched: 2026-09-05 01:55 CDT

# Migrating to VCN-Native Clusters

Find out how to migrate a cluster to integrate its Kubernetes API endpoint into your own VCN, using Kubernetes Engine (OKE).

In earlier releases (before March 16, 2021), Kubernetes Engine provisioned clusters with Kubernetes API endpoints that were not integrated into your own VCN. The Kubernetes API endpoint was public, and you could not restrict access to it. You can continue to create such clusters using the CLI or API (until the date specified in the Service Change Announcement[here](https://docs.oracle.com/iaas/Content/servicechanges.htm#servicechanges_topic_oke)), but not the Console.

After March 16, 2021, Kubernetes Engine can provision clusters with their Kubernetes API endpoints in a subnet in your own VCN (these clusters are known as "VCN-native clusters"). You have more flexibility to configure VCN-native clusters to meet your own security and networking requirements. You can configure the Kubernetes API endpoint to make it privately accessible within your VCN (and a peered on-premise network), or to make it publicly accessible from the internet:
- To make the Kubernetes API endpoint privately accessible, host the Kubernetes API endpoint in a private subnet and do not assign a public IP address to it.
- To make the Kubernetes API endpoint publicly accessible from the internet, host the Kubernetes API endpoint in a public subnet and assign a public IP address to it.

You can control access to the Kubernetes API endpoint subnet using security rules defined for network security groups (recommended) or security lists.

To take advantage of the security control offered by VCN-native clusters, you can migrate an existing cluster to integrate its Kubernetes API endpoint into your own VCN.

Cluster migration has the following stages:
- Stage 1: Migrate the cluster

You start the migration by selecting the cluster to migrate, and then specifying the existing VCN and the private or public subnet to host the new Kubernetes API endpoint. The migration usually takes around 15 minutes.

During this time, the Kubernetes API continues to be accessible via the original public endpoint that is not integrated into your own VCN. However, cluster lifecycle operations (such as cluster updates, node pool creation and deletion) are unavailable.

See[Migrating an Existing Cluster to be VCN-native](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingclusters.htm#contengmigratingclusters_topic_Using_the_Console).
- Stage 2: Set up access to the migrated cluster

When migration is complete, the cluster becomes accessible via the new Kubernetes API endpoint in your own VCN, as well as via the original public Kubernetes API endpoint that is not integrated into your VCN. You can now update the configuration of your kubectl, tools, and CI/CD pipelines to use the new Kubernetes API endpoint.

To verify that you have correctly updated your kubectl, tools, and CI/CD pipelines, you have the option to temporarily decommission the original public Kubernetes API endpoint, test that the updated configurations use the new Kubernetes API endpoint, and then rollback the decommissioning of the original endpoint.

See[Setting Up Access to a Migrated Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingclusters.htm#Configuring_migrated_cluster).
- Stage 3: Decommission the original public Kubernetes API endpoint that is not integrated into your own VCN

When you are confident that you have correctly updated the configuration of your kubectl, tools, and CI/CD pipelines to use the new Kubernetes API endpoint in your own VCN, you can decommission the original public Kubernetes API endpoint that is not integrated into your VCN. When you decommission the original Kubernetes API endpoint, the cluster is only accessible via the new Kubernetes API endpoint. Decommissioning usually takes less than five minutes.

Note that if you do not explicitly decommission the original endpoint, the cluster continues to be accessible via both the original endpoint and the new endpoint.

Having decommissioned the original endpoint, you have a number of days in which you can roll back the decommissioning and re-enable that original endpoint. The default rollback period is 30 days, but you can increase the rollback period to a maximum of 60 days.

See[Decommissioning the Original Public Kubernetes API Endpoint of a Migrated Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingclusters.htm#Decommisioning_migrated_cluster).

## Migrating an Existing Cluster to be VCN-native

### Using the Console

To migrate an existing cluster to be VCN-native by making it accessible via a new Kubernetes API endpoint in your VCN:
- 

On the Clusters list page, select the name of the cluster that you want to migrate. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).

Migration required labels appear on the Clusters list page beside the names of clusters with Kubernetes API endpoints that are not integrated into your VCN.

When you select a cluster that you can migrate, the Migrate Cluster button appears at the top of the Cluster details tab.
- If you want the cluster's Kubernetes API endpoint to be publicly accessible from the internet and hosted in a new public subnet in the same VCN as the cluster (creating and configuring new network resources as required), perform an Automatic Migration as follows:
- At the top of the Cluster details tab, select Migrate Cluster to integrate the cluster's Kubernetes API endpoint into your own VCN.
- In the Migrate to VCN-Native Cluster dialog box, select Automatic Migration to create a new regional subnet in the cluster's VCN with a 10.0.0.0/28 CIDR block, along with security lists and route tables.
- Select Launch Workflow and review the migration summary in the VCN-Native Endpoint Cluster Migration dialog box.
- Select Migrate to create new network resources and migrate the cluster.

Kubernetes Engine starts migrating the cluster, as shown in the Migrating Cluster dialog.
- Select Close to close the Migrating Cluster dialog.
- If you want the cluster's Kubernetes API endpoint to be privately accessible within your VCN or publicly accessible from the internet, and hosted in an existing regional public or private subnet in the same VCN as the cluster, perform a Custom Migration as follows:
- Confirm the following network resources already exist in the VCN and are configured correctly to host the Kubernetes API endpoint (if not, create and configure them appropriately):
- a regional public or private subnet (see[Kubernetes API Endpoint Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#subnetconfig__section_kcm_v2b_s4b))
- if the subnet is public, an internet gateway (see[Internet Gateway Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#internetgatewayconfig))
- if the subnet is private, a NAT gateway (see[NAT Gateway Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#natgatewayconfig)) and a service gateway (see[Service Gateway Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#servicegatewayconfig))
- a route table with the necessary route rules (see[Route Table for Kubernetes API Endpoint Subnets](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#routetableconfig__section_dpd_wwv_r4b))
- a network security group (recommended) and/or security list with the necessary ingress and egress rules (see[Security Rules for the Kubernetes API Endpoint](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#securitylistconfig__section_jsz_kqw_r4b)) For example configurations, see[Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfigexample.htm).
- At the top of the Cluster details tab, select Migrate Cluster to integrate the cluster's Kubernetes API endpoint into your own VCN.
- In the Migrate to VCN-Native Cluster dialog box, select Custom Migration .
- Select Launch Workflow and specify:
- Kubernetes API Endpoint Subnet: A regional subnet to host the cluster's Kubernetes API endpoint. The subnet you specify can be public or private. The Kubernetes API endpoint is always assigned a private IP address. If you specify a public subnet, you can optionally expose the Kubernetes API endpoint to the internet by assigning a public IP address to the endpoint (as well as the private IP address). To simplify access management, Oracle recommends the Kubernetes API endpoint is in a different subnet to worker nodes and load balancers. For more information, see[Kubernetes Cluster Control Plane and Kubernetes API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengclustersnodes.htm#processes).
- Use network security groups to control traffic: Optionally, restrict the access to the cluster's Kubernetes API endpoint using one or more network security groups (NSGs) that you specify. For more information about the security rules to specify for the NSG, see[Security Rules for the Kubernetes API Endpoint](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#securitylistconfig__section_jsz_kqw_r4b).
- Assign a public IP address to the API endpoint: If you selected a public subnet for the Kubernetes API endpoint, you can optionally expose the endpoint to the internet by assigning a public IP address to the endpoint (as well as the private IP address). If you do not assign a public IP address, update route rules and security rules to enable access to the endpoint using a service gateway and a NAT gateway (see[Kubernetes API Endpoint Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#subnetconfig__section_kcm_v2b_s4b)).
- Select Migrate to create new network resources and migrate the cluster.

Kubernetes Engine starts migrating the cluster.

Migration usually takes around 15 minutes to complete. During this time, the Kubernetes API continues to be accessible via the original public endpoint that is not integrated into your own VCN. However, cluster lifecycle operations (such as cluster updates, node pool creation and deletion) are unavailable.

When migration is complete, the Cluster details tab shows the name of the Kubernetes API endpoint subnet , the IP address of the Kubernetes API private endpoint , and (if you assigned a public IP address to the Kubernetes API endpoint) the IP address of the Kubernetes API public endpoint .

A message indicates that the cluster has been migrated, and is pending public API endpoint decommissioning. At this point, the newly migrated cluster is accessible via both the new Kubernetes API endpoint in your VCN, and via the original public Kubernetes API endpoint that is not integrated into your own VCN.

### Using the CLI

Use the[oci ce cluster cluster-migrate-to-native-vcn](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/cluster-migrate-to-native-vcn.html)command and required parameters to migrate an existing cluster to integrate its Kubernetes API endpoint into your own VCN:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

### Using the API

Run the[ClusterMigrateToNativeVcn](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/ClusterMigrateToNativeVcn)operation to migrate a cluster to integrate its Kubernetes API endpoint into your own VCN.

## Setting Up Access to a Migrated Cluster

Having migrated a cluster to integrate its Kubernetes API endpoint into your own VCN, you have to update the configuration of your kubectl, tools, and CI/CD pipelines to use the new Kubernetes API endpoint. At a minimum, you'll want to update the cluster's Kubernetes configuration file (commonly known as the 'kubeconfig' file) to enable access to the migrated cluster using kubectl, as described in this topic. You also need to update any manifest files that include references to the cluster's original Kubernetes API endpoint IP address.

Follow the instructions in this topic to generate a new kubeconfig file. These instructions assume the cluster's kubeconfig file is saved in the default location (`$HOME/.kube`) and with the default name (`config`). If that is not the case, adapt the instructions accordingly.
- 

In the terminal window where you normally run Oracle Cloud Infrastructure CLI commands, run the following command to update the cluster's existing kubeconfig file:

```

```

where:
- `--cluster-id <cluster-ocid>`is the OCID of the existing cluster you want to make VCN-native.
- `--file <kubeconfig-file-location>`is the location of the cluster's kubeconfig file.
- `--region <region-name>`is the region in which the cluster is located.
- `--kube-endpoint PRIVATE_ENDPOINT|PUBLIC_ENDPOINT`specifies whether to add the private IP address or the public IP address of the cluster's Kubernetes API endpoint to the kubeconfig file. For more information, see[Kubernetes Cluster Control Plane and Kubernetes API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengclustersnodes.htm#processes).

For example:

```

```

Assuming the kubeconfig file already exists in the location you specify, details about the cluster are added as a new context to the existing kubeconfig file, including the cluster's new Kubernetes API endpoint in your own VCN. The`current-context:`element in the kubeconfig file is set to point to the newly-added context.

For more information about setting up the kubeconfig file, see[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm).
- 

Verify that kubectl can connect to the cluster using the cluster's new Kubernetes API endpoint by entering the following command:

```

```

Information about the nodes in the cluster is shown.

You can now use kubectl to perform operations on the cluster using the cluster's new Kubernetes API endpoint.
Note  
  
Until the original API endpoint that is not integrated into your VCN is decommissioned, you can continue to generate the original kubeconfig file by omitting the`--kube-endpoint`option from the`oci ce cluster create-kubeconfig`command.

## Decommissioning the Original Public Kubernetes API Endpoint of a Migrated Cluster

### Using the Console

To decommission the original public Kubernetes API endpoint that is not integrated into your own VCN:
- 

At the top of the Cluster details tab, select Decommission when you want to:
- Temporarily decommission the original endpoint, test that the updated configurations use the new Kubernetes API endpoint, and then roll back the decommissioning.
- Permanently decommission the original endpoint.

Decommissioning usually takes less than five minutes to complete. When decommissioning is complete, a default rollback period of 30 days is added. During the rollback period, you can:
- restore the original endpoint
- extend the rollback period
Important  
  

When the rollback period ends, you can no longer roll back the decommissioning of the original endpoint. The original endpoint is permanently decommissioned, and the decommissioning process cannot be reversed.
- (Optional) Select Rollback to roll back the decommissioning and restore the original endpoint. Rollback usually takes less than five minutes to complete.
- (Optional) Select Extend rollback deadline to increase the rollback period to a maximum of 60 days.

### Using the CLI

Use the[oci ce cluster start-public-api-endpoint-decommission](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/start-public-api-endpoint-decommission.html)command and required parameters to decommission a cluster's original endpoint:

```

```

Use the[oci ce cluster rollback-public-api-endpoint-decommission](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/rollback-public-api-endpoint-decommission.html)command and required parameters to rollback the decommissioning of a cluster's original endpoint:

```

```

Use the[oci ce cluster extend-endpoint-decommission-rollback-deadline](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/extend-endpoint-decommission-rollback-deadline.html)command and required parameters to increase the rollback period when decommissioning a cluster's original endpoint:

```

```

where`--rollback-deadline-delay <delay>`specifies a duration in ISO 8601 format. For example,`--rollback-deadline-delay P10d`to increase the rollback period by 10 days.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

## Frequently Asked Questions about Cluster Migration

### What are VCN-native clusters?

Kubernetes Engine creates Kubernetes clusters that are completely integrated into your Oracle Cloud Infrastructure Virtual Cloud Network (VCN). Worker nodes, load balancers, and the Kubernetes API endpoint are part of your own VCN, and you can configure them as public or private. Such clusters that are fully integrated into your own VCN are known as "VCN-native clusters".

### How can I tell if a cluster is already a VCN-native cluster?

If you're not sure whether a cluster is already a VCN-native cluster, view information about the cluster (for example, on the Cluster details tab in the Console). If the cluster is already a VCN-native cluster, the cluster details include Kubernetes API Endpoint information. If the cluster is not yet a VCN-native cluster, the cluster details simply include the Kubernetes Address .

### Do I have to migrate all my existing clusters?

No, you only have to migrate existing clusters that you want to turn into VCN-native clusters. If you don't want to integrate a cluster's Kubernetes API endpoint into your own VCN, simply don't migrate that cluster.

### Does the migration involve any downtime?

While a cluster is being migrated to a VCN-native cluster, the cluster's Kubernetes API continues to be accessible via the original public endpoint that is not integrated into your own VCN. However, cluster lifecycle operations (such as cluster updates, node pool creation and deletion) are unavailable.

### Should I choose automatic migration or custom migration?

Automatic migration creates a regional subnet in the cluster's VCN with a 10.0.0.0/28 CIDR block, along with security lists and route tables. The subnet is public and the API endpoint is assigned a public IP address. Automatic migration only supports clusters with node pools in the same compartment as the cluster. For clusters with node pools in different compartments, perform a custom migration.

Custom migration enables you to choose an existing public or private regional subnet to host the cluster's Kubernetes API endpoint. If you choose a public regional subnet, you can optionally expose the Kubernetes API endpoint to the internet by assigning a public IP address to the endpoint. You can optionally choose to use network security groups.

### How do I configure a subnet in my VCN to host the Kubernetes API endpoint?

Refer to[Network Resource Configuration for Cluster Creation and Deployment](https://docs.oracle.com/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm)for details about configuring the Kubernetes API endpoint subnet, security lists, and route table.

### I want to test the migration to a VCN-native cluster. How can I create a cluster with a Kubernetes API endpoint that is not integrated into my VCN?

In the terminal window where you normally run Oracle Cloud Infrastructure CLI commands (and until the date specified in the Service Change Announcement[here](https://docs.oracle.com/iaas/Content/servicechanges.htm#servicechanges_topic_oke)), run the following command to create a test cluster with a Kubernetes API endpoint that is not integrated into your VCN:

```

```

where:
- `--compartment-id <compartment-ocid>`is the OCID of the compartment to which you want the test cluster to belong.
- `--kubernetes-version v<kubernetes-version-number>`is a supported version of Kubernetes (see[Currently Supported Kubernetes Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengaboutk8sversions.htm#supportedk8sversions)). For example,`--kubernetes-version v1.19.7`
- `--name <cluster-name>`is a name of your choice for the test cluster. For example,`--name test-vcn-native-migration`
- `--vcn-id <vcn-ocid>`is the OCID of the VCN in which to create the test cluster.

Having created a test cluster with a Kubernetes API endpoint that is not integrated into your VCN, you can now migrate the test cluster to make it a VCN-native cluster. See[Migrating an Existing Cluster to be VCN-native](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingclusters.htm#contengmigratingclusters_topic_Using_the_Console).
