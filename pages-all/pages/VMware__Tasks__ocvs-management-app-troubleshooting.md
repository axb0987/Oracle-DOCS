# Troubleshooting the VMware Solution Management Appliance
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvs-management-app-troubleshooting.htm
- Fetched: 2026-09-05 03:08 CDT

# Troubleshooting the VMware Solution Management Appliance

Apply these solutions when troubleshooting the VMware Solution Management Appliance.

## Creating a Management Appliance Takes Longer than Expected

If your Management Appliance remains in the Creating state longer than expected, check its work request to see if any issues exist with the creation workflow.

- Access the VMware Solution work request list page for the SDDC. See[Listing an SDDC's Work Requests](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/list-sddc-work-requests.htm)for more information.
- Select your work request in the Work Requests list. The work request is typically named "Create management appliance."
The details page for the work request opens.
- Select the Error messages section.
If no errors are listed, give it more time. If you see an error appears, proceed with next steps.
- Review any error messages that appear. The error messages might provide you more explanation if something is wrong. For example, a routing rule is missing.
- Fix any issues that appear in the error message list.
For example, if the routing rule is missing, add an applicable routing rule to your VCN.
- Wait for the Management Appliance to transition to the Failed state. This process can take up to two hours.
- Run the create Management Appliance workflow again.

## Errors in Management Appliance States

The Management Appliance can be in a wrong or inconsistent state after provisioning, or after system changes occur.

In the following example, the OCI Console shows the Management Appliance in the Needs Attention state.

[

Select View details to see the explanation. The State details appear.
  

  

The following table lists issues and troubleshooting solutions associated with the state details categories listed here.

Management Appliance State Details Troubleshooting
Issue Troubleshooting Steps
vSphere connectivity The Management Appliance connects to the vSphere API. It uses the credentials of the ocvssystem user which are stored in a vault secret described[Create Vault Secrets with User Credentials](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvs-management-app-install.htm#create-vault-secrets).

The credentials are used for read-only operations run by the Management Appliance, such as reading metric information.
- Ensure that latest vSphere ocvssystem user credentials are provided in the vault secret and the secret is linked to the management appliance.
- 

Check if the vSphere API is reachable from the Management Appliance.

For more information, see[Checking Connectivity to vSphere Client and NSX Manager](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvs-management-app-troubleshooting.htm#checking-connectivity-vSphere)
vSphere admin connectivity

For some operations the Management Appliance connects to vSphere API with admin privileges. This type of connectivity is similar to "vSphere connectivity," but in this case the Management Appliance, it has more permissions which allow it to do more serious modifications in vCenter.

The admin credentials are provided in a separate Vault secret and required for OCVS vSphere UI plugin registration and for unregistration (when the Management Appliance is deleted).

For security reasons, we recommend you revoke access to the credentials to the Management Appliance as soon as registration is done.
- Ensure that latest vSphere administrator user credentials are provided in the Vault secret and the secret is linked to the Management Appliance.
- 

Check if the vSphere API is reachable from the Management Appliance.

For more information, see[Checking Connectivity to vSphere Client and NSX Manager](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvs-management-app-troubleshooting.htm#checking-connectivity-vSphere)
NSX connectivity NSX connectivity is required for network configuration operations performed by the Management Appliance. For example, the Add ESXi Host operation uses this connectivity for making sure ESXi host has proper network transport node configured.
- Ensure that NSX latest admin user credentials are provided in the Vault secret and the secret is linked to the Management Appliance.
- 

Check if NSX API is reachable from the Management Appliance

For more information, see[Checking Connectivity to vSphere Client and NSX Manager](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvs-management-app-troubleshooting.htm#checking-connectivity-vSphere)
vSphere UI plugin registration The Management Appliance runs an internal web server which implements backend for the OCVS vSphere UI plugin. The plugin should be registered in vSphere before it can be used. The registration is done automatically by the Management Appliance.

When starting it calls vSphere API using vSphere administrator credentials. If admin credentials aren't available at that moment the registration operation might fail and OCVS vSphere UI plugin functionality aren't available.

Check if the vSphere administrator user credentials are provided in the Vault secret and have correct values and the secret is linked to the Management Appliance.

If you update the credentials, it takes up 3-5 minutes for the Management Appliance to complete registration before the vSphere UI plugin registration items receives the Healthy green state.

## SSH access to the Management Appliance Network Diagnostics and Log Collection

SSH access to the Management Appliance is required for troubleshooting purposes and you should proceed with caution. If SSH access is not available, it might cause Management Appliance to operate incorrectly.

Since the Management Appliance Compute instance is provisioned without a public IP address, you must have access to the subnet of your SDDC through a[bastion](https://www.oracle.com/security/cloud-security/bastion/)or another jump host with public IP address.

To apply SSH to the Management Appliance, use a private SSH key which is a paired key for the public key you used when creating the Management Appliance. For more information, see[SSH access to the Management Appliance Network Diagnostics and Log Collection](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvs-management-app-troubleshooting.htm#ssh-access-network-diagnostics).

## Checking Connectivity to vSphere Client and NSX Manager

To check the connectivity to vSphere Client and NSX Manager, follow these steps:

- Open your SDDC details page in OCI Console.
For more information, see[Getting an SDDC's Details](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-get.htm).
- Find the SDDC Information section.
- Find vSphere client IP address and NSX Manager IP address.
- Open an SSH session and run the following command:

```

```

If network connectivity exists, both commands produce output similar to the following:
```

```

Note  
  
The IP address might differ if you have a custom network setup.

## Collecting Logs

The following folders contain log files related to work of the Management Appliance vSphere UI plugin:
- Web server logs:`/opt/oracle/mgmt_agent/plugins/ocvp/stateDir/log`
- Management Agent:`logs/opt/oracle/mgmt_agent/agent_inst/log`

To copy the log output into a single support bundle file, run the following command:
```

```

This action generates the support-bundle.zip file in`/home/ops`folder. Download this file to your local environment and use it when contacting our Oracle Support for troubleshooting.

After file is downloaded, you can delete it from the Management Appliance by running the following command:
```

```

## Resetting the Management Appliance

Sometimes it might be necessary to reset the Management Appliance, such as if it's not functioning properly for unknown reasons, or if hardware issues that require you to provision a new Management Appliance instance. We recommended you check if OCVS UI plugin is unregistered before installing a new Management Appliance. See Manual unregistration of OCVS UI plugin section.

## Manually Unregistering the OCVS UI Plugin

If the Management Appliance is terminated without your administrator credentials being up-to-date, the Compute instance is terminated, but the vSphere UI still allows the OCVS UI Plugin plugin to appear to the user. In this case, the plugin's screen components are displayed as empty gray rectangles. If this occurs, you must perform a manual unregistration of OCVS UI Plugin plugin. Perform the following steps:

- Open Administration → Solutions → Client Plugins page.
- Find the OCI-OCVS Integration Plugin and select the link for details.
- Select the plugin server name's box and select Remove .
This action removes OCVS UI Plugin plugin registration and vSphere UI doesn't have any links to it any more.

## Manually Terminating the Management Agent

The Management Appliance uses the Management Agent service for keeping internal software up-to-date. Every Management Appliance creates a Management Agent Resource in OCI which is responsible for update delivery.

When the Management Appliance is terminated, the Management Agent Resource is terminated as well. However, in case of emergency termination of the Management Appliance, such as a hardware failure, the Management Agent Resource might still remain in inactive mode. In this case, you must delete the resource manually.

- Select your region from the OCI Console.
- Open the navigation menu and select Observability &amp; Management . Under Management Agent , select Agents .
- Select the Agents and Gateways menu section.
- Select the compartment of your SDDC.
- In the list of agents, find agent corresponding to your Management Appliance. It can be identified by Host column's value which has same name as your host name of the Management Appliance.

## Troubleshooting the OCVS UI Plugin

When you run automated activities with OCVS VMware UI plugin, such as Add ESXi host or Add Datastore, the activities can fail when running a configuration step. The failures can be the result of some custom configurations in your SDDC. You might rename some objects or add new types of objects into the system which might cause configuration algorithm to fail. Some job steps might have already succeeded and they might have created some objects that aren't needed because the full job execution has failed.

The following image shows how a failed Add ESXi Host Job appears. The job failed in the "Waiting for NSX to be configured for ESXi host" step.

[

When you experience an error in a job step, we provide a troubleshooting manual describing how to do manual recovery for that step an how to manually proceed with further steps. The manual proceed steps are based on our existing documentation[Add an ESXi Host to an Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html)and[Integrate OCI Block Volumes with Oracle Cloud VMware Solution](https://docs.oracle.com/en/learn/integrate-oci-block-volumes-ocvs/).

The following sections provide information on how you should address different job steps failures.

### Add ESXi Host Job Troubleshooting and Recovery Plan

The Add ESXi Host job in Management Appliance automates the following manual workflow[Add an ESXi Host to an Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html)which described in Oracle public documentation and available to the customer. When Add ESXi Host job is run, it makes status updates for each step it performs. If a step fails, proceed with the manual workflow described in[Add an ESXi Host to an Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html)starting from the point of failure.

Add ESXi Host Job Troubleshooting and Recovery Plan
Step Description Troubleshooting
1. Provision ESXi Host in OCI

This step provisions ESXi host for an SDDC in OCI.

This job step corresponds to[Task 1: Add an ESXi Host in OCI Console to a Cluster in Your SDDC](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#task-1-add-an-esxi-host-in-oci-console-to-a-cluster-in-your-sddc)section in[Add an ESXi Host to an Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html)document.

What can go wrong :

If this error happens it means that system couldn't provision ESXi host in OCI. The error message in the job step should display the root cause. The root cause might be connected to compute capacity or customer's limits, or there might be some other reason.

Step rollback : Delete any resources/configuration, that was created during ESXi host provisioning in OCI Console.

Proceed instructions : You can fix some root causes and run the "Add ESXi host" operation again. Because the step can leave a unneeded resources in OCI, you should perform a manual rollback (deletion of created resources and/or configuration in OCI). The error message should point to instructions for the manual rollback. Refer to manual guide:[Task 1: Add an ESXi Host in OCI Console to a Cluster in Your SDDC](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#task-1-add-an-esxi-host-in-oci-console-to-a-cluster-in-your-sddc).
2. Add ESXi Host to vCenter

This step creates the ESXi host object in vCenter. It refers to an existing ESXi host in OCI.

This job step corresponds to[Task 3: Add ESXi Host to the vCenter Cluster and Configure Host Networking](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#task-3-add-esxi-host-to-the-vcenter-cluster-and-configure-host-networking)→ Add ESXi Host to vCenter Cluster section in[Add an ESXi Host to an Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html)document.

What can go wrong :
- You have no permissions to call vSphere API.
- Networking/Hardware issues during step execution.

Step rollback : Remove created ESXi host from vCenter inventory:
- Connect to VMware vCenter server.
- Verify, that ESXi host was created.
- If ESXi host was created, open context menu by right-clicking on an ESXi host and select Remove from Inventory .

Proceed instructions : Proceed from[Task 3: Add ESXi Host to the vCenter Cluster and Configure Host Networking](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#task-3-add-esxi-host-to-the-vcenter-cluster-and-configure-host-networking)→ Add ESXi Host to vCenter Cluster .
3. Set ESXi Host to Maintenance Mode

This step sets the ESXi host to maintenance mode to start further operations.

This job step corresponds to the[Task 3: Add ESXi Host to the vCenter Cluster and Configure Host Networking](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#task-3-add-esxi-host-to-the-vcenter-cluster-and-configure-host-networking)→ Set ESXi Host to Maintenance Mode section in[Add an ESXi Host to an Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html)document.

What can go wrong :
- You have no permissions to call vSphere API.
- Networking/Hardware issues during step execution.

Step rollback : Exit maintenance mode for an ESXi host:
- Connect to VMware vCenter server.
- Verify that ESXi host is in maintenance mode.
- If ESXi host is in maintenance mode, open context menu by right-clicking on an ESXi host and select Maintenance Mode → Exit Maintenance Mode .

Proceed instructions : Proceed from[Task 3: Add ESXi Host to the vCenter Cluster and Configure Host Networking](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#task-3-add-esxi-host-to-the-vcenter-cluster-and-configure-host-networking)→ Set ESXi Host to Maintenance Mode .
4. Add ESXi Host to Distributed Switch

This step adds the ESXi host to distributed virtual switch. Distributed virtual switch is identified by name &lt;cluster-name&gt; -DSwitch where &lt;cluster-name&gt; is a name of the cluster ESX host is created in.

This job step corresponds to the[Task 3: Add ESXi Host to the vCenter Cluster and Configure Host Networking](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#task-3-add-esxi-host-to-the-vcenter-cluster-and-configure-host-networking)→ Add ESXi Host to Distributed Switch section in[Add an ESXi Host to an Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html)document.

What can go wrong:
- You have renamed the switch using a non-standard name and automation code can't identify the switch.
- You have several switches configured.
- Port groups vmdk have been renamed.
- You have no permissions to call vSphere API.
- Networking/Hardware issues during step execution.

Step rollback : Remove the ESXi host from the distributed virtual switch (DVS):
- Connect to VMware vCenter server.
- Navigate to the Networking tab in the VMware vCenter Server and find the distributed virtual switch, that the ESXi host was added to. Typically, DVS is named " &lt;cluster_name&gt; -DSwitch".
- Right-click on the DVS object and select Add and Manage Hosts... .
- In the dialog box, select Remove hosts , then select Next .
- Select the host that you want to remove from DVS and select Next .
- Select Finish .

Proceed instructions : Proceed from[Task 3: Add ESXi Host to the vCenter Cluster and Configure Host Networking](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#task-3-add-esxi-host-to-the-vcenter-cluster-and-configure-host-networking)→ Add ESXi Host to Distributed Switch .
5. Move ESXi Host to vCenter Cluster

This step moves the ESXi host object to vCenter cluster. It automatically starts NSX agent installation and transport node configuration process for the host.

This job step corresponds to the[Task 3: Add ESXi Host to the vCenter Cluster and Configure Host Networking](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#task-3-add-esxi-host-to-the-vcenter-cluster-and-configure-host-networking)→ Move ESXi Host to vCenter Cluster section in[Add an ESXi Host to an Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html)document.

What can go wrong:
- You have no permissions to call vSphere API.
- Networking/Hardware issues during step execution.

Step rollback : Move host out of the cluster if host is in the cluster:
- Connect to VMware vCenter server.
- Navigate to the Hosts and Clusters tab.
- Locate an ESXi host and verify that it's in the cluster.
- If the ESXi host is in the cluster, drag it to the datacenter object. You can also right-click the ESXi host and select Move To... .

Proceed instructions : Proceed form[Task 3: Add ESXi Host to the vCenter Cluster and Configure Host Networking](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#task-3-add-esxi-host-to-the-vcenter-cluster-and-configure-host-networking)→ Move ESXi Host to vCenter Cluster .
6. Verify NSX Configuration on the ESXi Host

This step checks the ESXi host's transport node in NSX It waits until it finishes configuration and has successful status.

This job step corresponds to the[Task 4: Verify NSX Configuration on the ESXi Host](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#task-4-verify-nsx-configuration-on-the-esxi-host)section in[Add an ESXi Host to an Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html)document.

What can go wrong :
- Internal NSX transport node configuration issue, such as an IP address conflict.
- No NSX transport node profile associated with the cluster exists. In this case, the step expires with a timeout message.
- Missing or wrong NSX credentials in NSX vault of management appliance.
- Networking/Hardware issues during step execution.

Step rollback : None. No rollback exists because the step doesn't change anything. It only checks for a proper state of transport node.

Proceed instructions : Configure the transport node manually in NSX console and proceed from[Task 5: Configure Datastores and Exit Maintenance Mode](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#task-5-configure-datastores-and-exit-maintenance-mode).
7. Configure Virtual Machine File System Datastore

This step configures the ESXi host to use VMFS datastore as primary storage that's used by the cluster. This step is run only if the ESXi host has a standard shape configuration.

This job step corresponds to the[Scenario 1: Configure Virtual Machine File System (VMFS) Datastores (Standard Shapes)](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#scenario-1-configure-virtual-machine-file-system-vmfs-datastores-standard-shapes)section, 1-9 items in[Add an ESXi Host to an Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html)document.

What can go wrong :
- You have no permissions to call vSphere API.
- Networking/Hardware issues during step execution.

Step rollback : Remove the ESXi host from the VMFS datastore:
- Connect to VMware vCenter server.
- Navigate to the Storage tab.
- Find the datastore that the ESXi host was added to.
- Navigate to Configure → Connectivity and Multipathing .
- Select the ESXi host that you want to remove from the datastore and select Unmount .
- Navigate to the Hosts and Clusters tab and select the ESXi host that you want to remove from the datastore.
- Navigate to Configure → Storage Adapters .
- Select iSCSI Software Adapter (named vmhbaXX).
- Select the Devices tab.
- 

Find the storage device you want to remove, select it and if it's operation state is Attached , select Detach to detach storage device from ESXi host.

Storage device ID can be found by its IQDN in Paths tab by querying results by IQDN (Target column) and noting device's ID in LUN ID column.
- 

After storage device's operation state is Detached , select the Static Discovery tab, find iSCSI server by IQDN ( Target Name column) or server IP and port, select it and select Remove .

IQDN and iSCSI server IP and port can be found in the OCI Console.
- Select the Dynamic Discovery tab and remove iSCSI server similarly as in previous step.
- Select Rescan Adapter .
- Select Rescan Storage .

Proceed instructions : Proceed from[Scenario 1: Configure Virtual Machine File System (VMFS) Datastores (Standard Shapes)](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#scenario-1-configure-virtual-machine-file-system-vmfs-datastores-standard-shapes).
8. Configure vSAN Datastore

This step configures the ESXi host to use vSAN datastore as primary storage. This step is run only if the ESXi host has a dense shape configuration.

This job step corresponds to the[Scenario 2: Configure vSAN Datastore and Fault Domain (Dense Shapes)](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#scenario-2-configure-vsan-datastore-and-fault-domain-dense-shapes)section, 2-7 items in[Add an ESXi Host to an Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html)document.

What can go wrong :
- You have no permissions to call vSphere API.
- Networking/Hardware issues during step execution.

Step rollback : Remove the ESXi host from vSAN cluster:
- Connect to VMware vCenter server.
- Navigate to the Hosts and Clusters tab.
- Select the cluster that ESXi host has been added to.
- Navigate to Configure → vSAN → Disk Management .
- Select the ESXi host that you want to be removed from the vSAN cluster and select Go to Pre-check.
- In the Data Migration Pre-Check page, select Full data migration as the vSAN data migration type and select Pre-check .
- Wait for the pre-check to complete and verify that any data/VMs that are on the disks are intact after the data evacuation. If everything is OK, select Enter Maintenance Mode for the ESXi host to enter maintenance mode.
- After the ESXi host is in maintenance mode, navigate to Configure → vSAN → Disk Management and select the ESXi host that you want to be removed from vSAN cluster.
- Select View Disks .
- Select the Actions menu (three dots) on the disk group and select Unmount .
- After the disks are unmounted, select the Actions menu (three dots) on the disk group item and select Remove .
- Exit maintenance mode for the ESXi host by right-clicking on the ESXi host and selecting Maintenance Mode → Exit Maintenance Mode .

Proceed instructions : Proceed from[Scenario 2: Configure vSAN Datastore and Fault Domain (Dense Shapes)](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#scenario-2-configure-vsan-datastore-and-fault-domain-dense-shapes).
9. Configure Fault Domain for ESXi Host

This step configures the fault domain (FD) for an ESXi host. You can change the fault domain manually later on. This step is run only if the ESXi host has a dense shape configuration.

This job step corresponds to the[Scenario 2: Configure vSAN Datastore and Fault Domain (Dense Shapes)](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#scenario-2-configure-vsan-datastore-and-fault-domain-dense-shapes)section, 8-10 items in[Add an ESXi Host to an Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html)document.

What can go wrong :
- You have no permissions to call vSphere API.
- Networking/Hardware issues during step execution.

Step rollback : Move the ESXi host from fault domain:
- Connect to VMware vCenter server.
- Select the Hosts and Clusters tab.
- Select the cluster that the new ESXi host was moved in to.
- Navigate to Configure → vSAN → Fault Domains .
- Find the fault domain that the new ESXi host is in.
- Select the ESXi host you want to move out of the fault domain.
- Select the Actions menu (three dots) in the corner of Fault Domain section and select Move Hosts → Remove from &lt;fault_domain_name&gt; option.
- In the dialog box, select Move .

Proceed instructions : Proceed from[Scenario 2: Configure vSAN Datastore and Fault Domain (Dense Shapes)](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#scenario-2-configure-vsan-datastore-and-fault-domain-dense-shapes).
10. Exiting maintenance mode for ESXi Host

This step exists maintenance mode for an ESXi host.
- For ESXi hosts, based on Standard shapes, this step is run as the last one.
- For ESXi hosts, based on Dense shapes, this step is run after step 6 (Verify NSX Configuration on the ESXi Host).

This job step corresponds to:
- For ESXi hosts, based on Standard shapes:[Scenario 1: Configure Virtual Machine File System (VMFS) Datastores (Standard Shapes)](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#scenario-1-configure-virtual-machine-file-system-vmfs-datastores-standard-shapes)section, item 10 in[Add an ESXi Host to an Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html)document.
- For ESXi hosts, based on Dense shapes:[Scenario 2: Configure vSAN Datastore and Fault Domain (Dense Shapes)](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#scenario-2-configure-vsan-datastore-and-fault-domain-dense-shapes)section, item 1 in[Add an ESXi Host to an Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html)document.

What can go wrong :
- Networking/Hardware issues during step execution.

Step rollback : No action is required. In case of failure, the ESXi host is going to remain in maintenance mode.

Proceed instructions :
- For ESXi hosts, based on Standard shapes, proceed from[Scenario 1: Configure Virtual Machine File System (VMFS) Datastores (Standard Shapes)](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#scenario-1-configure-virtual-machine-file-system-vmfs-datastores-standard-shapes)section, item 10.
- For ESXi hosts, based on Dense shapes, proceed from[Scenario 2: Configure vSAN Datastore and Fault Domain (Dense Shapes)](https://docs.oracle.com/en/learn/add-ocvs-esxi-host/index.html#scenario-2-configure-vsan-datastore-and-fault-domain-dense-shapes)section, item 1.

### Add Datastore Job Troubleshooting and Recovery Plan

The Add Datastore job in the Management Appliance automates the following manual workflow[Integrate OCI Block Volumes with Oracle Cloud VMware Solution](https://docs.oracle.com/en/learn/integrate-oci-block-volumes-ocvs/). When you run an Add Datastore job, it makes status updates for each step it performs. If a step fails proceed with manual workflow described in[Integrate OCI Block Volumes with Oracle Cloud VMware Solution](https://docs.oracle.com/en/learn/integrate-oci-block-volumes-ocvs/)starting from the point of failure.

Add Datastore Job Troubleshooting and Recovery Plan
Step Description Troubleshooting
1. Create OCI resources Creates OCI resources: block volume, datastore, datastore bluster and attaches created block volumes to the ESXi host Compute instances. This step corresponds to[Task 1: Create an OCI Block Volume](https://docs.oracle.com/en/learn/integrate-oci-block-volumes-ocvs/#task-1-create-an-oci-block-volume)and[Task 2: Attach the OCI Block Volume to ESXi Hosts](https://docs.oracle.com/en/learn/integrate-oci-block-volumes-ocvs/#task-2-attach-the-oci-block-volume-to-esxi-hosts)section.

If this step fails, you should not normally do anything because the workflow cleans up the resources it created. If there are still objects remaining after this failed step, contact Oracle Support.

Step rollback : You can manually roll back this step. The sequence of actions to perform is:
- 

Remove the datastore from the datastore cluster. This action should automatically detach block volumes from the ESXi host compute instances.

If the datastore cluster has only one datastore attached to it, the datastore cluster must be detached from SDDC cluster first, because last datastore in the datastore cluster can't be removed from datastore cluster if the datastore cluster is attached to the SDDC cluster.
- Delete the datastore resource.
- Delete the datastore cluster (if it was created during Datastore provisioning).
- Delete any block volumes you created.

Proceed instructions : You can retry running the job or follow the manual guide:[Task 1: Create an OCI Block Volume](https://docs.oracle.com/en/learn/integrate-oci-block-volumes-ocvs/#task-1-create-an-oci-block-volume).
2. Configure Host Storage Adapter for iSCSI Corresponds to the[Task 3: Configure Storage Adapter (vmhba) for iSCSI](https://docs.oracle.com/en/learn/integrate-oci-block-volumes-ocvs/#task-3-configure-storage-adapter-vmhba-for-iscsi)section.

What can go wrong :
- You have no permissions to call vSphere API.
- Networking/Hardware issues during step execution.

Step rollback : To remove added storage devices from storage adapter:
- Connect to VMware vCenter server.
- Select the first ESXi host in a cluster that the datastore was being created for.
- Navigate to Configure → Storage Adapters .
- Select iSCSI Software Adapter (named vmhbaXX).
- Select the Devices tab.
- Find the storage device you want to remove and verify that it's not consumed by any datastore.
- 

Select the storage device that's in the Operation state. If it's attached, select Detach to detach storage device from the ESXi host.

Storage device ID can be found by its IQDN in Paths tab by querying results by IQDN (Target column) and noting device's ID in LUN ID column.
- 

After the storage device's operation state moves to Detached , select the Static Discovery tab, find iSCSI server by IQDN (Target Name column) or server IP and port, select it and select Remove .

IQDN and iSCSI server IP and port can be found in OCI console.
- Select the Dynamic Discovery tab and remove the iSCSI server similarly as in previous step.
- Select Rescan Adapter .
- Select Rescan Storage .
- Repeat these steps for every other ESXi host in a cluster.

Proceed instructions : Proceed with manual configuration[Task 3: Configure Storage Adapter (vmhba) for iSCSI](https://docs.oracle.com/en/learn/integrate-oci-block-volumes-ocvs/#task-3-configure-storage-adapter-vmhba-for-iscsi)section.
3. Create Datastore in vCenter Corresponds to the[Task 4: Add the new VMFS Datastore to Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/integrate-oci-block-volumes-ocvs/#task-4-add-the-new-vmfs-datastore-to-oracle-cloud-vmware-solution-cluster)section.

What can go wrong :
- You have no permissions to call vSphere API.
- Networking/Hardware issues during step execution.

Step rollback :
- Connect to VMware vCenter server.
- Navigate to the storage tab in the VMware vCenter Server and find the datastore object that you want to delete.
- Right-click on the datastore object and select Unmount Datastore .
- In the Unmount Datastore dialog box, select every host that this datastore is attached to and select OK .
- Wait for the datastore to be unmounted from every ESXi host. You can monitor this by selecting Datastore and navigating to Configure → Connectivity and Multipathing . The datastore mount status for every host can be seen in the Datastore Mounted column.
- After Datastore is unmounted from every ESXi host, right-click on the datastore object and select Delete Datastore .

Proceed instructions : Proceed with manual configuration[Task 4: Add the new VMFS Datastore to Oracle Cloud VMware Solution Cluster](https://docs.oracle.com/en/learn/integrate-oci-block-volumes-ocvs/#task-4-add-the-new-vmfs-datastore-to-oracle-cloud-vmware-solution-cluster)section.
4. Create Datastore Cluster in vCenter

Creates datastore cluster in vCenter. This step is run only if a new datastore cluster creation was selected.

What can go wrong :
- You have no permissions to call vSphere API.
- Networking/Hardware issues during step execution.

Step rollback :
- Connect to the VMware vCenter server.
- Navigate to the Storage tab in the VMware vCenter Server and find the datastore cluster that you want to delete.
- Ensure that the datastore cluster doesn't have any datastore objects within it. If it has, move the datastore objects from the datastore cluster to the datacenter object by dragging the datastore objects from datastore cluster object to the datacenter object. You can also right-click on the datastore and select Move To... .
- Right-click on the datastore and select Delete .

Proceed instructions : These instructions are for the datastore cluster creation and configuration as vCenter UI presents the datastore cluster creation wizard with datastore cluster configuration.
- Connect to VMware vCenter server.
- Navigate to the Storage tab in the VMware vCenter Server and find the datacenter object that you want to create within the datastore cluster.
- Right-click on the datacenter object and select Storage → New Datastore Cluster .
- 

The New Datastore Cluster dialog box opens where the datastore cluster configuration begins:

- In the Name and Location section, enter the datastore cluster name in the Datastore cluster name field. Select "VMFS" in the Datastore type field and ensure Turn ON Storage DRS is enabled. Select Next .
- In Storage DRS Automation section, select "Fully Automated" for Cluster automation level field and select "Use cluster settings" for every other field. Select Next .
- In the Storage DRS Runtime Settings section ensure, that Enable I/O metric for SDRS recommendations is enabled. Set I/O latency threshold to 15 ms. Select "Utilized space" for the Space threshold field and set value to "80%." Select Next .
- In the Select Clusters and Hosts step, select the ESXi host clusters or ESXi hosts you want to create this datastore cluster for and select Next .
- In the Select Datastores step, select the datastores you want this cluster to contain and select Next .
- Select Finish .

After you select Finish , the datastore cluster is created, configured and the selected datastores) are automatically moved into datastore cluster you created.
5. Configure vCenter Datastore Cluster

Configures Datastore Cluster with default options in vCenter. This step is executed only if new Datastore Cluster creation was selected.

What can go wrong:
- You have no permissions to call vSphere API.
- Networking/Hardware issues during step execution.

Step rollback :

No action is required.

Proceed instructions :

No action is required. The datastore cluster configuration is done while creating the new datastore cluster. See the Proceed instructions step no. 4 in the Create Datastore Cluster in vCenter step. You can reconfigure the datastore cluster by selecting the datastore cluster and navigating to the Configure tab.
6. Move datastore to Datastore Cluster

Moves the created datastore to the datastore cluster.

What can go wrong :
- You have no permissions to call vSphere API.
- Networking/Hardware issues during step execution.

Step rollback :
- Connect to VMware vCenter server.
- Navigate to the Storage tab in the VMware vCenter Server and find the datastore object that you want to move to the datastore cluster.
- Drag the datastore object to the datastore cluster object. You can also right-click on the datastore object and selecting Move To... .

Proceed instructions :

No action is required. If the datastore cluster was created manually, there is nothing to do as datastore is automatically moved to the datastore cluster.
