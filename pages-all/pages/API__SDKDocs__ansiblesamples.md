# Example Ansible Playbooks
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm
- Fetched: 2026-09-05 01:36 CDT

# Example Ansible Playbooks

This topic provides a catalog of sample Ansible playbooks for Oracle Cloud Infrastructure (OCI) that illustrate how to carry out common infrastructure provisioning and configuration tasks using our Ansible collection.

These samples and solutions are organized in sections associated with OCI services. You can find a brief description of each playbook along with links to each sample on the[Oracle GitHub repository](https://github.com/oracle/oci-ansible-collection). Be sure to review the`Readme.md`file that is included in each playbook's root directory for additional instructions.

See[Getting Started](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblegetstarted.htm)to begin using our Ansible collection.

## Samples

### Block Volume

[Attaching a block volume to a Compute instance](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample playbook shows how to attach a block volume to a compute instance using the iSCSI volume attachment type, and then connect it to the compute instance using`iscsiadm`. The sample shows how to do the following:
- Generate a temporary, host-specific SSH key pair.
- Specify the public key from the key pair for connecting to the instance, and then launch the instance.
- Create a new Block Volume for the instance, attach the volume to the instance, and specify iSCSI as the volume attachment type.
- Connect to and then mount the volume from the Compute instance by executing`iscsiadm`commands over SSH using an Ansible module.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/block_volume/attach_connect_block_volume).

### Compute

[Launching an Always Free compute instance](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample shows how to[launch](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)and[access](https://docs.oracle.com/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm)an Always Free compute instance from the internet using SSH using OCI Ansible collections.

This sample shows how to do the following:
- Generate a temporary, host-specific SSH key pair.
- Specify the public key from that key-pair to connect to the instance during instance launch.
- Connect to the newly launched instance using SSH.

[Go to the sample for Always Free on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/compute/always_free_launch_compute_instance).

[Launching a compute instance using App Catalog](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample shows how a public compute instance can be launched using app_catalog and accessed from the internet using SSH with OCI Ansible collections.

This sample shows how to do the following:
- Generate a temporary, host-specific SSH key pair.
- Specify the public key from that key-pair to connect to the instance during instance launch.
- Fetch app_catalog and its versions and create a subscription for it.
- Launch the instance using app_catalog and connect to it using SSH.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/compute/app_catalog).

[Creating an instance pool](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample shows how to manage your compute instances using resources such as instance configurations and instance pools that are provided using OCI Ansible collections. Instance pools help you create and provision multiple compute instances within the same region based on a single instance configuration.

This sample shows how to do the following:
- Generate a temporary, host-specific SSH key pair.
- Specify the public key from that key-pair to connect to the instance during instance launch.
- Create an instance configuration that defines settings for creating a compute instance as part of the instance pool. The configuration provides details such as base image, shape, and metadata.
- Use the instance pool to launch compute instances based on the instance configuration.
- Connect to one of the compute instances using SSH.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/compute/create_instance_pool).

[Creating instance Console connections and capturing Console history](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample shows how a[serial and VNC console connection](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm)can be created for a compute instance, and how the serial console data can be captured and fetched from a compute instance using OCI Ansible collections. For more information about Console connections, see[Troubleshooting Instances Using Instance Console Connections](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm).

This sample shows how to do the following:
- Generate a temporary SSH key pair for the serial Console connection.
- Create an instance Console connection for a compute instance.
- Capture serial Console data for a compute instance, and then save the data to a local machine so you can troubleshoot and debug issues.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/compute/instance-console-connections-and-capture-console-history).

[Launching a compute instance](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample shows how to[launch](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)and[access](https://docs.oracle.com/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm)a public compute instance from the internet using SSH with OCI Ansible collections.

This sample shows how to do the following:
- Generate a temporary, host-specific SSH key pair.
- Specify the public key from the key pair for connecting to the instance, and then launch the instance.
- Connect to the newly launched instance using SSH.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/compute/launch_compute_instance).

[Enabling internet access from a compute instance using the OCI NAT Gateway](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample shows how you can use OCI Ansible collections to enable internet access from compute instances in a private subnet using a NAT Gateway in a public subnet. For more information about NAT gateways, see[NAT Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm)and[Access Resources on the Public Internet Through an Oracle Cloud Infrastructure NAT Gateway](https://blogs.oracle.com/cloud-infrastructure/access-resources-on-the-public-internet-through-an-oracle-cloud-infrastructure-nat-gateway-v2).

This sample shows how to do the following:
- Set up the VCN, the NAT gateway, the internet gateway, the public and private subnets, and the necessary security lists and route rules.
- Provision a bastion instance in the public subnet and a private instance in the private subnet.

Once set up, the private instance will have outbound Internet access through the NAT gateway, and will be accessible using SSH from the bastion instance.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/compute/nat_gateway_configuration).

[Enabling internet access from a compute instance using an OCI NAT Instance](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample shows how you can use OCI Ansible collections to enable internet access from compute instances in a private subnet using a NAT instance in a public subnet as discussed[here](https://blogs.oracle.com/cloud-infrastructure/automate-deployment-nat-instance-in-oracle-cloud-infrastructure-with-terraform).
Note  
  
An NAT gateway is available as a reliable and highly available solution in the OCI Networking service. Please refer to the[sample](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#compute__computeNATGateway)for more details.

This sample shows how to do the following:
- Set up the topology described in the whitepaper by creating the VCN, the internet gateway, the public and private subnets, and the necessary security lists and route rules. A NAT instance is provisioned in the public subnet and a private instance is provisioned in the private subnet.
- After the setup, the private instance has outbound internet access through the NAT instance in the public subnet.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/compute/nat_instance_configuration).

[Accessing Object Storage from a private instance using a service gateway](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample playbook shows how you can use OCI Ansible collections to enable private access to an Object Storage from a compute instance using a service gateway. For more information about service gateways, see[Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm). To read a blog post discussing how to connect compute instances using the service gateway, see[Connect Private Instances with Oracle Services Through an Oracle Cloud Infrastructure Service Gateway](https://blogs.oracle.com/cloud-infrastructure/connect-private-instances-with-oracle-services-through-an-oracle-cloud-infrastructure-service-gateway).

This sample shows how to do the following:
- Set up a user, group, and the policies required for managing buckets.
- Create and upload the required API keys to the user.
- Set up the VCN, the NAT gateway, the internet gateway, the public and private subnets, as well as the required security lists and route tables. A bastion instance is provisioned in the public subnet, and a private instance is provisioned in the private subnet.
- Provision a compute instance in the private subnet,
- Install the OCI command line interface (CLI) and configure the CLI using the cloud init script.
- Disable the NAT gateway to restrict public access to the private instance.
- Create a bucket from the private instance using the OCI CLI, then verify that the bucket is created.

Following this setup, the private instance has private access to Object Storage.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/compute/service_gateway).

### Kubernetes Engine

[Creating a cluster using Kubernetes Engine](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample creates a cluster with Oracle Cloud Infrastructure Kubernetes Engine (OKE) using OCI Ansible collections.

This sample shows how to do the following:
- Create and configure a VCN and related resources required for setting up an OKE cluster.
- Create a cluster.
- Create a node pool.
- Download the kubeconfig file for the cluster.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/container_engine/generate_kubeconfig).

### Database

[Creating an Always Free Autonomous AI Database](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample shows how you can use the OCI Ansible collection to create an Always Free Autonomous AI Database with Autonomous AI Transaction Processing and manage its lifecycle. See[Always Free Autonomous AI Database](https://docs.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/atp-cloud&id=ADBSA-GUID-03F9F3E8-8A98-4792-AB9C-F0BACF02DC3E)for more information.

This sample shows how to do the following:
- Set up an Autonomous AI Database with Autonomous AI Transaction Processing.
- List all of the Autonomous AI Transaction Processing instances available in a compartment, filtered by display name.
- Get the "facts" for a specified database.
- Stop and start an Autonomous AI Database.
- Delete an Autonomous AI Database.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/database/always_free_autonomous_database).

[Setting up an Autonomous AI Database](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample shows how you can use the OCI Ansible collection to create an Autonomous AI Database with Autonomous AI Transaction Processing and manage its lifecycle. Refer to[Autonomous AI Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html)for more information.

This sample shows how to do the following:
- Set up an Autonomous AI Database with Autonomous AI Transaction Processing.
- List all of the Autonomous AI Transaction Processing instances available in a compartment, filtered by display name.
- Get the "facts" for a specified database.
- Stop and start an Autonomous AI Database.
- Delete an Autonomous AI Database.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/database/autonomous_database).

[Creating a Bare Metal and Virtual Machine DB system](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample shows how you can use the OCI Ansible collection to[create a DB System](https://docs.oracle.com/en/cloud/paas/base-database/create-dbs/index.html). For more information about OCI co-managed DB Systems, see[About Bare Metal and Virtual Machine Database Systems](https://docs.oracle.com/en/cloud/paas/base-database/about/index.html).

This sample shows how to do the following:
- Set up a Virtual Machine DB System.
- Get facts of a specific DB System and list available DB Homes.
- List all the databases available in specified DB Home and get facts of specific database.
- Collect DB Node's VNIC information of a specified DB system.
- Extract Public and Private IPs of the DB Node from VNIC.
- Create a backup from initial database.
- Restore a database from latest backup.
- Create a new database from backup.
- Update database fields.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/database/database_db_system).

### File Storage

[Creating and mounting a file system](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample shows how you can use the OCI Ansible collection to create and access a File Storage file system through compute instances.

This sample shows how to do the following:
- Generate all network related dependencies (e.g. VCN, subnets) and security lists with the configuration required by File Storage.
- Generate the certificates required by instances.
- Create File Storage components such as mount target, file system, export, and snapshot.
- Mount the file system through a compute instance and access the contents through another compute instance.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/database/database_db_system).

[Exporting multiple file systems and mount targets](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample shows how you can use the OCI Ansible collection to export one file system using two different export paths on two different mount targets. It also demonstrates how a single mount target can export paths from two different file systems.

This sample shows how to do the following:
- Generate all network related dependencies (e.g. VCN, subnets) and security lists with the configuration required by File Storage.
- Generate the certificates required by instances.
- Create File Storage components such as mount target, file system, export, and snapshot.
- Export one file system to two different mount targets.
- Export paths from a single mount target to two different file systems.
- Mount the file system through a compute instance.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/file_storage/multiple_file_systems_with_mount_targets).

### Identity

[Adding a user and group](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample shows how you can use the OCI Ansible collection to perform basic Oracle Cloud Infrastructure Identity and Access Management (IAM) tasks. The sample assumes the default user configured in the OCI configuration is in the Administrator group or has the required access for managing users, groups, policies.

This sample shows how to do the following:
- Create a new group.
- Create a policy.
- Create a user then add it to the group and policy.
- Create user password.
- Generate SSH keys and assign them to the user.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/identity/add-user-and-group).

### Load Balancing

[Creating a load balancer](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample shows how you can use the OCI Ansible collection to create a public load balancer.

This sample shows how to do the following:
- Generate all network-related dependencies, like a VCN and subnets.
- Generate the certificates required by the load balancer.
- Create a public load balancer.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/load_balancing/create_load_balancer).

### Networking

[Provisioning a VCN with private subnets](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample shows how you can use the OCI Ansible collection to provision a virtual cloud network (VCN) with two private subnets in different availability domains and a Site-to-Site VPN. The Site-to-Site VPN uses a dynamic routing gateway (DRG), customer-premises equipment (CPE), and an IPSec connection. The provisioned resources are illustrated in[this networking scenario](https://docs.oracle.com/iaas/Content/Network/Tasks/scenariob.htm).

This sample shows how to provision the following resources:
- A VCN
- Two private subnets
- A dynamic routing gateway
- Customer-premises equipment
- An IPSec connection between DRG &amp; CPE

Finally, it retrieves IPSec connection configuration information and status.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/networking/private_subnets_with_vpn).

### Object Storage

[Getting a namespace](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample playbook shows how to use the OCI Ansible collection to get the tenancy namespace in Object Storage.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/object_storage/get_namespace).

[Listing objects and buckets](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample playbook shows how to use the OCI Ansible collection to list all Object Storage objects from all buckets in a namespace.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/object_storage/list_objects).

[Deleting objects](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm#)

This sample playbook shows how to use the OCI Ansible collection to delete objects created within a specified range of days from all buckets in a namespace. You can modify the sample so that it deletes objects older than a specified number of days, which helps you prune old or unwanted objects stored in the Object Storage service.

[Go to the sample on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/samples/object_storage/delete_objects).

## Solutions

### MuShop

MuShop is a showcase of several Oracle Cloud Infrastructure (OCI) services in a unified reference application. The sample application implements an e-commerce platform built as a set of microservices. The accompanying content can be used to get started with cloud native application development on OCI.

MuShop can be deployed in different ways to explore OCI based on your subscription. OCI offers Always Free tier with resources that can be used indefinitely.

This project is an example of how you can build OCI infrastructure using the OCI Ansible collection.

[Go to the solution on Oracle GitHub](https://github.com/oracle/oci-ansible-collection/tree/master/solutions/oci-cloudnative)
