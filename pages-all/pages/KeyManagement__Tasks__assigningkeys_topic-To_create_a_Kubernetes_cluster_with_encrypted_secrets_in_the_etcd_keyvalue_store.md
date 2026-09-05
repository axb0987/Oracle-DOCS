# Creating a Kubernetes Cluster with Encrypted Secrets
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_create_a_Kubernetes_cluster_with_encrypted_secrets_in_the_etcd_keyvalue_store.htm
- Fetched: 2026-09-05 02:31 CDT

# Creating a Kubernetes Cluster with Encrypted Secrets

Learn how to create a Kubernetes cluster with encrypted secrets in the etcd key-value store in OCI.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_create_a_Kubernetes_cluster_with_encrypted_secrets_in_the_etcd_keyvalue_store.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_create_a_Kubernetes_cluster_with_encrypted_secrets_in_the_etcd_keyvalue_store.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_create_a_Kubernetes_cluster_with_encrypted_secrets_in_the_etcd_keyvalue_store.htm#)
- 

Note  
  

These instructions assume you have already followed the steps in[Encrypting Kubernetes Secrets at Rest in Etcd](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengencryptingdata.htm)and created:
- A dynamic group including all clusters in the compartment
- A policy to give the dynamic group access to a master encryption key in an OCI vault

- Open the navigation menu and select Developer Services . Under Containers &amp; Artifacts , select Kubernetes Clusters (OKE) .
- Under List Scope , in the Compartment list, choose the compartment where you want to create a Kubernetes cluster that has Kubernetes secrets encrypted with a Vault service master encryption key.
- 

Select Create Cluster , follow the instructions under[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm)in[Creating Kubernetes Clusters Using Console Workflows](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm), and select the Encrypt Using Customer-Managed Keys option.
- 

Note  
  

These instructions assume you have already followed the steps in[Encrypting Kubernetes Secrets at Rest in Etcd](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengencryptingdata.htm)and created:
- a dynamic group including all clusters in the compartment
- a suitable policy to give the dynamic group access to the master encryption key in Vault

Open a command prompt and run`oci ce cluster create`to create a cluster where Kubernetes secrets at rest in the etcd data-store are encrypted with a Vault service master encryption key:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see[KMS CLI Command Reference.](https://docs.oracle.com/iaas/tools/oci-cli/3.37.4/oci_cli_docs/cmdref/kms.html)
- 

Run the[CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster)operation for creating kubernetes cluster with encrypted secrets.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
