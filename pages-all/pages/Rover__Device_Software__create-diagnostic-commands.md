# Creating a Diagnostic Command for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/create-diagnostic-commands.htm
- Fetched: 2026-09-05 02:58 CDT

# Creating a Diagnostic Command for a Roving Edge Infrastructure Device

Describes how to create a diagnostic command for a Roving Edge Infrastructure device.

Begin by recording the OCID of the attached VNIC. After you record that OCID, you can continue on to create the diagnostic command.

## Using the Device Console

- Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- Select the instance that has the attached VNIC whose OCID you want to get. The instance's Details page appears.
- Select Attached VNICs under Resources . The Attached VNICs page appears. All attached VNICs are listed in tabular form. The primary VNIC is indicated by the Primary VNIC label next to it.
- Select the attached primary VNIC whose OCID you want to get. The VNIC's Details page appears.
- The VNIC's OCID appears under VNIC Information . Select Copy to copy the OCID and subsequently paste it in the VNIC OCID box in the Create Diagnostic Command dialog box.
- Open the navigation menu and select Node Management &gt; Diagnostic Commands . The Diagnostic Commands page appears. All diagnostic commands are listed in tabular form.
- Select Create Command . The Create Diagnostic Command dialog box appears.
- Enter a Name for the diagnostic command.
- Select the Command Type from the list.

Note  
  

Currently, only VNIC Packet Capture is available as a command type.
- Enter the VNIC OCID .
- Select the Packet Length in bytes from the list.
- Select the Capture Duration in seconds from the list.
- Select Create Command .
