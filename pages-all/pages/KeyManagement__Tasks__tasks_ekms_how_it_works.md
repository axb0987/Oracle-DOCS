# How External KMS Works
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_ekms_how_it_works.htm
- Fetched: 2026-09-05 02:36 CDT

# How External KMS Works

Learn about the External Key Management Service (EKMS) model, including the operations that happen inside and outside of Oracle Cloud Infrastructure (OCI).
With EKMS, you can host encryption keys on-premises using third-party key management systems. OCI services integrate with EKMS through OCI KMS APIs to perform cryptographic operations. Key characteristics of EKMS include the following:
- The key material created in third-party key management systems is never imported into Oracle Cloud.
- Cryptographic operations are run in the third-party key management system.
- Only the key references are stored in OCI vaults, meaning all key management operations remain in the third-party key management system.
- If access to the third-party system is revoked, cryptographic operations in OCI fail.
- Behavior is consistent for OCI EKMS across Oracle public cloud and Alloy environments.

OCI enforces the following timeout limits:
- read timeout: 1 second
- connection timeout: 500 milliseconds

OCI intentionally aligns these limits with downstream service timeout constraints to ensure consistent behavior and prevent cascading failures. If EKMS doesn't complete a request within the read timeout window, it retries the request and, if the request still isn't successful, EKMS returns a timeout response to the downstream service.

## External KMS Integration

OCI services such as Object Storage and Database can use EKMS-managed keys for their workloads. Integration is based on industry-standard protocols and secure connectivity, including the following:
[
- OCI services use EKMS-managed keys for their workloads.
- EKMS uses OAuth2 to authenticate requests by including a customer-granted bearer token in the authorization header.
- All cryptographic operations are transmitted over a secure network connection to the on-premises HSM.
- The third-party management service verifies the OAuth2 JWT token from OCI Identity service before allowing operations.
