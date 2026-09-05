# Assigning a Key to a Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_Block_Volume.htm
- Fetched: 2026-09-05 02:31 CDT

# Assigning a Key to a Block Volume

Assign a key to a block volume using the OCI Console..

## Using the Console

Important  
  
The Block Volume service does not support encrypting volumes with keys encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When using your own keys, you must use keys encrypted using the Advanced Encryption Standard (AES) algorithm. This applies to block volumes and boot volumes.

- Open the navigation menu and select Storage . Under Block Storage , select Block Volumes .
- Under List Scope , in the Compartment list, select the compartment where you want to create a block volume that's encrypted with a Vault service master encryption key.
- 

Select Create Block Volume , and then follow the instructions in[Creating a Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/creatingavolume.htm)
