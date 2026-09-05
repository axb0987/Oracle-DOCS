# Moving an HSM Cluster Resource
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_moving_hsmcluster_resource.htm
- Fetched: 2026-09-05 02:33 CDT

# Moving an HSM Cluster Resource

Learn how to move an HSM cluster resource from one compartment to another.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_moving_hsmcluster_resource.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_moving_hsmcluster_resource.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_moving_hsmcluster_resource.htm#)
- 

- Open the navigation menu , select Identity &amp; Security , and then select Dedicated Key Management .
- In the Dedicated Key Management home page, select a cluster from the list
- In the HSM Cluster Details page, select Move Resource .
- Select a compartment to which you want to move the resource.
- Select Move resource .

The cluster resource is moved to the new compartment.
- 

Use the[oci kms kms-hsm-cluster hsm-cluster change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/kms-hsm-cluster/hsm-cluster/change-compartment.html)command and required parameters to change the compartment of HSM cluster resource.
```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[ChangeHsmClusterCompartment](https://docs.oracle.com/iaas/api/#/en/key/latest/HsmCluster/ChangeHsmClusterCompartment)API with the KMSHSMCLUSTER endpoint to move an HSM cluster resource to a different compartment within the same tenancy.
Note  
  
Each region uses the KMSHSMCLUSTER API endpoint for HSM cluster operations. For regional endpoints, see the[API Endpoints](https://docs.oracle.com/iaas/api/#/en/key/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
