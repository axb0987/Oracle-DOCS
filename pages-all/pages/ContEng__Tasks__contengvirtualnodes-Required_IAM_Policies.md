# Required IAM Policies for Using Virtual Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengvirtualnodes-Required_IAM_Policies.htm
- Fetched: 2026-09-05 01:57 CDT

# Required IAM Policies for Using Virtual Nodes

Find out about the IAM policies to create to use virtual nodes with Kubernetes Engine (OKE).

Administrator users do not require additional permissions to create and use clusters with virtual nodes and virtual node pools.

To enable non-administrator users to create and use clusters with virtual nodes and virtual node pools, you must give such users the required permissions. To grant these permissions, create an IAM policy with the following policy statements:

```

```

```

```

```

```

Note that if a group is not in the default identity domain, prefix the group name with the identity domain name, in the format`group '<identity-domain-name>'/'group-name'`. You can also specify a group using its OCID, in the format`group id <group-ocid>`
