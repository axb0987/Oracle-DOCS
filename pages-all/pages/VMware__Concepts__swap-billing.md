# Transferring VMware Solution Billing Commitments
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/swap-billing.htm
- Fetched: 2026-09-05 03:07 CDT

# Transferring VMware Solution Billing Commitments

You can transfer the billing commitment, HCX commitment, and billing end date from one ESXi host to another. Billing commitments can be transferred from a deleted host or an existing host.

- Use unexpired commitments left over from deleted ESXi hosts to create new hosts.
- Swap billing commitments from one active ESXi host to another.
- Upgrade ESXi hosts and transfer billing commitments from the old host to the upgraded host.
- Transfer HCX Enterprise license commitments from one host to another during a software upgrade or to replace a failed host.
- You can swap billing commitments of compatible hosts between SDDCs and clusters. You can manage SDDC billing commitment assignments as you require, ensuring that SDDCs remain organized and cost effective.

HCX Enterprise commitments are transferred along with billing commitments. If you're running the old and new hosts in parallel (such as during an upgrade) you're only charged for HCX commitments on the old host after 24 hours. After 24 hours, you're charged for HCX Enterprise usage in 1 month increments. There is no cost for HCX Advanced usage.

## Using Billing From a Deleted Host to Create a Host

If you've deleted an ESXi host before its billing commitment ends, you can use the remaining billing from the old host to[create a new host](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/esxi-host-create.htm). The original billing commitment end date is transferred the new host. End date persistence helps you keep hosts in sync with the other hosts in the SDDC.

- To use a billing commitment from a deleted host, it must have at least 24 hours remaining on its term.
- You can only assign billing to a host of the same shape and CPU as the deleted host.
- You can't transfer an hourly billing commitment.

Commitment Type Can I re-use it?
Hourly No, hourly commitment transfer is not supported.
Monthly Yes, if there's at least 24 hours remaining on the term.
1 Year Yes, if there's at least 24 hours remaining on the term.
3 Year Yes, if there's at least 24 hours remaining on the term.

See[Creating a VMware Solution SDDC ESXi Host](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/esxi-host-create.htm)for instructions.

## Transferring Billing From a Deleted Host to an Existing Host

If you've deleted an ESXi host before its billing commitment ends, you can[update an existing host](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/esxi-host-update.htm)to use the remaining billing from the old host.

The original billing commitment end date is transferred the new host. End date persistence helps you keep the new host in sync with the original hosts in the SDDC.

- To use a billing commitment for this scenario, it must have at least 24 hours remaining on its term.
- You can only assign billing to a host of the same shape and CPU as the deleted host.
- You can't transfer an hourly billing commitment.

Commitment Type Can I re-use it?
Hourly No, hourly commitment transfer is not supported.
Monthly Yes, if there's at least 24 hours remaining on the term.
1 Year Yes, if there's at least 24 hours remaining on the term.
3 Year Yes, if there's at least 24 hours remaining on the term.

See[Editing a VMware Solution SDDC ESXi Host](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/esxi-host-update.htm)for instructions.

## Swapping Billing Between Active Hosts

Over time, you might have many hosts in your SDDCs, all with different billing commitments and end dates. You can[transfer billing commitments between hosts](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/esxi-host-swap-billing.htm)in the same or different SDDC according to your business and organization requirements.
For example, suppose you have two SDDCs, A and B. Each SDDC has a mix of hosts with 1 year or monthly commitment types. You want to organize your SDDCs so that SDDC A contains only hosts with monthly commitments, and SDDC B contains only hosts with 1 year commitments. Swap billing between hosts until your SDDC commitments are organized the way you want them.
- Both hosts must be active.
- End dates of swapped billing commitment terms are transferred from the old host to the new host.
- To use a billing commitment for this scenario, it must have at least 24 hours remaining on its term.
- You can't swap an hourly billing commitment.
- You can't swap hourly-to-hourly or monthly-to-monthly billing commitments because there is no end date change associated to swapping those commitment types.

Can I swap these commitments? Host 2
Hourly Monthly 1 Year 3 Year
Host 1 Hourly No, not supported Yes, if there's at least 24 hours remaining on the term. Yes, if there's at least 24 hours remaining on the term. Yes, if there's at least 24 hours remaining on the term.
Monthly Yes, if there's at least 24 hours remaining on the term. No, not supported Yes, if there's at least 24 hours remaining on the term. Yes, if there's at least 24 hours remaining on the term.
1 Year Yes, if there's at least 24 hours remaining on the term. Yes, if there's at least 24 hours remaining on the term. Yes, if there's at least 24 hours remaining on the term. Yes, if there's at least 24 hours remaining on the term.
3 Year Yes, if there's at least 24 hours remaining on the term. Yes, if there's at least 24 hours remaining on the term. Yes, if there's at least 24 hours remaining on the term. Yes, if there's at least 24 hours remaining on the term.

See[Swapping Billing Between Active VMware Solution SDDC Hosts](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/esxi-host-swap-billing.htm)for instructions.

## Transferring Billing to a Planned Replacement Host

If you need to[replace an ESXi host](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/esxi-host-replace.htm), or[upgrade the software for a host](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/upgrade.htm), the workflow automatically transfers billing commitment from the old host to the new host while temporarily keeping the old host active. Then, with both the new host and the old host still running, you can perform the required maintenance, and then finally terminate the old host.

Commitment Type New Host Commitment After Transfer Old Host Commitment After Transfer
Hourly Hourly Hourly
Monthly Monthly Hourly
1 Year 1 Year Hourly
3 Year 3 Year Hourly

See[Replacing a VMware Solution SDDC Failed ESXi Host](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/esxi-host-replace.htm)and[Upgrading a VMware Solution SDDC's Software](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/upgrade.htm)
