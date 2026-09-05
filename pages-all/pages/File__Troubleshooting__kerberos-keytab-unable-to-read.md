# Error "Unable to read keytab" When Validating Kerberos Keytab
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/kerberos-keytab-unable-to-read.htm
- Fetched: 2026-09-05 02:06 CDT

# Error "Unable to read keytab" When Validating Kerberos Keytab

When validating a Kerberos keytab, a "Validate Keytab server error: Unable to read keytab" error occurs.

Cause : The[keytab](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/kerberos.htm#prerequisites__keytab)might have been Base64-encoded twice. If the Vault secret format is set as plain-text, OCI Vault encodes the value for you.
