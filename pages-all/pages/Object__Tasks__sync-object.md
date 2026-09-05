# Synchronizing Object Storage Objects
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/sync-object.htm
- Fetched: 2026-09-05 02:51 CDT

# Synchronizing Object Storage Objects

Synchronize a file system directory with Object Storage objects in a bucket.

Synchronization traverses the directories and sub-directories of the specified file system, and copies new and changed objects from the source to the destination, and optionally deleting those that aren't present in the source.

Synchronizing Object Storage objects is only available using the CLI.

## Using the CLI

Use the[oci os object sync](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/sync.html)command and required parameters to synchronize the objects in a file system and a bucket:

```

```
Use the Optional Parameters listed in the[oci os object sync](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/sync.html)page to specify the criteria for when objects need to be synchronized.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

## Verifying Uploaded Object Integrity

An MD5 checksum is computed for each uploaded object or for each part of a multipart object, which helps ensure that the object stored is the object that was uploaded. There's no automatic verify checksum option when running a synchronization (`os object sync`).

A cryptographic hash using MD5 is provided for all objects uploaded to an Object Storage bucket using the synchronization method. This hash verifies the object's data integrity. Object Storage provides the object hash value in base64 encoding.

The MD5 hash is listed in the details of the object as the Content MD5 Hash or opc-multipart-md5 value. See[Getting Object Details](https://docs.public.content.oci.oraclecloud.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_get_object_details.htm)for more information.

Run the following command to covert the base64 encoded hash value to hexadecimal,
```

```

For example:
```

```

Now generate the`md5sum`from the source file and verify both values match:
```

```

For example:
```

```

### Verifying Multipart Uploaded Objects

You can use preconfigured scripts available on GitHub to verify the MD5 checksum for multpart uploads to your Object Storage bucket. We recommend you use the`part-size`parameter to simplify calculating the MD5 checksum. For more information and links to these scripts, see[Support opc-multipart-md5 checking](https://github.com/oracle/oci-cli/issues/134)
