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

            
# Resource Management and monitoring

    1. Managing resource and basic monitoring

# Host Scalability

    1. vSphere cluster and Disaster Recovery



