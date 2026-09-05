# Configuring the Windows Server Certificate Authority
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_adcs_integration.htm
- Fetched: 2026-09-05 02:34 CDT

# Configuring the Windows Server Certificate Authority

Learn how to configure ADCS in the Window server.

You must configure the certificate authority (CA) to store the private key in the HSM cluster. For this configuration, you must first add the Active Directory Certificate Services (ADCS) role to the Windows server. After you have added the ADCS role, you can use the Key Storage Provider (KSP) to create and manage the CA's private key in the HSM cluster. KSP is an interface that connects the Windows Server to the HSM cluster.

## Prerequisites

To set up Windows Server as certificate authority (CA) with the HSM cluster, you need the following prerequisites:
- An active HSM cluster.
- OCI Dedicated KMS client service running in the Windows Server OS.
- An Cryptographic User (CU) account to manager certificate authority's private key on the cluster.

## Adding the Active Directory Certificate Services Role

To create the Windows Server CA, you must first add the Active Directory Certificate Services (ADCS) role to the Windows server. The ADCS role lets you use the KSP provider to create and store the CA's private key on the cluster.

- From the Windows Start menu, go to Windows Server , then start Server Manager .
- Click Manage at the top right corner and then select Add roles and features .
- In the Before you begin page, read the information and then click Next .
- In the Select Installation Type page, select Role-based or feature-based installation and click Next .
- In the Select Destination server page, select Select a server from the server pool and then click Next .
- In the Select Server roles page, select the following and then click Next .

- Active Directory Certificate Services
- Add Features.
- In the Active Directory Certificate Services page, click Next . In the Role Services page, select the following:

- Select Certificate Authority.
- In the Confirm installation selections page, verify the details and then Click Install .
- After installation completes, click the Configure Active Directory Certificate Services on the destination server link.
- In the Credentials page, verify or change the credentials and click Next .
- In the Role Services page, select Certification Authority and click Next .
- In the Setup Type page, select Standalone CA and click Next .
- In the CA Type page, select Root CA and click Next .
- In the Private Key page, select Create a new private key and click Next .
- In the Cryptography page, specify the following options and click Next :

- Select a cryptographic provider : Select Cavium Key Storage Provider .
- Key length : Choose one of the key length options.
- Select the hash algorithm for signing certificates issued by this CA : Choose an hash algorithm.
- In the CA Name page, provide the following details and click Next .

- Common name.
- Distinguished name suffix.
- Preview of distinguished name.
- In the Validity Period page, enter the validity period in years, months, weeks, or days and then click Next
- In the Certificate Database page, provide the location for certificate and logs and click Next .
- In the Configure page, click Configure .
- In the Results page, click Close .

Note  
  
You can verify whether the CA has been installed correctly by executing`sc query certsvc`from the command line.

## Signing a CSR with a Windows Server CA

Learn how to sign a CSR using Windows server CA.

Use your Windows server certificate authority (CA) with the HSM cluster to sign a certificate signing request (CSR).

You need a valid certificate signing request (CSR) to complete this task. Create a CSR using one of the following methods:
- Open SSL
- Windows Server Internet Information Services (IIS) Manager
- Windows CLI (using the`certreq`utility)

Complete the following steps to sign a CSR with Windows server CA.

- Connect to your Windows server and start the Windows Server Manager.
- In the Server Manager Dashboard , click Tools .
- Click Certification Authority .
- In the Certification Authority page, do the following:

- Open the Actions menu and select All Tasks , then select Submit new request .
- Select your CSR file and click Open .
- In the Certification Authority window, select Pending Requests and select the pending request.
- From the Action menu, select All Tasks , then select Issue .
- In the Certification Authority window, select Issued Requests to view the signed certificate.
- Optional. To export the signed certificate, do the following:

- In the Certification Authority window, select the certificate.
- Select the Details tab, then select Copy to File .
- Complete the instructions in the Certificate Export Wizard .
-
