# NFS Client Reports an "NFS Server Not Responding" Message
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/mt-nfs-server-not-responding.htm
- Fetched: 2026-09-05 02:06 CDT

# NFS Client Reports an "NFS Server Not Responding" Message

An NFS client reports an "NFS Server not responding" message from a mount target.

This is a general troubleshooting guide that covers various factors related to this OS error message, which can have several causes. Review this information to help identify the cause and its associated troubleshooting tips.

The cause of this issue can be any of the following:

Cause 1 : The NFS client itself can't communicate to the File Storage mount target IP address because of an OS- or Kernel-related issue.

Check the OS-related TCP network settings such as:
- Whether the error message is coming from a single instance, or multiple instances.
- Verify that you're using the latest kernel patch and`nfs-utils`package.
- Check the load, performance, and memory usage of the instance during the affected period.
- Verify MTU settings, in particular, check for any mismatch in the default MTU settings.
- Check if`iptables`settings are causing dropped or denied NFS connections.

Cause 2 : A TCP network communication (VCN) issue exists between the NFS client and the mount target.

Check for network communication issues:
- Check whether any network firewall is causing dropped NFS requests.
- Use`rpcinfo -t <mount_target_IP> prognum`to test for mount, NFS, and`lockd`port connectivity from the NFS client.
- Use`traceroute -n -T -p <NFS_ports> <mount_target_ip>`to check connectivity.
- Use`sudo traceroute --mtu <mount_target_IP>`or`sudo tracepath <mount_target_IP>`to check for packet losses and drops because of mismatches in the MTU size.
- Use`nfsstat -o net`to check for any dropped packets.
- Use`nfsiostat <mount_path>`to check for detailed request data, such as`retrans`,`RTT`, and so on.
- Use`mountstats <mount_dir>`to check for any abnormal RPC stats.

Cause 3 : The File Storage mount target, which acts as the NFS server itself, isn't responding.

Check or collect the following for mount target issues:
- Use`dmesg -T`to check for issues.
- Check`/var/log/messages`for messages, including the timestamp of the message with timezone.
- Collect the file system or mount target OCID.

In all cases, collecting a packet capture from the NFS client at the time of the error is helpful in troubleshooting the issue further. For example:`tcpdump -i <interface_name> host <NFS_client_IP> -w /tmp/FSS.pcap`

For Windows users, collect information using Wireshark or similar tools.

Because these issues might be related to Compute instances and a VCN, issues can require collective troubleshooting. Engage[OCI support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm)and[create a service request](https://support.oracle.com)
