# Paths in File Systems
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Concepts/filesystempaths.htm
- Fetched: 2026-09-05 02:02 CDT

# Paths in File Systems

The File Storage service uses three kinds of paths :
- 

Export Paths are part of the information contained in an export that makes a file system available through a mount target. The export path uniquely identifies the file system within the mount target, letting you associate up to 100 file systems behind a single mount target. The export path is used by an instance to mount (logically attach to) the file system. This path is unrelated to any path within the file system or the client instance. It exists solely as a way to distinguish one file system from another within a single mount target.

In this mount command example,`10.0.0.6`is the mount target IP address.`/FileSystem1`is the unique export path that was specified when the file system was associated with a mount target during creation.

`sudo mount 10.0.0.6:/FileSystem1 /mnt/mountpointA`

Important  
  

The export path must start with a slash (/) followed by a sequence of zero or more slash-separated elements. If there are many file systems associated with a single mount target, the export path sequence for the first file system can't contain the complete path element sequence of the second file system export path sequence. Export paths can't end in a slash. No export path element can be a period (.) or two periods in sequence (..). No export path can exceed 1024 bytes. Lastly, no export path element can exceed 255 bytes.

Valid examples:
- `/example`and`/path`
- `/example`and`/example2`

Invalid examples:
- `/example`and`/example/path`
- `/`and`/example`
- `/example/`
- `/example/path/../example1`
Caution  
  
If one file system associated with a mount target has '/' specified as an export path, you can't associate another file system with that mount target.
Note  
  
Export paths can't be edited after the export is created. To use a different export path, you must create a new export with the appropriate path. Optionally, you can then delete the export with the old path.

See[Managing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/managingmounttargets.htm)for more information about mount targets and exports.
- 

Mount Point Paths are paths within a client instance to a locally accessible directory to which the remote file system is mounted.

In this mount command example,`/mnt/mountpointA`is the path to the directory on the client instance on which the external file system is mounted.

`sudo mount 10.0.0.6:/FileSystem1 /mnt/mountpointA`

See[Mounting File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/mountingfilesystems.htm)for more information.
- 

File System Paths are paths to directories within the file system, and contain the contents of the file system. When the file system is mounted, you can create any directory structure within it you like. Snapshots of the file system can be accessed using the file system path, under the file system's root directory at`.snapshot/name`.

The following example shows the path to a snapshot called 'January 1' when navigating from the instance:

`/mountpointA/.snapshot/January1`
