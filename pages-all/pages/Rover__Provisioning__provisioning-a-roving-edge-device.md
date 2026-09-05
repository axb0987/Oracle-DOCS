# Self-Provision the Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm
- Fetched: 2026-09-05 03:02 CDT

# Self-Provision the Device

The latest Roving Edge devices and Roving Edge Ultras ship from the factory to eligible realms with only a small installer OS. To enhance security and flexibility in assigning devices to different projects, the installer OS enables you to self-provision the device at your location instead of Oracle provisioning the device. As part of the installation process, you self-provision the device. Self-provisioning involves configuring device network settings, connecting to your OCI tenancy, setting up device credentials, and installing the full Roving Edge software.

To self-provision a device, perform the following tasks:
- [Determine If the Device Needs to be Self-Provisioned](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__determine-provisioning)
- [Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__self-provisioning-prerequisites)
- [Prepare to Self-Provision the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__gather-information)
- [Configure Device Networking](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__device-networking)
- [Set Up Connectivity to OCI](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__oci-connectivity)
- [Set Up Credentials](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__set-up-credentials)
- [Download and Install Software](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__install-software)

If you encounter problems, see[Troubleshooting: Self-Provisioning](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../troubleshooting.htm#troubleshooting-device-provisioning)

## Determine If the Device Needs to be Self-Provisioned

Some devices are provisioned at the factory by Oracle and other devices are self-provisioned on-site by you.

Look at the serial console main menu.
- 

If you see the following menu heading, follow the instructions in this section to self-provision the device. See[Prepare to Self-Provision the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__gather-information),
```

```

- 

If you see the following menu heading, the device was provisioned at a secure Oracle facility. Go to[Configure Network Parameters for a Factory Provisioned Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../Setup-RED/finish-the-set-up-for-preprovisioned-devices.htm#finish-the-set-up-for-preprovisioned-devices).
```

```

## Prerequisites

The following tasks must be completed before you can self-provision the device:
- [You've created a dynamic group and a required policy for self-provisioning.](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../Getting_Started/setting_policies.htm#allowing-roving-edge-infrastructure-devices-to-be-provisioned)
- [The device has network connectivity to the OCI region for this device.](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../Setup-RED/cable-device.htm#install-the-device)
- [A controlling host, such as a laptop, is connected to the serial port.](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../Setup-RED/cable-device.htm#install-the-device)
- [The controlling host has a terminal emulator.](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../Setup-RED/setting-up-terminal-emulation.htm#setting-up-terminal-emulation)
- 

The OCI CLI is installed on the controlling host. See[Working with the CLI, Quickstart](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm)to install the CLI based on the host OS.
- [The device is powered on.](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../Setup-RED/power-on-device.htm#unlock-the-device)

## Prepare to Self-Provision the Device
- 

Have your device Activation code . The code is a unique character string. Oracle provides you with the activation code when you request a device. If you don't have it, check with the person who requested the device. Example activation code:
```

```

- 

Sign in to the OCI tenancy where the new device node was created, and get the following information:
- 

Node OCID – Copy the OCID for the node associated with this device:

While signed in to the tenancy, in the navigation menu, select Hybrid , then select Nodes . Select the node that was created for this device. Select the OCID copy button. Paste the OCID where you can retrieve it later.

Example: ocid1.rovernode. &lt;realm&gt; . &lt;region&gt; . &lt;unique-id&gt;
- 

While signed in to your tenancy, perform the following steps to create an OCI Vault secret so that you can back up the recovery key:
- 

Create or select an existing vault. (For details, see[Creating a Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm).):
- In the navigation menu , select Identity &amp; Security , and then select Vault .
- 

Select an existing vault or create a new vault with the following parameters
- Name : Example,`REDBackup`
- Assign the vault as`default`or`Virtual Private`.
- 

On the Master Encryption Keys list page for the vault you're using, select Create Key . This key is used to encrypt secrets in the next step. Specify the following parameters. (For details, see[Creating a Master Encryption Key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm).):
- You can select either options for Protection Mode .
- Name : Example,`REDBackupMasterKey`
- Key Shape: Algorithm : you must select`AES`. The other two algorithms,`RSA`and`ECDSA`, can't be used as encryption key for secret.
- Key Shape: Length you can select any of the options provided.
- 
On the Secrets list page, select Create Secret . Specify the following parameters. (For details, see[Creating a Secret.)](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets_topic-To_create_a_new_secret.htm)
- 

Name : Example, &lt;device-node-name&gt;`-recovery-key`.

We recommend using a meaningful and unique name, such as`<device-node-name> -recovery-key`. This is especially helpful for identifying the correct key when you have multiple devices.
- Method: Select Manual secret generation .
- Select Secret Type Template as Plain-Text and in Secret Contents enter`RED_RECOVERY_KEY`. This initial content helps prevent unexpected secret overwriting.
- Secret rotation : Leave this section blank.
- 

Copy the Secret OCID for later use.
Note  
  
If a device is reprovisioned, its recovery key is updated. We recommend storing each recovery key in a separate secret, distinct from previous keys, or those used by other devices.
Important  
  
Ensure that the device’s active recovery key is properly secured to prevent unauthorized access.
- 

Establish a temporary OCI CLI session in the terminal emulator on your controlling host:

For more information, see[Token-based Authentication for the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/clitoken.htm).
Note  
  

The session expires after 24 hours. If self-provisioning takes longer than that, you must establish a new session.
- 

Generate a session token by creating a temporary session that's used to authenticate with OCI during self-provisioning:

```

```

- 

Display the configuration file that was created for the temporary session.

You refer to this output in a subsequent task called[Set Up Connectivity to OCI](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__oci-connectivity). Example:
```

```

What's Next?

[Configure Device Networking](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__device-networking)

## Configure Device Networking

This task configures the device network settings to enable access to the public network.

When working with the serial console menus, enter the menu number for the menu option.
- 

From the local computer that's displaying the serial console Basic Configuration Interface menu, select Configure Networking .
- 

Use the menu options to configure the device network parameters according to your network environment. Configure these parameters:
- 

IP address: Enter an IP address using one of the these formats:

A.B.C.D/P or A.B.C.D/M (P - prefix length or M - netmask). Example:`203.0.113.2/24`
- 

Gateway: Enter the gateway IP address. Example:`203.0.113.1`
- 

DNS servers: Enter DNS servers IP addresses, as A.B.C.D, separated by comma. Example:`216.146.35.35, 216.146.36.36`
- 

(Optional, but recommended) NTP servers: Enter NTP server IP addresses separated by a comma. Example:`203.0.113.15, 203.0.113.16, 203.0.113.17`
- 

(Don't use) Proxy URL: Don't specify a proxy URL. See[The Roving Edge installer proxy URL isn't working](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../known-issues.htm#roving-edge-installer-proxy-url-not-working).
- Select Test network connectivity to OCI . The device makes an HTTP call to oracle.com to verify public network access and name resolution.
- 

Select Check OCI server clock and device clock . The device fetches the OCI server clock and compares it with the device clock.

Authentication fails if the client's clock is skewed more than 5 minutes from the server's clock. For more information, see[Maximum Allowed Client Clock Skew](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#clock). If the device clock is skewed more than 5 minutes from the server clock, reenter the NTP servers to update and sync the time. Then run the clock check again.

What's Next?

[Set Up Connectivity to OCI](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__oci-connectivity)

## Set Up Connectivity to OCI

This task registers the device with OCI. Registration links the device with the corresponding device order in the OCI Cloud Console.
- In the serial console, type Ctrl+C to return to the Basic Configuration Interface (main menu).
- Select Set Up OCI Connectivity .
- Select Region : Enter the region listed in the`config`file output. Examples: us-ashburn-1, uk-london-1, us-phoenix-1
- Select Node OCID : Enter the OCID from[Prepare to Self-Provision the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__gather-information), Step[2](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__prepare-get-ocid).
- 

Select Secret OCID (if available): Perform one of the following actions:
- (Recommended) Enter the Secret OCID from[Prepare to Self-Provision the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__gather-information). If you get an error, see[During self-provisioning, you get a RED_RECOVERY_KEY error](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../troubleshooting.htm#troubleshooting-device-provisioning__recovery-key-error).
- (Discouraged) Leave the secret OCID blank. You must manually keep the Recovery Key secure using OCI KMS or by using a similar Cloud KMS. See[Using Your Own Master Key with Roving Edge Infrastructure Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../Getting_Started/user_master_key.htm#UserMasterKey). If you forget the unlock passphrase and the recovery key, Oracle can't help you recover the device, and the device must be replaced.
- 

Select Session token : Enter the contents of the`security_token_file`that's listed in the`config`file output.

Only select the session token output. Omit any`%`symbols and any characters after the`%`symbol. In the following example,`% user1 OC1_CUSTOMER`$ isn't copied and entered.
```

```

- 

Select Session private key : Enter the contents of the`key_file`that's listed in the`config`file output.

Only copy the lines starting with`BEGIN PRIVATE KEY`and ending with`END PRIVATE KEY`. Omit any other characters. In the following example,`OCI_API_KEY% user1 OC1_CUSTOMER $`$ isn't copied and entered.
```

```

After you paste the key, press Return twice to exit input mode.
- Select Activation code : Enter the activation code that was provided to you by the sales representative.
- 

Select Register device to OCI .

The device serial number is registered to the OCI node in your tenancy, Complete Device Registration runs automatically, and the following output is displayed:
```

```

If this step fails, try it again by running Complete Device Registration .
- (Optional) Verify that the serial number registered with the node in your tenancy matches the serial number on the device. For Roving Edge 2 devices, see[Roving Edge Device 2 – Front Panel](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../Setup-RED/rear_panel_identification.htm#rear_panel_identification__red2-front-panel).

What's Next?

[Set Up Credentials](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__set-up-credentials)

## Set Up Credentials

This task creates a passphrase, password, and recovery key. Descriptions of each credential are provided in the following steps.
Important  
  

You must store the device unlock passphrase, password, and recovery key in a secure place such as OCI Vault or somewhere equivalent. If you forget the unlock passphrase and are unable to find the recovery key, Oracle can't help you recover the device, and the device must be replaced.
- In the serial console, type Ctrl+C to return to the Basic Configuration Interface (main menu).
- 

Select Set Up Credentials .
- 

Select Device Unlock Passphrase , then enter a passphrase.

After the device is self-provisioned, the master key passphrase is used to unlock the device. Until the device is unlocked, the device has limited functionality.

The first time you use this passphrase to unlock the device, you're prompted to change the passphrase.

Passphrase requirements:
- 

Minimum Length: 8 characters
- 

Maximum Length: 64 characters
- 

Must Include the following characters:
- One lowercase character
- One uppercase character
- One digit
- One special char from this list:
```

```

If you need to manage this password in the future, see[Changing the Passphrase](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../Getting_Started/changing-the-passphrase.htm#changing-the-passphrase).
- 

Select Web Console UI Password (root user) , then enter a password.

The password is used to access the Roving Edge Web UI Console which is used to manage resources on the device.

The first time you use this password to access the Roving Edge Web UI Console, you're prompted to change the password.

If you need to manage this account and password in the future, see[User Credentials for Roving Edge Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../IAM/User_Credentials/user_credential_management.htm#UserManagement).
- 

Select Recovery Key .
- 

If the recovery key is successfully backed up, the secret OCID is shown.

To view the Recovery Key, see[Getting a Secret's Contents](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/concepts_concepts_concepts_secretrules_view_secret_content.htm)and enable the Show decoded Based64 digit option.
- 

If you left the secret OCID blank in Set Up Connectivity to OCI , Step[5](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__connectivity-secret-ocid), you must manually keep the Recovery Key secure using OCI KMS or by using a similar Cloud KMS. Save the key in a secure location now.

See[Using Your Own Master Key with Roving Edge Infrastructure Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../Getting_Started/user_master_key.htm#UserMasterKey).
Note  
  

The recovery key might be needed later if you forget the master key passphrase, or if the master key is shredded because of multiple failed sign-in attempts.
- 

After the key is saved, press Return.
- 

Choose to either hide or unhide the credentials by selecting the appropriate menu option.

What's Next?

[Download and Install Software](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__install-software)

## Download and Install Software

The device is shipped with a small installer OS. In this task, you download and install the complete Roving Edge software.

The software file size is about 25 GB. We recommend that you use a high-speed network for this task.
Important  
  
Don't interrupt the download or installation processes.
- In the serial console, type Ctrl+C to return to the Basic Configuration Interface (main menu).
- 

Select Download installation files .

Wait for the download to complete.
- 

Select Start installation .

The installation completes within 10 minutes, then the device reboots. The reboot can take another 10 minutes. When the reboot is finished, the following Roving Edge Device menu is displayed.
```

```

All future access to the serial console requires the device unlock passphrase.

If the installation fails, the interface displays a BASE64 encoded string which contains a compressed archived with the logs. For example:
```

```

Copy and save the BASE64 output (text in between === lines) to a file. Then send the file to Oracle Support. See[Collecting Self-Provisioning Logs](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../troubleshooting.htm#troubleshooting-device-provisioning__collecting-logs). You can also restart the installation.

What's Next?

[Unlock the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/../Setup-RED/unlock-the-device.htm#unlock-the-device)
