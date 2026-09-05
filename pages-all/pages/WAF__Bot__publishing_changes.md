# Publishing Changes
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/publishing_changes.htm
- Fetched: 2026-09-05 03:10 CDT

# Publishing Changes

Publish changes in the Web Application Firewall service.

Many of the actions you can take for an edge policy require publishing before they can take effect. Updates to your WAF policy appear in the list to be published using the Unpublished Changes feature under WAF Policy for the edge policy. Pending changes do not persist across browser sessions. Once you publish changes, it cannot be edited until changes propagate to the edge nodes.

## Publishing Changes using the Console

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.

All the WAF policies in that compartment are listed in tabular form.
- (Optional) Apply one or more of the following Filters to limit the WAF policies displayed:

- 

State
- 

Name
- 

Policy Type : Select Edge Policy .
- Select the name of the edge policy whose unpublished changes you want to publish.

The Details page of the edge policy you selected appears.
- Select Unpublished Changes under WAF Policy .

The Unpublished Changes list appears.
- Select the arrow beside any unpublished change entry in the list to review the change.
- Select Publish All .
- Confirm the publish.

## Discarding Changes using the Console

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.

All the WAF policies in that compartment are listed in tabular form.
- (Optional) Apply one or more of the following Filters to limit the WAF policies displayed:

- 

State
- 

Name
- 

Policy Type : Select Edge Policy .
- Select the name of the edge policy whose unpublished changes you want to discard.

The Details page of the edge policy you selected appears.
- Select Unpublished Changes under WAF Policy .

The Unpublished Changes list appears.
- Select the arrow beside any unpublished change entry in the list to review the change.
- Check the boxes for one or more unpublished change entries you want to discard.
- Select Discard .
-
