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
           

