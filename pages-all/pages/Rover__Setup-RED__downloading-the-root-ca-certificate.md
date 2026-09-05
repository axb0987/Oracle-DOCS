# Download the Root CA Certificate
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/downloading-the-root-ca-certificate.htm
- Fetched: 2026-09-05 03:02 CDT

# Download the Root CA Certificate

To access the Device Console, the computer (host) that you use to access the Device Console must have the root CA certificate from the Roving Edge Device. The root CA certificate is the top most certificate in the certificate chain of trust and is used by the computer to verify the authenticity of the Device Console.

Perform the tasks in this section to download the root CA certificate and sign in to the device UI for the first time.

## Prerequisites

To perform the tasks in this section, you need the following Roving Edge device items:
- IP address
- hostname
- Username
- Password

## Ensure The Host Has OpenSSL Installed

Most Linux and MacOS computers have OpenSSL installed. For Microsoft Windows, you might need to install OpenSSL.

To decide if OpenSSL is installed on Microsoft Windows, search for openssl. If OpenSSL isn't installed, follow the organization's best practices for installing OpenSSL.

The following links take you to popular OpenSSL sites from which OpenSSL can be obtained:
- [https://wiki.openssl.org/index.php/Binaries](https://wiki.openssl.org/index.php/Binaries)
- [https://github.com/curl/curl-for-win](https://github.com/curl/curl-for-win)
- [https://curl.se/windows/](https://curl.se/windows/)

## Task 1 - Configure the hosts File

Adding the device IP address and hostname to the hosts file the computer to find the Device Console IP address regardless of the DNS configuration.

Use one of the following procedures based on the OS. Linux
- 

In a text editor, open the`/etc/hosts`file. The following example uses the vim editor:
```

```

- 

Enter the administrator password.
- 

Open a new line and enter the device IP address and hostname. Example:
```

```

- 

Save the`/etc/hosts`file. MacOS
- 

Open a terminal:

Navigate to Finder &gt; Utilities , then select Terminal .
- 

Open the`/etc/hosts`file in a text editor. The following example uses the nano editor:
```

```

- 

Enter the administrator password.
- 

Create a new line and enter the device IP address and hostname. Example:
```

```

- 

Save the`/etc/hosts`file. Microsoft Windows
- 

Open Notepad as the administrator.
- 

In Notepad, open the following file:
```

```

- 

Open a new line and enter the device IP address and hostname. Example:
```

```

- 

Save the`hosts`file.

## Task 2 - Download the Root Certificate File from the Device

Use one of the following procedures based on the computer OS.

If the computer runs Microsoft Windows, also select the procedure based on the browser type. Linux and MacOS
- 

In a terminal window, use the following command to download the certificate from the Roving Edge device:

```

```

The root certificate`redroot.pem`is downloaded to the home directory. Microsoft Windows with Firefox The following steps are for Firefox version 115.
Note  
  

Browsers evolve over time. If some browser steps don't match what you see in the browser, consult the browser documentation.
- 

In the browser address field, enter the device address and port number:
```

```

If a security risk warning is displayed, accept the risk, and ignore the warning:`Roving Edge Device is currently unavailable`.
- 

Click the padlock symbol that's to the upper left of the browser address bar.
- 

In the Site Information dialog box, select Connection Secure , then select More information .

The Firefox Security menu is displayed.
- 

Select View Certificate .

The Device Console now displays certificate information.
- 

Select the tab called &lt;hostname&gt; -root-CA .
- 

Scroll down to the Miscellaneous section.
- 

Select the PEM (Cert) link, and save the file somewhere convenient such as the Downloads folder. Microsoft Windows with Edge The following steps are for Microsoft Edge version 128.0.2739.67.
Note  
  

Browsers evolve over time. If some browser steps don't match what you see in the browser, consult the browser documentation.
- 

In the browser address field, enter the device address and port number:
```

```

- 

Select the secure icon next to the URL.
- 

Select Certificate or Manage Certificate .
- 

Select Details .
- 

Select Export .
- 

Browse to a convenient download location such as Downloads.
- 

Select Save .

The root certificate file is saved with a`.crt`extension. Microsoft Windows with Chrome The following steps are for Google Chrome version 135.0.7049.42.
Note  
  

Browsers evolve over time. If some browser steps don't match what you see in the browser, consult the browser documentation.
- 

In the browser address field, enter the device address and port number:
```

```

The sign-in page reports that the device is unavailable because the connection is insecure until the certificate is imported.
- 

Select the Not secure icon next to the URL field.
- 

Select Certificate details .
- 

Select the Details tab.
- Under Certificate Hierarchy , select the top certificate.
- 

Select Export .
- Browse to a convenient download location such as Downloads.
- 

Select Save .
- Close the Certificate Viewer.

## Task 3 - Import the Root Certificate into The Browser

Import the downloaded root certificate into the browser using one of the following tasks based on the browser type. Firefox
Note  
  

Browsers evolve over time. If some browser steps don't match what you see in the browser, consult the browser documentation.
- 

In Firefox, use the navigation menu to open Settings .
- 

In the Find in Settings field, enter certificates .
- 

Select View Certificates .

The Certificate manager is displayed.
- 

With the Authorities tab selected, select Import .

Browse to the location of the downloaded certificate file, select it, then select Open .
- 

In the Certificate Manager, select Trust this CA to identify websites , then select OK .
- 

In the Certificate Manager, select OK .
- 

Refresh the browser tab that's connected to the device.

You're prompted to enter the username and password. Edge
Note  
  

Browsers evolve over time. If some browser steps don't match what you see in the browser, consult the browser documentation.
- 

In Edge, use the navigation menu to open Settings .
- 

In the Find in Settings field, enter certificates .
- 

Select Manage certificates .

The Certificate manager is displayed.
- 

In the Certificates dialog box, select Import .
- In the Import Wizard , select Next .
- Select Browse , and navigate to the location of the downloaded certificate file.
- 

In the file type menu, select All Files .
- 

Select the downloaded certificate file, and select Open .
- 

Select Next .
- 

Select Automatically select the certificate store based on the type of certificate .
- 

Select Next .
- 

Select Finish .
- 

Select OK .
- 

In the Certificate manager , select Close .

Now you can sign in to the Device Console.
- 

Refresh the browser tab that's connected to the device.

You're prompted to enter the username and password. Chrome
Note  
  

Browsers evolve over time. If some browser steps don't match what you see in the browser, consult the browser documentation.
- 

In Chrome, use the navigation menu to open Settings .
- Select Privacy and security .
- 

Select Security .
- 

Select Manage certificates .
- 

Select Manage imported certificates .

The Certificate Manager is displayed.
- 

Select the Trusted Root Certificates tab.
- 

Select Import .

The Certificate Wizard is displayed.
- 

Select Next .
- 

Select Browse , and browse to the location of the downloaded certificate file, select it, then select Open , then select Next .
- 

Select Place all certificates in the following store , then select Next .
- 

Select Finish .
- 

Select OK to acknowledge the import was successful.
- 

Close the Certificate Wizard .
- 

Refresh the browser tab that's connected to the device.

You're prompted to enter the username and password.

The Roving Edge device is installed and ready for use.

Consider your next action:
- 

Learn about ways to access the device. See[Accessing Roving Edge](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../Access/access.htm#access).
- Start creating Roving Edge Infrastructure resources. See[Networking for Roving Edge Infrastructure Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../Network/networking_management.htm#NetworkingManagement)and[Compute Instances](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../Compute/compute_management.htm#IAM)
