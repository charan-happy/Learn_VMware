
overview

introducing vcenter server

choosing the version of vcenter server

planning and designing a vcenter server deployment

Installing vcenter server and its components

installing vCenter server in an enhanced linked mode group 

Exploring vCenter server

Creating and managing a vcenter server inventory

Exploring vCenter servers Management features

Managing vCenter server settings

vSphere web client administration


Vmware appliance Management Administration



>> vCenter server brings the advantages of client-server architecture to the ESXI host and to virtual machine (VM) Management

>> vCenter server is an application that serves as a centralized management tool for ESXI hosts and their respective VMs.

>> vCenter server acts as a proxy that performs tasks on the individual ESXI hosts that have been added as members of vCenter server installation.

>> vcenter server offers core services in the following areas :
 Resource Management for ESXI hosts and VMs
 Template Management
 VM Deployment
 VM Management
 Scheduled Tasks
 Statistics and Logging
 Alarms and Event Management
 ESXI Host Management
 
>> Vcenter server can be installed in two ways. 1. windows based virtual appliance 2. Linux based virtual appliance

To understand the value of vCenter server in vSphere deployment. Let's look at the below :
 Centralized user authentication
 web client server
 Extensible Framework

>> vCenter server is not a requirement for vsphere hypervisor deployment. we can create and run even without it. However to use the advanced features of vSphere product suite -features such as vSphere Update Manager, vMotion, Storage vMotion, vSphere DRs, vSphere HA, vSphere Distributed Switches, host profiles, vSphere FT, VM Encryption- vcenter server must be licensed, installed and configured accordingly.

>> Platform Service Controller (PSC) is a set of components that comprise the service of vCenter Single sign-on (SSO), including the Secure Token Service (STS) and Identity Management Service (IDM)-addresses the problem of creating new account and adding it into multiple VMware products.

>> PSC is vital to our vSphere environment due to

psc offers below services to vsphere :

  Single Sign-on (SSO)
  Licensing
  Certificate Authority
  certificate store
  Service Registry

PSC will provide a common service across your entire VMware Environment.

PSC can be installed as an embedded or external component of vcenter server, just like database

using vSphere Web Client for Administration
--------------------------------------------


Extensive framework:
---------------------
Just as centralized authentication is not a core vCenter Server service, we don't include vCenter Server's extensible framework as a core service. Rather, this extensible framework provides the foundation for vCenter Server's core services and enables third-party developers to create applications built around vCenter Server

vcenter server virtual appliance only supports postgreSQL As a database.

vcenter server virtual appliance naturally runs only on VM and with linux os of photon os.


Planning & Designing a vcenter server Deployment:
------------------------------------
Most important questions to ask before planning & designing a vcenter server deployment
How much hardware do I need to power vCenter Server?

How do I provide high availability for vCenter Server?

How do I prepare vCenter Server for disaster recovery?

If I run vCenter Server in a VM, do I need a separate management cluster?

Should I use a vCenter Server with an embedded Platform Services Controller or with an external Platform Services Controller?


The amount of hardware that a vcenter server requires is directly related to the number of hosts and VMs it will be managing. The virtual hardware of the vcenter server virtual appliance is predefined and established before it is deployed.

The bareminimum requirement for a linux based appliance is 2 cpus, 10 GB of RAM, 300 GB of disk space, A network adapter (Gigabit Ethernet is strongly recommended )these allows to run ~10 hosts and 100 VMs with 13 individual virtual disks.

 

  >> Protecting platform service controller :
    --> PSC is an integral part of vcenter server. There are 3 methods to ensure no downtime for PSC. 1. Deploying in a HA enabled cluster 2. Deploying multiple nodes 3. Have a solid backup plan

  >> Protecting vCenter Servers :
      --> If the vCenter Server computer is a physical server, one way to provide availability is to create a standby vCenter Server system that you can turn on in the event of a failure of the online vCenter Server computer
      --> making use of p2v to regularly backup the physical vcenter server instance to a standby VM.
      --> if you are using the Linux-based vCenter Server virtual appliance, vSphere 6.5 introduced a native solution called vCenter High Availability (vCHA). This solution uses a cluster of three vCenter Server nodes—an Active, a Passive, and a Witness node—to provide an automated process of synchronization and failover between the Active and Passive nodes. The Witness node provides a quorum—the tie-breaking entity—in the event of network isolation between the Active and Passive nodes, often referred to as a split-brain event

  >> Protecting vCenter Database :
   --> provide HA by creating multiple SQL servers
   --> include using SQL log shipping or database mirroring to create a database replica on a separate system

Running vCenter and its components as VM :
------------------------------------------
yes, it is recommended to run vCenter and it's components as VM.


Installing vCenter Server and its components :
-------------------------------------------
>> The vCenter Server virtual appliance is a Photon OS–based VM that comes prepackaged and preinstalled with vCenter Server. It is commonly referred to as the vCSA, vCVA, or sometimes just the vCenter appliance

>> vMware vCenter server appliance Installer has become one of the central places for install, upgrade, migration and restore operations within your environment.

>> The auxilary components of vCenter server bundle are 
1. vCenter Authentication proxy
2. vSphere web clients (Flash based and HTML5 based) 
3. vSphere Update Manager
4. vSphere Auto Deploy
5. vSphere syslog collector
6. vSphere ESXI Dump Collector

In addition, the ISO that packages the vCenter Server Appliance Installer contains the binaries necessary to set up Update Manager Download Service

Installing platform service controller

- vCenter Single Sign-On (SSO) is a prerequisite for vCenter and is part of the Platform Services Controller. Not only must it be installed for vCenter to run, it must also be running before the vCenter Server itself is installed.

use the following steps to install a PSC running SSO:

1. Mount the ISO (or burn it to a CD)

2. once Mounted launch the vCenter Server Appliance Installer. To begin, navigate to x :\vcsa-ui-installer, where x is the drive or mount point, depending on your operating system. There will be three directories available to you, allowing you to run installer on Mac OS X (/mac/installer.app), Microsoft Windows (\win32\installer.exe), or Linux (/lin64/installer).

3. The vCenter Server Appliance Installer should appear. Click Install, review the Introduction screen, which explains the two-stage appliance deployment operation, and then click Next.

4. On the End User License Agreement (EULA) page, select the check box to accept and click Next.

5. On the Select Deployment Type page, as shown in Figure 3.9, we'll choose the second option, Platform Services Controller, and click Next.

6. You'll need a running ESXi host to deploy the vCSA to. At a minimum, the host needs to be running version 6.0 to work for this installation. Provide the ESXi hostname or IP address, a username (in this case, root), and the appropriate password. Click Next.

7. A pop-up box will prompt you with an SSL certificate warning, which will be the certificate thumbprint of the ESXi host. Click Yes to proceed to the next screen.

8. Supply a VM (or display) name for the Platform Services Controller virtual appliance. You will also need to provide a password for the root account of this VM. Click Next to continue.

9. Select the datastore that you want the Platform Services Controller to reside on, and then click Next.

10. The final steps of Stage 1 are to provide the network information for the VM deployment. Working from top to bottom of the screen, first you must choose a network. On the ESXi host, this could also be called a port group

11. Second, select between IPv4 or IPv6 as the protocol. You'll most likely want to use a static IP address for Platform Services Controller—so on the third field, IP Address, select Static. However, if DHCP is available on the selected network, you can use that option. You'll need to provide a hostname, the associated IP address, a subnet mask, a gateway, and at least one DNS server. The hostname established in this step will be used to sign the SSL certificate generated upon deployment.

12. Finally, new in vSphere 6.7 for appliance deployments, you have the option to provide unique ports that the Platform Services ontroller will use. Leave these as default, and click Next.

13. On the last page of Stage 1, review all the configuration details, to make sure there are no errors. Click Finish to deploy the virtual appliance.

14. After the appliance has been successfully deployed, you'll begin Stage 2 to finalize the Platform Services Controller's configuration. Review the Introduction page, which explains the two-stage appliance deployment operation, and then click Next.

15. In the Appliance Configuration section, provide an NTP source. Unless necessary, due to a lack of NTP server availability in your environment, avoid using the VMware time sync tool because a time-drift can occur unless it's set up in a specific way.

For troubleshooting purposes, enable SSH access, and then click Next.

16. on the following screen, you're asked if you would like to configure a new Single Sign-On instance or join an existing one. Again, choose to configure a new SSO instance. You'll need to create a domain name, an SSO administrator password, and a site name. Click Next to continue.

17. The PSC installer will now ask you to join the Customer Experience Improvement Program that enabled VMware to collect telemetry data from your environment. Depending on your security requirements, either check the box to join or uncheck it to opt-out. Then click Next.

18. Finally review all configuration details for errors, Click Finish to proceed with configuring the Platform Services Controller virtual appliance. You'll receive one last warning that you will be unable to pause the installation after you proceed—essentially, there is no turning back from this point—so double-check those final configuration details, and then click OK

19. When installation is complete, click Close to close the installer.

Installing vCenter Server


Steps are same as above

After you install vCenter server, a number of new services will be installed to facilitate the operation of vCenter server.

 >> VMware vCenter Server, the core of vCenter Server that provides centralized management of ESX/ESXi hosts and VMs

>> VMware Services Lifecycle Manager API, the interface to the VMware Lifecycle Manager (vMon) that provides the watchdog service to the Platform Services Controllers and vCenter Server, ensuring each node has healthy services and proper start order

>> VMware Postgres, the embedded database on vCenter Server where configuration and historical data from the environment is preserved

>> VMware vSphere Web Client, the web server that runs the user interface

Installing vCenter server in an Enhanced Linked MOde group :
-------------------------------------------------------------
- The multiple instances of vCenter Server that share information among them are referred to as an enhanced linked mode group, or simply enhanced linked mode. In an enhanced linked mode environment, there are multiple vCenter Server instances, and each of the instances has its own set of hosts, clusters, and VMs. They are all registered back to the same PSC and SSO instance.

- ou might prefer to deploy multiple vCenter Server instances in enhanced linked mode to accommodate organizational or geographic constraints, or you might want to manage multiple vCenter Servers from a single user interface. You can have up to 15 vCenter Servers participating in a linked mode group.

Before you install additional vCenter Server instances, you must verify the following prerequisites:

All computers that you wish to run vCenter Server in an enhanced linked mode group must be registered to the same SSO domain, sometimes referred to as a vSphere domain. The servers can exist in different Active Directory domains only if a two-way trust relationship exists between the domains.

DNS must be operational. Also, the DNS name of the servers must match the server name.

You must use the same version of vSphere when deploying additional Platform Services Controllers and vCenter Servers; you cannot combine vCenter Server 6 instances in an enhanced linked mode group with earlier versions of vCenter Server via fresh installation.

Enhanced Linked Mode is supported between the Linux-based vCenter virtual appliance and the installable Windows version of vCenter.

Each vCenter Server instance must have its own backend (Windows) or embedded (Appliance) database.

After you've met the prerequisites, installing vCenter Server in an enhanced linked mode group is straightforward, though you have two choices to achieve this: deploying an additional Platform Services Controller for your new vCenter Server to use or connecting the new vCenter Server to the already-deployed Platform Services Controller

Most vSphere administrators will likely now install their vCenters in enhanced linked mode by default.

Exporing vCenter Server :
----------------------------
vsphere web client Home screen :

1. Navigator 
2. content Area
3. Alarms and Work in progress
4. Recent Tasks

Understanding Inventory views and objects :
---------------------------------------------
Every vcenter has one or more root objects; These are datacenter objects. Which serves as a container for all other objects.prior to adding an object to the vcenter server inventory. You must create at least one datacenter object.

Hosts and cluster view
VMs and templates view
Datastores view
Network view

creating a datacenter object :

Perform the following steps to create a datacenter object:

Launch the vSphere Web Client, if it is not already running, and connect to a vCenter Server instance.

On the home screen, select Hosts And Clusters.

In the navigator, right-click the vCenter Server object and select New Datacenter.

Type a name for the new datacenter object and click OK.

Adding ESXI Hosts :
----------------
The process of adding an ESXi host to vCenter Server automatically installs a vCenter agent on the ESXi host through which vCenter Server communicates and manages the host.

Perform the following steps to add an ESXi host to vCenter Server:

1. Launch the vSphere Web Client, if it is not already running, and connect to a vCenter Server instance.

2. From the navigator, select vCenter Hosts And Clusters, or simply click the Hosts And Clusters icon on the home screen.

3. In the navigator, right-click the datacenter object and select Add Host.

4. In the Add Host Wizard, supply the IP address or fully qualified hostname and user account information for the host being added to vCenter Server. This will typically be the root account.

5. When you're prompted to decide whether to trust the host, and an SHA1 fingerprint is displayed, click Yes.

6. The next screen displays a summary of the ESXi host being added, along with information on any VMs currently hosted on that server. Click Next.

7. On the next screen, you need to assign a license to the host being added. The option to add the host in evaluation mode is also available.

8. The next screen offers the option to enable lockdown mode. There are two lockdown mode options. Normal lockdown mode ensures that the management of the host occurs via vCenter Server, not through the vSphere Client connected directly to the ESXi host. Strict lockdown mode takes normal mode one step further and disables the Direct Console User Interface (DCUI). For now, leave this disabled and click Next.

9. On the VM location screen, you will be asked where you want to move any existing VMs running on this host. If you have folders set up within the VMs And Templates view, these folders will be displayed under the datacenter object here. For now, simply select the datacenter you already have created and click Next.

10. Review your host details and click Finish at the summary screen.

11. Repeat this process for all the ESXi hosts you want to manage using this instance of vCenter Server.

creating a cluster :
-------------------
Perform the following steps to create a cluster:

1. Launch the vSphere Web Client, if it is not already running, and connect to a vCenter Server instance.

2. Right-click a datacenter object in the Hosts And Clusters view.

3. Select New Cluster to open the New Cluster Wizard.

4. Supply a name for the cluster.

