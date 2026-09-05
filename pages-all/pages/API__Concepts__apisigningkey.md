# Required Keys and OCIDs
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm
- Fetched: 2026-09-05 01:35 CDT

# Required Keys and OCIDs

Whether you're using an Oracle client (see[Software Development Kits and Command Line Interface](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm)) or a client you built yourself, you need to do the following:
- Create a user in IAM for the person or system who will be calling the API, and put that user in at least one IAM group with any required permissions. See[Adding Users](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingusers.htm). You can skip this if the user exists already.
- 

Get these items:
- RSA key pair in PEM format (minimum 2048 bits). See[How to Generate an API Signing Key](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#two).
- Fingerprint of the public key. See[How to Get the Key's Fingerprint](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#four).
- Tenancy's OCID and user's OCID. See[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#five).
- Upload the public key from the key pair in the Console. See[How to Upload the Public Key](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#three).
Note  
  
We recommend adding a tag to each private key.
- If you're using one of the Oracle SDKs or tools, supply the required credentials listed above in either a configuration file or a config object in the code. See[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm). If you're instead building your own client, see[Request Signatures](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm).
Important  
  

This key pair is not the SSH key that you use to access compute instances. See[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm).

Both the private key and public key must be in PEM format (not SSH-RSA format). The public key in PEM format looks something like this:
```

```
To increase the security of your API keys, we recommend that you append an extra line with "OCI_API_KEY" at the end of the private key. If you or someone in your organization accidentally commits the private key to a public GitHub repository, OCI will notify you to take corrective actions. The private key in PEM format with the label looks something similar to this:
```

```

## How to Generate an API Signing Key

Note  
  
You can use the Console or command line tools available for Linux, Mac OS or Windows to generate an API signing key.

### Generating an API Signing Key (Console)

You can use the Console to generate the private/public key pair for you. If you already have a key pair, you can choose to upload the public key. When you use the Console to add the key pair, the Console also generates a configuration file preview snippet for you.

The following procedures work for a regular user or an administrator. Administrators can manage API keys for either another user or themselves.

About the Config File Snippet

When you use the Console to add the API signing key pair, a configuration file preview snippet is generated with the following information:
- `user`- the OCID of the user for whom the key pair is being added.
- `fingerprint`- the fingerprint of the key that was just added.
- `tenancy`- your tenancy's OCID.
- `region`- the currently selected region in the Console.
- `key_file`- the path to your downloaded private key file. You must update this value to the path on your file system where you saved the private key file.

If your config file already has a DEFAULT profile, you'll need to do one of the following:
- Replace the existing profile and its contents.
- Rename the existing profile.
- Rename this profile to a different name after pasting it into the config file.

You can copy this snippet into your config file, to help you get started. If you don't already have a config file, see[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm)for details on how to create one. You can also retrieve the config file snippet later for an API signing key whenever you need it. See: To get the config file snippet for an API signing key.

#### To generate an API signing key pair

Prerequisite: Before you generate a key pair, create the`.oci`directory in your home directory to store the credentials. See[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm)for more details.
- View the user's details:
- If you're adding an API key for yourself :

In the navigation menu , select the Profile menu and then select User settings .
- If you're an administrator adding an API key for another user : Open the navigation menu and select Identity &amp; Security . Under Identity , select Users . Locate the user in the list, and then click the user's name to view the details.
- In the Resources section at the bottom left, click API Keys
- Click Add API Key at the top left of the API Keys list. The Add API Key dialog displays.
- 

Click Download Private Key and save the key to your`.oci`directory. In most cases, you do not need to download the public key.

Note : If your browser downloads the private key to a different directory, be sure to move it to your`.oci`directory.
- Click Add .

The key is added and the Configuration File Preview is displayed. The file snippet includes required parameters and values you'll need to create your configuration file. Copy and paste the configuration file snippet from the text box into your`~/.oci/config file`. (If you have not yet created this file, see[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm)for details on how to create one.)

After you paste the file contents, you'll need to update the`key_file`parameter to the location where you saved your private key file.
If your config file already has a DEFAULT profile, you'll need to do one of the following:
- Replace the existing profile and its contents.
- Rename the existing profile.
- Rename this profile to a different name after pasting it into the config file.
- Update the permissions on your downloaded private key file so that only you can view it:
- Go to the`.oci`directory where you placed the private key file.
- Use the command`chmod go-rwx ~/.oci/<oci_api_keyfile>.pem`to set the permissions on the file.

#### To upload or paste an API key

Prerequisite: You have generated a public RSA key in PEM format (minimum 2048 bits) . The PEM format looks something like this:

```

```

- View the user's details:
- If you're adding an API key for yourself :

In the navigation menu , select the Profile menu and then select User settings .
- If you're an administrator adding an API key for another user : Open the navigation menu and select Identity &amp; Security . Under Identity , select Users . Locate the user in the list, and then click the user's name to view the details.
- In the Resources section at the bottom left, click API Keys
- Click Add API Key at the top left of the API Keys list. The Add API Key dialog displays.
- In the dialog, select Choose Public Key File to upload your file, or Paste Public Key , if you prefer to paste it into a text box
- Click Add .

The key is added and the Configuration File Preview is displayed. The file snippet includes required parameters and values you'll need to create your configuration file. Copy and paste the configuration file snippet from the text box into your`~/.oci/config file`. (If you have not yet created this file, see[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm)for details on how to create one.)

After you paste the file contents, you'll need to update the`key_file`parameter to the location where you saved your private key file.

If your config file already has a DEFAULT profile, you'll need to do one of the following:
- Replace the existing profile and its contents.
- Rename the existing profile.
- Rename this profile to a different name after pasting it into the config file.

[To get the config file snippet for an API signing key](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#)

The following procedure works for a regular user or an administrator.
- View the user's details:
- If you're getting an API key config file snippet for yourself :

In the navigation menu , select the Profile menu and then select User settings .
- If you're an administrator getting an API key config file snippet for another user : Open the navigation menu and select Identity &amp; Security . Under Identity , select Users . Locate the user in the list, and then click the user's name to view the details.
- Under the Resources section at the bottom left, click API Keys
- On the left side of the page, click API Keys . The list of API key fingerprints is displayed.
- Click the the Actions menu (three dots) for the fingerprint, and select View configuration file .

The Configuration File Preview is displayed. The file snippet includes required parameters and values you'll need to create your configuration file. Copy and paste the configuration file snippet from the text box into your`~/.oci/config file`. (If you have not yet created this file, see[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm)for details on how to create one.) After you paste the file contents, you'll need to update the`key_file`parameter to the location where you saved your private key file.
If your config file already has a DEFAULT profile, you'll need to do one of the following:
- Replace the existing profile and its contents.
- Rename the existing profile.
- Rename this profile to a different name after pasting it into the config file.

### Generating an API Signing Key (Linux and Mac OS X)

Use the following[OpenSSL](http://www.openssl.org/)commands to generate the key pair in the required PEM format.
- 

If you haven't already, create an`.oci`directory to store the credentials:
```

```

- 

Generate the private key with one of the following commands.
- 
To generate the key, encrypted with a passphrase you provide when prompted:
Note  
  
We recommend that you use a passphrase for your key.

```

```

- 

To generate the key with no passphrase:

```

```

- 

Change the file permission to ensure that only you can read the private key file:

```

```

- 

Generate the public key from your new private key:

```

```

- 

Copy the contents of the public key to the clipboard using pbcopy, xclip or a similar tool (you'll need to paste the value into the Console later). For example:

```

```

Your API requests will be signed with your private key, and Oracle will use the public key to verify the authenticity of the request. You must upload the public key to IAM (instructions below).

### Generating an API Signing Key (Windows)

If you're using Windows, you'll need to install[Git Bash for Windows](https://git-scm.com/download/win)before running the following commands.
Note  
  
Be sure to include the`openssl`binary in your Windows path. On default installations, the openssl.exe file can be found in`C:\Program Files\Git\mingw64\bin`.

Use the following[OpenSSL](http://www.openssl.org/)commands to generate the key pair in the required PEM format.
- 

If you haven't already, create a`.oci`directory to store the credentials. For example:
```

```

- 

Generate the private key with one of the following commands:
- 
To generate the key that is encrypted with a passphrase you provide when prompted:
Note  
  
We recommend that you use a passphrase for your key.

```

```

- 

To generate the key with no passphrase:

```

```

- 

Generate the public key from your new private key:

```

```

- 

Copy the contents of the public key to the clipboard (you'll need to paste the value into the Console later). For example:

```

```

Your API requests will be signed with your private key, and Oracle will use the public key to verify the authenticity of the request. You must upload the public key to IAM (instructions below).

## How to Get the Key's Fingerprint

You can get the key's fingerprint with the following OpenSSL command.

For Linux and Mac OS X:
```

```

For Windows:
Note  
  
If you're using Windows, you need to install[Git Bash for Windows](https://git-scm.com/download/win)and run the command with that tool.
```

```

When you upload the public key in the Console, the fingerprint is also automatically displayed there. It looks something like this: 12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef

## Where to Get the Tenancy's OCID and User's OCID

Both OCIDs are in the Console, which can be accessed by signing in here:[https://cloud.oracle.com](https://cloud.oracle.com). If you don't have a sign-in and password for the Console, contact an administrator. If you're not familiar with OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

### Tenancy's OCID

Get the tenancy OCID from the Oracle Cloud Infrastructure Console on the Tenancy Details page:
- In the navigation bar, select the Profile menu and then select Tenancy: &lt;your_tenancy_name&gt; .
- 

The tenancy OCID is shown under Tenancy Information . Select Copy to copy it to the clipboard.

### User's OCID

Get the user's OCID in the Console on the page showing the user's details. To get to that page:
- If you're signed in as the user:

In the navigation menu , select the Profile menu and then select User settings .
- The user OCID is shown under User Information . Select Copy to copy it to the clipboard.

## How to Upload the Public Key

You can upload the PEM public key in the Console, which can be accessed by signing in here:[https://cloud.oracle.com](https://cloud.oracle.com).
Note  
  
If you don't have a login and password for the Console or aren't seeing a Profile menu, contact an administrator.
- Open the Console, and sign in.
- In the navigation menu , select the Profile menu and then select User settings .
- Select Token and keys .
- Select Add API Key .
- In the Add API Key dialog box, select the Paste a public key radio button.
- Paste the contents of the PEM public key in the dialog box and select Add .

The key's fingerprint is displayed (for example, 12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef).

Notice that after you've uploaded your first public key, you can also use the[UploadApiKey](https://docs.oracle.com/iaas/api/#/en/identity/latest/ApiKey/UploadApiKey)
