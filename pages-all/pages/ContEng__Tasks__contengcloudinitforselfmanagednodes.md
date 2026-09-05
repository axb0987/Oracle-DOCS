# Creating Cloud-init Scripts for Self-managed Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm
- Fetched: 2026-09-05 01:54 CDT

# Creating Cloud-init Scripts for Self-managed Nodes

Find out how to create the cloud-init script for a self-managed node that you want to add to an enhanced cluster created with Kubernetes Engine.

When creating a self-managed node to add to an enhanced cluster, you have to provide a cloud-init script that specifies the cluster's Kubernetes API private endpoint and base64-encoded CA certificate.

To create the cloud-init script for a self-managed node:
- Obtain the Kubernetes API private endpoint of the enhanced cluster to which you want to add the self- managed node using the Console or the CLI:
- Using the Console:
- On the Clusters list page, select the name of the enhanced cluster to which you want to add the self-managed node. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).

On the Cluster details tab, the Kubernetes API private endpoint is shown, including the port number. For example,`10.0.103.170:6443`
- Make a note of the cluster's Kubernetes API private endpoint, without the port number. For example,`10.0.103.170`
- Using the CLI:
- Enter:

```

```

The`grep`command extracts the URL of the cluster endpoint from the output of the`ce cluster create-kubeconfig`command. The`sed`command removes the protocol and port information from the cluster endpoint's URL to leave just the IP address.
- Make a note of the cluster's Kubernetes API private endpoint. For example,`10.0.103.170`
- Obtain the cluster's base64-encoded CA certificate from the cluster's kubeconfig file using the Console or the CLI:
- Using the Console:
- On the Cluster details tab, make a note of the cluster's OCID. For example,`ocid1.cluster.oc1.phx.aaaaaaaa______ivq`
- From the Actions menu, select Access cluster .
- In the Access cluster dialog, select Cloud Shell Access , and select Launch cloud shell .
- In the Cloud Shell window, enter the following command:

```

```

where:
- `<cluster-ocid>`is the value of the`--cluster-id`parameter shown in step 2 in the Access Your Cluster dialog.
- `<region-identifier>`is the value of the`--region`parameter shown in step 2 in the Access Your Cluster dialog.

For example:

```

```

The base64-encoded CA certificate is shown in the Cloud Shell window as a long alphanumeric string starting with the characters`LS0t`.
- Make a note of the cluster's base64-encoded CA certificate.
- Using the CLI:
- Enter:

```

```

The base64-encoded CA certificate is shown in the Cloud Shell window as a long alphanumeric string starting with the characters`LS0t`.
- Make a note of the cluster's base64-encoded CA certificate.
- Create the cloud-init script as follows:
- In a text editor of your choice, create a new text file.
- Copy and paste the following script into the file:

```

```

where:
- `<cluster-endpoint>`is the cluster's Kubernetes API private endpoint that you obtained earlier (without the port number). For example,`10.0.103.170`
- `<base64-encoded-certificate>`is the cluster's base64-encoded CA certificate that you obtained earlier (starting with the characters`LS0t`).

For example:

```

```

-
