# Updating Vault from a Backup
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_update_a_vault_from_a_backup.htm
- Fetched: 2026-09-05 02:32 CDT

# Updating Vault from a Backup

Learn how to update a virtual private vault from a backup using the OCI Console.
Note  
  
The only type of vault you can back up is a virtual private vault.
- On the Vaults list page, find the vault that you want to work with. If you need help finding the list page, see[Listing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults-listing-vaults.htm).
- On the vault's details page, select Actions , then select Update Vault from Backup .
- Select a source. You can import a backup from the following sources: an Object Storage bucket, a preauthenticated Object Storage URL, or a file on your local machine or a mapped network location.
- Do one of the following, depending on what you chose in the previous step:
- Select a bucket from the dropdown menu. If needed, you can change the compartment to find a bucket in a different compartment. Then, select the file in the bucket containing the backup of the vault. Avoid entering confidential information.
- Select Object Storage URL , and then provide a preauthenticated Object Storage URL for the file containing the backup of the vault you're updating.
- Select Upload a file , then use the Choose a file field to select or drag a file from your local machine or a mapped network location.
-
