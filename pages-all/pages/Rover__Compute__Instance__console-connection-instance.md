# Connecting to the Console of an Instance for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/console-connection-instance.htm
- Fetched: 2026-09-05 02:58 CDT

# Connecting to the Console of an Instance for a Roving Edge Infrastructure Device

Describes how to connect to the serial or VNC console of an instance for a Roving Edge Infrastructure device using the console connection you create.

## Using the Device Console

- Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- (optional) Select a State from the list to limit the instances displayed to that state.
- Select the instance for which you want to create the console connection. The instance's Details page appears.
- Select Console Connection under Resources . The Console Connection page appears. All console connections are listed in tabular form.
- Select the Actions menu ( ) to the right of the console connection entry you want to connect to an instance and select one of the following options:

- 

Copy Serial Console Connection for Linux/Mac
- 

Copy Serial Console Connection for Windows
- 

Copy VNC Connection for Linux/Mac
- 

Copy VNC Connection for Windows

The connection information you select is copied to your clipboard. The connection string resembles the following:
```

```

where`@ x.x.x.x`is the Roving Edge Infrastructure device's IP/resolvable domain name. Use this for troubleshooting.

If you have not setup your local SSH config to provide the required private key, modify the string to provide the key:
```

```

On newer versions of the SSH Client on Macintosh computers, you may have to explicitly enable RSA SSH keys. In ~/.ssh/config add:
```

```

- Open a command prompt window and paste the clipboard contents into it. Press Enter . When you first connect to the serial console, you are prompted to validate the fingerprint of the server host key. The fingerprint of the server host key is the SHA256 hash of the server host's public SSH key. The server SSH handshake response is signed with the associated private key. Validating the server host key's fingerprint protects against potential attacks.

If the pasting and entering of the clipboard contents is successful, the following banner appears in the command prompt window.
```

```
