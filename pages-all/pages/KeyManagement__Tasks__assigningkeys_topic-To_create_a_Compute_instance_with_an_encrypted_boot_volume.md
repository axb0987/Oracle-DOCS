# Creating a Compute Instance with an Encrypted Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_create_a_Compute_instance_with_an_encrypted_boot_volume.htm
- Fetched: 2026-09-05 02:31 CDT

# Creating a Compute Instance with an Encrypted Boot Volume

Learn how to create a Compute instance with an encrypted boot volume in OCI.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_create_a_Compute_instance_with_an_encrypted_boot_volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_create_a_Compute_instance_with_an_encrypted_boot_volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_create_a_Compute_instance_with_an_encrypted_boot_volume.htm#)
- 

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Under List Scope , in the Compartment list, choose the compartment where you want to create an instance with a boot volume that's encrypted with a Vault service master encryption key.
- 

Select Create Instance , and then follow the instructions in[Launching an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
- 

- First, create the JSON input for configuring the instance and boot volume: Open a command prompt and run`oci compute instance launch --generate-full-command-json-input`.
- 

Copy, and then paste the output from the command into a text file for editing. Edit the JSON to provide values appropriate for your tenancy and desired image operating system and instance shape. The following example shows the minimum settings required to create an instance and encrypted boot volume.

```

```

Avoid entering confidential information in the instance name.
- Save the file with a ".json" file extension.
- In the command prompt, run oci compute instance launch --from-json file://&lt;file_path&gt;, providing the location of the file you saved in the previous step. For example: oci compute instance launch --from-json file://c:\temp\compute-boot-volume.json.
- 

Use the[Create Compute Instance](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/WorkRequest/GetWorkRequest)
