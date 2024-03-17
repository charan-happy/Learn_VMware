1. overview

2. Exploring VMware vSphere 6.7

3. Why choose vSphere 6.7


Virtualization :  Abstracting the computing resources from one machine to build another machine

Vmware vsphere is a comprehensive collection of products and features that together provide a  full array of enterprise virtualization functionality. The vSphere product suite includes the following products and features

    Ø Vmware ESXI 	The core of vSphere product suite is the hypervisor, which is virtualization layer that servers as the foundation for the rest of the product line.  The hypervisor solely comes in the form of Vmware ESXI in vmware

    Vmware vCenter Server	vCenter Server, like Active Directory, is meant to provide a centralized management platform and framework for all ESXi hosts and their respective VMs. vCenter Server allows IT administrators to deploy, manage, monitor, automate, and secure a virtual infrastructure in a centralized fashion. To help provide scalability, vCenter Server leverages a backend database that stores all the data about the hosts and VMs.
    
    vSphere Update Manager (VUM)	vSphere Update Manager is a component of vCenter Server that helps users keep their ESXi hosts and select VMs patched with the latest updates. 
    
    vSphere Update Manager provides the following functionality:
     ◆ Scans to identify systems that are not compliant with the latest updates 
     ◆ User-defined rules for identifying out-of-date systems 
     ◆ Automated installation of patches for ESXi hosts 
     ◆ Full integration with other vSphere features like Distributed Resource Scheduler

    vSphere virtual Symmetric Multi-processing	The vSphere Virtual Symmetric Multi-Processing (vSMP or Virtual SMP) product allows you to construct VMs with multiple virtual processor cores and/or sockets. vSphere Virtual SMP is not the licensing product that allows ESXi to be installed on servers with multiple processors; it is the technology that allows the use of multiple processors inside a VM

    vSphere vMotion and Storage vMotion	vMotion moves the execution of a VM, relocating the CPU and memory footprint between physical servers but leaving the storage untouched. Storage vMotion builds on the idea and principle of vMotion: you can leave the CPU and memory footprint untouched on a physical server but migrate a VM’s storage while the VM is still running.

    vSphere Distributed Resource Scheduler (DRS)	DRS, simply put, leverages vMotion to provide automatic distribution of resource utilization across multiple ESXi hosts that are configured in a cluster

    vSphere Storage DRS(SDRS)	Storage DRS helps balance storage capacity and storage performance across a cluster of datastores using mechanisms that echo those used by vSphere DRS.

    Storage I/O control (SIOC) and Network I/O Control (NIOC)	Storage I/O Control (SIOC) allows you to assign relative priority to storage I/O as well as assign storage I/O limits to VMs. These settings are enforced cluster-wide; when an ESXi host detects storage congestion through an increase of latency beyond a user-configured threshold, it will apply the settings configured for that VM. The result is that you can help the VMs that need  Priority access to storage resources get more of the resources they need.

    Storage based Policy Management (SBPM)	Profile-driven storage is built on two key components: ◆ Storage capabilities, leveraging vSphere APIs for storage awareness (VASA) 
    
    ◆ VM storage profiles Storage capabilities are either provided by the storage array itself (if the array can use VASA and/or defined by a vSphere administrator. These storage capabilities represent various attributes of the storage solution.

    vSphere High Availability (HA)	The vSphere HA feature provides an automated process for moving and restarting VMs that were running on an ESXi host at a time of server failure

    vSphere Fault Tolerance (FT)	vSphere FT will also automatically re-create the secondary (mirrored) VM on another host if the physical host for the secondary VM fails. This ensures protection for the primary VM at all times.

    vSphere Storage APIs	VADP is a set of application programming interfaces (APIs) that back up vendors leverage in order to provide enhanced backup functionality of virtualized environments. VADP enables functionality like file-level backup and restore; support for incremental, differential, and fullimage backups; native integration with backup software; and support for multiple storage protocols.

    Vmware Virtual SAN (vSAN)	vSAN pools the aggregate storage across the compute nodes, allowing you to create a datastore that spans multiple compute nodes.

    vSphere Replication	VSphere Replication enables customers to replicate VMs from one vSphere environment to another vSphere environment. Typically, This means from one datacenter to another data center. vSphere replication happens per-VM basis.

    Ø vSphere Content Library

Licensing :
--------------
vSphere licensing is based on the number of physical CPUs in the server, and the number of virtual machines that you want to run. There are three main types of vSphere licenses:

vSphere Essentials: This license allows you to run up to 3 virtual machines on a single physical server.
vSphere Standard: This license allows you to run up to 8 virtual machines on a single physical server.
vSphere Enterprise: This license allows you to run an unlimited number of virtual machines on a single physical server


