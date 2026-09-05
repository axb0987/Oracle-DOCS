# Accessing File Systems from Running Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsaccessinglocalfilesystem.htm
- Fetched: 2026-09-05 02:07 CDT

# Accessing File Systems from Running Functions

Find out how to access file systems from running functions deployed to OCI Functions.

A function you've deployed to OCI Functions can access the file system of the container in which it's running as follows:
- the function can read files from all directories
- the function can write files to the /tmp directory

For example, you might want a function to download an Excel file and then read its contents. To meet this requirement, you might create a function that writes the file to the /tmp directory in the container's filesystem, and then subsequently reads the file.

When writing files to the /tmp directory, the /tmp directory is generally always writable. However, the maximum allowable size of the /tmp directory depends on the maximum memory threshold specified for the function:

Maximum memory threshold for the function (MB) Maximum allowed size of /tmp (MB) Maximum allowed number of files (inodes) in /tmp
128 MB 32 MB 1,024
256 MB 64 MB 2,048
512 MB 128 MB 4,096
1024 MB 256 MB 8,192
2048 MB 512 MB 16,384
3072 MB 768 MB 24,576
