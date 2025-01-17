# Software Distribution
From Operating Systems and You, the google-coursera IT certification. 
## Windows : Software Packages
### Executable file(.exe)
 Contain instructions for a computer to execute when they're run. 
Executable isnt something unique to Windows, but the special implementation of Windows is the portable executable or PE format. 


#### PE format (Portable Executable)
The filename extension of PE are :
- acm, .ax, .cpl, .dll, .drv, .efi, .exe, .mui, .ocx, .scr, .sys, .tsp

"The PE FORMAT is a datastructure that encapsulates the information necessary for the Windows OS loader to manage the wrapped executable code. This includes dynamic library references for linking, API export and import tables, resource management data and thread-local storage (TLS) data." (https://en.wikipedia.org/wiki/Portable_Executable, 19 of August 2022)
### Microsoft Install package(.msi)
Used to guide a program called the Windows Installer in the installation, maintenance, and removal of programs on the Windows operating system. 
### Windows Store 
A platform to download and install universal Windows platform apps. 
Can work on desktop PCs or Windows tablet. 
The format is APPX
For more information :  https://docs.microsoft.com/en-ca/windows/win32/appxpkg/make-appx-package--makeappx-exe-?redirectedfrom=MSDN
### How to install program from the terminal

#### .exe
For exe : only write the path and the name of the files : 
`PS C:\Users\jpara\Documents\Etudes\CoursGenInfo\hello.exe`


## Linux : Software Packages
Difference between distribution. 
### Debian
Packaged as a .deb file for Debian
To install a .deb : dpkg 
`sudo dpkg -i atom-amd64.deb`
To remove
`sudo dpkg -r atom`
To find the list of program
`dpkg -l`

## Mobile App Packages
Install through App stores : a central, managed marketplace for app developers to publish and sell mobile apps. 
Or with sideloading, but it's more dangerous. 
For Google Play Custom App Publishing API : https://developers.google.com/android/work/play/custom-app-api/get-started

## Windows : Archives
The core or source software files that are compressed into one file. 
To compress on PS
```
Compress-Archive -Path C:\Users\jpara\Documents\Etudes\CoursGenInfo\Directory ~Desktop\CompressedDir
```
For more info : https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.archive/compress-archive?view=powershell-7.2&viewFallbackFrom=powershell-5.0

to unzip :
```
Expand-Archive -LiteralPath <PathToZipFile> -DestinationPath <PathToDestination>
Expand-Archive .\Compressed.zip Decompressed
```
## Linux : Archives
To extract a file using 7zip, use the command 7z and the flag e for extract and then the file you want to extract.
It's a to compressed.
```
7z a dir1
7z e dir1
```

### Tar 
See : http://www.linfo.org/tar.html

## Windows : Package Dependencies
Dependency :Counting on other pieces of software to make an application work, since one bit of code depends on another, in order to work. 
A library :  a way to package a bunch of useful code tha tsomeone else wrote.
TO install sysinternals and the chocolatey 
```
Register-PackageSource -Name chocolatey -ProviderName chocolatey -Location https://chocolatey.org/api/v2
```
Find-Package sysinternals -IncludeDependencies

## Linux : Package Dependencies and Package Manager
Package managers : come with the works to make package installation and removal easier, including installing package dependencies. 
dpkg is a package manager for Debian-based Linux systems.

Apt and dpkg : both command-line package management interfaces

Differences (from https://www.makeuseof.com/apt-vs-dpkg/ )
 - APT or apt-get uses dpkg to install Package 
 - APT can Download packages while dpkg only let you install local file. 
 - Dpkg don't install dependencies. APt will.

Installation with apt : `sudo apt install <program>`
Uninstall with apt : `sudo apt remove <remove>`
Update with apt : `sudo apt upgrade` or `sudo apt update`

PPA : A Personal Package Archive, a software repository for uploading source packages to be built and published as an Advanced Packaging Tool (APT) repository by Launchpag

In Linux repository sources are listed in : /etc/apt/sources.list
#Package Managers
## Windows : Package Manager
Package manager : Makes sure that the process of software installation, removal, update, and dependency management is as easy and automatic as possible. 
### Chocolatey : Third-party package manager
Example : `choco install notepadplusplus.install`

Can also use NuGet, another package manager

## Windows : Underneath the hood
To look what do an installer program do, we can use the Process Monitoring of the Microsoft CIS internals toolkits. 
Orca.exe : a database table editor for creating and editing Windows Installer packages and merge modules. The tool provides a graphical interface for validation, highlighting the particular entries where validation errors or warnings occur. 

Windows Software Development Kit(SDK) : includes redistributable components, documentation, installer, database validation tool, database table editor, database schema, development tools, VBScript tools, sample product and code samples. 

Process Monitor : An advanced monitoring tool for Windows that shows real-time file system, Registry and process/thread activity. 

## Linux : Underneath the Hood 
Normally : from an app you have the code, the README files and a setup_script

# Device Software Management
Driver : Used to help our hardware devices interact with our Operating System
## Windows : Device Manager
In Windowws, Microsoft groups all of the devices and drivers on the computer in a single Microsoft management console :  the Device Manager
Access it in run : devmgmt.msc
Or Windows+x > Devices Manager

## Linux : Devices and Drivers
In Linux, even hardware are considere a file. 
When a new device is connected, a device file is created in the /dev directory. 

Character devices or character special files : 
- like keyboard, or mouse transmit data character by character.
- Raw devices, meaning that the programs don't read and write aligned block
Block devices or block special files: 
- like USB drives, hard drives, and CDROMS, transfer blocks of data; a data block.
-  Buffered access to hardware devices and provide some abstraction from their specifics
SD devices : mass storage devices
/dev/sd[a-Z] 

To see the list of block on linux : `lsblk`
To see the list of the device : https://web.archive.org/web/20160424173724/https://www.kernel.org/doc/Documentation/devices.txt

udev : "(userspace / dev) is a device manager for the Linux kernel, as the successor of devfsd and hotplug, udev primarily manages devices nodes in the /dev directory" (https://en.wikipedia.org/wiki/Udev, 20 august 2022)

# Windows : Operating System Updates
Windows IT Pro Blog : https://techcommunity.microsoft.com/t5/windows-it-pro-blog/bg-p/Windows10Blog

# Linux : Operating System Updates
With : `apt- upgrade`
But it doesnt upgrade the kernel. To know the version of the kernel : `uname -r`
For the full upgrade : `sudo apt full-upgrade`
Linux kernel is a monolithic kernel

# Filesystems

## Review of Filesystems 
Filesystem : Used to keep track of files and file storage on disk. 

In Windows : NTFS
In Linux : ext4
Fat32 works with Windows, Linux and MacOS

## Disk Anatomy
"A store device can be split into partition. "
"A partition is the piece of a disk tha tyou can manage. "
"To add a filesystem to a disk, first you need to create a partition."

It's possible to add different filesystems on different partitions of the same disk. 

"When you format a filesystem on a partition, it becomes a volume."

Partition table : tells the OS how the disk is partitioned. 
Two mains partition table schemes : Master Boot Record (MBR) and GUID Partition Table(GPT)

MBR : Max 2TB of volume size, mostly on Microsoft, only 4 Partitions 
GPT : becoming the new standard : 2TB or greater, one type of partition and unlimited nbr of partitions. 

## Windows : Disk Partitioning and Formatting a Filesystem
Using the GUI : Disk Management

"DiskPart is a disk partitioning utility on the Windows operating system which uses the command line to perform operations."
"DiskPart utility can be used to manage partitions of hard disks including creating, deleting, merging, or expanding partitions and volumes. It can also be used to assign a file formatting system to a partition or volume."

PS : `Diskpart` 
Then list disk
To wipe a disk : clean

### Cluster 
"Cluster size is the smallest division of storage possible in a drive. cluster size is important because a file will take up the entire size of the cluster regardless of how much space it actually requires in the cluster."

### Mounting
"Making something accessible to the computer, like a filesystem or a hard disk."


## Linux: Disk Paritioning and Formatting a Filesystem

Look for the partition : `sudo parted -l`
Then `sudo parted <path to the disk>

## Linux : Mounting and Unmounting a Filesystem
`sudo mount <path>`
`sudo umount <path>`

Go see `cat /etc/fstab` 
    "Lists all available disk partitions and other types of file systems and data sources that may not necessarily be disk-based" (https://en.wikipedia.org/wiki/Fstab)
And `sudo blkid`

## Windows: Swap
Virtual memory : "How our Os provides the physical memory available in our computer (like RAM) to the applications that run on the computer"

Windows use Memory Manager to manage virtual memory. 
"In Windows, pages saved to disk are stored in a special hidden file on the root partition of a volume called pagefile.sys"

## Linux : Swap
Swap space : "the dedicated area of the hard drive used for virtual memory" in Linux. 
Mkpart a part  : `mkpart primary linux-swap 5GiB 100%`
Then : (quit first) `sudo mkswap /dev/sdb2`
Finaly : `sudo swapon /dev/sdb2`

## Windows : Files
The data is the actual content of a file. 
File meta-data : everything else related to that file. 
With every NTFS files, there is a MTF section with MTF entry that include : file name, timestamp, permissions, compression, location, etc. 
MTF = (Master file table)

### Way to access a file : 
- Shortcut
- Symbolic links : shortcut at the files system level. There is an MTF with the location of another file. the difference with shortcut is that the operating system treats them like substitutes for the file they're linked to in almost every meaningful way. 
    - To make a link : mklink
- Hard link :  "when you create a hard link in NTFS, an entry is added to the MFT that points to the linked file record number, not the name file."

## Linux: Files
"In Linux, metadata and files are organized into a structure called an inode. Inodes are similar to the Windows NTFS MFT records"
"In Linux, an inode stores everything about a file, except for the filenam and the file data"
### Softlink
The equivalent of shortcut in Linux are *softlink*.  "They're great for creating shortcuts to other files. 
To create a softlink : `ln -s important_file important_file_softlink`
### Hardlink
Hardlink point to a physical location on a disk, "if you delete the file of a hardlink, all other hardlinks would still work."
to create a hardlink `ln important_file important_file_hardlink`

## Windows: Disk Usage
Check the disk usage with "Computer management>Storage>Disk Management"

### Defragmentation
"The idea behind disk defragmentation is to take all the files stored on a fiven disk, and reorganize them into neighboring location."
Mostly useful for disk-drive. 
For solid state disk  : Trim "to reclaim unused portions of the solid state disk."
Now done automatically, but can also be done manually with defragment and Optimize Drives tools.

## Linux : disk Usage
To know the disk usage : `du -h`
To know how much free space :` df`

## Windows : Filesystem Repair
"Data buffer : A region of Ram that's used to temporarily store dat awhile it's being moved around."
"So if you don't properly unmount a file system and give your buffer enough time to finish moving data, you run the risk of data corruption."
To check for the disk : `chkdsk /F C:`

## Linux : Filesystem Repair 
`sudo fsck /dev/sda` : can damage the disk if use will using it. 

# Life of a Process

## Program vs Processes Revisited
Programs : "The applications that we can run, like the Chrome web browser."
Processses : "Programs that are running"
Each process avec a Process ID. 
Background processes or deamon processes : run in the background. 

## Windows : Process Creation and Termination
"When Windows boots up, or starts, the first non-kernel user mode that starts is the Session Manager Subsystem or smss.exe. The smss.exe process is in charge of setting some stuff up for the OS to work."
Then smss.exe start the Client/Server Runtime Subsystem (crss.exe) which take care of the Windows GUI and CLI. 
To find the process on PS : `get-process`
`cat .\processes.txt | Select-String "firefox"`
To kill a mocking process : `taskkill /pid 10420`

## Linux : Process Creation and Termination
"In Linux processes have a parent child relationship. This means that every process that you launch comes from another process."
Genesis : "When you startup your computer, the kernel creates a process called init, which has a PID of 1."

# Managing Processes
## Windows: Reading Process Information 
"You can think of processes as programs in motion."
Task manager (taskmgr.exe) "is one method of obtaining process information"

## Linux : Reading Process Information
to list every processes : `ps -x`
To search : `ps -x | grep "string"`
For a more detail list : `ps -ef`

## Windows: Signals
Signal is "a way to tell a process that something's just happened".
"One of the most common signals [...] is called SIGINt, which stands for signal interrupt. 

## Linux : Signals 
"You can use sigint to interrupt a process and the default action of this signal is to terminate the process that's interruption."
CTRL-C to do sigint. 

## Windows: Managing Processes
Process Explorer : "A utility Microsoft created to let IT Support Specialists, system administrators and other users look at running processes."

## Linux: Managing Processes
To end a program : `kill <PID>`
With signal : kill -KILL <PID>` (Last resort, because no clean up)
To stop : kill -tstp <pid>

## Mobile App Management
Can't see all the process, but we can see the foreground and background app.

# Process Utilization

## Windows : Resource Monitoring
With Process Explorer or `Get-Process`
To try by the CPU usage : `Get-Process | Sort CPU -descending | Select -first 3 -Property ID, ProcessName, CPU`

## Linux : Resource Monitoring
One of the most useful command for resource monitoring is `top` which list the process by usage

To see the load average : `uptime` (funky time)

`lsof` : it's list the open files and what processes are using them. 

# Remote Access

## Remote Connection and SSH
Remote connection : "Allows us to manage multiple machines from anywhere in the world."
Secure shell (SSH) : "A protocol implemented by other programs to securely access one computer from another" 

Virtual private Network (VPN) : "Allows you to connect to a private network, like your work network, over the Internet". 

## Remote Connections on Windows 
PuTTY : "A free, open source software that you can use to make remote connections through several network protocols, including SSH".

Using putty with powershell : `putty.exe -ssh cindy@104.104.104.104 22`

Putty Link 

Remote Desktop Protocol (RDP)

## Remote Connection File Transfer
Secure Copy(SCP) : "A command you can use in Linux to copy files between computers on a network"
`scp /home/jepar/Desktop/myfile.txt cindy@104.131.122.215`

## Remote Connection File Transfer on Windows
With putty : pscp.exe (PuTTy Secure Copy Client)
`pscp.exe ~\Desktop\myfile.txt cindy@101.101.101.101`
Used Shared Documents
See also net share (https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh750728(v=ws.11)?redirectedfrom=MSDN)

# Virtual Machine
Virtual instance : "A single virtual machine"

# System Monitoring : 
Logging : "The act of creating log events"

## The Windows Event Viewer
"The events logged by the operating system are stored in an application called the __Event Viewer__."
On run : eventvwr.msc

## Linux Logs
All the logs are in the /var/log
Good one to check is : /var/log/syslog

# Operating System Deployment
"Imaging a machine means to format a machine with an image of another machine. This includes everything, from the operating system to the settings."

## Operating Systems Deployment Methods 
Disk Cloning tool : "It make a copy of an entire disk and allows you to back up a current machine or set up a new one." 
Ex : clonezilla and symantec Ghost

On linux : `dd if=/dev/sdd of=~/Desktop/my_usb.image.img bs =100M`