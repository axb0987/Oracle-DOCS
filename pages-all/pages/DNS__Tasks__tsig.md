# Managing TSIG Keys
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm
- Fetched: 2026-09-05 01:59 CDT

# Managing TSIG Keys

Transaction signature (TSIG), also referred to as Secret Key Transaction Authentication, ensures that domain name service (DNS) packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets.

TSIG keys are used to enable DNS to authenticate updates to secondary zones. TSIG keys provide an added layer of security for IXFR and AXFR transactions. A TSIG key consists of a key name, a signing algorithm, and a secret. See[RFC 2845](http://www.rfc-editor.org/rfc/rfc2845.txt)for more information. TSIG keys can also be managed in DNS Zone Management. See[Managing DNS Service Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/managingdnszones.htm)for more information.

## TSIG Key Tasks

You can perform the follwing TSIG key tasks:
- [Creating a TSIG Key](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-create.htm)
- [Listing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-list.htm)
- [Getting a TSIG Key's Details](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-get.htm)
- [Editing a TSIG Key](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-update.htm)
- [Moving a TSIG Key Between Compartments](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-move.htm)
- [Deleting a TSIG Key](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-delete.htm)
