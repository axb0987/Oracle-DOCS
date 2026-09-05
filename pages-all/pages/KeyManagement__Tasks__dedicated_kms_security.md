# Security
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_security.htm
- Fetched: 2026-09-05 02:33 CDT

# Security

Encrypt Dedicated KMS data communication.

The end-to-end communication between your client instance and the HSM partitions in your cluster is encrypted. Only your client and your HSMs can decrypt the communication.
The following process explains how the client establishes end-to-end encryption with the HSM:
- Your client establishes a Mutual Transport Layer Security (MTLS) connection with the server that hosts your HSM hardware. The client checks the server's certificate to ensure that it's a trusted server and server also checks client certificate and ensure it is issued by the HSM partition owner.  

  

- Next, the client establishes an encrypted connection with the HSM hardware. The HSM has the Partition Owner Authentication certificate that you signed with your own certificate authority, and the client has the CA's root certificate (Partition Owner Cert). Before the client–HSM encrypted connection is established, the client verifies the HSM's certificate against its root certificate. The connection is established only when the client successfully verifies that the HSM is trusted.
