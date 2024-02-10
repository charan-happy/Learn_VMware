# Introdution to Vmware Vsphere

    1. Physical Datacenter
    2. Vmware ESXI 6.7

# Centralized Administration

    1. Vcenter Server
    2. Vsphere SSo

# Virtual Networking
    
    1. Introduction to Networking
    2. Standard Switch
   
# Virtual Storage

    1. Introduction to Virtual Storage
    2. Content Library

# Virtual Machine

    1. Introduction to Virtual Machine
    2. Virtual Machine Management
    3. Custom Specification file

# Resource Management and monitoring

    1. Managing resource and basic monitoring

# Host Scalability

    1. vSphere cluster and Disaster Recovery



# Introdution to Vmware Vsphere

    1. Physical Datacenter

![physical Datacenter](https://github.com/Charan-happy/Learn_VMware/assets/89054489/8800307d-9fd6-44a6-9957-2f28353a82b7)

![virtualization](https://github.com/Charan-happy/Learn_VMware/assets/89054489/c0ab4d46-7d1a-43ce-901d-c1b0c5de7145)

        physical Datacenter
            - Datacenter is a secured facility to house IT equipment's for enterprise organizations consisting of servers, networking devices and storage systems.
            - It provides complete redundancy on power supplies, environmental controls (ex; air conditionning, fire suppression, redundant data communications, connections and security Devices)
           
        virtualization 
                - It is a technique where underlying hardware is abstracted to present physical machine as multiple virtual machines.
                - Virtualization is achieved with the combination of hardware and a special software usually refered as "Hypervisor" or "Virtual Machine Manager"
                - the primary goal of hypervisor is to abstract computing resources of the hardware and seamlessly share with all virtual  machines running different guest operating systems in them.
              
               EX: VMWare Vsphere ESXI 6.7

    2. Vmware ESXI 6.7

        Introduction to vSphere ESXI 6.7
                - vsphere is a infrastructure virtualization Suite providing - virtualization, management, resource optimization, application availability along with operational automation capabilities bundles in a package.
                - Vsphere usually consists of ESXI host and VCenter server.
                - Vsphere ESXI 6.7 is a production ready hypervisor sold in kits of licenses.
                - Vcenter is sold separately. It is essential for centralized management of multiple ESXI hosts.
                - Hypervisors are also referred as virtual machine manager (VMM)

        Hardware Requirements
             To install VSphere ESXI 6.7 host machine must have :
                    1. Processor
                        - 64-bit x86 processors released post september 2006
                        - Atleast two CPU cores with NX/XD bit enabled in BIOS
                        - Hardware virtualization on 64 bit CPU must be enabled to accomdate 64 bit VMS.
                   
                    2. Memory
                        - Minimum 4 GB RAM , Recommended 8 GB
                    3. Network
                        - one or more Gigabit or faster Ethernet controllers
                        
        Deployment of ESXI
            ESXI installation can be done :
                    - Interactively using CD/DVD or USB
                    - Using Scripts
                    - PXE Booting (network based installation)
                    - vSphere Auto deployment
        
        ESXI's User interface
            1. Direct Console user interface (DCUI)
            2. VSphere 6.5 HTML Client (GUI)
            3. CLI's -->ESXI Shell (local text support) and SSH SHell (Remote text support)
            4. Common information model (CIM)
            5. VMWare VSphere API/SDK
        
        Post Deployment configuration
                1. Log into Direct Console user interface (DCUI)
                2. Perform management network configurations and test
                3. Enable CLIs for troubleshooting
                4. Using ESXi host client (HTML 5 based)
               
               Enable NTP (NTP client - uses UDP and port #123 to communicate with NTP server). Input license key, view system logs.

        Resource Management in ESXI
            Following operating system's resources on physical system are virtualized and shared among VMs by vSphere ESXI
            1. compute (CPU and RAM)
                - Time slice the physical processor across all VMS
                - Contiguous addressable memory space is created for all VMS when started.
                - Explicit locks imposed to ensure virtual memory of one VM is not access by another VM.
            2. Network
                - Majority of protocols available on physical switches are supported virtual switches.
                - Supports: VLANs, NIC teaming and outbound to external network
                - Single tier networking only allowed . No need of spanning tree protocol
            3. Disk
                - VM File system (VMFS) - supports multiple ESXI hosts simultaneous read /write access to common shared storage resources.
                - VMFS - a clustered file system specially designed for high performing VMS
                     - It provides strong base for following 
                           - Distributed infrastructure services - live migration, HA, DRS, FT
               - It shares interfaces with storage resources which enables several storage protocol (FC, FCOE & ISCSI) to access the datastores where VMs can reside.
               - VMFS store all files that makes up a one VM into a single folder. Hence, helps achieving business continuity or disaster recovery.
               - VMFS datastore can grow dynamically with aggregation of storage resource with zero downtime.

# Centralized Administration

    1. Vcenter Server

        vCenter server 6.7
            - vCenter Server is mandatory for centralized administration of all ESXI hosts and VMS.
            Deployment Types:
            1. windows based vCenter server - require microssoft KB 2897602. Installing vCenter server on windows server operation system and configured.
            2. vCenter Server Appliance (VCSA)
                    - vCenter server installed and configured on SUSE linux and available as OVF or OVA file for deployment.
        vCenter Server Installation
            - vCenter server deployment involves following components installation:
                    1. Database Server
                    2. VMware vSphere single sign on
                    3. vSphere web client (GUI)
                    4. Additional Services
                    5. Platform Services Controller
                  
        vCenter Server Composition
            - vcenter server is a collection of following services :
                1. Database :
                    - Stores critical data: inventory items, security roles, resource pools, performance, info --inbuilt postgreSQL database supports 2000 hosts and 35000 VMS. External oracle database for enterprise
                2. Core Services :
                    Management of : Resources, VMs, inventory services, scheduled tasks, log's, alarms and events. 
                    Additional Services : vsphere update Manager, vRealize orchestrator and few more.
                3. Distributed Services :
                    Live VM migration (vMotion)
                    vSphere High Availability (HA)
                    vSphere Distributed resource Scheduling (DRS)
                4. ESXI Management
                    Establishes communication between vCenter server and ESXI hosts.
                    enables centralized administration.

                5. User access Control
                    - creates and manage users, groups
                    - Assign roles and permissions
                6. vSphere SDK
                    - collection of application programming interface (APIs)
                    - Enables to create customized applications, plugins with vCenter
                7. vCenter Server lookup Services
                    - Enables secure communication of components in vSphere infrastructure.
                8. vCenter single sign on 
                    - integrates external identity source with vSphere infrastructure
                    - Identify sources supported by vCenter Server :
                        - Active Directory (integrated windows authentication)
                        - Active directory as an LDAP server
                        - open LDAP
                        - Local OS
                        
        Platform Service Controller (PSC)
            - vCenter server can be deployed either on Physical or virtual machine and choosing any one of following modes :
                - Embedded PSC
                - External PSC
        
            - Platform service controller - includes few shared inseparable infra services:
                    - vCenter single sign on (SSO)
                    - License Server - for centralized license management in  vsphere and integrated products.
                    - Lookup service - to manage multiple instances of vCenter server
                    - Certification authority (CA)
                    - certificate store
                    - Directory service
        PSC Deployment
            - Recommended :
                - Enhanced linked mode with external PSC with or without vSphere HA
            - Not recommended :
                - Enhanced linked mode with embedded PSC
                - combining both deployment methods - embedded and external PCS
       
        Additional components
            - vSphere web client -GUI to vCenter server
            - vSphere auto deploy : Enables installation of ESXI on multiple diskless hosts
            - vSphere ESXI Dump collector: Consolidates VMKernel memory dumps from multiple ESXi's to a server on network, instead of disk when host failure occurs.
            - vSphere syslog collector : redirects ESXI's logs to common server on network
        
        ESXI hosts interaction with vCenter Server
            - Daemon process running on ESXI host -Hostd
            - Daemon process running on vCenter - vpxd
        - when host added, vCenter server deploys agent "vpxa" on ESXI
        VCSA 6.7
            SUSE Linux based virtual appliance.

            Consists of embedded DB: PostgreSQL - supports max 2000 ESXI's and 35000 VMs.
            Also accomdates external DB (like oracle)

            less expensive

            can be accomdated with external PSC

            vcenter appliance instance can be combined with windows based vCenter server

            linked mode is also supported

        vSphere web client
            vCenter server's GUI.
                contains multiple pane's which can be pinned/unpinned.
                1. Navigator
                    - Host & cluster inventory (default view)
                    - VMs & Template inventory
                    - Storage inventory
                    - Network inventory
                
                2. Recent objects
                3. Recent tasks
                4. Alarms
                    vcenter server "Home" page contains:
                        - inventories
                        - Operations and policies
                        - Administration
                        - Plug-ins for installation
                        
        user Access Control
            The access control system allows the vCenter server administrator to define a user's privileges to access objects in the inventory

            Key Concepts:
            
            1. Roles:
                - Allow Users to execute tasks.
                - clustered in categories
                - can exist as: system roles, sample roles and custom-built roles
            
            2. Objects:
                - objects are entities on which actions are executed.
                - objects can be data centers, folders, resource pools, clusters, hosts, datastores, networks, and VMs.
                - All objects have a Permissions tab
            
            3. user/group:
                - person or group involved in execution of the action.
            4. Privilege:
                - combination of a user or group and a role that is applied to an object in the inventory
                - Propagate down the object hierarchy to all sub objects or it can be applied only to an immediate object
                - As a best practice, always define a role using the minimum number of privileges possible for better security and added control
                
        Access control to ESXI       

            ESXI Firewall
                - To restrict the access based on ports
                - the remote access is allowed based on IP or IP range
           ESXI Lockdown mode
                - only vpxUser have authentication permission
                - only vCenter can administer the ESXI. All other modes are disabled
                - DCUI is enabled with root user account.
         
    2. Vsphere SSo
        Demo
# Virtual Networking
    
    1. Introduction to Networking
    
    vSwitches
      
    standard vSwitch
          - created & configured on an ESXI host
    Distributed vSwitch
      - created & configured on vCenter server at data center level.
      - works as standard switch spanning across multiple hosts
      - Enables VMs to preserve consistent network configuration, as they migrate

    Standard Switch - software version of L2 switch supporting both IPV4 and IPV6

    It accomdates:
        - virtual machine port groups
        - VMKernel ports: Needed to connect storage, migration, HA, DRS, FT, VSAN, ESXI Management

    Port group - Template containing configuration details to create virtual switch ports on either standard or distributed virtual switch.

    - virtual machine port group & VMKernel port will connect VMs to outside world through Physical NIC(s) connected to UPLink ports of virtual switch
    - Designing virtual network depends on the layout of physical network
    - All ports or port groups on vSwitch will share smae uplinks (NICs)
    - NIC teaming is supported.
    - CISCO discovery protocol (CDP) details can be viewed on physical NCIs.
          - if CDP enabled administrator can identify physical switch port linked to vSwitch
          - physical switch's property (software version, device id ..etc) can be viewed in web client   
    
    vLAN Tagging

        ESXI (VMkernel) supports VLAN tagging  - IEEE 8.2.1Q standard.

        VLAN IDs are assigned (configured) at port group's level
            - At source, VM's packets are tagged with VLAN ID when exiting vSwitch.
            - untie the same when packets received by vSwitch and delivered to destination.
    Advantages of VLAN :
        - save money
        - configuring multiple software based broadcast domains
        - Restricting traffic to a subnet of switch port.

    Configuring standard vSwitch
            Network Security policy
                - Promiscuous mode
                - MAC address change
                - Forged transmit
            Traffic shipping (outbound only) - restrict network traffic to a VM or group of VMs and for security

            NIC Team - for load balancing , fail over detection and management

            - originating port ID
            - Source MAC Hash
            - Source/Destination IP Hash

    Distributed vSwitches
        - Elevates network management to datacenter level
        - DVswitch behaves like template for network configuration on individual ESXI's 
        - Allow configuration of virtual machine port group or VMKernel port - refered as distributed ports. It's state is stored in vCenter server DB.
       
        - No. of uplink ports on DVswitch indicates Max # physical NICs allowed.
      
      Benefits :  
        - Streamline datacenter management
        - Allows availing features - private vLAN, port mirroring, inbound traffic shapping etc
        - Migrates networking statistics and policies along with vMotion.
        - Allows customization if any required
    DVSwitch consists of :
      1. control plane :
            - Resides inside vCenter server
            - In charge of configuring DVSwitch, distributed ports/port groups, NIC teaming
            - Accountable for port migration
      2. I/O plane
            - Refered as hidden virtual switch (DVSwitch template) in VMM
            - Manages I/O hardware on the host
            - Liable for forwarding packets.
    1. Standard Switch
        Demo
# Virtual Storage

    1. Introduction to Virtual Storage
        Types of Storage
            vSphere supports following storage technologies:
                1. Direct attach storage (DAS)
                  
                2. Storage area network (SAN)
                    - Fiber channel
                    - ISCSI
                    - Fiber channel over ethernet (FCOE)
                3. Network attached storage (NAS)
                    - network file system (NFS)
                    - Common internet File system (CIFS)
                 Note : CISF is not supported by VMware Vsphere

|storage type|Format of data|cost|performance |
|---|---|---|---| 
|DAS|Block|least|good|
|FC|Block|Expensive|Excellent|
|ISCSI|Block|Nominal|Better|
|FCOE|Block|Nominal|Better|
|NAS|file|Nominal|Better| 

        Datastore
            - a logical storage unit located either on a disk space or span across several physical devices
            - Datastores contains - VM files, templates and ISO images
        Types:
        1. VMFS Datastore :
            VMFS is optimized for storing & accessing large files
            
            max volume size of VMFS datastore is 64 TB.

            Allows concurrent access to shared storage

            Expands dynamically

            Block Size: 1 MB, suitable for storing large virtual disk files (62 TB)

            Usage of sub block addressing, suitable for storing small files :
                - sub block size : 8 kb
                Features supported :

                - on disk & block level locking
                - Migration of live virtual machine from one ESXI host to another without downtime
                - Auto restarting of a suspended or failed virtual machine on another esxi host
                - clustering of virtuall machines across multiple physical servers.
               
        2. NFS Datastore
                - File system level storage shared over the network
                - Supports NFS version 3 over TCP/IP
                - NFS is used for file sharing between unix systems
        
        Configuring software ISCSI

            - Configure a VMKernel port for accessing IP storage
            - Enable tthe ISCSI software adapter
            - configure the ISCSI qualified name (IQN) and alias (if required)
            - configure ISCSI software adapter properties, such as static or dynamic discovery addresses and ISCSI port binding
            - optional ISCSI security configuration using challenge handshake authentication protocol (CHAP)
          
          To configure ISCSI storage multipathing:
                - use multiple NICs
                - Connect each NIC to a separate VMKernel port
                - Associate VMKernel ports with the ISCSI initiator
        
        Raw Device Mapping
            - RDM enables VM to store data directly on the lun
            - The mapping file is hosted on  VMFS datastore and is linked to the raw LUN
        
        Use RDMs if your VM meets following conditions :
            - To take snapshots at storage array level
            - If clustered to a physical machine
            - if hosting huge amount of data & does not want to convert into a virtual disk
            
        Configuring NFS Datastore

            1. Create a VMkernel port: Separate it from the ISCSI network
            2. Provide the following information:
                    - NFS server name (or IP address)
                    - Folder on the NFS server, For ex: LuN1 & LUN2
                    - Export folder with no_root_squash permission
                    - Host to create datastore on 
                    - whether to mount the NFS file system read-only
                    - Default is to mount read/write
                    - NFS datastore name
                  
            3. Configure on each ESXI host that you want to access the datastore
                Note : NFS datastores are suitable for storing VMs, however does not support all features
        vSAN
            - Enabled on cluster, grouping SSDs and local hard disks drives of each host -software defined storage
            - File system created on VSAN -"object store file system "
            - Data on VSAN resides in the form of flexible data container referred as objects
            - vSAN datastore --> logical volume spanning across entire cluster. It consists of both data and meta data
          
          
            - single VSAN can have mulitple storage policies associated
            - OSFS and VMFS volume on each host will be combined to a single datastore.
             VSAN version -6.5 

             VSAN datastore consists of :
                - Namespaces (home folder)
                - VM files - VMDK or VMSD or VSWP files
      
      VSAN pre-requisistes :
        1. vcenter server
        2. create a cluster of ESXI's (min 3 nodes) each node :
            - Must have computing resource
            - Min one SSD along with HDDs.

        SSD --> Read cache & write buffer
        
        HDD --> Persistent storage

        3. Must have a dedicated network with 2 NICs (each 10 GB speed for FT)
        4. vSAN cluster consists of max 8 nodes (hosts)

       Note : Host without local storage can also be part of VSAN. however Host's local storage and VSAN cannot coexist together independently

        virtual Volumes (VVOl)

            Converged storage (DAS/SAN/NAS & Cloud) abstraction layer, providing services like :
                - Forming useable storage resource pools
                - Enable rapid replication, cloning, VM-level data services
                - Improved DR & data guard facility
                - Auto mapping pre-VM storage policies to storage capabilities
       
       VVOL pre-requisites :
        1. storage array must be VMware vsphere API storage awarness (VASA) compatible
        2. API takes care - virtual disk creation, management operations
        3. No need to configure Luns or NFS storage
        4. Administratior must :
            - create protocol end point - SPOC to access virtual disks
            - Define storage container - storage capabilities (static or dynamic size & spans on storage array)
        
        VVOL Advantages :

            - Minimize storage expenses 
            - Decreases manual effort involved in storage management
            - Handle exponential data growth
            - Quick reaction to data access and analysis needs.
            - Policy based provisioning along with capability monitoring
            - Fine tuning support
            

        Comparing storage protocols

|protocol|Boot Enable|vmotion|vSphere HA|DRS|RDM|
|---|---|---|---|---|---|
|fC|yes|yes|yes|yes|yes|
|ISCSI|yes|yes|yes|yes|yes|
|FCOE|yes|yes|yes|yes|yes|
|NFS|yes|yes|yes|yes||
|DAS|yes|yes|||yes|
|VSAN||yes|yes|yes||
|VVOL||yes|yes|yes||

    1. Content Library
    
  - A VMware content library is a repository containing virtual machine templates and other types of files12. It is a solution that allows customers to keep their virtual machine resources synchronized in one place31. It is available in vSphere 6.0 and later31. Customers can use the templates in the library to deploy virtual machines and vApps in the vSphere inventory.

- content library provides several benefits including centralized storage, easy deployment, version control and sharing

vApps in VMware

A vApp, or virtual application, is a logical grouping of virtual machines (VMs) and their associated resources, such as storage and networking, that can be managed as a single entity. vApps provide a way to simplify the management of complex virtual environments by allowing administrators to perform operations on multiple VMs at once.

vApps can be used to create and deploy applications, test new software, and provide disaster recovery capabilities. They can also be used to isolate workloads from each other, which can improve security and performance.

To create a vApp, you must first create the VMs that you want to include in the vApp. Once the VMs have been created, you can use the vSphere Client to create a vApp and add the VMs to it.

vApps can be managed using the vSphere Client or the vSphere Web Client. The vSphere Client provides a graphical user interface (GUI) for managing vApps, while the vSphere Web Client provides a web-based interface.

vApps are a powerful tool for managing virtual environments. They can simplify the management of complex environments, improve security and performance, and provide disaster recovery capabilities.


VMware tools :
    - VMware Tools is a suite of utilities that enhances the performance and usability of virtual machines running on VMware vSphere. It provides a variety of features, including: Enhanced performance, Improved usability, Increased security.

# Virtual Machine

    1. Introduction to Virtual Machine
        Collection of files

            - Collection of virtual hardware constitute a virtual machine
            - VM folder in VMFS datastore contains following files :
                 <vm-name>.vmx --> Configuration file
                 <vm-name>.vmdk & <vm-name>-flat.vmdk --> virtual harddisk files
                 <vm-name>.nvram --> file containing VM's BIOS Settings
                 <vm-name>.log --> VM's current log file & #.log ---> set of files used to archieve old log entries
                 <vm-name>.vswp --> swap files used to reclaim memory during periods of contention
                 <vm-name>.vmsd --> snapshot description file
                 <vm-name>.vmtx --> if VM is converted to VM template, .vmx file will be replaced by .vmtx
                
        VMS Maximum Thresholds
            - vcpus: 256
            - vMemory: 6128 GB
            - VMDK Size: 62 TB
            - VM hardware Version: 14
            - vNICs: 10
            - SCSI adaptor: 15
            - CD/DVD, floppy and USB drive : 1
       
       Note : VMware tools installation is mandatory on all virtual machines

        SCSI Adapters
            By inducing 1st virtual disk to the VM, a SCSI adapter gets auto added

            ESXI offers following SCSI adapters & are choosen based on guest OS.
            - BUSLogic parallel
            - LSILogic parallel
            - LSILogic SAS
            - VMware Paravirtual SCSI
            - AHCI SATA controller
          
        Virtual disk and Vm's configuration file resides in same location.

        Types of Virtual Disks
|Types|Thick provisioned (lazy Zero) | Thick Provisioned (Eager zero) |Thin Provision |
|---|---|---|---|
|Time Taken| less |Less and depends on disk's size| least|
|Virtual Disk Layout|contiguous file blocks usually|contiguous file blocks definitely|varies & depends upon the dynamic state of the voluem at the time of block allocation|
|Zeroing of allocated data blocks|when first write operation initiated on the block| when blocks are created and allocated|when blocks are allocated|
|Block allocation|Fully preallocated|Fully preallocated| Allocated and expanded on demand|

        Advantages of thin provision :

            - optimizes the allocation of storage for the virtual environments
            - Enables VM's to consume space on demand
            - Enables existing storage to be shared among VM's on the ESXI server & hence economical
            - provides alarms & reports facilities to track allocation vs current usage of storage capacity
            - Supports storage array duplication to improve storage usage and to backup VMs.
      
        Virtual Disk Mode

                There exist special disk mode - Independent <br>
                        It has two options: Persistent and Non Persistent

        Virtual NIC

        Following types are available:
            - e1000 - e1000e: High performance NICs for few guest Os's
            - VMXNET2 and VMXNET3: need VMware tools as drivers
            - Single Root - IO virtualization (SR-IOV) pass-through: eliminates need of VMKernel port group while exchanging data between VM and Physical NIC. Supported by ESXI 5.5 and later for RHEL 6, windows server 2008 R2 with SP1 etc
        
    2. Virtual Machine Management

            Virtual Machine Management

                It involves: Creating Templates & clones, Modify VMs, Migrate VMs, Create VM Snapshots, Create a vApp

            Template

                Master copy of a VM, using which new VMs can be provisioned quickly.

                Template image includes:
                    - A specific VM's configuration
                    - guest OS
                    - Set of applications
            
            -  Template can be created in following methods:

                1. Clone VM to template

                    VM can be either in powered on or powered off state. original VM remains unchanged.

                    While Cloning to template virtual disk can be :
                        - Remain in same format as source
                        - Thin-provisioned
                        - Thick Provisoned (LZ)
                        - Thick Provisioned (EZ)
                       
                2. Convert VM to template
                    - VM Must be in powered off state. original VM is replaced by template (.vmx file will be replaced by .vmtx file)
               
                3. clone a template 
                    - Select existing template in inventory and then clone to new template
            Clone

                - cloning is an another method availed to deploy VM from template
                - A clone is an identical Copy of the VM
                - Cloned VM can be either in powered on or powered off state
                - VM cloning from one datacenter to another is possible
                - VM can also be deployed from a template in one datacenter to another datacenter
             
            Migration

|Migration Type|Virtual Machine Power state|Change Host or Datastore|Across virtual Data Center|Shared Storage|CPU compatibility|
|---|---|---|---|---|---|
|Cold|off|Host or datastore or both|yes|no|Different CPU families allowed|
|suspended|Suspended|Host or datastore or both|yes|No|Must meet CPU compatibility requirements|
|vMotion|on|Host|No|yes|Must meet CPU compatibility requirements|
|storage vMotion|on|Datastore|No|No|NA|
|Enhanced vMotion|on|Both|No|No|Must meet CPU compatiblity requirements|

            Pre-requisites and Limitations of vSphere vMotion

            - A visibility to all storage (DAS, SAN or NAS) used by the VM.
            - permits 128 parallel vMotion migrations/VMFS datastore
            - Minimum Network adapter's capacity : 4 concurrent vMotion migrations/Gb and 8 concurrent vMotion migrations/10 Gb
            - Identically named virtual machine port groups are connected to the same physical networks.
            - Compatible CPUs :
                  - CPU feature sets of both hosts must match
                  - Certain features can be concealed by using Enhanced vMotion Compatibility (EVC) or compatibility Masks.
           
            Pre-requisites and Limitations of vSphere Storage vMotion

                - Use the VMkernel data mover or storage APIs - Array Integration(VAAI) to copy data.
                - Mirror I/O calls to file blocks copies to virtual disk on the destination datastore
                - Perform upto 4 parallel disk migrations per operation
                - The limit is two concurrent svMotion operations per host
            
            Enhanced vMotion compatibility(EVC) operational concept

                    - Enhanced vMotion migration is a manual process
                    - DRs and vSphere Storage DRS do not leverage enhanced vSphere vMotion
                    - Maximum of two concurrent Enhanced vMotion migrations per host supported
                    - Enhanced vMotion migrations count when considering concurrent limitations for both vSphere vMotion and vSphere storage vMotion.
                    - Enhanced vMotion Migration uses Multi-NIC when available
                   
            Snapshots

                - snapshots enable you to roll back the state of the VM so that you can return to the same state repeatedly.
                - snapshots give the ability to back out of the patch or upgrade process if problems occur during patching or upgrading
                - This feature avoids the need to create multiple VMs.
            
                Snapshot consolidation :

                    - A technique employed to commit a chain of snapshots to the original VM.
                   Note : delta files continue to remain on the datastore even when the snapshot manager shows snapshot does not exist.

                   - snapshot consolidation resolves known issues with snapshot management like:
                         - The snapshot descriptor file is commited directly, but snapshot manager falsly displays that all snapshots are removed.
                         - The snapshot files (-delta, vmdk)are still part of the VM
                         - Snapshot files continue to expand until the VM runs out of datastore space.
                      
            vApps
                - vAPP is a container for one or more VM.
                - It is an object in the vCenter server inventory and served to package/manage related applications.
                - The following configurations are done in vAPP settings:
                        - CPU and Memory allocation
                        - IP allocation policy
                        - VM startup and shutdown order
                      
    1. Custom Specification file

            Demo

# Resource Management and monitoring

    1. Managing resource and basic monitoring
   
        Resource Pools

        - Required for controlling and coordinating compute (CPU & Memory resource)
        - Enables admins to divide and allocate resources to VMs and other resource pools
        - Consolidating and managing resources from different hosts in DRS
        - organized in hierarchical pattern
        - Also serve as a means to delegate privileges to other users and groups.
       
       Resource Management Parameters:

            Shares - Guranteed proportion of compute resources

            Reservation - Bare min resources needed

            Limit - Max resources allocated to the pool

            Expandable reservation - Pool specific attribute

        Monitoring Resources

            Monitor OS resources with appropriate tools

            Tools available in VMs guest OS (windows): Perfmon, IOmeter, Task Manager

            Monitoring tools available within vSphere ESXI and vCenter Server : vSphere logs, vCenter performance Charts
            
            vRealize Operations Manager (vrops) : 
                - Used for virtual Infrastrucuture (vSphere) monitoring.
                - Gathers performance data from each object at every level.
                - Stores data for analysis :
                      - Supply near real-time info about issues or potential issues
                      - offers analysis at a deeper level than vCenter server provides.
        
        Alarm

            - A notification sent as reaction to selected circumstance that occur with an object in vSphere ecosystem
            - predefined alarms exist and can be configured to our needs.
           
           Types of alarms :
                - Condition based alarm monitor for specific condition or state
                - Event based alarm monitor for specific events occuring on this object.
               
        - An alarm requires a trigger
  
        Types of Triggers:

        1. Condition based  - alarm triggered when a predefined condition is satisfied
                EX: A VM's current snapshot size is above 2 GB. A host using 90% of its total memory
        2. Event based alarm triggered when an event occurs:

                    EX: Host's hardware health has changed, A license has expired in the data center

        memory Over commitment

            - Allows host to configure more memory for VMs than it physically has.
            - VMs do not always use their full allocated memory
            - Memory overhead is stored in a swap file (.vswp)
            - Hypervisor/VMM manages allocation and reallocation of compute to VMs based on demand
          
          EX: Host machine memory is 4 GB and memory allocation to VMs created is 8 GB.

        Memory Reclaiming Techniques

            1. Economize use of physical memory pages :
                - Transparent page sharing facilitates pages having identical contents to be stored only once.
               
            2. Deallocate memory from one VM for another
                    Ballooning mechanism, is invoked when memory is scarce, forces VMs to use their own paging areas.
            
            3. Memory Compression
                - When memory contention is high, this method attempts to reclaim some memory performance.
                
            4. Host level SSD Swapping
                - Utilizes solid state drive (SSD) on the host for a host cache swap file which might increase performance.
                
            5. Page VM memory out to Disk
                    - usage of VMKernel swap space begins as the last resort. performance drops down.
        
        Hyperthreading

            - Hyper  threading enables a core to execute two threads (logical CPUs) or sets of instructions, at the same time.
            - To enable Hyperthreading :
                    - verify that the system supports hyperthreading
                    - Enable hyperthreading in the system BIOS
                    - Ensure that hyperthreading for the ESXI host is turned on.


# Host Scalability

    1. vSphere cluster and Disaster Recovery

        Cluster
            - Creating cluster means grouping ESXI host's inside vSphere to share resources
            - When hosts are added to cluster, resource pool of each host will merge within cluster resource pools
            - Features supported on cluster :
                    - vSphere High Availability (HA)
                    - vSphere Distributed Resource Scheduler (DRs)
                    - virtual Storage Area Network (vSAN)
                    - Fault Tolerance (FT)

        vSphere High Availability

            - VMware has simple inexpensive and higher level of availability solution for important work loads running on VMs with benefits:
                - Hardware non specific
                - Minimizes planned downtime for usual maintainance activities
                - Auto recovery if failure occurs

            If HA is configured on cluster,
            - one host will be elected as "Master" automatically. master interacts with vcenter server and monitors the state of all slave hosts and their VMs.
            - in case of failure, VMs on failed host are migrated (vMotion) and restarted on another host. Hence, HA does not assure Zero downtime.
            - Heart beat messages are exchanged via network and datastore.
        
        Distributed Resource Scheduling

            cluster is well balanced when resources on the every host is evenly utilized

            DRS :
                - Uses cluster-level balance metrics(standard deviation of resource utilization data from hosts in the cluster) to implement load-balancing decisions.
                - Executes its algorithm once every 5 minutes (by default) to study imbalance in the cluster.
                - Leverage vMotion to migrate running VMs from one ESXI host to another.
            
            Goals of DRS :
            - scale and manage compute resources.
            - Optimal workload balance for better performance
            - Minimizes administration effort
          
          Automation levels to configure DRS :
                - Fully automated - DRS applies initial placements and load balancing recommendations automatically.
                - partially automated - DRS applies recommendations only for initial placements
                - manual - DRS suggests both initial placements and load balancing recommendations. Implementation is manual.
        
        vSphere Fault Tolerance

            - vSphere fault Tolerance provides continuous availability (zero downtime) for VMs.
            - This is achieved by creating a live shadow copy (secondary) of the running VM (primary) and then placing that in virtual lockstep.
           -  Vmware vLockstep technology capture inputs and events that occur on the running VM (captures changes in the compute) and forwards the same to the live shadow copy which is running on another host.
           -  FT created and maintained identical to and continuously available running VM is replaced by its shadow copy, in the event of fail over situation.
           

iSCSI in VMware

iSCSI (Internet Small Computer System Interface) is a storage networking standard that allows data to be transferred over an IP network. In the context of VMware, iSCSI is used to connect virtual machines (VMs) to storage devices that are located on a separate physical server. This allows VMs to access storage resources without being directly connected to them, which provides greater flexibility and scalability.

iSCSI works by encapsulating SCSI commands within TCP/IP packets and sending them over an IP network. This allows iSCSI to be used over any type of IP network, including Ethernet, Fibre Channel over Ethernet (FCoE), and InfiniBand.

To use iSCSI in VMware, you will need to install the vSphere iSCSI Software Initiator on each ESXi host that you want to connect to iSCSI storage. You will also need to configure the iSCSI storage device to allow connections from the ESXi hosts.

Once you have configured iSCSI, you can create VMFS datastores on the iSCSI storage devices. VMFS datastores are used to store virtual machine files. You can then create and deploy VMs on the VMFS datastores.

iSCSI is a reliable and efficient way to connect VMs to storage devices. It is a cost-effective solution for organizations that need to provide storage for a large number of VMs.

Memory Virtualization

Memory virtualization is a technique that allows multiple virtual machines (VMs) to run on a single physical machine. Each VM has its own virtual memory address space, which is isolated from the memory address spaces of other VMs. This isolation is achieved through the use of hardware-assisted virtualization (HAV) or software-based virtualization (SBV).

HAV uses special hardware features to create and manage virtual memory address spaces. These features include:

Page tables: Page tables are data structures that map virtual memory addresses to physical memory addresses. HAV uses special hardware to manage page tables, which allows for fast and efficient address translation.
Segmentation: Segmentation is a technique that divides memory into segments. Each segment has its own access rights, which can be used to protect memory from unauthorized access. HAV uses special hardware to manage segmentation, which allows for fine-grained control over memory access.
SBV uses software to create and manage virtual memory address spaces. SBV does not require any special hardware, but it can be less efficient than HAV.

Benefits of Memory Virtualization

Memory virtualization offers a number of benefits, including:

Isolation: Memory virtualization isolates the memory of each VM from the memory of other VMs. This isolation helps to protect VMs from security breaches and software crashes.
Portability: Memory virtualization allows VMs to be easily moved from one physical machine to another. This portability makes it easier to manage and deploy VMs.
Scalability: Memory virtualization allows multiple VMs to run on a single physical machine. This scalability can help to reduce hardware costs.
Conclusion

Memory virtualization is a powerful technology that can be used to improve the security, portability, and scalability of virtual machines.

 "Contiguous addressable memory space" is a fundamental concept in virtualization that ensures memory isolation, efficient memory management, and optimized performance for virtual machines. It provides a dedicated and continuous memory space for each VM, allowing them to operate securely and efficiently within the host machine's memory resources.