# Known Issues for Vault
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/known_issues_for_vault.htm
- Fetched: 2026-09-05 02:31 CDT

# Known Issues for Vault

Vault known issues.

## External Key Version Returns "ExternalKeyReferenceDetails" as Null
Details Create external key version operation returns "externalKeyReferenceDetails" parameter as a null value in the response: Workaround

Do a GET call to display details of "externalKeyReferenceDetails" parameter.

## External Key Vault Returns "ExternalKeyReferenceDetails" as Null
Details Create external key vault operation returns "externalKeyReferenceDetails" parameter as a null value in the response: Workaround

Do a GET call on external key reference which displays all the details.

## Create Vault Returns "Unknown Error"
Details Create Vault operation fails resulting in an "Unkown Error" when you add large tags (overall size lesser than preset limit of 5 KB): Workaround
