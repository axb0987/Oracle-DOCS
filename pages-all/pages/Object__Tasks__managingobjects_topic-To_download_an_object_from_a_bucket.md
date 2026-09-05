# Downloading an Object Storage Object from a Bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_download_an_object_from_a_bucket.htm
- Fetched: 2026-09-05 02:51 CDT

# Downloading an Object Storage Object from a Bucket

Download an object from an Object Storage bucket or folder to your computer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_download_an_object_from_a_bucket.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_download_an_object_from_a_bucket.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_download_an_object_from_a_bucket.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Objects .
The Objects tab opens. All objects in the selected bucket are displayed in a table.
- From the Actions menu for the object you want, select Download .
The Download object dialog box appears while the object is downloading, and displays the download status.
- 

Use the[oci os object get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/get.html)command and required parameters to download an object from a bucket:

```

```

where`file_location`is the destination path for the file being downloaded, such as`C:\workspace\Downloads\MyFile.txt`or`/home/user/Documents/Downloads/MyFile.txt`.

For example:
```

```

No information is returned when you run the command. The file is downloaded to the specified destination.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/GetObject)operation to download an object from a bucket.

Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API:
```

```

The object name is everything after the`/o/`
