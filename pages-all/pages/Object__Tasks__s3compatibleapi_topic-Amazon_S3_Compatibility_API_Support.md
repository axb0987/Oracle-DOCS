# Object Storage Amazon S3 Compatibility API Support
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/s3compatibleapi_topic-Amazon_S3_Compatibility_API_Support.htm
- Fetched: 2026-09-05 02:51 CDT

# Object Storage Amazon S3 Compatibility API Support

Learn about how Object Storage supports Amazon S3 Compatibility API.

Amazon S3 Compatibility API support is provided at the bucket level and object level. Amazon S3 Compatibility API supports version ids.

## Bucket APIs

The following bucket APIs are supported:
- [DeleteBucket](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/DeleteBucket)
- [GetLocation](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/GetLocation)
- [HeadBucket](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/HeadBucket)
- [GetService](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/GetService)(list all my buckets)
- [ListObjects](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/ListObjects)
- [PutBucket](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/PutBucket)

## Object APIs

The following object APIs are supported:
- [BulkDelete](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/BulkDelete)
- [DeleteObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/DeleteObject)
- [GetObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/GetObject)
- [HeadObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/HeadObject)
- [PutObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/PutObject)
- [RestoreObjects](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/RestoreObjects)

## Multipart Upload APIs

The following multipart upload APIs are supported:
- [AbortMultipartUpload](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/AbortMultipartUpload)
- [CompleteMultipartUpload](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/CompleteMultipartUpload)
- [InitiateMultipartUpload](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/InitiateMultipartUpload)
- [ListParts](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/ListParts)
- [ListUploads](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/ListUploads)
- [UploadPart](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/UploadPart)

## Tagging APIs

The following tagging APIs are supported:
- [DeleteBucketTagging](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Tagging/DeleteBucketTagging)
- [GetBucketTagging](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Tagging/GetBucketTagging)
- [PutBucketTagging](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Tagging/PutBucketTagging)

## SSE-C Support

Using optional API headers, you can provide your own 256-bit AES encryption key that's used to encrypt and decrypt objects uploaded to and downloaded from Object Storage.

To use your own keys for server-side encryption, specify the following three request headers with the encryption key information:

Headers Description APIs Supported
`x-amz-server-side-encryption-customer-algorithm`Specifies "AES256" as the encryption algorithm.

[GetObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/GetObject)

[HeadObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/HeadObject)

[PutObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/PutObject)

[InitiateMultipartUpload](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/InitiateMultipartUpload)

[UploadPart](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/UploadPart)
`x-amz-server-side-encryption-customer-key`Specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data.
`x-amz-server-side-encryption-customer-key-md5`Specifies the base64-encoded 128-bit MD5 digest of the encryption key. This value is used to check the integrity of the encryption key.

Object Storage has distinct APIs for copying objects and copying parts. Amazon S3 uses the presence of the following headers in[PutObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/PutObject)and[UploadPart](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/UploadPart)to find copy operations. To copy a source object that's encrypted with an SSE-C key, you must specify these three headers so that Object Storage can decrypt the object.

Headers Description APIs Supported
`x-amz-copy-source-server-side-encryption-customer-algorithm`Specifies "AES256" as the encryption algorithm to use to decrypt the source object.

[PutObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/PutObject)

[UploadPart](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/UploadPart)
`x-amz-copy-source-server-side-encryption-customer-key`Specifies the base64-encoded 256-bit encryption key to use to decrypt the source object.
`x-amz-copy-source-server-side-encryption-customer-key-md5`Specifies the base64-encoded 128-bit MD5 digest of the encryption key used to decrypt the source object.

## Working S3 SDKs

Note the following regarding API features that aren't supported when using the preceding SDKs and tools:
- AWS Signature Version 2 (SigV2) isn't supported. Use AWS Signature Version 4 signing mechanism instead.

## Support for Encryption Using Your Own Keys in Vault

Using optional API headers, you can provide your own encryption key in Vault to encrypt objects uploaded to Object Storage.

To use your own keys in Vault for server-side encryption, specify the following request header with the OCID of the key in Vault:

Headers Description APIs Supported
`x-amz-server-side-encryption-aws-kms-key-id`OCID of an existing key in Vault to be used to encrypt the object.

[PutObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/PutObject)

[InitiateMultipartUpload](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/InitiateMultipartUpload)

[UploadPart](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/UploadPart)

## `Content-Encoding`Header Support for`aws-chunked`

S3-compatible clients can upload objects using`aws-chunked`in the`Content-Encoding`header. Both single-part uploads and multipart`UploadPart`requests are supported. AWS SigV4 streaming payloads are supported, including:
- `STREAMING-AWS4-HMAC-SHA256-PAYLOAD`
- `STREAMING-AWS4-HMAC-SHA256-PAYLOAD-TRAILER`
- `STREAMING-UNSIGNED-PAYLOAD-TRAILER`

Clients can send`aws-chunked`uploads with either HTTP`Content-Length`or`Transfer-Encoding: chunked`headers. Clients must provide`x-amz-decoded-content-length`, which the Amazon S3 Compatibility API treats as the actual object or part size. Chunk signatures are validated, so uploads with tampered chunk data or invalid chunk signatures are rejected. Trailer signatures are validated for signed trailer-mode uploads, so tampered trailer blocks are also rejected. Trailer checksum validation is supported for:
- CRC32
- CRC32C
- SHA256
- CRC64NVME

Checksum mismatches causes the upload to fail during request processing. SHA256 trailer checksums integrate with existing`additional-checksum`behavior, so they can be persisted consistently with existing Amazon S3 Compatibility API checksum semantics. CRC32, CRC32C, and CRC64NVME trailer checksums are verification-only, so they're validated but not persisted as object metadata. Existing Amazon S3 Compatibility API upload behavior for unchunked uploads remains unchanged.

## Checksum Support for S3 DeleteObjects / BulkDelete

Newer versions of the AWS SDK don't automatically add the`Content-MD5`header, and have instead switched to new headers (such as`x-amz-checksum-crc32`) as the default checksum. The`DeleteObjects`/`BulkDelete`flow in Amazon S3 Compatibility API supports`x-amz-checksum-sha256`and`x-amz-checksum-crc32c`as alternatives to`Content-MD5`for validating the request body.

If backward compatibility is needed with MD5 checksums, use the`LegacyMd5Plugin`so the SDK adds the`Content-MD5`header as before.

For Example:

```

```

Note  
  

If you specify`checksumAlgorithm`in the request,`LegacyMd5Plugin`omits the`Content-MD5`header.

## Supported Amazon S3 Clients

You can configure various client applications to talk to Object Storage's Amazon S3-compatible endpoints. This topic provides some configuration examples for supported Amazon S3 Clients.

### AWS SDK for Java

The AWS SDK for Java repository, file download, and documentation links are available on GitHub:[https://github.com/aws/aws-sdk-java](https://github.com/aws/aws-sdk-java).

Here is an example of configuring AWS SDK for Java to use Object Storage

```

```

### AWS SDK for Javascript

The AWS SDK for Javascript repository, documentation links, and installation instructions are available on GitHub:[https://github.com/aws/aws-sdk-js](https://github.com/aws/aws-sdk-js).

Here is an example of configuring AWS SDK for Javascript to use Object Storage

```

```

### AWS SDK for Python (Boto3)

The AWS SDK for Python (Boto3) repository, documentation links, and installation instructions are available on GitHub:[https://github.com/boto/boto3](https://github.com/boto/boto3).

Here is an example of configuring AWS SDK for Python to use Object Storage

```

```

### Mounting Object Storage Buckets Using s3fs

s3fs lets Linux and macOS mount Object Storage as a file system. The s3fs repository, documentation links, installation instructions, and examples are available on GitHub:[https://github.com/s3fs-fuse/s3fs-fuse](https://github.com/s3fs-fuse/s3fs-fuse).

s3fs isn't suitable for all applications. Understand the following limitations:

- Object storage services have high latency compared to local file systems for time to first-byte and lack random write access. s3fs achieves the best throughput on workloads that only read large files.
- You can't partially update a file, so changing a single byte requires uploading the entire file.
- Random writes or appends to files require rewriting the entire file.
- s3fs doesn't support partial downloads, so even if you only want to read one byte of a file, you need to download the entire file.
- s3fs doesn't support server-side file copies. Copied files must first be downloaded to the client and then uploaded to the new location.
- Metadata operations, such as listing directories, have poor performance because of network latency.
- s3fs doesn't support hard links or the atomic renames of files or directories.
- s3fs provides no coordination between several clients mounting the same bucket.

To mount an Object Storage bucket as a file system

- Follow the installation instructions provided on GitHub:[https://github.com/s3fs-fuse/s3fs-fuse](https://github.com/s3fs-fuse/s3fs-fuse).

If you're unable to install using a pre-built package, follow the compilation instructions here:[https://github.com/s3fs-fuse/s3fs-fuse/blob/master/COMPILATION.md](https://github.com/s3fs-fuse/s3fs-fuse/blob/master/COMPILATION.md).
- Enter your Access Key/Secret Key pair credentials in a ${HOME}/.passwd-s3fs credential file:

```

```

For example:

```

```

Then, set owner-only permissions for the credential file:

```

```

- Create a mount point to mount an Object Storage bucket:

Where:
- `bucket_name`is the name of the bucket that you want to mount.
- `local_directory_name`is the name of the local directory where you want to mount the bucket.
- `namespace_name`is the unique system-generated assigned to your tenancy at account creation time. You can use the CLI or the Console to obtain your namespace name. See[Object Storage Namespaces](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm)for details.
- `region_ID`is the region identifier where the bucket resides. See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)for details.
- `endpoint`: If you want to mount a bucket that was created in your home region, you do not need to specify the`endpoint`parameter. If you want to mount a bucket that was created in a different region, you need to specify the`endpoint`parameter.
- To automatically mount the bucket as a file system on system startup using s3fs, add following to the`/etc/fstab`file:

```

```

- To verify the s3fs bucket mount, run the`df -h`command. The output shows the new mount point for the bucket. Navigate to the new mount point and run the`ls`command to list all objects in the bucket.

To troubleshoot mounting an Object Storage bucket
- If you get authorization errors, review your IAM policies and ensure you have one that lets you mount a bucket as a file system. For example:

```

```

- Ensure that you're using the correct namespace name in the URL in the s3fs command. To verify your namespace name, see[Object Storage Namespaces](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm).
- Ensure that the named bucket that you are trying to mount exists and is in a compartment that you have access to. Use one of the following ways to verify the bucket name:
- Log into the Console and find the named bucket in the compartment that you have access to.
- Use the CLI command`oci os bucket list --namespace <object_storage_namespace> --compartment-id <target_compartment_id>`.
- To mount a bucket that was created in a region other than your home region, you need to specify that other region in both the`url`and`endpoint`parameters.
- If you mount a bucket as the root user, other users can't list or access objects in the bucket unless you add`-o allow_other`to the s3fs command or`allow_other`to the`/etc/fstab`mount options. You can also supply specific UID and GID parameters to specify user access details.
- 

If you reviewed and verified the troubleshooting solutions and need to contact Support, run the mount command again in DEBUG mode to get more failure details. Add the following to the end of the command and save the output:

```

```

To unmount an Object Storage bucket from a file system
Run the following command, specifying the mount point:

```

```

### AWS Command Line Interface (CLI)
