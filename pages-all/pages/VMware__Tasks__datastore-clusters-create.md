# Creating a VMware Solution Datastore Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/datastore-clusters-create.htm
- Fetched: 2026-09-05 03:08 CDT

# Creating a VMware Solution Datastore Cluster

Create a VMware Solution datastore cluster.

## Using the Console

- Open the navigation menu and select Hybrid . Under VMware Solution , select Datastore clusters .
The Datastores clusters list opens. All datastore clusters are displayed in a table.
- Select Create datastore cluster .
The Create workload datastore cluster panel opens.

### 1. Basic information

Enter the following information:
- Name : Enter a friendly name for the datastore cluster. Avoid entering confidential information.
- Create in compartment : Select the compartment that you want to store the datastore cluster in.
- Availability domain : Select the isolated, fault-tolerant Oracle data center that hosts cloud resources such as instances, volumes, and subnets.

### 2. Datastores

Enter the following information:
- Add existing datastores : Select this option to add one or more datastores to the datastore cluster. In the selected compartment, select up to 32 datastores from the list of existing datastores that's displayed, and then select Add datastores .
- Create datastore : Select this option to create a datastore for the datastore cluster. For option descriptions, see[Creating a VMware Solution Datastore](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/datastore-create.htm)

### Tagging

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
