# Creating a Stack from a Resource Creation Page
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm
- Fetched: 2026-09-05 02:55 CDT

# Creating a Stack from a Resource Creation Page

Populate a resource creation page in another OCI service in the Console and then use the Save as stack button to create a stack in Resource Manager.

For example, create a stack from the Create compute instance page. Use the new stack to install, configure, and manage your compute instance through the "infrastructure-as-code" model.
Note  
  
Some resources don't yet have the Save as stack button.

- Open the resource creation page that you want to use for a new stack.

For example, open the Create compute instance page:
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select Create instance .
Note  
  
If creating a stack from the resource creation page for a compute instance, then ensure that you review requirements for instances. See[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
- Populate configuration fields to specify stack details.
For example, select the image you want to use in a stack for creating instances.
- Select Save as stack .

Depending on resource type, one of the following opens:
- Save as stack panel (for Kubernetes clusters and other resources)
- Create stack page (for compute instances and VCNs)
- (Optional) Edit the default stack name and enter a stack description. Avoid entering confidential information.
- Select the compartment that you want to store the stack in.
- (Optional) Under Tags , add one or more tags to the stack.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Save the stack: Perform one of the following actions:
- Save as stack panel: Select Save .
- Create stack dialog box: Select Next twice and then select Create .

The result depends on the panel or page. For Save as stack , the Open stack link appears. For Create stack , the Stack details page opens.
- To view a stack created from the Save as stack panel, perform one of the following actions:
- Select Open stack .
- On the Stacks list page, select the new stack. The newest stack is at the top of the list. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm)
