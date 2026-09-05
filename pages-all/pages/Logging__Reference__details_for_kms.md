# Details for Key Management
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_kms.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for Key Management

Logging details for Key Management.

## Resources
- Vaults

## Log Categories

API value (ID): Console (Display Name) Description
cryptooperations Crypto Operations Contains information such as who performed the crypto operations, what the operation was, and the key and key version used.

## Availability

Key Management logging is available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#top).

## Comments

You can enable logs on crypto operations on keys for a particular vault.

## Contents of a Key Management Log

A Key Management log record contains the following fields:

Field Description
clientIpAddress Client IP address making the Crypto API call.
keyVersionId Key version OCID used to perform the operation.
principalId User OCID performing the operation.
requestAction Takes the following values:
- ENCRYPT
- DECRYPT
- SIGN
- VERIFY
- GENERATEDEK
- EXPORTKEY
statusCode API response HTTP status code.

## Sample Key Management Log
```

```
