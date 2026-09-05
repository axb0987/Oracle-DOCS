# Exporting Vault Keys and Key Versions
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/exportingkeys.htm
- Fetched: 2026-09-05 02:35 CDT

# Exporting Vault Keys and Key Versions

Learn how to export a software-protected master encryption key or key version for performing cryptographic operations.

After exporting a key, you can use the key locally, and then discard the key from local memory to protect the key contents. Using an exported key locally improves availability, reliability, and latency.
Note  
  
You can't export HSM-protected keys from OCI KMS.

## Required IAM Policy

Caution  
  
Keys associated with volumes, buckets, file systems, clusters, and stream pools will not work unless you authorize Block Volume, Object Storage, File Storage, Kubernetes Engine, and Streaming to use keys on your behalf. Additionally, you must also authorize users to delegate key usage to these services in the first place. For more information, see[Let a user group delegate key usage in a compartment](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#os-bv-admins-use-key-id)and[Create a policy to enable encryption keys](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#services-use-key)in[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). Keys associated with databases will not work unless you authorize a dynamic group that includes all nodes in the DB system to manage keys in the tenancy. For more information, see[Required IAM Policy in Exadata Cloud Service](https://docs.oracle.com/iaas/exadatacloud/exacs/preparing-for-ecc-deployment.html#GUID-EA03F7BC-7D8E-4177-AFF4-615F71C390CD)

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: for typical policies that give access to vaults, keys, and secrets, see[Let security admins manage vaults, keys, and secrets](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#sec-admins-manage-vaults-keys). For more information about permissions or if you need to write more restrictive policies, see[Details for the Vault Service](https://docs.oracle.com/iaas/Content/Identity/Reference/keypolicyreference.htm).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

## Before You Begin

Exporting a key requires you to generate your own RSA key pair to wrap and unwrap the key material. You can use the third-party tool of your choice to generate the RSA key pair.

You can export the key or key version by using the CLI only. We've included example scripts that you can refer to. The scripts include all steps of the export process, from wrapping the key material to exporting the software-protected key or key version.

If you're using MacOS or Linux, you'll need to install the[OpenSSL](http://www.openssl.org/)1.1.1 series to run commands. If you plan to use the RSA encryption algorithm that uses a temporary AES key, then you must also patch OpenSSL with a patch that supports it, see[Configuring OpenSSL to Wrap Key Material](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/to_configure_and_patch_openssl.htm). If you're using Windows, you'll need to install[Git Bash for Windows](https://git-scm.com/download/win)and run commands with that tool.
