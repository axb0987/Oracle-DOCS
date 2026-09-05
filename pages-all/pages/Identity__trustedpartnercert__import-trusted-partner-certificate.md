# Importing a Trusted Partner Certificate
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/trustedpartnercert/import-trusted-partner-certificate.htm
- Fetched: 2026-09-05 02:29 CDT

# Importing a Trusted Partner Certificate

Import a trusted partner certificate to an identity domain in IAM.

- On the Trusted Partner Certificates list page, select Import certificate . If you need help finding the list page, see[Listing Trusted Partner Certificates](https://docs.oracle.com/en-us/iaas/Content/Identity/trustedpartnercert/list-trusted-partner-certificate.htm).
- Enter an alias for the trusted partner certificate in the Alias field (for example,`TPcert1`).
The certificate that you import is an authorization certificate for the trusted partner. It contains a keystore . The keystore is used to authenticate and encrypt the data for the trusted partner for security purposes. A keystore entry is identified by an alias .
- Upload the Distinguished Encoding Rules (DER) file that contains the trusted partner certificate to import by dragging the file to the page or by selecting select one and browsing to its location.
- Verify that the path and name of the DER file you selected appear in the Certificate field.
-
