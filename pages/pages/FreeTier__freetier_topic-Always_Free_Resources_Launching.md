# Quickly Launch Your Always Free Resources Using Resource Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources_Launching.htm
- Fetched: 2026-09-04 15:37 CDT

# Quickly Launch Your Always Free Resources Using Resource Manager

Learn how to automatically create a full set of Always Free resources in a few minutes using the Resource Manager service's templates feature.

[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)[templates](https://docs.oracle.com/iaas/Content/ResourceManager/Reference/templates.htm)are pre-built Terraform configurations that help you easily create sets of resources used in common scenarios using a single, simple workflow. When you provision your Always Free resources using the provided template, your resources are created with the settings and configuration you need to start creating applications in the cloud. You don't need to have experience with Terraform to use the template.

## To provision your Always Free resources using Terraform and Resource Manager

Tip  
  
Note that Terraform refers to the set of resources being provisioned as a "stack." For a general introduction to Terraform and the "infrastructure-as-code" model, see[Terraform: Write, Plan, and Create Infrastructure as Code](https://www.terraform.io/).

- Log into your Oracle Cloud Infrastructure account.
- On the Stacks list page, select Create stack . If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/list-stacks.htm).
- On the Create stack page, under Choose the origin of the Terraform configuration , select Template .
- Under Stack configuration , select Select template .
- In the Browse templates panel, select the Architecture tab, select Sample e-commerce application (MuShop Basic) , and then select Select template .
The page is populated with information contained in the Terraform configuration.
- (Optional) To use[custom providers](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm), select Use custom providers and then select the bucket that contains the custom provider.
- (Optional) Edit the default stack name and enter a stack description. Avoid entering confidential information.
- Select the compartment that you want to create the stack in.
- (Optional) Under Tags , add one or more tags to the stack.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Next .
- In the Configure variables panel, review the variables listed from the Terraform configuration and change as needed.

Important  
  
Don't add your private key or other confidential information to configuration variables.
- Select Next .
- In the Review panel, verify the stack configuration.
- Select Create .

Your set of Always Free resources takes no more than a few minutes to provision.
