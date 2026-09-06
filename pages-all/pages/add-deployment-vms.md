# Add Docker Deployment VMs
- Source: https://docs.oracle.com/iaas/visual-builder-studio/doc/add-deployment-vms.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/visual-builder-studio/doc/add-deployment-vms.html#dcoc-content-body)

# Add Docker Deployment VMs

When you add a Docker deployment VM, you allocate an OCI VM Compute instance to run your builds in Docker executors.
- From the VM Pool tab, click + Add VMs .
- Add details to the Creating Docker Executors dialog:
- Number of VMs : Specify the number of Docker deployment VMs you want to create.
- Executors created per VM : Enter the maximum number of Docker executors you want to deploy in each Docker deployment VM.

- Region : Select the same region that you chose for the Management VM in Step 5c of[Add Your First Docker Deployment VM](https://docs.oracle.com/iaas/visual-builder-studio/doc/add-your-first-docker-deployment-vm.html#GUID-9B2A578C-4993-4122-B2F2-DCEAD5CEC28E).
The drop-down list displays regions your OCI account is subscribed to.
- Shape : Select the Docker executor's shape.
Wait for a few seconds. VB Studio calculates the number of Compute VM instances that can be created with the selected shape and displays it in the dialog box. If the required number of Compute VM instances aren't available, choose another shape.
- Volume : Specify the storage capacity for each Docker deployment VM.
- Number of OCPUs : If you've selected a Flex shape, specify the number of OCPUs to add in each Docker deployment VM.
- Amount of Memory : If you've selected a Flex shape, specify each Docker deployment VM's memory.
- Use only for projects : (Optional) Select one or more projects to assign to this Docker deployment VM. After the Docker deployment VM is created, it will be restricted to running builds for the assigned projects. Builds for these projects will only run on this VM, and builds from other projects won't run on this VM.
- Use only for images : (Optional) Select one or more images to assign to this Docker deployment VM. After the Docker deployment VM is created, it will be restricted to running builds using the assigned images.
- Reserved Public IP : (Optional) Select a Reserved Public IP to assign to this Docker deployment VM. The Reserved Public IP must be defined in the compartment of the specified OCI account. After the Docker deployment VM is created, the specified Reserved Public IP will always be assigned and used by the Docker deployment VM.
- For VCN Select , choose Default or Custom .
- If you chose Default , click Create . You are finished with this task.
- If you chose Custom , continue to the next step.
- Fill out the additional details for the custom VCN:
- VCN Compartment : Select the compartment.
If you're an Oracle Cloud OS Management Service (OSMS) user, don't select the OSMS compartment or a compartment with an OSMS policy.
- VCN : Select the VCN.
- Subnets Compartments : Select the compartments where your public subnets are. By default, it adds your VCN's compartment. If required, you can add more compartments.
- Subnets : Select a subnet. The list shows public subnets only.
You can add multiple public subnets. If VB Studio can't create a Docker executor on the first subnet you've added, it tries to create it on the second subnet, and so on.
- Click Validate Network Setup .
- Click Create .

Note  
  
After the Docker deployment VM is created, it is listed on the VM Pool tab of the Build Executors page. Restrictions for both projects and images are indicated with a Lock icon in the Restricted column. Click the Lock icon to display details about the assigned Docker deployment VM restrictions.

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
