<details><summary>1. What is virtualization? <br></summary>The process of creating virtual versions of physical components, i.e., Servers, Storage Devices, and Network Devices on a physical host, is called virtualization. Virtualization lets you run multiple virtual machines on a single physical machine which is called ESXi host.</details>
<details><summary> 2. Types of virtualization<br></summary>There are 5 basic types of virtualization.

Server virtualization: consolidates the physical server, and multiple OS can be run on a single server.<br>
Network Virtualization: Provides complete reproduction of physical network into a software-defined network.<br>
Storage Virtualization: Provides an abstraction layer for physical storage resources to manage and optimize virtual deployment.<br>
Application Virtualization: increased mobility of applications and allows migration of VMs from one host to another with minimal downtime.<br>
Desktop Virtualization: virtualize desktop to reduce cost and increase service</details>
<details><summary> 3. What is a hypervisor <br></summary>A hypervisor is a virtualization layer that enables multiple operating systems to share a single hardware host. Each operating system or VM is allocated physical resources such as memory, CPU, storage, etc., by the host </details>
<details><summary> 4. Types of hypervisor<br></summary>There are two types of hypervisors.

Hosted hypervisor (works as application i-e VMware Workstation)<br>
Bare-metal (virtualization software i-e VMvisor, Hyper-V which is installed directly onto the hardware and controls all physical resources).</details>
<details><summary> 5. what is HCL<br></summary> HCL Stands for Hardware Compatibility List. It is a single Point of reference to ensure any hardware that we are planning to use with VMware products has been tested and certified to work fine. </details>
<details><summary> 6. what is ESXI<br></summary>It is a Baremetal/type-1 Hypervisor developed by VMware. It is designed to run VMs directly on the physical hardware. It provides a robust and efficient platform for virtualization, offering features such as HA, scalability, and resource management. </details>
<details><summary> 7. Difference between ESX and ESXi<br></summary> Overall the functionality of both ESX and ESXi are the same. But, the difference is in the architecture and operations Management. ESXI uses Direct Console User Interface (DCUI) instead of service control to manage the ESXI host, Due to low code base ESXI installation is quicker than ESX and ESXI consumes less disk space when compared to ESX. </details>
<details><summary>8. What is Host and Guest machine <br></summary**>Host:** It is a physical Machine/server on which VMware software was installed. It provides necessary hardware resources such as CPU, Memory, Storage, and Network for the VM to run. It also provides the underlying operating system and hardware drivers required for the guest operating system to operate.** Guest:** It is a VM that runs isolately on top of the Host machine. These can be created using various Operating systems including Linux, windows providing flexibility in running different software and applications.</details> 
<details><summary> 9. What is VMware workstation<br></summary>- it is a hosted Hypervisor that runs on different operating systems like Linux and Windows. It allows users to create and run VMs on their computers. It is mainly used by developers, Testers, and It professionals who need to run multiple VMs on a single computer.</details>
<details><summary>10. what is virtual machine <br></summary>It is a software-based emulation of a physical machine. It provides a way to run multiple Os in a VM. VMs are often used for development and testing purpose. Advantages of Using VMs includes scalability, portability, resource efficiency, isolation</details>
<details><summary>11. what are the virtual machine files <br></summary> A physical representation of a physical computers hardware and software configuration . It encapsulates all the necessary components such as Operating system, application, data in a single file. .vmx file, .vmdk,.nvRAM file, .vmxf and .vmsd files</details>
<details><summary>12. what is vmkernel <br></summary>VMkernel is a operating system created by VMware. It acts as a virtual interface between a Vm and host to communicate each other. It's functions include process creation, process controls, process threads, signals, filesystems etc. </details>
<details><summary>13. what is cluster <br></summary>it is a group of ESXI hosts that are combined managed together as a single entitiy. It provides several benefits include resource pooling, high availability, loadbalancing, fault tolerance</details>
<details><summary> 14. what is vlan<br></summary> A logical network segmentation within a physical network. vLANS enable the creation of multiple isolated within a single physical networking infrastructure. This allows for better network organization, security and traffic management. It is done at layer 2 of the network protocol suite. </details>
<details><summary> 15. what is vcenter server<br></summary> vcenter server is an application that enables you to manage vsphere infrastructure from a centralized location. It has features like Centralized management, High Availability, scalability, security, Extensibility</details>
<details><summary> 16. what is platform service controller<br></summary></details>
<details><summary>17. what are the services in platform service controllers <br></summary></details>
<details><summary>18. Types of deployment supported in vcenter<br></summary></details>
<details><summary>19.  what is the operating system of vcenter server appliance<br></summary></details>
<details><summary>20. what is SSO <br></summary></details>
<details><summary>21. what is datastore<br></summary></details>
<details><summary>22. what is VVOls<br></summary></details>
<details><summary>23. what is VMFS <br></summary></details>
<details><summary>24. what is VMDK <br></summary></details>
<details><summary>25. what types of network storage is supported in vsphere <br></summary></details>
<details><summary>26. disk types in vmware <br></summary></details>
<details><summary>27. what is template <br></summary></details>
<details><summary>28. what is clone<br></summary></details>
<details><summary>29. comparision between clone and template <br></summary></details>
<details><summary>30. what is snapshot<br></summary></details>
<details><summary>31.   what is vmware tools<br></summary></details>
<details><summary>32. what is hardware version <br></summary></details>
<details><summary>33. memory management techniques in VMware <br></summary></details>
<details><summary>34. what is standard switch <br></summary></details>
<details><summary>35. what is distributed switch<br></summary></details>
<details><summary>36. what is traffic shaping <br></summary></details>
<details><summary>37. what is port group <br></summary></details>
<details><summary>38. Network adapter types in VMware<br></summary></details>
<details><summary>39. what are security policies available in standard and Distributed switch <br></summary></details>
<details><summary>40.what is vMotion <br></summary></details>
<details><summary>41. what is storage vMotion <br></summary></details>
<details><summary>42. what is DRS<br></summary></details>
<details><summary>43. what is SDRS <br></summary></details>
<details><summary>44. what is High Availability <br></summary></details>
<details><summary>45. what is fault tolerance <br></summary></details>
<details><summary>46. what is EVC <br></summary></details>
<details><summary>47. what is VCHA <br></summary></details>
<details><summary>48. what is Resource pool <br></summary></details>
<details><summary>49. what is vAPP <br></summary></details>
<details><summary>50. what is Host profiles <br></summary></details>
<details><summary>51. what is Hot Add <br></summary></details>
<details><summary>52. what is VUM <br></summary></details>
<details><summary>53. what is vcenter converter<br></summary></details>
<details><summary>54. what is content library in vmware <br></summary></details>
<details><summary>55. what two types of content library available in vmware<br></summary></details>
<details><summary>56. what is cold migration <br></summary></details>
<details><summary>57. what is hot migration <br></summary></details>
<details><summary>58. how vSphere Licensing works <br></summary></details>
<details><summary>59. Which Licence editions are available in vsphere 6.7<br></summary></details>
<details><summary>60.which are Editions available in vCenter Server<br></summary></details>
<details><summary>61. what is vsphere Replication <br></summary></details>
<details><summary>62. what is SRM <br></summary></details>
<details><summary>63. what is VMware NSX <br></summary></details>
<details><summary>64. what are key features of VMware NSX <br></summary></details>
<details><summary>65. what are the ways of Installing ESXI<br></summary></details>
<details><summary>66. what are the ways of Upgrading ESXi <br></summary></details>
<details><summary>67. what is customized ESXI ISO<br></summary></details>
<details><summary>68. what is DCU <br></summary></details>
<details><summary>69. what are the ways of accessing ESXI<br></summary></details>
<details><summary>70. what is lockdown mode in ESXi <br></summary></details>
<details><summary>71. what is maximum number of snapshots can be used in single chain <br></summary></details>
<details><summary>72. what is vcenter server<br></summary></details>
<details><summary>73. what is difference between vcenter server for windows and vcenter server appliance <br></summary></details>
<details><summary>74. what is platform service controller<br></summary></details>
<details><summary>75. what is operating system in vcenter server appliance<br></summary></details>
<details><summary>76. which databases are supported with vcenter server appliance 6.7<br></summary></details>
<details><summary>77. Types of Deployment Supported in vcenter server   <br></summary></details>
<details><summary>78. what are CPU, Memory, and storage requirements for vcenter server applinance 6.7   <br></summary></details>
<details><summary>79. which services are in vcenter server appliance with platform service controller<br></summary></details>
<details><summary>80. what is vcenter server enhanced linked mode  <br></summary></details>
<details><summary>81. what is the latest version of VMFS   <br></summary></details>
<details><summary>82. differnce between VMFS 5& VMFS 6   <br></summary></details>
<details><summary>83.  What is permananent Drive loss    <br></summary></details>
<details><summary>84. what is all paths down    <br></summary></details>
<details><summary>85.  what is RDM   <br></summary></details>
<details><summary>86.  what are RDM compatibility modes   <br></summary></details>
<details><summary>87. which protocols are supported for VCSA backup    <br></summary></details>
<details><summary>88. what is heartbeating in vsphere HA    <br></summary></details>
<details><summary>89.  which 2 types of heartbeats are used by vsphre HA    <br></summary></details>
<details><summary>90.  what is Election process in vsphere HA   <br></summary></details>
<details><summary>91.  how election process works in vsphere HA   <br></summary></details>
<details><summary>92.  what is Master & Slave in vsphere HA    <br></summary></details>
<details><summary>93. what is fault tolerance    <br></summary></details>
<details><summary>94.  which locking technology is used by Vmware FT    <br></summary></details>
<details><summary>95.  what is licensing limits in VMware Fault Tolerance   <br></summary></details>
<details><summary>96. what is DRs    <br></summary></details>
<details><summary>97.  what are the DRs Rules   <br></summary></details>
<details><summary>98. What is the use of Update Manager    <br></summary></details>
<details><summary>99. what is the process of upgrading vsphere components or infrastructure<br></summary></details>

[interview questions](https://www.techwrix.com/top-50-vmware-interview-questions-and-answers-of-2023/)

[scenario based interview questions](https://interviewprep.org/vmware-engineer-interview-questions/)
# interview questions :

#1. What is VMKernel, and why is it important?
VMkernel is a virtualization interface between a Virtual Machine and the ESXi host, which stores VMs. It is responsible for allocating all available resources of the ESXi host to VMs such as memory, CPU, storage, etc. It’s also controlled special services such as vMotion, Fault tolerance, NFS, traffic management, and iSCSI. To access these services, the VMkernel port can be configured on the ESXi server using a standard or distributed vSwitch. Without VMkernel, hosted VMs cannot communicate with the ESXi server.

#2. What are the hypervisor and their types?
A hypervisor is a virtualization layer that enables multiple operating systems to share a single hardware host. Each operating system or VM is allocated physical resources such as memory, CPU, storage, etc., by the host. There are two types of hypervisors.

Hosted hypervisor (works as application i-e VMware Workstation)
Bare-metal (is virtualization software i-e VMvisor, Hyper-V which is installed directly onto the hardware and controls all physical resources).
#3. What is Virtualization?
The process of creating virtual versions of physical components, i.e., Servers, Storage Devices, Network Devices on a physical host, is called virtualization. Virtualization lets you run multiple virtual machines on a single physical machine which is called ESXi host.

#4. What are the different types of virtualization?
There are 5 basic types of virtualization.

Server virtualization: consolidates the physical server, and multiple OS can be run on a single server.
Network Virtualization: Provides complete reproduction of physical network into a software-defined network.
Storage Virtualization: Provides an abstraction layer for physical storage resources to manage and optimize virtual deployment.
Application Virtualization: increased mobility of applications and allows migration of VMs from a host to another with minimal downtime.
Desktop Virtualization: virtualize desktop to reduce cost and increase service
VMware Fault Tolerance (FT) Interview Questions
#5. What is VMware FT?
FT stands for Fault Tolerance very prominent component of VMware vSphere. It provides continuous availability for VMs when an ESXi host fails. It supports up to 4 vCPUs and 64 GB memory. FT is very bandwidth-intensive, and 10GB NIC is recommended to configure it. It creates a complete copy of an entire VM such as storage, compute, and memory.

#6. How many vCPUs can be used for a VM in FT in VMware vSphere 7.0?
In VMware vSphere 7.0, there can be up to 8 vCPUs with the VMware vSphere Enterprise Plus license.

#7. What is the name of the technology used by VMware FT?
vLockstep technology is used by VMware FT

#8. What is Fault Tolerant Logging?
The communication between two ESXi hosts is called FT logging when FT is configured between them. The pre-requisition of configuring FT is to configure the VMKernel port.

#9. Will the FT work if the vCenter Server goes down?
vCenter Server is only required to enable Fault Tolerance on a VM. Once it is configured, vCenter is not required to be online for FT to work. FT failover between primary and secondary will occur even if the vCenter is down.

#10. What is the main difference between VMware HA and FT?
The main difference between VMware HA and FT is: HA is enabled per cluster, and VMware FT is enabled per VM. In HA, VMs will be re-started and powered-on on another host in case of a host failure, while in FT, there is no downtime because the second copy will be activated in case of host failure.

Virtual Networking Interview Questions
#11. What is virtual networking?
A network of VMs running on a physical server that is connected logically with each other is called virtual networking.

#12. What is vSS?
vSS stands for Virtual Standard Switch is responsible for the communication of VMs hosted on a single physical host. it works like a physical switch that automatically detects a VM which wants to communicate with another VM on the same physical server.

#13. What is vDS?
vDS stands for Virtual Distributed Switch acts as a single switch in a whole virtual environment and is responsible for providing central provisioning, administration, and monitoring of the virtual network.

#14. How many maximum standard ports per host are available?
4096 ports per host are available either in a standard switch or distributed switch.

#15. What are the main benefits of a distributed switch (vDS)?
vDS can provide:

The central administration for a virtual data center
Central provision, and
Monitoring
#16. What is the VMKernal adapter, and why is it used?
VMKernel adapter provides network connectivity to the ESXi host to handle network traffic for vMotion, IP Storage, NAS, Fault Tolerance, and vSAN. For each type of traffic, such as vMotion, vSAN, etc. separate VMKernal adapter should be created and configured.

#17. What is the main use of port groups in data center virtualization?
You can segregate the network traffic using port groups such as vMotion, FT, management traffic, etc.

#18. What are the three-port groups configured in ESXi networking?
Virtual Machine Port Group – Used for Virtual Machine Network
Service Console Port Group – Used for Service Console Communications
VMKernel Port Group – Used for VMotion, iSCSI, NFS Communications
#19. What is VLAN, and why use it in virtual networking?
A logical configuration on the switch port to segment the IP Traffic where each segment cannot communicate with other segments without proper rules is called VLAN. Every VLAN has a proper number called VLAN ID.

#20. What is VLAN Tagging?
The practice of inserting VLAN ID into a packet header to identify which VLAN packet belongs to is called VLAN tagging.

#21. What are the three network security policies/modes on vSwitch?
Promiscuous mode
MAC address change
Forged transmits
#22. What is the promiscuous mode on vSwitch?
Promiscuous mode is a security policy that can be defined at the virtual switch or portgroup level in vSphere ESX/ESXi. A virtual machine, Service Console, or VMkernel network interface in a portgroup that allows the use of promiscuous mode can see all network traffic traversing the virtual switch.

By default, a guest operating system’s virtual network adapter only receives frames that are meant for it. Placing the guest’s network adapter in promiscuous mode causes it to receive all frames passed on the virtual switch that is allowed under the VLAN policy for the associated portgroup. This can be useful for intrusion detection monitoring or if a sniffer needs to analyze all traffic on the network segment.

#23. What is MAC address changes network policy?
The security policy of a virtual switch includes a MAC address change option. This option affects the traffic that a virtual machine receives.

When the Mac address changes option is set to Accept, ESXi accepts requests to change the effective MAC address to a different address than the initial MAC address.

When the Mac address changes option is set to Reject, ESXi does not honor requests to change the effective MAC address to a different address than the initial MAC address. This setting protects the host against MAC impersonation.

#24. What is the Forged transmits network policy?
The Forged transmits option affects traffic that is transmitted from a virtual machine.

When the Forged transmits option is set to Accept, ESXi does not compare source and effective MAC addresses.

VMware vCenter Server Interview Questions
#25. What are the main components of vCenter Server architecture?
vCenter Server provides a centralized platform for management, operation, resource provisioning, and performance evaluation of virtual machines and hosts.

When you deploy the vCenter Server Appliance, vCenter Server, the vCenter Server components, and the authentication services are deployed on the same system.

The following components are included in the vCenter Server appliance deployments:

The authentication services contain vCenter Single Sign-On, License service, Lookup Service, and VMware Certificate Authority.
The vCenter Server group of services contains vCenter Server, vSphere Client, vSphere Auto Deploy, and vSphere ESXi Dump Collector. The vCenter Server appliance also contains the VMware vSphere Lifecycle Manager Extension service and the VMware vCenter Lifecycle Manager.
#26. What are PSC and its components?
PSC stands for Platform Services Controller, first introduced in version 6 of VMware vSphere, which handles infrastructure security functions. It has three main components.

Single Sign-On (SSO)
VMware Certificate Authority (CA)
Licensing service
#27. What are the two main deploying methods of PSC?
You can install PSC in VMware vSphere 6.7 in two ways:

Embedded
External
But, in VMware vSphere 7.0, we can install PSC only in Embedded mode; External PSC deployment has been deprecated in VMware vSphere 7.0 or onwards.

#28. What are the different types of vCenter Server deployment?
It has two deployment types till VMware vSphere 6.7.

Embedded Deployment
External deployment
In VMware vSphere 7.0 and onwards, External PSC has been deprecated. We can only install PSC in Embedded mode.

#29. What is vRealize Operation (vROP)
vROP provides the operation dashboards for performance analytics, capacity optimization, and monitoring the virtual environment.

#30. What is vCloud Suite?
vCloud Suite combines multiple VMware components to give a complete set of cloud infrastructure capabilities in a single package, including virtualization, software-defined datacenter services, disaster recovery, application management, etc.

#31. What is the basic security step to secure vCenter Server and users?
Authenticate vCenter Server with Active Directory. By using this, we can assign specific roles to users and can also efficiently manage the virtual environment.

Virtual Storage (Datastore) Interview Questions
#32. What is a datastore?
A datastore is a storage location where virtual machine files are stored and accessed. Datastore is based on a file system which is called VMFS, NFS.

#33. What is the .vmx file?
It is the configuration file of a VM

#34. What information .nvram file store?
It stores BIOS-related information of a VM.

#35. What .vmdk file do and used?
vmdk is a VM disk file and stores data of a VM. It can be up to 62 TB in size in the vSphere 5.5 and onward versions.

#36. How many disk types are in VMware?
There are three disk types in vSphere.

Thick Provisioned Lazy Zeroes: every virtual disk is created by default in this disk format. Physical space is allocated to a VM when a virtual disk is created. It can’t be converted to a thin disk.
Thick Provision Eager Zeroes: this disk type is used in VMware Fault Tolerance. All required disk space is allocated to a VM at the time of creation. It takes more time to create a virtual disk compare to other disk formats.
Thin provision: It provides an on-demand allocation of disk space to a VM. When data size grows, the size of a disk will grow. Storage capacity utilization can be up to 100% with thin provisioning.
#37. What is Storage vMotion?
It is similar to traditional vMotion; in Storage vMotion, a virtual disk of a VM is moved from one datastore to another. During Storage vMotion, virtual disk types think provisioning disk can be transformed to thin-provisioned disk.

What’s New in vSphere 6.0
#38. What is the VM Hardware version for vSphere 6.0?
Version 11

#39. What VM hardware version for vSphere 6.5?
Version 13

#40. What VM Hardware version for vSphere 6.7 and vSphere 7.0?
Version 14 for ESXi 6.7, Version 15 for ESXi 6.7 U2, Version 17 for ESXi 7.0, Version 18 for ESXi 7.0 U1, and Version 19 for ESXi 7.0 U2

#41. In which version of vSphere PSC was introduced?
Platform Services Controller (PSC) is introduced in vSphere 6.0. vSphere 6.0 is also known as Virtual hardware version 11.

#42. How many maximum hosts can manage a vCenter Server in vSphere 6.0?
In vSphere 6.0, a single vCenter Server can manage up to 1000 hosts either in Windows or vCenter Appliance (vCSA). In vSphere 6.5 and 6.7, 2000 hosts, and in vSphere 7.0, 2500 can be managed by a single vCenter Server.

#43. How many hosts can be managed by a cluster in vSphere 6.0?
A single cluster can manage a maximum of 64 hosts in VMware vSphere 6.0 and onward versions.

#44. How can maximum VMs be managed by a single cluster?
A single cluster can manage a maximum of 8000 VMs.

#45. What is VVol?
Virtual Volume is a new VM disk management concept introduced in vSphere 6.0 that enables array-based operations at the virtual disk level. VVol is automatically created when a virtual disk is created in a virtual environment for a VM.

#46. How many licensing options are for vSphere 6.0?
There are three licensing options for vSphere 6.0:

Standard Edition: Contains 1 vCenter Server Standard license, up to 2 vCPUs for Fault Tolerance, vMotion, Storage vMotion, HA, VVols, etc.
Enterprise Edition: Same as Standard Edition additionally APIs for Array Integration and Multipathing, DRS, and DPM.
Enterprise Plus: Includes all Standard and Enterprise Editions features with additional Fault Tolerance up to 4 vCPUs and 64GB of RAM. It also includes Distributed vSwitch and the most expensive licensing option of vSphere 6.0.
#47. How much Maximum RAM can support vSphere 6.0?
It supports up to 12TB of RAM per host in vSphere 6.0 and vSphere 6.5 and 16TB of RAM per host in VMware vSphere 6.7 and 7.0.

Content Libraries Interview Questions
#48. What is the Content Library?
Content Library is the central location point between two different geographical locations with vCenter Servers where you can store VM templates, ISO images, scripts, etc. and share them between geographical locations

#49. What are the main benefits of content libraries?
We create VM templates and share on another geographical location without creating again on other locations. It has many benefits, such as sharing and consistency, storage efficiency, and secure subscription.

#50. How many types of Content Libraries have?
It has three types:

Local: library of local control.
Published: local library which contents (VM templates, ISO images, etc.) for a subscription.
Subscribed: A library that syncs with the published library
#51. What are the requirements and limitations of Content Libraries?
A content library has the following requirements and limitations

Single storage, which can size up to 64TB
Maximum of 256 items per library
Sync occurs once every 24 hours
#52. What is VMFS?
VMFS is a file system for a VM in VMware vSphere. VMFS is a datastore that is responsible for storing virtual machine files. VMFS can also store large files, which size can be up to 64TB in vSphere 6.0. In the latest versions of VMware vSphere, VMFS 6 is used to store VMs.

VSAN Interview Questions
#53. What is vSAN?
Virtual SAN is software-defined storage first introduced in vSphere 5.5 and is fully integrated with vSphere. It aggregates locally attached storage of ESXi hosts, which are part of a cluster, and creates a distributed shared solution.

#54. What is cold migration?
To move a powered-off VM from one host to another is called cold migration.

#55. What is Storage vMotion?
To move a powered-on VM from one datastore to another is called Storage vMotion.

#56. What are the different configuration options for VSAN?
There are two configuration options for vSAN:

Hybrid: Uses both flash-based and magnetic disks for storage. Flash are used for cashing, while magnetic disks are used for capacity or storage.
All-Flash: Uses flash for both caching and for storage
#57. Are there VSAN ready nodes are available in the market?
Yes, vSAN-ready, such as VxRail 4.0 and 4.5, are available in the market. VxRail is the combination of min 3 servers that are part of a cluster and can scale up to 64 servers.

#58. How minimum servers/hosts are required to configure vSAN?
To configure a vSAN, you should have a minimum of 3 ESXi hosts/servers in the form of a vSAN cluster. If one of the servers fails, a vSAN cluster will fail.

#59. How are many maximum ESXi hosts allowed for vSAN?
64 hosts are max allowed to configure a vSAN cluster.

#60. How many disk groups and max magnetic disks are allowed in a single disk group?
A maximum of 5 disk groups are allowed on an ESXi host, which is a part of a vSAN cluster, and a maximum of 7 magnetic and 1 SSD per disk group is allowed.

#61. How many types of storage can we use in our virtual environment?
Direct Attached Storage
Fiber Channel (FC)
iSCSI
Network Attached Storage (NAS)
#62. What is NFS?
Network File System (NFS) is a file-sharing protocol that ESXi hosts use to communicate with a NAS device. NAS is a specialized storage device that connects to a network and can provide file access services to ESXi hosts.

#63. What is Raw Device Mapping (RDM)?
Raw Device Mapping (RDM) is a file stored in a VMFS volume that acts as a proxy for a raw physical device. RDM enables you to store virtual machine data directly on a LUN. RDM is recommended when a VM must interact with a real disk on the SAN.

#64. What is iSCSI storage?
An iSCSI SAN consists of an iSCSI storage system, which contains one or more storage processors. TCP/IP protocol is used to communicate between host and storage array. an iSCSI initiator is configured with the ESXi host. an iSCSI initiator can be hardware-based, either dependent or independent, and software-based is known as an iSCSI software initiator.

#65. What is the format of iSCSI addressing?
It uses TCP/IP to configure.

#66. What are iSCSI naming conventions?
iSCSI names are formatted in two different ways:

the iSCSI qualified name (IQN)
extended unique identifier (EUI)
vApp Interview Questions
#67. What is vApp?
vApp is a container or group where more than one VM can be package and manage multi-tiered applications for specific requirements; for example, Web server, database server, and application server can be configured as a vApp and can be defined their power-on and power-off sequence.

#68. What settings can be configured for vApp?
We can configure several settings for vApp, such as CPU and memory allocation, and IP allocation policy, etc.

Miscellaneous Interview Questions
#69. What is VMware Tanzu?
VMware Tanzu is the suite or portfolio of products and solutions that allow its customers to Build, Run, and Manage Kubernetes-controlled container-based applications. This technology is introduced in VMware vSphere 7.0.

#70. What is VMware DRS?
DRS stands for Distributed Resource Scheduler, which automatically balances available resources among various hosts by using clusters or resource pools. With the help of HA, DRS can move VMs from one host to another to balance the available resources among VMs.

#71. What are share, limit, and reservation?
Share: A value that specifies the relative priority or importance of a VM access to a given resource.

Limit: Consumption of a CPU cycle or host physical memory that cannot cross the defined value (limit).

Reservation: This value defines in the form of CPU or memory and must be available for a VM to start.

#72. What are the alarms why we use them?
An alarm is a notification that appears when an event occurs. Many default alarms exist for many inventory objects. Alarms can be created and modified using vSphere Web Client;

#73. What are the hot-pluggable devices that can be added while VM is running?
We can add HDDs and NIC while VM is running.

#74. What is a Template?
When a VM is converted into a format that can be used to create a VM with pre-defined settings is called a template. An installed VM can be converted into a template, but it cannot be powered on.

#75. What is Snapshot?
To create a copy of a VM with the timestamp as a restore point is called a snapshot. Snapshots are taken when an upgrade or software installation is required. For better performance, a snapshot should be removed after a particular task is performed.

#76. How to convert a physical machine into a VM?
Three steps are required to convert a physical machine to a VM:

An agent needs to be installed on the Physical machine
VI client needs to be installed with Converter Plug-in
A server to import/export virtual machines
#77. What is vMotion, and what is the main purpose of using it in a virtual environment?
It is a very prominent feature of VMware vSphere used to live migrate running VMs from one ESXi host to another without any downtime. Datastores and ESXi hosts can both be used while vMotion.

#78. What is the difference between a clone and a template?
A clone is a copy of a virtual machine. Cloning a VM will save time if multiple VMs with the same configurations are required to configure. While a template is a master copy of an image created from a VM, which can be later used to create many clones. After converting a VM to a template, it can’t be powered-on or edited.

#79. What monitoring method is used in vSphere HA?
Network Heartbeat
Datastore Heartbeat
#80. How is the master host elected in vSphere HA?
When HA is enabled in a cluster, all hosts take part in a selection process to be selected as a master host. A host which has the highest number of datastores mounted will be selected as a master host. All other hosts will remain slave hosts.

#81. What is the purpose of VMware Tools?
It is a suite of utilities that are used to enhance the performance of a VM in the form of graphics, mouse/keyboard movement, network card, and other peripheral devices.

#82. What is VMware DPM?
Stands for Distributed Power Management is a feature of VMware DRS that is used to monitor required resources in a cluster. When the resources are decreases due to low usage, VMware DPM consolidates workloads and shut down the hosts which are not being used, and when resources are increased it automatically power on the un-used hosts.

#83. What is the ESXi Shell?
It is a command-line interface. It is used to run the repair and diagnostics of ESXi hosts. It can be accessed via DCUI, vCenter Server enables/disable, and via SSH.

#84. How to run ESXTOP on the ESXi host?
To run ESXTOP on an ESXi host, we’ll need two pre-requisites:

Install vSphere Client on a host where you want to configure
Enable SSH from DCUI by using the “Troubleshooting Options” link
#85. What is VMware vCenter Enhanced Linked Mode and How It Works?
VMware vCenter Server Enhanced Linked Mode (ELM) is one of the vSphere advanced features that allows connecting multiple vCenter Servers to provide a single interface where you can view, search, and manage permissions, replications of roles, policies, and licenses between multiple vCenter Servers.

It allows you to simplify enterprise virtual environments deployed in the same or multiple sites with multiple vCenter Server while deploying vCenter Server as VCSA or Windows Servers.


# Scenario based Interview Questions :

#1. An administrator wants to connect the ESXi host directly from the vSphere Web Client. Which ports are required for this purpose?

Typically vSphere Web Client is used to connect vCenter Server, and VClient is used to connect ESXi hosts. But vSphere Web Client can also be used to connect vCenter Server, but for this purpose, you will need 443 TCP, 902 TCP and UDP, and 903 TCP ports to be opened from Security Profile.

#2. The clock time of an ESXi 6.x host is not correct. What should an administrator do to correct this issue?

To correct the time on the ESXi host, modify the time for the host using the vSphere client and correct the NTP settings in the /etc/ntp.conf file.

#3. An administrator wants to shut down the host using the ESXi host. Which option would be used in the Direct Console User Interface to perform this task?

To shut down the host for Direct Console User Interface (DCUI), an administrator will press F12 Key.

#4. An administrator can access the ESXi host via vCenter Server using vSphere Web Client but cannot directly via VClient. What should he do to access ESXi host directly?

If the ESXi host connected to vSphere Web Client is being accessed and can’t be accessed directly, we should check that Lockdown is not enabled. If it is enabled, we should be disabled. Because if Lockdown is enabled, ESXi hosts can only be accessed via vCenter Server; you cannot directly access any host.

#5. An administrator wants to use the VMware Certificate Authority (VMCA) as an Intermediate Certificate Authority (CA). He already replaces the Root Certificate and Machine Certificates (Intermediate CA). What should he do next?

After replacing the root certificate and machine certificate (intermediate CA), the following two steps are needed to perform.

Replace Solution User Certificates (Intermediate CA)
Replace the VMware Directory Service certificate.
#6. If Strict Lockdown Mode is enabled on an ESXi host, which action should an administrator perform to allow ESXi Shell or SSH access for users with administrator privileges?

The administrator will add the users to Exception Users and enable the service to allow ESXi Shell or SSH access.

#7. SSO is an essential component of the vCenter Server. Which SSO component issues Security Assertion Markup Language tokens?

VMware Security Token Service component of SSO grants SAML tokens.

#8. What is a valid Identity Source used to configure vCenter Single Sign-On?

OpenLDAP is a valid Identity Source for configuring vCenter SSO.

#9. What happens to the files contained on shared storage When a Content Library is deleted?

When Content Library is deleted, all stored files in the content library will be deleted.

#10. What is the maximum number of vCPUs required for a VM in vSphere 6.0?

Maximum 128 vCPUs can be allocated to a VM vSphere 6.0.

#11. A windows domain user can be logged in to vSphere using vSphere Web Client. What are the requirements to be met for this feature to be available and functional?

An administrator can allow users to log in to vSphere Web Client using Windows session authentication. For this purpose, Install the vSphere Web Client Integration browser plug-in on each computer from where a user will sign in. The users must be signed in to Windows using Active Directory user accounts. And, an administrator must create a valid Identity Source in Single Sign-On for the users’ domain.

#12. An administrator wants to clone a virtual machine using the vSphere Client. Which explains why the Clone option is missing?

To clone a VM can be performed from vCenter Server either you connected via vSphere Web Client or VClient. If you are directly connected to an ESXi host, you cannot perform cloning of a VM.

#13. What will happen if the .nvram file is deleted accidentally from a VM?

.nvram file is used to store the BIOS state of a VM. If it is deleted for some reason, then, .nvram file will be created again when the virtual machine is powered on.

#14. An administrator wants to connect the vSphere 5.5 Client to ESXi 6.x host. What will occur?

If the administrator tries to connect the vSphere 5.5 Client to ESXi 6.x host, the operation will prompt the administrator to run a script to upgrade the vSphere Client.

#15. Which one of the secondary Private VLANs (PVLANs) types can send packets to Isolated PVLAN?

A promiscuous type of PVLAN can communicate and send packets to an Isolated PVLAN.

#16. What sample roles are provided by default when vCenter is installed?

When vCenter is installed, Virtual machine user and Network Administrator roles are provided.

#17. What will happen when all paths down (APD) event occurs for the software FCoE storage?

If all paths down events occur, Spanning Tree Protocol is enabled on the network ports.

#18. What methods are available for upgrade a host from ESXi 5.x to ESXi 6.x?

vSphere Update Manager (VUM), esxcli command-line tool, and vSphere Auto Deploy can be used to upgrade.

#19. What administrator should do before upgrading virtual machine hardware?

Before upgrading a VM hardware, we should create a backup or snapshot of the VM, upgrade VMware Tools to the latest version, and verify that the VM is stored VMFS or NFS datastore.

#20. vCenter Server up-gradation fails at the vCenter Single Sign-On installation. What should you do to complete the upgrade process?

Before upgrading the vCenter Server, please verify that the VMware Directory service can stop by manually restarting it. If it stopped manually, then you can start the up-gradation process of the vCenter Server.

#21. What prerequisites should be considered before upgrading the vCenter Server Appliance?

In case of up-gradation of vCenter Server Appliance (vCSA) or after fresh installation, Client Integration Plugin (CIP) will be installed in both cases.

#22. After deploying a PSC, vCenter Server is not being installed and shows the following error:

Could not contact Lookup Service. Please check VM_ssoreg.log.
If this error appears, verify that the clocks on the host machines running the PSC, vCenter Server, and the vSphere Web Client are synchronized. And also, ensure that there is no firewall blocking port 7444 between the PSC and vCenter Server.

#23. An administrator installed Windows Server 2008 and wants to install vCenter Server on it but failed when installing on a Windows virtual machine?

vCenter Server installation requires 64bit Windows OS to install. If you try to install it on Windows Server 2008, it will not be installed, and installation will be failed. vCenter Server will be installed in Windows Server 2008 R2 or higher Windows OS.

#24. What is the minimum Virtual Hardware version required for vFlash Read Cache?

vFlash Read Cache was first in vSphere 5.5, and the minimum Virtual Hardware version for vSphere 5.5 is version 10.

#25. ESXi host is added in vCenter Server but not responding in vSphere Web Client. If this issue occurs due to a firewall, which port should be opened?

If the administrator sees no response of added ESXi 6.x host in vCenter Server, the issue is caused by network firewall blocking traffic. Then he should check that port 902 (UDP) is not blocked by a firewall. If it happens, enable the port from Security Profile by using vSphere Web Client by selecting said ESXi host in vCenter Server.

#26. Suppose a VM is unexpectedly powered off. Which VM logs files should be considered to troubleshoot the issue?

If it happens, an administrator should check vmware.log and hostd.log log files to troubleshoot the issue.

#27. Why a VM appeared as an orphaned VM?

If a VM appears in an orphaned state, this could cause a VMware High Availability host failure has occurred. And the virtual machine was unregistered directly on the ESXi host.

#28. While upgrading an ESXi 5.5 host to ESXi 6.x, the following error appears: MEMORY_SIZE

What does this require to do?

It indicates insufficient memory on the ESXi host to complete the upgrade process of an ESXi host from ESXi 5.5 to ESXi 6.x.

#29. To remove a host from a vSphere Distributed Switch (vDS), the following error message is observed:

The resource ’10’ is in use

Before removing vDS, it is ensured that VMkernel network adapters on the vDS are not in use. If any of the resources of vDS is being used, then above mentioned error message with resource ID will appear.

#30. An administrator wants to monitor network traffic and capture network traffic for a VM but cannot see the expected traffic in the packet capture tool. What should he do to resolve the problem?

If an administrator needs to capture network traffic for a VM, he should Enable Promiscuous Mode on the relevant port group. Then you can capture the network traffic by using any networking traffic capturing tool.

#31. A vSAN Cluster is created with six nodes along with the fault domain, and three of them moved into the fault domain. A one-member node of the fault domain fails. What will happen with the remaining two nodes exist in the fault domain?

When a member node of the fault domain fails, the remaining two fault domain members will be treated as failed.

#32. At which level is a vSAN Fault Domain configured?

A fault domain is configured at the vSAN Cluster level, and nodes will be added to this domain. If any member node fails due to any reason, the remaining members of the fault domain will also be considered as fail.

#33. It is observed that a VM storage activity on an ESXi 6.x host is negatively affecting a VM storage activity on another host that is accessing the same VMFS Datastore. Which action would mitigate the issue?

To control the storage activity of a VM from affecting another VM’s storage activity, Storage IO Control (SIOC) should be enabled. Storage I/O Control provides much-needed control of storage I/O and should be used to ensure that the performance of your critical VMs is not affected by VMs from other hosts when there is contention for I/O resources.

#34. While upgrading an ESXi host from 5.5to 6.0, the administrator runs the following command:

esxcli software vib list --rebooting-image
What will be shown by this command?

This command will show all active VIBs (vSphere Installation Bundle). VIB is a collection of files like tarball or zip packaged into a single archive to facilitate distribution.

#35. To troubleshoot a CPU performance issues of a VM, which counters will be used to demonstrate CPU contention?

To test the performance of an ESXi host in the form of memory, CPU, and network utilization, the ESXTOP tool is used. It is an excellent tool available for VMware administrators to troubleshoot performance issues. For configuring ESXTOP, you’ll need vSphere Client, and putty and SSH sessions should be enabled. For CPU performance testing, %RDY, %MLMTD, and %CSTP counters are used.

#36. An administrator tries to run esxtop by enabling SSH and using putty to troubleshoot CPU performance issues, but no output is displayed. How to resolve this issue?

To display output in ESXTOP, press f and place an asterisk next to each field that should be displayed.

#37. An administrator wants to monitor VMs on a host using vCenter Server and send notifications when memory usage crosses 80%. What should an administrator do in the vCenter Server to accomplish this?

To monitor VM’s memory usage that reaches 80%, a vCenter Server alarm will be created to monitor VM’s memory usage and set an action to email the notification.

#38. An administrator created a DRS cluster, and it became unbalanced. What are likely causes to become unbalanced?

DRS cluster can become unbalanced when Affinity rules are preventing VMs from being moved. And a device is mounted to a VM prevents vMotion from one host to another.

#39. An IT administrator configured two vCenter Servers within a PSC and needs to grant a user privilege that can access all environments. What is the access level required to access all the environments?

To access multiple vCenter Servers within a PSC, requires Global Permission to access all environments.

#40. An administrator created 10 ESXi 6.x hosts via Auto Deploy for a new Test/Dev cluster, and all hosts are configured to obtain their IP address via DHCP. Which DCUI option should the administrator use to renew the DHCP lease for the hosts?

The “Reset Management Network” of the Direct Console User Interface (DCUI) option is used to renew the DHCP lease for the hosts.
