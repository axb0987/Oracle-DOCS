# Recovering a Deleted Object Version from Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/recover-object-version.htm
- Fetched: 2026-09-05 03:02 CDT

# Recovering a Deleted Object Version from Roving Edge Infrastructure

Describes how to recover a deleted object version contained within an object storage bucket on your Roving Edge Infrastructure devices.

Recovering a deleted object version requires removing the delete marker that was created when you deleted the latest version of an object. The previous version of the object listed just below the delete marker is recovered and becomes the latest version of the object.

## Using the Device Console

- Open the navigation menu and select Object Storage &gt; Object Storage . The Buckets page appears. All buckets are listed in tabular form.
- Select the bucket containing the object whose deleted version you want to recover. The bucket's Details page appears. All objects are listed in tabular form.
- Enable Show Deleted Objects to display those objects that were versioned, but subsequently deleted.
- Select the Down arrow at the right side of the object's entry to display the versions that you can recover. Look for the entry that includes " (Delete Marker) " under the Last Modified column.
- Select the Actions menu ( ) of the entry with the Delete Marker identifier and select Delete .
- Confirm the deletion.
