# Increasing the Cluster Limit
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_increase_cluster_limit.htm
- Fetched: 2026-09-05 02:32 CDT

# Increasing the Cluster Limit

Learn how to request an HSM Cluster limit increase for OCI Dedicated Key Management.

Before you provision an HSM cluster, you must request a[Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Vault_Limits)increase for "HSM cluster count". By default, the HSM cluster limit is zero for all tenancies. When making the request, include the following:
- Tenancy and region for the limit increase
- Service Category: Key Management
- Limit name: hsm-cluster-count

For instructions on submitting a limits increase, see[Creating a Limit Increase Request](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm)
