# Manage Delegation Preferences
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-delegation-preferences.htm
- Fetched: 2026-09-05 03:15 CDT

# Manage Delegation Preferences

Delegation preferences allow you to setup and manage a delegate for certain tasks and activities in Oracle Access Governance in the event that you are unable to carry out the task, for example due to absence from the office.
Users can delegate tasks/activities using the Oracle Access Governance Console. You can use the My Preferences page or the Identity details page to assign delegated tasks/activities to another user or identity collection. You can choose when to start the delegation process and also specify the duration of the delegation. In Oracle Access Governance, you can delegate:
- Access Reviews : Some other user or identity collection can perform access reviews on your behalf
- Approvals : Some other user or identity collection can perform approvals on your behalf
You may want to delegate approvals or access reviews for the following reasons:
- Unavailability because of vacation, sickness, or working on other tasks
- To have the most qualified person to make the decisions
- Develop someone else’s ability to handle additional assignments
Delegation settings can be accessed from a number of paths in the Oracle Access Governance Console:
- My Stuff → My Preferences : This option takes you directly to the Delegation tab, where a user can setup delegations for tasks assigned to themselves.
- My Stuff → My Access : From the identity detail page you can select the Delegation tab and setup your own user's delegation preferences.
- Who Has Access To What → My Direct's Access : A user's manager can select users they directly manage from this page, and amend delegation details for the selected user.
- Service Administration → Manage Identities : An administrator can select View Details or Manage delegations for a user listed in the Manage Identities page, and amend delegation details for the selected user.
The user types that can create and manage delegations are:
- Administrator : Users with the`AG_Administrator`application role can update their own delegations, and delegations for other users.
- Managers : Users that manage a user can update their own delegations, and delegations for users they manage directly,
- Users : Users can maintain their own delegation preferences.

## Set up Your Delegation Preferences

Perform the following steps to navigate to the Delegations tab:
- Log in to the Oracle Access Governance Console.
- Navigate to the delegations tab using one of the following paths:
- My Stuff → My Preferences .
- My Stuff → My Access → Delegations .
- Who Has Access To What → My Direct's Access → &lt;User&gt; → Delegations .
- Service Administration -&gt; Manage Identities → &lt;User&gt; → View Details/Manage delegations → Delegations .
Perform the following steps to add a new delegation:
- In the Delegations screen, click the Add a delegation button.

You will be navigated to the Add a delegation pop-up window.
- Select what you want to delegate in the Which tasks do you want to delegate? field. You can delegate the following tasks:
- Access reviews
- Approvals
- The field Who do you want to delegate to? allows you to either delegate the selected task to an individual or an identity collection.
- If An individual option is selected, enter the name of the delegator in the Who? field
- If An identity collection option is selected, enter the name of the identity collection group in the Who? field
Note  
  
The Identity collection can have one or more than one member in it.
- Select the date range for the delegation from the How long do you want the delegation to last? field. It can be either an indefinite time or a specific time range. Selecting:
- Indefinitely : Allows you to set the delegation for an indefinite time.
- During a time range : Allows you to select a date range for the delegation.
- Select whether to send notifications to the original assignee. You can chose to send notifications to the delegator and the delegate, or to the delegate only using this check box. When setting a delegation preference for yourself, this checkbox is selected by default. For delegation preferences set by others, the checkbox is not selected by default. Set the Include original assignee in notifications checkbox as required.
- Click Save .
Tasks or activities created after assigning a delegate are visible on both the dashboards of the delegator (the one who delegated the task) and the delegate (the one to whom the task/activity was delegated to).
Note  
  
Tasks or activities that were created before delegation will not appear on the delegate’s dashboard immediately. It may be a few hours before the existing tasks/activities are processed and displayed.

## Edit a Delegation

Perform the following steps to edit a delegation:

- In the Delegations screen, click the Edit button.

You will be navigated to the Edit pop-up window.
- You can change the individual assignee or identity collection to which you have delegated the task, by updating the Who? field. You cannot change assignee from an individual to an identity collection, or identity collection to an individual.
- Select the date range for the delegation from the How long do you want the delegation to last? field. It can be either an indefinite time or a specific time range. Selecting:
- Indefinitely : Allows you to set the delegation for an indefinite time.
- During a time range : Allows you to select a date range for the delegation.
Note  
  
You can only modify the dates, not the delegate type.
- Click Save .

## Delete a Delegation

Perform the following steps to delete a delegation:

- In the Delegations screen, click the button.
-
