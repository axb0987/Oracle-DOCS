# Rotating Keys
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos-key-rotation.htm
- Fetched: 2026-09-05 02:03 CDT

# Rotating Keys

Rotating a Kerberos keytab used for File Storage authentication must done carefully to avoid an availability outage.

NFS clients using Kerberos for authentication refresh tickets based on an interval specified by the KDC administrator. When rotating keytab entries, the mount target must accept both the old values and the new values until all clients have refreshed their tickets. If the old keytab entry is removed too early, clients that haven't refreshed their tickets can experience an availability outage.

To safely update a Kerberos keytab used in File Storage authentication:
- Generate a keytab from the KDC with new key versions, and convert it into Base64 format.
- Upload the keytab to OCI Vault as a new secret version of the existing keytab secret. Ensure that the selected format of the new secret version is Base64. For more information, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).
- Update the mount target's Keytab Information :
- Open the navigation menu and select Storage . Under File Storage , select Mount Targets .
- Select a Compartment .
- Select the mount target that you want to update.
- Select the Actions Menu and then select Manage kerberos .
- In Manage Kerberos panel, in the Keytab information section:
- Select the new keytab version as the Current keytab secret version
- Select the old keytab version as the Backup keytab secret version .
- Wait until all NFS clients have refreshed their Kerberos tickets.
- Remove the Backup keytab secret version from the mount target configuration.
-
