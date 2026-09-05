# Viewing Details about Delegated Authentication
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/delegatedauth/view-details-ad-bridge.htm
- Fetched: 2026-09-05 02:21 CDT

# Viewing Details about Delegated Authentication

View the details of delegated authentication for an identity domain in IAM.
The Delegated authentication list page displays the name and status of each Microsoft Active Directory (AD) Bridge that IAM uses to communicate with an AD domain. You can also see other information about the bridge, such as whether it's activated or deactivated for delegated authentication.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- Select Security .
- Select Delegated authentication .
The Delegated authentication list page displays the name and status of the AD bridges.
Tip  
  
Select the AD Bridge to see detailed configuration information about it, and how many users and groups were transferred by the bridge from AD into IAM.
- Expand the node to the right of the AD Bridge to view activation information.
An Activate delegated authentication switch indicates whether the AD domain is activated or deactivated for delegated authentication.

Activate delegated authentication might be unavailable (that is, you can't turn the switch on or off) for one of the following reasons:
- The status of the AD Bridge is`No Clients Found`. You can't activate delegated authentication for the AD domain because the AD domain doesn't work until you install a client for the AD domain. Select Select here to download the client to download the client for the AD domain.
- The status of the AD Bridge is`Incompatible Client Found`. You can't activate delegated authentication for the AD domain because the AD domain doesn't work until you install the correct version of the client for the AD domain. Select Select here to download the client to download the updated client for the AD domain.
- The AD Bridge isn't configured for delegated authentication. To configure it:
- Select the AD domain.
- Select Configuration .
- In the Configure the Microsoft Active Directory Domain page, scroll down until you see the Authentication Settings area.
- Select Enable local authentication .
- Select Save .
-
