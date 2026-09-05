# Updating a key from a Backup
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys_topic-To_update_a_key_from_a_backup.htm
- Fetched: 2026-09-05 02:32 CDT

# Updating a key from a Backup

Learn how to update a key from a backup using the OCI Console.
Note  
  
The only type of encryption key that you can back up is a master encryption key protected by a hardware security module (HSM). This topic doesn't apply to keys protected by software.
- On the Master Encryption Keys list page, find the key that you want to work with. If you need help finding the list page, see[Listing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm).
- Select the name of the key you want to update to see its details page.
- Select Actions , then select Update Key from Backup .
- Select a backup source. You can import a vault backup from the following sources: an Object Storage bucket, a preauthenticated Object Storage URL, or a file on your local machine or a mapped network location.
- Do one of the following, depending on what you chose in the previous step:
- Select a bucket from the dropdown menu. If needed, you can change the compartment to find a bucket in a different compartment. Then, use the Select a file to select the file that contains the backup you're using for the key update.
- Select Object Storage URL , and then provide a preauthenticated Object Storage URL to the file that contains the backup you're using for the key update.
- Using Upload a file , drag a file or select one from your local machine or a mapped network location.
-
