# Deleting a VMware Solution Datastore
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/datastore-delete.htm
- Fetched: 2026-09-05 03:08 CDT

# Deleting a VMware Solution Datastore

Delete a VMware Solution datastore from your tenancy.

Note  
  
Before you can delete a datastore, it must be detached from a datastore cluster.

## Using the Console

- Open the navigation menu and select Hybrid . Under VMware Solution , select Datastore .
The Datastores list opens. All datastores are displayed in a table.
- From the Actions menu for the datastore that you want to delete, select Delete .
The Delete datastore panel opens.
- (Optional) Select Delete attached block volume .
For the block volume to be successfully deleted, the block volume must not have any attachments. After the block volume is deleted, you can't recover the its data. If you plan to import the block volume as another datastore, we recommend you don't select this option.
- Enter the name of the datastore you're deleting to confirm the deletion.
- Select Delete .
