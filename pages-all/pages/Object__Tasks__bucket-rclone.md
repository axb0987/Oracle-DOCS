# Mounting an Object Storage Bucket as a File System in Windows using RCLONE
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/bucket-rclone.htm
- Fetched: 2026-09-05 02:50 CDT

# Mounting an Object Storage Bucket as a File System in Windows using RCLONE

Learn how to mount an Object Storage bucket to a Windows instance as a file system using RCLONE.

Follow the steps in this topic to mount an Object Storage bucket as a file system in a Windows instance using RCLONE.

For more information, see[RCLONE](https://rclone.org/).

## Step 1: Generate Secret Keys

In this section, you generate a new secret key. Then you access the Customer secret keys page to copy the access key that was generated simultaneously with your secret key. Both of these keys are needed later in the RCLONE configuration.

- Select the Profile icon in the upper right of the Console, then select User Settings .
- From the My profile page under Identity &amp; Security , select the Tokens and keys tab.
- Scroll to the Customer secret keys section and select the Generate secret key button.
- In the Generate secret key panel that opens, enter a descriptive name for the key and select the Generate secret key button on the lower right of the panel.
The generated secret key is displayed. Copy the key and store it in a secure and accessible location. After you close the dialog box, you can't access the secret key any more.
- Find your secret key in the Customer secret keys list and copy the Access key value.
For more information, see[Working with Customer Secret Keys](https://docs.oracle.com/iaas/Content/Identity/access/managing-user-credentials.htm#Working2).

## Step 2: Confirm the Object Storage Namespace

- Select the Profile icon in the upper right of the Console, then select Tenancy: &lt;your_tenancy&gt; .
The tenancy's details page opens.
- Find and record the Object storage namespace value.

## Step 3: Install RCLONE

- Run PowerShell as an administrator and enter the following commands to install and configure RCLONE:

```

```

- Enter the following command to run the RCLONE installer:

```

```

The RCLONE installation menu opens.
- Select`n) New remote`from the list of RCLONE options.
Enter the following information for each prompt and press Enter. The screen prompts are in bold .
```

```

- Enter the following commands at the prompt to install the required tools:

```

```

- Run the following command to test the connection:

```

```

- Run the following command to map Object Storage as a network drive:

```

```

To unmount, run the following command:`CTRL+C`.

### Step 4: Install RCLONE as a Service

To keep the drive mapped and persistent as a network drive even after you restart the server, perform the following steps:

- If RCLONE is still running, enter`Ctrl + C`to close it.
- Enter the following commands at the prompt to install and run RCLONE as a service. You must provide an administrator username and password for the Windows OS where the drive is being mapped.

```

```
