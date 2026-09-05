# Onboarding with External KMS
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_onboarding.htm
- Fetched: 2026-09-05 02:35 CDT

# Onboarding with External KMS

Steps required to onboard a third-party key management system for integration with OCI External Key Management Service (EKMS).

The EKMS onboarding process includes details about setting up network components, setting up a new user account, providing user permissions, configuring a private endpoint, and configuring both network policies and IAM policies for accessing vault and keys.

The following diagram is a workflow that shows the steps to onboard the EKMS feature:  

  

- Set up the third-party key management service for OCI EKMS. Use the[OCI EKMS vendor API specifications](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Reference/ekms-vendor-api.htm)to enable cryptographic operations.
- Expose a secure and reliable service endpoint for OCI EKMS vendor APIs,[authenticated using JWT tokens issued by OCI Identity Cloud Service (IDCS)](https://docs.oracle.com/en/cloud/paas/iam-domains-rest-api/op-admin-v1-signingcert-jwk-get.html). ​
- Establish network connectivity between OCI and the third-party KMS. See[Deploying the External Key Manager](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_deploying_ctm.htm).
- Set up a secure and reliable network connection between OCI EKMS and the third-party KMS. See[Setting Up Networking Components](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_setting_up_network_components.htm)and[Setting up FastConnect for Colocation](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_configuring_fastconnect.htm).
- Configure an OCI IDCS application to authenticate OCI EKMS with the third-party KMS. See[Setting up TLS Connectivity](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_setting_up_tls_connectivity.htm)and[Setting Up Authentication and Authorization](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_setting_up_auth_authorization.htm).
- Create an external vault and keys linked to the third-party KMS.
- Provision an external vault and associated keys within OCI that are integrated with the third-party KMS.
- Enable customer-managed keys for OCI resources.
- Configure OCI resources such as Object Storage buckets or Autonomous AI Database to use customer-managed keys from the external vault.
You can use the following tasks to manage onboarding tasks:
- [Deploying the External Key Manager](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_deploying_ctm.htm)
- [Setting Up Networking Components](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_setting_up_network_components.htm)
- [Setting up FastConnect for Colocation](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_configuring_fastconnect.htm)
- [Setting up TLS Connectivity](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_setting_up_tls_connectivity.htm)
- [Setting Up Authentication and Authorization](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_setting_up_auth_authorization.htm)
- [Creating a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_creating_ekms_private_endpoint.htm)
