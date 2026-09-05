# Getting the Configuration File Snippet for an API Signing Key
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/access/to_get_the_config_file_snippet_for_an_API_signing_key.htm
- Fetched: 2026-09-05 02:16 CDT

# Getting the Configuration File Snippet for an API Signing Key

Find the configuration file snipped for an API signing key from the Console.

The following procedure works for a regular user or an administrator.
- View the user's details:
- If you're getting an API key configuration file snippet for yourself :

In the navigation menu , select the Profile menu and then select User settings .
- If you're an administrator getting an API key configuration file snippet for another user : Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains . Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select Users . Locate the user in the list, and then click the user's name to view the details.
- Under Resources , click API keys . The list of API key fingerprints is displayed.
- Click the the Actions menu (three dots) for the fingerprint, and select View configuration file .

The Configuration file preview is displayed. The file snippet includes required parameters and values you'll need to create your configuration file. Copy and paste the configuration file snippet from the text box into your`~/.oci/config file`. (If you have not yet created this file, see[SDK and CLI Configuration File](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm)for details on how to create one.) After you paste the file contents, you'll need to update the`key_file`parameter to the location where you saved your private key file.
If your configuration file already has a DEFAULT profile, you'll need to do one of the following:
- Replace the existing profile and its contents.
- Rename the existing profile.
-
