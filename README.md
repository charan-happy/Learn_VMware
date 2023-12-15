# Learn_VMware

--------------
Topics to Learn
---------------
# 1. Cloud and virtualization concepts
- [Hardware and software](#hardware-and-software)
- [Virtual Machines](#virtual-machine)
- [Before and After virtualization](#before-and-after-virtualization) 
- [The Hypervisor and it's types](#the-hypervisor-and-its-types)
# 2. VMware Workstation
- [Create virtual Machine](#creating-virtual-machine)
- [VM files](#virtual-machine-files)
- [Snapshots](#snapshots)
- [Desktop to enterprise virtualiztion](#from-personal-desktop-to-enterprise-virtualization)

# 3. Datacenter
- [Compute systems](#compute-systems)
- [Networks](#networks)
- [Storage](#storage)
- [Building Datacenter](#building-datacenter)
# 4. The virtual Datacenter
- [vSphere](#vsphere)
- [Server virtualization](#server-virtualization)
- [Storage virtualiztion](#storage-virtualization)
- [Network virtualization](#network-virtualization)
- [Application and Desktop virtualization](#application-and-desktop-virtualization)
- [From physical to virtual datacenter convergence](#from-physical-to-virtual-datacenter---convergence)

# 5. VMware Virtualization Solutions
- [vMotion](#vmotion)
- [storage vMotion](#storage-vmotion)
- [vSphere High Availability(HA)](#vsphere-high-availability-ha)
- [Distributed Resource Scheduler (DRS)](#vsphere-distributed-resource-scheduler-drs)
- [Fault Tolerance](#vsphere-fault-tolerance-ft)
- [vsphere Replication](#vsphere-replication)
- [VMware vSAN](#vmware-vsan)
- [Hyper Converged Infrastructurre](#hyper-converged-infrastructure)
- [VMware NSX](#vmware-nsx)
- [VMware Cloud Foundation](#vmware-cloud-foundation)
- [vCloud Automation center](#vcloud-automation-center)
- [vmware Cloud](#vmware-cloud)
- [Tanzu](#tanzu)
- [Cloud health](#cloudhealth)
  
  
### Hardware and software

- Hardware in computers refers to the physical electronic components that make up a computer system, such as the motherboard, CPU, memory, storage drives, graphics card, and other peripheral devices.

Below are the list of common hardware components

1. processor/cpu
   
   ![processor](/images/Processor%20CPU.png)

   
2. RAM
   ![RAM](images/Ram.png)

3. ROM
   ![ROM](/images/ROM.png)
4. Motherboard
   ![Motherboard](/images/Motherboard.png)
5. Chipset
   ![Chipset](/images/Microchip.png)
6. storage
   ![Storage](/images/Storage%20HDD.png)

Each of the above hardware devices uses something that we do not touch to function which is called software.

Software is the brain of our hardware.it provides instructions on how the hardware should operate. Hardware cannot function without software.

Software is what allows our hardware to perform activities that we value such as send an email, tweet a friend.

**software** : Just like how different parts of brain control different types of actions, there are different types of software that control different levels of computer actions.

  > 1. system software [Responsible for startup{boot}process,memory{RAM},creating UI,BIOS, firmware loading EX: OS]

  2. Application software [It tells system to carry out a that a user want to accomplish such as read an email or listen to music.]

**Virtualization** is the layer of technology that goes between the physical hardware of a device and the operating system (software) and creates one or many copies of the device  

![virtual Layers](/images/Virt_layers_desk.png)
### virtual Machine

- A software computer that is, like a physical computer runs an Os and applications.

virtualization programming gathers the resources of the physical components using code and cloning them in the virtualization layer, creating virtual hardware. Once the virtual hardware is created, it can be used to build a virtual machine.

virtualization layer interacts directly with the hardware

A VM also requires the same components a physical computer needs such as a keyboard, a mouse, a CPU, RAM and more to be fully functional.

![Vm components](/images/VM_components.png)

The objective of virtualization is to have an instance (a copy) of something in a reality(virtual) on top of our reality(hardware)

The virtual layers allows us to install the OS of our choice to the VM, this is called Guest OS.

virtualization program packages all of the virtual components of a VM together as a set of files. That set of files is the VM, the files are executed in the virtual layer, creating a virtual machine.

Vmware is a virtualization company that delivers virtual machine software to individuals and businesses.

VM(virtual Machine) vs PM(Physical Machine)
|PM|VM|
|---|---|
|Difficult to move or copy|Easy to move and copy due to independence of physical hardware and encapsulation into files|
|Bound to a specific set of hardware components|Easy to manage because they are isolated with another VM running on the same Physical hardware|
|often have a short life cycle||
|Require personal contact to upgrade hardware|Insulated from physical hardware changes|

### Before and after virtualization
The main goal of virtualization is efficiency. The outcomes of vitualization are partitioning, sustainability, and isolation which reveals how virtualization has made technology more efficient.

- The ability to run multiple OS on a single physical system and share the underlying hardware is called **partitioning**

- 
### The Hypervisor and its types

- The hypervisor itself is a software that is installed on top of hardware, creating the virtualization layer and acting as a platform for the VMs to be created on.

- The hypervisor pulls the physical resources, such as CPU and Memory from the hardware and turns them into virtual hardware. The hypervisor is the key to enabling virtualization.

- **TYPE 1** hypervisor sits directly between the hardware and the virtual machine, which has its very own operating system. 

It is refered as **baremetal hypervisor**

The highlights of using a bare metal hypervisor is that any problems present in one VM do not affect other VMs running on the hypervisor. This allows users to run multiple programs all at once on the VMs and multitask without worrying about one of those programs crashing and stopping all the other programs from working.

OS creates the user interface where a user just needs a click on icons to get everything done.

To make it possible for a user to interact with the bare-metal hypervisor, the hypervisor includes a management program that creates a user interface. without management software you would just get a black screen when you turn on the computer because there is no OS.

VMware version of TYPE-1 hypervisor is **ESXI**, and the management layer software is called **vcenter**

![Type-1 Hypervisor](/images/Type1_Hypervisor_Layers.png)

- The second method of virtualization is called hosted virtualization.  To setup a computer with hosted virtualization, a type 2 hypervisor called hosted hypervisor needs to be installed on top of the operating system that already exists, the host os, not on top of hardware like a baremetal hypervisor

![Type-2 Hypervisor](/images/Type2_Hypervisor_Layers.png)

the hosted(type 2) hypervisor depends on the host OS to provide direct access to the computer's hardware resources to manage those resources to create virtual machine.

There are 2 different hosted hypervisors available to download through VMware; vmware workstation and VMware fusion. If the computer being virtualized is running a windows or a linux operating system. The user would need to download VMware's workstation as a type2 hypervisor and for apple VMware fusion.

### Creating Virtual Machine


### Virtual Machine files

- Virtual machine file management is performed by the host (VMware Hypervisor)

----------------------------------
| File Type | File name | Description |
| --- | --- | --- |
|Log file | `<vmname>`.log | Keeps a log of the Vm's activity and is used in troubleshooting |
|Virtual Disk file | `<vmname>`.vmdk | Stores the contents of the VM's disk drive<br>A virtual disk is made up of one or more .vmdk files. The number of .vmdk files depend on the size of the virtual disk |
| BIOS file | `<vmname>`.nvram | This is the file that stores the state of the virtual machine's BIOS |
|Snapshot file | `<vmname>`.vmsd or `<vmname>`.vmsn | This is a centralized file for storing information and metadata about snapshots |
|Suspend State file | `<vmname>`.vmss | This is the suspended state file, which stores the state of a suspended virtual machine |
|Configuration file | `<vmname>`.vmx | Stores information, such as vm Name, BIOS information, gues OS type, and memory size |
|||



### snapshots

![snapshot](/images/Host_VM_Base_snapshot1.png)

- the snapshot feature is most useful when you want to preserve the state of the virtual machine so you can return to the same state repeatedly. To simply save the current state of your virtual machine and then pick up the work later with the virtual machine in the same state it was when you stopped, suspend the virtual machine.
  
- we can take snapshot while Vm is powered on, powered off, or suspended. 

A snapshot preserves the virtual machine just as it was when you took the snapshot  - the state of the data on all the virtual machine's disks and whether the virtual machine is powered on, powered off, or suspended

#### what is captured by the snapshot

- The snapshot captures the entire state of the virtual machine at the time you take the snapshot. this includes :

1. The state of all the virtual machine disks
2. The contents of the virtual machine's memory
3. the virtual machine settings
   
when you revert to the snapshot, you return all these items to the state they were in at the time you took the snapshot.



### From personal desktop to enterprise virtualization

The data center performs three main functions: it processes, stores, and transmits data. This requires three main types of hardware;

1. Compute
2. Storage
3. Network


### compute systems

![Data Center](/images/Virt_DC.png)

| Computer | Server |
| --- | --- |
| More userfriendly | Less userfriendly |
| small in size | Large in size |
| Portable | Not portable |
| It comes with more input/output devices such as mouse,keyboard and monitor. So, user can interact with the system | Servers do not usually include components for direct user interaction |
|||

![server types](/images/Server%20Types.png)

Datacenter servers fall under 3 types. Tower, rack-mounted, and blade. The **tower** system is traditional PC tower. More likely these can be a personal computer

The **rack-mounted** system is thin, large rectangular computer system that slides onto the racks of a frame. 

The **blade** server, like the rack-mounted, has rectangular hardware inserted into large frame.

Virtualization is an ideal complement for blade servers because it delivers benefits such as resource optimization, operational efficiency and rapid provisioning.

Provisioning is the process of supplying resources based on capacity, availability and performance requirements.

Architecture means the type processor used by the server.  

#### clustering

- In data center, a number of simmilarly configured servers can be grouped together with connections to the same network and storage to provide an aggregate set of resources in the virtual environment, called **cluster**

### Networks

![Network components](/images/Network_components.png)

A network connects computers, servers, and other devices to each other so they can communicate and transfer data. The data center network is critical component of the data center.

In data center, the programs, websites, and other applications that needs to be delivered to consumers are kept in the data center storage.

A data center network is made up of many hardware components such as cables, routers, and switches, to name few, that create a 'net' of communication paths.

Connecting servers and the storage to a network allows both servers and storage to communicate with each other as well as with other networks.

let's understand the hardware involved in networking :

1. Router : A device that is part of a network that can send/receive data from its network to another. once data reaches the desired network, the router sends the data to the right location in the network using IP address. Devices are connected to the internet using a router.

2. Switch : connects devices to each other within a network. The switch is responsible for creating the communication paths while the router directs where on the paths the information needs to go.
   
3. NIC : short for network interface controller, NIC is a piece of networking hardware built with ethernet technology that is part of, or attaches to, the motherboard and connects to a computer to network
   
4. Ethernet Cable : a type of networking cable that physically connects devices such as servers, routers, and switches on a network using ethernet protocol.
   
5. Port : In computer networks, ports are the interfaces that serve as the point of communication between the network  and a device that is on the network. For EX: an ethernet outlet on a server is a port that can be connected to a router or switch port.
   
To simply put, Router and the switch create the network and the ethernet cable and NIC allows the device to join the network.

A network can have different layouts and range. In fact, it is the scope of the layout itself that identifies what type a network is. The type of network that normally uses Ethernet cables is called **LAN** short for Local Area Network. This type of network usually used in one location, such as office, home or school. 

There are other networks that reach further such as WANs(wide area networks) but linking up to a WAN usually requires renting access to a line that transmits data by wire, radio or optic cables. Businesses that have mulitple locations usually use WAN.

In order for the data to understand where it needs to go on the network, a network implements a protocol to direct the information to its destination. A protocol is a set of rules that dictates how information is exchanged between communication devices, in the case of a data center, between a server and a data storage device. These rules are like a language. Only devices with similar protocols understand the rules of that language and therefore can transmit information (data) to each other. As with any set of rules, they need to be applied somehow, and in the case of data center networks, they are applied through the hardware mentioned above as well as through software.

![Network topology](/images/Network_protocol.png)

- The protocol most commonly used for a data center network is called TCP/IP. Transmission Control Protocol/ Internet Protocol (TCP/IP) is a program that computers use to send messages to each other. Like virtualization, a network communication protocol can be explained by breaking it down into different layers. The TCP layer of the program breaks the content of the message a computer sends into smaller bits of information called packets that are sent and received between computers. The IP layer of the message is the address of the computer the message is being sent to. Think of these two parts as a letter being sent in the mail. The address is written on the envelope, and the message is what is inside the envelope.

- Every computer on the network has an IP address. In a traditional hardware-based data center, a network cable connects to a router, and the router then connects to a switch, which connects to the servers. As many servers as there are ports on the switch can be connected. The router itself is actually a small computer that stores the IP addresses for each IP network in its memory. When a signal comes into the router, the router reads the IP address and sends it to the correct port attached to the IP network where the destination computer is located.

- On a network, the way in which the computers, servers, storage, and network hardware are arranged is referred to as the network topology. In other words, the topology is a map of the network that indicates where the servers or other devices like storage or printers are attached physically on the network. 

![Network_topology](/images/Network_topology.png)

### storage

![VC_Datacenter](/images/Virt_DC.png)

Availability refers to the expectation that a device is running rather than  experiencing downtime. if you lose a flash drive it can be inconvenient, but if a data center storage device goes offline, the business and enterprises that rely on that storage will suffer.

the method used to improve the availability of storage is called **redundancy**.

Redundancy can be implemented in such a way that the system will create a copy of data, saved in another location, that may be accessed in the event that the original location becomes corrupted or breaks down. 

Datastores can be deployed in two methods. `1. Direct-attached Storage and 2. Network-based storage`.

#### RAID

- To ensure availability in the data center, a type of data storage technology called `RAID (Redundant Array of Independent Disks)` is used. RAID is multiple storage drives (two or more), hard drives for example, that are linked together to create one single large volume of storage. This results in increased performance and/or data redundancy.

- There are different types, or as they are usually referred to, levels, of RAID and depending on which level of RAID is used (i.e., RAID 0, 1, 4, 5, or 10), storage availability and redundancy are achieved using one or a combination of three methods; mirroring, striping, and parity.

When the mirroring method is used, two same-sized drives are linked together and what gets written to the first also gets written to the second, creating an exact copy for redundancy purposes.

![RAID1](/Images/RAID_1.png)

- With the striping method, on the other hand, the data being written traverses along the linked drives, so no drives are identical. The linked drives function as one single drive, and the data is ‘striped’ between the two as shown by the RAID 0 example in the image below. The benefit of striping is that it increases capacity and results in faster performance because it takes less time to write the data a single time to one disk (in this case, two disks functioning as one) than it does to write the data multiple times to create a copy on each of the linked drives, as is done using the mirroring method.

- Therefore, in the case of RAID 0, the desired outcome is performance rather than redundancy. 

- At first, this may not seem like a desirable storage option, but there are some tasks, such as graphic design or media compilation that require higher performing storage like RAID 0 for a temporary amount of time.

![RAID 0](/Images/RAID_0.png)

Mirroring offers redundancy as opposed to striping because, as shown in the above image, if one drive goes down, all the data is preserved on the other disk. One way to get the best of both methods is with a RAID 10 (1+0) or a RAID 0+1 storage configuration, which incorporates both mirroring and striping.

Another RAID technique, called parity, is a way of checking if there are errors in a string of data. Parity is used in certain RAID configurations by adding a data bit at the end of a string of data being written to a disk.

`01010101 0`

The first set of characters 01010101 of the example data output above represent a string. After the string, the last highlighted character 0 displayed above is the parity bit.

The example above uses even parity. A parity bit of 0 means that the number of 1s, including the parity bit, is even. This is confirmed by the four 1s in the string. If one of the 1s was accidentally switched to a 0 during the transmission, the number of 1s including the parity bit would be odd and therefore incorrect. If the data string does not match the data bit, it means that there was an error in the transmission of the data.

`01010101 1`

In the example data output above, the number of 1s including the parity bit 1, is five, and therefore odd.

RAID levels that use parity, assign one of the disks in the volume as a parity disk where the parity information is stored. Should a disk failure occur, the parity information can be used to recover the lost data from the failed disks.



![Raid_5](/Images/RAID_5.png)

#### File level and block level storage

The difference between block level storage and file level storage is how the storage is organized and accessed on the storage device and from other devices, such as servers.

- In `block level storage`, a storage device such as a hard disk drive (HDD) is identified as something called a `storage volume`.  A storage volume can be treated as an individual drive, a “block”. This gives a server's operating system the ability to have access to the raw storage sections. The storage blocks can be modified by an administrator, adding more capacity when necessary, which makes block storage fast, flexible, and reliable.

File level storage is a type of storage that has a file system installed directly onto it where the storage volumes appear as a hierarchy of files to the server, rather than blocks. This is different from block type storage, which doesn't have a default file system and needs to have an administrator create one in order for non-administrator users to navigate and find data.

![Block & File level storage](/Images/block-level_storage.png)

One benefit of using file storage is that it is easier to use. Most people are familiar with file system navigation as opposed to storage volumes found in block level storage, where more knowledge about partitioning is required to create volumes.

Partitioning is the creation of sections on a disk that are set aside for certain files or software. Based on the operating system used, the partitions will be assigned a name or letter. For example, the letter C: is given to the main partition on Windows devices. This may seem familiar as most PCs purchased from a store have pre-configured hard drives with default partitions. However, for block storage devices purchased on their own, the user will most likely need to partition the drive before a file system can be installed as they do not come pre-configured with default partitions.



#### Direct attached storage

Direct Attached Storage (DAS) means that a physical storage device is directly attached to a server or personal computer. The hard drive of a laptop is a type of DAS because it fits the definition of a storage device directly attached to a personal computer.


![Direct Attached Storage](/Images/DAS.png)

he following are types of storage that can be used as DAS:

`Hard Disk Drive (HDD)` - Uses magnetic rotating disks to hold data, which is then read by a rotating arm that reads and writes the data onto the disk. Many personal computers have HDDs, or as they are usually referred to, “hard drives”.

`Solid State Drive (SSD)` - Made out of a collection of electronic circuits (chips) that store and transmit data. Unlike hard disk drives, solid-state drives don’t have any moving parts like the arm of the HDD that has to rotate to find the right location on a disk. This means that SSDs are faster and more durable. Another benefit of SSDs is their efficiency, due to the fact that they don’t have any moving parts, so they require less energy to operate.

`Optical Disk Drive (ODD)` - Uses lasers to read and write data onto optical disks. A good example of a type of media that uses an optical disk drive is a DVD player. Although most optical disks can only hold 50GB or less as opposed to the commonly available 256GB to 1TB (terabyte) HDDs and SSDs, ODDs are convenient because they are inexpensive and highly portable.
⁠⁠​​ 

The types of storage mentioned above have different benefits, but each has the ability to store data and can be used as an external storage option. The direct attached storage architecture is beneficial for personal use or for small businesses that need to purchase a set amount of data storage at a time, and it is simple enough not to need a significant IT management presence. The goal is to grow data storage in increments by simply adding additional drives when needed.

In order to set up DAS, the storage device needs to have the correct technology employed so it can speak the same language as the server it’s attached to. This "language" is called a `protocol`. 

On a storage device, the protocol can be identified by the ports and outlets it uses. An example would be the USB (Universal Serial Bus) protocol, which can be identified by the USB ports and cables. Because storage devices come in various protocols, the server may need an adapter to communicate with the storage device so users can store and access data from it.

The protocol adapter for servers is called an HBA (host bus adapter). This is a piece of hardware, similar in appearance to a card with a port for a plug, which is plugged-in to a server and adapts the server to the storage device’s protocol (language). Once the HBA is attached to the server, and the cables with the right protocol are used, a storage device can be attached, allowing the DAS to now be able to talk to the server. The protocols most commonly used for DAS are SCSI, SATA, SAS, and USB. So, if a SCSI protocol HBA is attached to the server, and the HBA is connected to a SCSI storage device with cables, it will be able to transmit data from the server to the storage and vice versa.

One downside of using DAS is that the extra storage can only be used by the server it's attached to .

#### Network attached storage

NAS, short for Network Attached Storage, involves attaching a storage device to a network that, in turn, allows storage to be accessed and distributed on the network to servers attached to the same network. The NAS storage normally connects to the network through an Ethernet protocol and has its own IP address.

![NAS](/Images/NAS_storage.png)

NAS is the easiest to use because it is file level storage.

The protocols used for transmitting data over a NAS differ from those used for DAS because the storage is a type of file level rather than block level storage. NAS is connected to a router and/or switch, which connects it to a Local Area Network (LAN). To communicate to servers on the LAN, the storage uses a TCP/IP (Transmission Control Protocol/Internet Protocol), which is the basic internet protocol, or language data is transmitted in through the internet.

Because the data shared on a NAS is in files, any system trying to access data needs to follow a file path. For example, `/mystoragedevice/Public/mydata/file1.txt` is how a server would get to file1 in the mydata folder on the storage device called `mystoragedevice`.

Because files are shared on a network, it is not enough to just connect the device to the network; the file system also needs to follow a network protocol to be accessed. For example, on the internet, HTTP is a protocol and usually comes before a web address. Without using `http://`, the website will not come up. This is usually filled in for you by the browser if you forget, but if you look at the address bar, it will be there. Files on a network are like websites; the correct protocol and file path must be used in order to access them. Commonly used file system protocols used on NAS devices are NFS (Network File System) and CIFS (Common Internet File System). NFS is commonly used with Linux and Unix based operating systems while CIFS is used for file sharing on Microsoft based machines.

One way to tell which protocol, NFS or CIFS, is being used, is by looking at the path name. NFS files are accessed by using the format `<IP Address>:/<DriveVolumeName>/<NameofShare>` while CIFS files use the format `//<IP Address>/<NameofShare>` .

#### Storage area network

A SAN (Storage Area Network) is one or many block level storage devices clustered together that are attached to a high-speed network and that applications running on the servers, can connect to in order to access the data. A characteristic of a SAN is that even though the storage is in another physical location, to the server, it looks and acts as if it was attached as a DAS.

A SAN requires that servers trying to connect to it also have certain protocols. Because a SAN requires a high-speed connection, faster protocols such as** iSCSI, Fiber Channel (FC),** and more recently **Fiber Channel over Ethernet (FCoE)** are used to transmit data at higher speeds on the TCP/IP network (internet).

This ability for storage to be shared outside of a local network makes a SAN an efficient storage type for larger companies whose employees need to access stored data from more than one location. Because a SAN requires higher speeds and a wider network area, it can be more expensive to set up but the ability to modify the size of the storage from anywhere at any time, called scalability, outweighs the costs for big organizations.

|NAS | SAN|
| --- | --- |
| It is a storage that connects to a network | It is a network of storage that servers can connect to. |
| It manages storage as a file system directly | It doesn't manage storage as a file system directly |
| It is faster & efficient | It is slower & inefficient |
|||

![SAN](/Images/SAN.png)

#### Storage protocol

Many types of storage protocols are available for configuring data center storage. The most efficient protocol for a particular data center depends on factors such as the size of the data center, types of servers used, and available budget. For example, some protocols ensure faster data transmission speeds but cost more to implement. Configuring storage with protocols that match the amount of data traffic a data center wants to handle can increase efficiency and ensure data gets to customers.

| Protocol | Application |
| --- | --- |
|SCSI (Small Computer System Interface) | Medium- sized blade servers, Enterprise servers, DAS|
|SATA (Serial Advanced Technology Attachment) |Small-sized tower server, DAS |
|eSATA (external SATA)| Small-sized tower server, DAS|
|SAS (Serial Attached SCSI)| Medium-sized blade servers, Enterprise servers, DAS |
| FC (Fiber Channel) (single-mode) (SMF)| Enterprise servers, SAN |
|FC (Fiber Channel) (multi-mode) (MMF) | Enterprise servers, SAN |
|FCoE (Fiber channel over Ethernet) | Enterprise servers, SAN |
| ISCSI (internet small computer system Interface) |Enterprise Servers, NAS |
|||

#### Storage provisioning

The cost of managing data center storage can rise quickly when you consider the expense of purchasing new devices, along with operating costs such as energy expenses, as well as staff to monitor data capacity and maintain the hardware. Therefore, using and allocating storage in a data center needs to be done in the most efficient way possible without affecting reliability, making sure data is delivered to the customer.

Provisioning is the process of strategically assigning storage space to servers based on the capacity of the storage device(s), availability, and performance requirements. Storage provisioning can be performed in two ways, traditional (thick provisioning) and virtual (thin provisioning).

In order for a disk to be provisioned, the storage volumes are partitioned to create logical disks. Simply put, a logical disk is a virtualized disk. The capacity of a logical disk physically exists in a device somewhere, but the logical disk itself does not physically exist.

Provisioning requires that disk space is turned into logical rather than physical units because physical disk space cannot be shifted around strategically as quickly as logical space can be. Remember, logical disks are data representations of physical disks, not physical hardware.

In traditional provisioning, also called thick provisioning, disk space is strategically pre-allocated to a server or a virtual machine. This means that the logical space provided by partitioning is equal to the amount of actual physical space set aside on the disk.

![Thick provisioning](/Images/Thick_virtual_disk.png)

For example, when you set up an operating system like Windows, a certain amount of storage space is provisioned for certain files and programs. With this method, you first estimate how much storage the program will need for its entire life cycle. You then provision a fixed amount of storage space to the disk in advance.

### Building Datacenter

To simply Put, a company building a datacenter can use one of two infrastructure models: a converged infrastructure or a best-of-breed infrastructure.

A **converged** infrastructure integrates all the datacenter hardware and software components into a single package from a provider. The provider offers a preconfigured unit optimized for the datacenter being built.

A **Best-of-breed** infrastructure is when the datacenter has different top of the line components such as best-of-breed servers, storage devices, and networking equipment from multiple vendors.  EX: HP servers, cisco networking devices, IBM storage devices .

this type of infrastructure results in lower cost from competitive pricing. Prevents vendor lockin and enables the repurposing of existing data center components.

![datacenter toploly](/images/data-center-topology_highres.png)

**zombies** are computer assets, such as VMs, storage, and servers that are no longer doing useful work. These systems are still running. Using energy, and incurring costs instead of being shutdown.


The purpose of the data center is making applications available to users. Businesses use the data center to support the applications they need with the goals of reducing the total cost of Information Technology (IT) and ensuring applications are available when needed. The goal of virtualizing the data center is to address both cost savings for an organization and availability to the user.

The process of virtualizing a data center is intended to take it from hardware defined data center to what is called Software defined data center (SDDC) also known as virtual data center.


### vSphere

Vmware Vsphere is a suit of virtualization technology designed for larger enterprise data management.

![vsphere structure](/images/data-center-topology_highres.png)

Main components of Vsphere :

1. ESXI - Vmware's Type 1(bare metal) hypervisor
2. vCenter - vSphere's management layer
3. vSphere client - A program that configures the vcenter, host and operates in virtual machines
4. vSphere Host Client - A program that only configures the host and operates its virtual machines
   
   ![vsphere client](/images/CVC_vSphere_Clients.png)

 ESXI :
 ------
  ![Esxi](/images/esxi-servers.jpg)

- The 3 things tht makes up vsphere.

EXSI is a type=-1 hypervisor software that is installed directly onto a physical server and creates the foundation for the virtual layer. ESXI enables the server hardware to be partitioned into multiple logical computers, which you now know are VMs. (or)

Virtual machines run on and consume resources from ESXI, but ESXI is running on top of the physical server itself to help administer the hardware resources.  ESXI is like a command center that all the applications on the Vm talk to, then it turns around and tells the hardware what to do.

The ESXI baremetal architecture consists of two main parts. when the server is powered up, the two parts are loaded in sequence. The first part is called the  unix microkernel, and the second part is called the VMware kernel.


#### vcenter

![vcenter architecture](/images/vcenter_manage.png)

In vsphere, the management layer is called vCenter, a software that is installed on a dedicated server to specifically manage ESXI server and other components of a Virtualized data center

To connect vCenter server to manage vCenter and ESXI host, we use vSphere cient.

#### vSphere Host Client

when ESXI is installed, it creates the management layer for ESXI host, but that layer doesnot automatically know what to tell the data center to do. This is because the management server is just hardware and software; It needs to be programmed by the real people (administrators) who know what settings to adjust in order to meet data consumption demands. VMware created a user interface called vSphere Host Client to directly manage an ESXI host.

![vSphere Host client ](/images/vsphere_host_client.png)

the vsphere Host Client is a graphical user interface program installed on the ESXI host that allows data center administrators to connect to ESXI remotely from any windows PC. The VMware Host Client allows administrators to perform numerous administrative tasks and monitor the host or virtual machines at the host level. 

#### vsphere client

The vSphere Client is a graphical user interface program installed on the vCenter server that allows data center administrators to connect to vCenter or ESXi remotely from any Windows PC

### server virtualization

creating virtual instances of physical servers to run multiple Operating systems on a single physical server.

Benefits :

Resource optimization

Cost savings

Improved scalability and flexitbility

Enhanced disaster recovery and backup capabilities

### storage virtualization

Virtualized Storage is designed to give VMs the adequate amount of storage needed to host their operating systems and therefore, their applications. 

virtualizing storage takes storage capacity and pools it together in the virtual data center and then distributes that capacity to the VMS.

![storage virtualization](/images/storage_virt_1.png)

Virtual  storage is represented logically. Logical computing basically means represented as a software rather than hardware. 

- The first step in creating virtual storage from physical storage is taking physical storage capacity and transfering it into logical capacity. This is done by creating a partition and using the space on that partition to create a logical drive, also represented as LUN (logical unit number) <br> a LUN can be a whole drive or part of the drive depending on how the drive is partitioned. <br> The LUN is used to identify which device the logical disk's capacity comes from. So, what the virtual machine or server sees when it is saving data to the virtualized storage (pool) is a block number or drive letter that maps to the physical device's logical unit.

- LUN is the number used to identify the storage device's logical units, however, it is commonly used to describe the logical drive itself.

![storage virtualization](/images/storage_virt_2.png)

Creating virtual storage is a multistep process, The storage capacity needs to be measured and added to a container before being poured into the pool. LUNs are smaller units, which are put into a larger unit called "volume". The volumes are then turned into a unit called "datastore", which gets virtualized.

#### Datastores

A method for setting up a storage resource for virtualized servers to access and save data is grouping logical storage into something called a datastore

![datastores](/images/datastores.png)

In order to protect virtual server's data, the virtual memory is setup in a different location. Normally, virtual data is setup in two locations. This way, if one storage stops working, the virtual server simply switches to using another virtual storage server.

In order to access the datastore, it is common to install a file system onto the datastore. In vSphere, datastores are set up with the following file system formats:

- Virtual Machine File System (VMFS) - High-performance file system that is optimized for storing virtual machines. Your host can deploy a VMFS datastore on any SCSI-based local or networked storage device, including Fibre Channel and iSCSI SAN equipment.
  
- Network File System (NFS) - File system on a Network Attached Storage (NAS) storage device.

#### How virtual machines access storage 🤔

- Virtual machines use virtual disks to store their operating system, application software, and other data files. A virtual disk will be stored as a VMDK (virtual machine disk) file with the extension .vmdk on a datastore. What the virtual disk does is hide the physical storage layer from the virtual machine’s operating system. Regardless of the type of storage device that your host uses, the virtual disk always appears as a local device to the virtual machine.

- The virtual machine configuration files are stored as VMX files with the .vmx extension. To the user, these files, along with .vmdk files, can be found in the Documents folder of the host machine

![vm_storage](/images/vm_storage.png)

#### Thin provisioning

- Storage Provisioning, is most likely thick provisioned, where the desired amount of storage capacity was set aside for a virtual disk or LUN (logical unit number) at the time of its creation.
- However, in a virtual data center, storage needs fluctuate more than they do in a physical data center as a result of virtualization. This is a good thing because flexible storage results in the ability to deliver more virtual machines, and therefore, more applications. However, in the case of thick provisioning, setting aside a physical chunk of storage that can only be used for a certain purpose is simple but not necessarily efficient because the unused storage is confined to that disk and not available for other users.
- Thin provisioning, in contrast, assigns the LUN a ceiling amount but the storage space actually used grows as data is being written to it. Think of it as ‘on-demand’ storage that allows the unused storage to be distributed to virtual disks that need it at that moment.
- To thin provision a virtual disk, the hypervisor provisions the entire space required for the disk’s current and future activities, for example, a fixed amount of 40GB is provisioned to a disk. However, the thin disk commits only as much storage space as the disk needs for its initial operations.

- we can also add storage space to a virtual machine beyond the provisioned amount by expanding its virtual hard disk. When you expand a virtual hard disk, the added space is not immediately available to the virtual machine. To make the added space available, you must use a disk management tool to increase the size of the existing partition on the virtual hard disk to match the expanded size.

![Datastore provision for ESXI](/images/Thin_Provision%20&%20Thick_provision.png)

![Thick virtual disk](/images/Thick_virtual_disk.png)

- When you expand the size of a virtual hard disk, the sizes of partitions and file systems are not affected. As an alternative to expanding a virtual hard disk, you can instead add a new virtual hard disk to the virtual machine.

- VMware's hypervisor, ESXI, supports thin provisioning for virtual disks

### network virtualization

A traditional network is made up of a router, a switch, NICs , ports, and cables. These physical components have virtual counterparts that make up the virtual network. 

The virtual network shares the router and NIC (network interface card/adapter) with the physical network, but the other components are virtualized. The first layer of the virtual network is the virtualized switch called a vSwitch, which links up the virtual devices

![virtual network](/images/virtual%20Network.png)

- Virtual switches allow virtual machines on the same ESXi server host to communicate with each other using the same protocols that would be used over physical switches, without the need for additional networking hardware. A virtual machine can be configured with one or more virtual Network Interface Cards (NIC), also referred to as virtual Ethernet adapters. Each virtual NIC responds to the standard Ethernet protocol as would a physical NIC and has its own IP address and MAC address. As a result, virtual machines have the same properties as physical machines from a networking standpoint.

- MAC (Media access control ) addresses are assigned to NICs in order to communicate at lower layer of the network, The data link layer of the OSI model.

Another advantage of using virtual networks is the ability to establish VLANs.

![vlan visual](/images/vlan_visual.png)

- A VLAN, short for virtual local area network, enables a single physical LAN (local area network) to be further segmented so that groups of ports are isolated from one another as if they were on physically different network segments. VLANs can be used to break up very large LANs into smaller virtual LANs
-  This may be useful to control network traffic such as broadcasts (another name often used for a VLAN is a Broadcast Domain). A broadcast is a method of sending data packets to every device on a network, like sending a text message to every contact on your Mobile. Broadcasts are commonly used by a router to request information about devices on the network or when a new computer is added to the network as a way to “get attention” to let other computers and devices know it’s there.
- Although broadcasts save time, there are cases where some messages might not be intended to be read by particular recipients either for security or because they are not relevant to that recipient
- without VLANs, each broadcast domain would need its own physical switch. Imagine the cabling involved and also the potential number of NICs required at the hosts.
- The reason for virtualizing a network is similar to why virtualization is applied to servers; a virtualized network can host more devices than a physical network. A vSwitch can host many more VMs than a physical switch can host servers. A virtual network is also more flexible and therefore, has more scalability to accommodate large data operations.

#### Types of virtual networks

The three main network types used to setup VMs with a connection.

**Bridged Network** A bridged network is a network type where both a virtual machine and the host that it is running on are connected to the same network. Bridged networking connects a virtual machine to the network using the host computer's Ethernet adapter. The network used by the host is the main public network, which is generally referred to as “the internet”. This is possible because the host shares its IP address with the VM.

- With bridged networking, the virtual network adapter (vnic) in the virtual machine connects to a physical network adapter (NIC) in the host system. The host network adapter enables the virtual machine to connect to the LAN (Local Area Network) that the host system uses. Bridged networking works with both wired and wireless host network adapters.

![Bridge Network](/images/Bridge%20Network.png)

- Bridged networking configures the virtual machine as a unique identity on the network, separate from and unrelated to the host system. The virtual machine is a full participant in the network. It has access to other machines on the network, and other machines on the network can contact it as if it were a physical computer on the network.

**NAT Network** NAT (Network Address Translation) takes an IP address and translates it into another IP address. On a NAT network, a virtual machine does not have its own IP address on the external network. Instead, a separate private network is set up on the host computer.

NAT is useful when you have a limited supply of IP addresses. NAT works by translating addresses of virtual machines in a private network called a VMnet to that of the host machine. When a virtual machine sends a request to access a network resource, to the network resource it appears as if the request came from the host machine.

The NAT device on the network translates the information going to the host's public IP address and forwards it to the private IP address for the VMs.

The VMnet is able to connect to the public external network using the translated IP addresses enabled by a feature called port forwarding. Port forwarding allows incoming web traffic to pass through a specific port, chosen by the administrator, to the internal network.

Incoming network traffic is transmitted in the form of data packets. The NAT device is able to sort the packets intended for each virtual machine and sends them to the correct destination. A data packet contains a unit of data, information about the network it is traveling on, and where it is going. When a packet does not reach its destination, this is called packet loss.

The topology of a NAT network generally involves a VM connected to a virtual network interface card (vnic) which allows it to connect to the virtual switch (vswitch). The vswitch is also connected to a NAT device that translates the IP addresses and allows port forwarding to connect to the external network.

![NAT_Network](/images/NAT_Network.png)

**Host-only Network**

Host-only networking creates a private internal network for the VMs to connect to, similar to a NAT network. However, without IP address translation, the VMs can only stay in the private network and do not have direct access to the public external network.

Host-only networking provides a network connection between the virtual machine and the host computer, using a virtual Ethernet adapter (vnic) that is visible to the host operating system. This approach can be useful if you need to set up an isolated virtual network.

![Host_only_Network](/images/Host_Network.png)

If you use host-only networking, your virtual machine and the host virtual adapter are connected to a private Ethernet network. Addresses on this type of network are also provided by a DHCP server.

### Application and Desktop virtualization

- A virtualized data center can solve the legacy application deployment on VMs by virtualizing the applications themselves and allowing them to be accessed remotely by a user.

VMware uses a technology called **ThinApp** to deliver virtualized applicatioins compatible with any machine. Thinapp analyzes the machine that needs thee app and decides what underlying software it needs in order to be compatible with that machine. 

For ex: if the user's os is running windows internet explorer 10 but the app requires explorer 7 or below, a compatible verion of the browser will be packaged into the virtualized application. 

The app is then delivered as a remote package that can be uploaded and used without acutally running on the orginal physical or virtualized hardware. This is called `application isolation`. it enables software delivery without changes to the file system or the database of the host computer.

There is another virtualization technology that can be used along with application virtualization, called desktop virtualization, to deliver computer functions in software form to an end user.

With desktop virtualization, the entire desktop environment meaning all the programs that usually run on top of OS, can be delivered to an end user on a remote machine.

VMware's desktop virtualization technology is called `Horizon`. Horizon delivers software-defined (virtual) desktop environments to customers. It was designed to solve computing resource issues faced by what is called "mobile workforce". 

Horizon takes the resources needed to create a desktop environment from data centers and virtual data centers and then delivers them to the end user's devices (laptops, thin clients, and mobile devices). Once connected to the virtual desktop, all an end user needs to begin interacting with the desktop is a keyboard and mouse.

with a virtualized desktop, the end user does not have access to an entire operating system, only the programs that run on top of it.

### From physical to virtual datacenter - convergence

Moving from a hardware-based data center to a virtual data center is done with a combination of strategy, technology, and processes.

#### strategy

- once the decision is made to move toward a virtual data center, there are two strategies for making the move: containment and consolidation.
  
The strategy of `containment` is the practice of not deploying any existing applications for customers on virtual servers. 

The down-side of containment is that the data center won’t get any benefits from its old applications running this way. The data center will operate like two data centers, one will be virtualized, and the other will be a traditional hardware-based data center

With this strategy, it could take years before deriving all the benefits and savings of the virtual data center.

the second strategy, `consolidation` is the solution for moving applications that are running in the old hardware-based data center model to the virtual data center model. The technology used in order to consolidate and convert current hardware-based servers to virtual servers is known as P2V (physical to virtual) software. VMware’s P2V is called vCenter Converter. It was developed by VMware to quickly convert local and remote physical machines into virtual machines without any downtime.

![P2V](/images/vcenter-converter.png)

#### Technology

- To understand what P2V software does, it’s important to understand what drivers do. Drivers are software used by computers to enable different hardware components of a computer to operate.

If a part in a server is changed, it will be necessary also to install a new driver that speaks the language of the new part, to act as its interpreter.

In a nutshell, P2V software performs the following actions:

  1. Looks at the existing hardware server and determines what size the virtual server will need to be.
  2.Creates the virtual server and configures it so it will work in the system correctly.
  3. Copies the data on the hardware server to the virtual server.
  4. Cleans up the virtual server image.
      - Gets rid of any unnecessary applications and drivers.
      - Adds any new application needed.
      - Adds any new drivers that are needed.

#### processes

One issue with going through old hardware servers and converting them to virtual servers is that it takes time. The more applications on the server, the more time it takes. Sometimes you can take a server offline for a while to do the conversion, but in some environments, it is not desirable to withhold user access, even temporarily, to applications.

There are two approaches to converting a hardware server to a virtual server. Each has advantages and disadvantages.

The prefered approach is called `cold conversion` To do a cold conversion, the applications on the server must be shut down in order to convert everything to the virtual server. Because all the applications are shut down, there are no changes going on while the conversion is being done. This is basically a copy of the old server being moved to the new virtual server. Although widely used, one downside to this method is that it may inconvenience some users who won’t be able to use the applications while the conversion is being done.

A `hot conversion` is done without shutting the applications down. End users are happy that they can keep using the applications; however, there is a chance that changes taking place on the application during the conversion process may be lost.

`Why are changes lost in the conversion process?` Remember we said it takes time for the P2V software to read the old hardware server image and then convert it to the new virtual server image. If a change occurred in an application after it was read, but before it was converted to the virtual server and users were switched over to using the virtual server, those changes would be lost.

Virtual Machine:

- Utilizes multiple hardware components of server resources

- Single server can support multiple virtual machines

- Applications on a virtual machine are isolated from each other
Provides a “sandbox” environment that isolates system issues to the virtual machine

- Boot time is faster than a physical device

Container:

- Lightweight / uses fewer resources
- Single server can support more containers than virtual machines
- Containers share an operating system, so applications are not isolated
Container images can be more efficiently created/deployed than virtual machine images
- Boot time is faster than a virtual machine
  
### vMotion

- Foundation of vSphere consists of the hypervisor (ESXi), the management server (vCenter), and the user interfaces vSphere Client and vSphere Host Client. These three are the foundation of vSphere but vSphere also includes other products as part of the vSphere ‘suite’. VMware offers these other products as solutions to solve more specific computing and data center efficiency issues

Using vSphere vMotion, you can move running virtual machines from one ESXi host to another ESXi host without service interruption. Moving a VM from one server to another without interrupting the end user’s connection is called `live migration`.

There are three underlying technologies that allow vMotion to do live migration. 

- First, the entire state of the VM is encapsulated, which means to condense and enclose, as a set of files on shared storage such as Storage Area Network (SAN) or Network Attached Storage (NAS). The servers, which are able to access shared storage through networks, can access those encapsulated files in the NAS or SAN Virtual Machine File System (VMFS), giving them access to the VM being migrated.

- Second, the state of the VM is rapidly transferred over a high-speed network, allowing the virtual machine to instantaneously switch from running on the source ESXi Server to the destination ESXi Server. This entire process takes less than a few seconds on a Gigabit Ethernet network.

- Third, the networks being used by the virtual machine are also virtualized by the underlying ESXi Server, ensuring that even after the migration, the virtual machine network identity and network connections are preserved. Once the destination machine is activated, VMotion pings the network router to ensure that it is aware of the new physical location of the virtual MAC address. Since the migration of a virtual machine with VMotion preserves the precise execution state, the network identity, and the active network connections, the result is zero downtime and no disruption to users

![vmotion](/images/vSphere_vMotion.png)

### Storage vMotion
With vSphere Storage vMotion, you can move the disks and configuration files of a running virtual machine from one datastore to another datastore without service interruption. Storage vMotion has several uses in administering virtual infrastructure, including the following examples:

Storage maintenance and reconfiguration. You can use Storage vMotion to move virtual machines off of a storage device to allow maintenance or reconfiguration of the storage device without virtual machine downtime.
Redistributing storage load. You can use Storage vMotion to manually redistribute virtual machines or virtual disks to different storage volumes to balance capacity or improve performance.
You can use Storage vMotion to migrate virtual machines when you upgrade VMFS on datastores.

![vsphere_storage vmotion](/images/vSphere_Storage_vMotion.png)

### vSphere High Availability (HA)

vSphere HA increases the availability of VMs by pooling servers (hosts) and the VMs that reside on them in a cluster and monitoring them. In the event of a failure, the virtual machines on a failed host are restarted on alternate hosts.

When HA is installed, it designates one server as a master server which talks directly to vCenter. Meanwhile, a software agent (program) on each server in the resource pool creates a “heartbeat” for the host. Agents on the different hosts contact and monitor each other through the exchange of heartbeats by default every second. If a 15-second period elapses without the receipt of heartbeats from a host, and the host cannot be pinged, the host is declared as failed. The virtual machines running on the failed host are restarted on the alternate hosts with the most available unreserved capacity (CPU and memory.)The master host continuously monitors all servers in the resource pool and if it detects a loss of “heartbeat”, it initiates the restart process of all affected virtual machines on other servers.

![vsphere-High Availability](/images/vSphere_HA.png)

### vSphere Distributed Resource Scheduler (DRS)

vSphere Distributed Resource Scheduler automatically manages resources and power across ESXi hosts. Before obtaining the benefits of cluster-level resources such as HA, a DRS cluster has to be created. A DRS cluster is a collection of ESXi hosts and their virtual machines that have shared resources and a shared management interface

DRS implements a shared management interface so that the cluster's resources can be easily monitored and managed. DRS has to be implemented first because it is responsible for aggregating the resources of all the servers into a cluster-wide resource pool.

![vsphere DRS](/images/vSphere_DRS.png)

### vSphere Storage Distributed Resource Scheduler (Storage DRS)

With vSphere Storage DRS, you can manage multiple datastores as a single resource called a datastore cluster. Clustering datastores is more efficient because historically, provisioning virtual machine storage has posed operational challenges. During the provisioning process for virtual machines, virtual disk datastores are often randomly selected, leading to over- or underutilized datastores

. To help resolve these issues, Storage DRS was added as a feature of VMware vSphere that provides smart virtual machine placement and storage load-balancing mechanisms based on space capacity. It helps decrease the amount of operational effort (the work a data center administrator performs) associated with the provisioning of virtual machines and monitoring of the storage environment.

![vsphere_storage DRS](/images/vSphere_Storage_DRS_new.png)

### vSphere Fault Tolerance (FT)

When vSphere Fault Tolerance is enabled on a virtual machine, a secondary copy of that virtual machine and its files is created on another ESXi host and datastore. The secondary VM is continuously available to replace the primary VM in the event of a storage or host failure.

`The difference between FT and HA is that with HA`, when the server fails, the end-user will see the virtual machine fail and reboot, while with FT, the transfer to a different server is seamless and will not be noticeable to the end user. This seamless transfer is similar to vMotion except that with vMotion the transfer is done while both servers are running whereas FT transfers the VM when its host fails.

![vsphere fault tolerance](/images/vSphere_Fault_Tolerance.png)

### vSphere Replication

VMware vSphere Replication is a hypervisor-level replication engine that makes the recovery of virtual machines faster and easier. Having an offline copy at a different location is beneficial for not only data protection and disaster recovery but also for when a data center needs to change locations, usually referred to as data center migration.

An example of how vSphere Replication would be used is in the case of an unfortunate environmental disaster like a flood or storm that causes damage to a data center. Instead of having to go offline while repairs are being made, administrators can use vSphere Replication to switch to the copy which is hosted at another site.

One of the features of vSphere Replication is that it is integrated with vSphere Web Client, which eases administration and monitoring. This means that creating a target site for the replicated VMs is easily done through a wizard.

![vsphere_replication](/images/vSphere_Replication.png)

### VMware VSAN

A data center that wants to transition to a software-defined data center (SDDC) can start by using vSphere to virtualize its servers. The next step would be to virtualize storage.

VMware designed an extension of vSphere, called VSAN, to virtualize storage in data center servers. VSAN interacts with vSphere to create one layer of virtualization software, which is managed by the vCenter management layer. There is no need to purchase external storage configurations such as Network Attached Storage (NAS) or Direct Attached Storage (DAS). VSAN does this by clustering the servers and then combines the storage resources of the cluster into a storage pool called a VSAN datastore. The virtualized storage is then available to be distributed to virtual machines.

VSAN stands for Virtual Storage Area Network. A VSAN is a virtualized SAN (storage area network), created by using virtual routing and switching to network the clustered storage. This is similar to how SAN uses physical networking to make storage available to the physical data center.

![vsan](/images/SAN.png)

### Hyper converged Infrastructure

Hyper converged Infrastructure (HCI) is a software-defined data center infrastructure.

VMware VSAN, along with VMware vSphere, creates what is called a `hyper-converged infrastructure`. A key benefit of a hyper-converged infrastructure is that it allows a growing data center to capitalize on its existing hardware investments. A hyper-converged infrastructure is a converged infrastructure that has been virtualized. 

A converged infrastructure integrates all physical data center components from a single vendor while a hyper-converged infrastructure integrates virtualized data center components from one vendor, in this case, VMware.

![vsphere hyperconverged infrastructure](/images/HighConverged%20HCL.png)

### VMware NSX

NSX expands standard network virtualization beyond just virtual switches.

With NSX, you create a software layer of networking on top of the physical network that includes virtual routers, load balancing, virtual private networks (VPNs), firewalls, and more. That software layer of networking can then be divided into many virtual networks. NSX is more centralized than the traditional data center.

![VMware NSX](/images/NSX-graphics.png)

#### NSX-T

For NSX to function properly in a virtualized environment, you need vCenter Server. This is because, without vCenter Server, NSX will not be able to integrate with vSphere and the hypervisor. To mitigate the use of vCenter Server, VMware now offers a next-generation solution to software-defined networking called NSX-T Data Center. NSX-T Data Center does not require vCenter Server. Since it does not require vCenter Server, administrators can now support the ever-growing number of cloud architectures such as AWS, containers, and Kubernetes

![NSX-T](/images/NSX-T.png)

To manage NSX-T Data Center, NSX Manager is needed. The NSX Manager is installed as a virtual appliance on any ESXi host in your vSphere environment. NSX Manager provides administrators with a centralized management tool that features a GUI to configure and monitor NSX-T components. NSX-T Data Center supports a management cluster of three NSX Managers to ensure high-availability. A management cluster is recommended for production environments.

NSX-T Data Center puts a stronger focus on security and networking in the cloud. It lets administrators deploy the best technology needed for applications running within their environments.

### VMware cloud Foundation

With VMware Cloud Foundation, a set of products that make it easy for anyone with the right hardware to move their existing system to a virtual data center.

(virtual data center and SDDC both are same )

VMware Cloud Foundation brings together vSphere, vSAN, NSX, and SDDC Manager.


![vmware cloud foundation](/images/Vmware%20cloud%20foundation_01.png)

VMware Cloud Foundation works seamlessly with the virtualized desktops of Horizon, with vRealize’s time-saving automation of manual processes, with using the free and open source OpenStack on top of VMware infrastructure through VMware Integrated OpenStack, and with the virtual containers of vSphere Integrated Containers.

![vsphere_cloudfoundation_01](/images/Vmware%20cloud%20foundation_01.png)

VMware Cloud Foundation can be used to virtualize on-premises or to migrate off-premise

### vCloud Automation Center

`VMware vCloud Automation Center` is a cloud management product full of features and benefits for users and IT administrators. Through a single self-service catalog, you’re able to quickly deliver and easily manage the personalized infrastructure, applications, and services your business needs, while improving overall IT efficiency. 

First, your diverse environment is harmonized into a unified resource-pool. Then, you can easily and flexibly tailor services for each group or department, so different users can access the IT resources that fit their needs in record time.

Individuals have access to user-friendly self-service portals to create their own machines, be they virtual, cloud, or physical – so you won’t have to!

VMware vCloud Automation Center is not limited to working only with VMware products – it’s purpose-built to deliver services on different platforms from different vendors (e.g., AWS and Azure) at the right size and service-level for the task you need to be performed. And it extends to new technology and use-cases, meaning that you’re able to use new cloud services faster with more options for the future. All of which helps you achieve the business advantages that come from cloud computing.

### VMware cloud

VMware has a solution called VMware Cloud™ that can be utilized to manage applications (including containerized apps) across any cloud - be it public, private, or hybrid. VMware Cloud is an application platform designed to give administrators the flexibility to deploy and manage applications wherever they’re needed - in the cloud or in a container in Kubernetes. VMware Cloud works with both enterprise-sized cloud providers such as AWS, Azure, and Google, and on many other smaller-scale cloud providers.

![vmware cloud](/images/The_Cloud.jpg)

VMware has integrated cloud and virtualization technology tools into a simplified infrastructure called VMware Cloud™. VMware Cloud enables organizations to modernize their applications to be compatible with various cloud platforms and merge these applications to the cloud.


### Tanzu

Tanzu encompasses the full life-cycle of modern applications, automating the delivery of containerized applications, managing them centrally, and bringing a stronger focus on the cloud and all the advantages the cloud can bring. Tanzu enables applications in K8s to run independently and frees those applications from infrastructure.

Tanzu is an application program interface (API) that talks to the cloud environment and acts as an intermediary between Kubernetes and the cloud. For example, Tanzu allows organizations running an on-premise cloud with vSphere to integrate K8 into vSphere tools so that everything can be controlled from one interface. Currently there are three Tanzu solutions: Tanzu Basic, Tanzu Standard, and Tanzu Advanced.

The following breaks down each version and what role each plays in cloud native development:

`Tanzu Basic`: Provides integration between a vSphere private cloud and Kubernetes, as well as providing access to open source tools while also maintaining vSphere security policies.

`Tanzu Standard`: Provides integration between any cloud environment (private, public, multi, etc.) and Kubernetes. It also provides central control of K8 clusters located anywhere in the cloud while providing security policies for clusters across multiple environments.

`Tanzu Advanced`: Manages Kubernetes across multiple cloud environments and focuses on developer needs by providing tools for fast and secure container production, as well as advanced tools that provide information on container performance.

![vmware tanzu](/Images/vmware%20Tanzu.png)

`How Tanzu works`, Tanzu runs on a Kubernetes grid and manages several K8s clusters. This creates a Tanzu Kubernetes Grid (TKG). To manage the clusters, organizations have VMware Tanzu Mission Control. The purpose of Tanzu Mission Control is to operate and secure K8s and modern apps in the cloud. It provides a single point from which to:

- manage a K8s cluster life-cycle
- attach clusters regardless of where the clusters are running - in any public cloud and through any K8s vendor
- manage policies
- perform health-checks
- monitor the entire environment from one place
- and more.

### Cloudhealth

`cloudhealth` helps to analyze and report on your cloud costs, usage, performance, and security. Let’s take usage and costs as examples.

CloudHealth makes it very easy for you to see how well you’re using your infrastructure. It gives you extremely detailed information on what applications you’re running, down to the hour – even down to the minute. You can customize the time-period you want to look at and monitor either groups of resources or specific resources such as CPU, memory, and disk.

Amtrak, Yelp, Dow Jones, Skyscanner, and many other leading enterprises and service providers are using CloudHealth to manage those complexities better.

Now, let's go with [Interview Questions](/Interview_Questions.md)

