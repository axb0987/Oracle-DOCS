# Managing Folders in an Object Storage Bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_create_a_new_folder.htm
- Fetched: 2026-09-05 02:51 CDT

# Managing Folders in an Object Storage Bucket

Create and delete folders and subfolders in an Object Storage bucket to organize objects.

Use the Console to create folders and subfolders in which you can upload and store your objects according to your organizational needs.

## Using the Console

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Objects .
The Objects tab opens. All objects in the selected bucket are displayed in a table.
- Perform one of the following tasks:

- 

To add a new folder: Select Create new folder from the Actions menu.
- 

To add a folder or subfolder to an existing folder: Select the existing folder to open it. Select Create new folder from the Actions menu.
The Create new folder panel opens.
- Enter a name for the folder or subfolder. Avoid entering confidential information.
- Select Create folder .
The folder or subfolder is created and displayed in the Objects table, either at the root level of the Objects list or under an existing folder depending on where you created it.

### Deleting a Folder

When you delete a folder in the Objects list, all the objects contained in the folder are deleted. If object versioning is enabled on the bucket, you can restore those objects. See[Restoring a Deleted Object](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_recover_a_deleted_object.htm)for more information.

- Find the root or parent folder of the folder you want to delete in the Objects list.
- From the Actions menu for the folder, select Delete folder .
-
