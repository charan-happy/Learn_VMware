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

Datastores can be deployed in two methods. 1. Direct-attached Storage and Network-based storage.

- pending Raid and some other topics in storage
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

EXSI is a type=-1 hypervisor software that is installed directly onto a physical server and creates the foundation for the virtual layer. ESXI enables the server hardware to be partitioned into multiple logical computers, which you now know are VMs.

Virtual machines run on and consume resources from ESXI, but ESXI is running on top of the physical server itself to help administer the hardware resources.  ESXI is like a command center that all the applications on the Vm talk to, then it turns around and tells the hardware what to do.




### server virtualization


### storage virtualization

### network virtualization

### Application and Desktop virtualization

### From physical to virtual datacenter - convergence

### vMotion

### Storage vMotion

### vSphere High Availability (HA)

### vSphere Distributed Resource Scheduler (DRS)

### vSphere Storage Distributed Resource Scheduler (Storage DRS)

### vSphere Fault Tolerance (FT)

### vSphere Replication

### VMware VSAN

### Hyper converged Infrastructure

### VMware NSX

### VMware cloud Foundation

### vCloud Automation Center

### VMware cloud

### Tanzu

### Cloudhealth


Now, let's go with [Interview Questions](/Interview_Questions.md)

