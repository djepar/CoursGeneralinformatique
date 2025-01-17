## Course Introduction 
Google System Administration and IT Infrastruction 
System admnistration : "The field in It that's responsible for maintaining reliable computer systems in a multi-user environment."

## What is System Administration?
"IT infrastructure encompasses the software, the hardware, network, an services required for an organization to operate in an enterprise IT environment."

## Servers Revisited: 
Server : "Software or machine that provides services to other software or machines". 

## The Cloud
Data Center : "A facility that stores hundreds, if not thousands, of servers."

# Systems Administration Tasks

## Organization Policies
__Questions to keep in mind__ 
- Should users be allowed to install software?
- Should users have complex passwords with certain requirements?
- Should users be allowed to view non-work-related websites, like Facebook?
- If you hand out a company phone to an employee, should you set a device password?

## User and Hardware Provisioning
Hardware and software need to be standarize in some way. 
Stages 
- Procurement (buying)
- Deployment (installing)
- Maintenance (update and fix)
- Retirement (remove and replace)

# Applying Changes

## With Great Power Comes Great Responsibility
Uses admin session the less as possible. 
Record with script or Start-transcript what you do // or do documentation so you remember what you done (in case something went wrong)
- script : `script session.log` and when done `exit` || Ctrl-D
- Start-Transcript : `Start-Transcript -Path C:\Transcript.txt


Rollback : Reverting to a previous state

## Never Test in Production
Production : "the parts of the infrastructure where certain service is executed and served to its users."

Test environment : "A virtual machine running the same configuration as the production environment, but isn't actually serving any users of the service. "

Secondary or stand-by machine : "This machine will be exactly the same as a production machine, but won't receive any traffic actual users until you enable it to do so." 

"For even bigger services, when you have lots of servers providing the service, you may want to have canaries." 

## Assessing Risk
How important is the service, and how critical if the service fails. 

"In general, the more users your services reaches, the more you'll want to ensure that changes aren't disruptive. The more important your service is to your company's operations, the more you'll work to keep the service up." 

## Fixing Things the Right Way
Reproduction case : "Creating a roadmap to retrace the steps that led the user to an unexpected outcome."
Questions when doing a reproduction case: 
"""
- What steps did you take to get to this point?
- What's the unexpected or bad result?
- What's the expected result?
"""

# Intro to IT Infrastructure Service
## Types of IT Infrastructure Services
IaaS : Infrastructure as a Service like Amazon EC2, Linode. Windows Azure and Google Compute Engine. 

NaaS : Networking as a Service

SaaS : Software as a Service

PaaS : Plateform as a Service

DaaS : Directory as a Service

# Network Services
## FTP, SFTP, and TFTP
FTP or File transfer service : no encryption, authentication
SFTP or Secure File transfer: SSH encryption, authentication
TFTP or Trivial FTP : no encryption, no authentication

Other way of booting a computer : PXE Boot (preboot execution)

## NTP 
One of the oldest protocol : Network Time Protocol.
Keep the clock synchronize while connected to a network. 

## Network Support Services Revisited
Intranet : "An internal network inside a company; accessible if you're on a company's network."
Proxy server : "Acts as an intermediary between a company's network and the Internet."

## DNS
"Domain Name System (DNS) :Maps human-understandable names to IP addresses"

## DNS for Web Servers
First : purchasing a domain name. 
Second : pointing our website files to the domain name. 

## Unable to Resolve a Hostname or Domain Name
Ping a website you know work
nslookup a website you know work
Look for the /etc/host file

# Managing System Services 

## Managing Services in Linux
To see if there is a ntp deamon on Linux : `service ntp status`
To change date : `sudo date -s "2017-01-01 00:00:00"`
See the date : `date`
Stop ntp " `sudo service ntp stop`
Restart ntp: `sudo service ntp start`

## Managing Services in Windows
To manage the service update
`Get-service wuauserv` We can see if it's running.
To get more infore : `Get-service wuauserv | Format-List`
Stopping the service : `Stop-Service wuauserv` 
Then, to check if it's stop with `Get-Service wuauserv` 

## Configuring Services in Linux
"The configuration files for the installed services are located in the /etc/ directory. "

Ex: 
```
sudo apt install vsftpd
service vsftpd status
lftp localhost
//to change config --> /etc/vsftpd.conf

```
lftp : "an ftp client program that allows us to connect to an ftp server."

# Configuring Network Services
## Configuring DNS with Dnsmasq
Install Dnsmasq : `sudo apt install dnsmasq`
Start : `sudo service dnsmasq start`
Try : `dig www.example.com @localhost`
Stop : `sudo service dnsmasq stop`
Run in debug mode : `sudo dnsmasq -d -q` (try in parallel to see magic)

## Configuring DHCP with Dnsmasq
`ip address show eth_cli`
`cat dhcp.conf`
Run `sudo dhclient -i eth_cli -v` then `ip address show eth_cli`

# Software Services
## Configuring Communication Services
Communication service "enable employees in a company to talk to one another."
Instant communication 
- Internet Relay Chat (IRC) : chat messages. Work in a client/server model. 
- Paid for option : like HipChat and Slack. 
- XMPP : Extensible Messageing and Presence Protocol (Ex : Pdgin and Adium )

## Configuring Email Services
Two ways to set up email domain address
- "Run your own managed server. Using this option, you set up the emails services software on a server, then you create a DNS record for your mail server."

DNS : "A record is used for hostnames, but for email servers, we use MX for the mail exchange record."

Email protocol 
- Pop3 (Post Office Protocol 3): once view, can only accessible on one device. Good for storage limitation. 
- IMAP (Internet Message Access Protocol) : the email are on the server
- SMTP : protocol use to send email

## Configuring Security Services
HTTPS (Hyper text Transfer Protocol Secure) : "The secure version of HTTP, which makes sure the communication your web browser has with the website is secured through encryption."

HTTPS can be done with Transport layer Security (TLS) or SSL

# File Services
## Network File Storage
Network File System (NFS): "you can install NFS server software that modify the configuration files for the directories that you want to allow shared access to. Onece you do that, the NFS service will be running in the background of the server"

"The Server Message Block (SMB) protocol is a network file sharing protocol that allows applications on a computer to read and write to files and to request services from server programs in a computer network." 9https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831795(v=ws.11)?redirectedfrom=MSDN)

# Print Services
With Linux : Cups (Common UNIX Printing System)

#Platform Services
## Web Servers Revisited
Web server : "stores and serves content to clients through the Internet"
The most popular is Apache

## What is a database server
Databases " allow us to store, query, filter, and manage large amounts of data"
"Data base management system (DBMS), [...] is a computer program that interacts with a databsae. A DBMS allows you to control access to a database, write data, run queries, and perform  any other tasks related to database management."

# Troubleshooting Platform Services
"HTTP status codes are codes or numbers that indicate some sort of error or info messages that occurred when trying to access a web resource."

# Managing Cloud Resources
"Software as a Service (SaaS) : The software is already pre-configured and the user isn't deeply involved in the cloud configuration"
" Infrastructure as a Service(IaaS) : You're hosting your own services in the cloud. You need to decide how you want the infrastructure to look, depending on what you want to run on it."
Need to think of the Region : "If one of them fails for some reason, the others are still available and services can be migrated without visibly affecting users."
Private cloud : "When your company owns the services and the rest of your infrastructure - whether on-site or in a remote data center"
Hybrid cloud : private-public cloud. 

## Typical Cloud Infrastructure Setups
Typical Balancer "Ensures that each VM receives a balanced number of queries"
Autoscaling : "It allows the service to increase or reduce capacity as needed, while the service owner only pays for the cost of the machines that are in use at any given time"

## When and How to Choose Cloud
"Most cloud provides offer free trials, so it's a good idea to test that out to see if they meet your needs, and to check how well your company's infrastructure integrates with the cloud provider's."

# Introduction to Directory Service
## What is a Directory Server
"Directory Server : Contains a lookup service that provides mapping between network resources and their network addresses"


Should support replication : "The stored directory data can be copied and distributed across a number of physically distributed servers, but still appear as one, unified datastore for querying and administrating."
"Directory services : useful for organizing data and making it searchable for an organization"
OUs : Organization units

Advantages of replicatoins :
Redundancy  : "Directory server replication grants you redundancy by having multiple copies of the database being served by multiple servers."
Decreased latenty : "The added servers that provide lookup services also reduce the latency for client querying the service."
## Implementing Directory Services
Directory System Protocol (DSP)
Directory Information Shadowing Protocol (DISP)
Directory Operational Binding Management Protocol (DOP)
Active Directory
Lightweight Directory Access Protocol (OpenLDAP) --> favorite directory protocol right now. 

## Centralized Management
Centralized management : "A central service that provides instructions to all of the different parts of my IT infrastructure"
"Directory services provide centralized authentication, authorization, and accounting, also known as AAA." 
Configuration management can be done with : chef, puppet, sccm. 

# LDAP (Lighweight Directory Access Protocol)
LDIF : Data Interchange format :
dn = distinguished name, dc : domain component, ou : organizational unit, cn : common name;

## LDAP Authentification
To authenticate : 
- anonymous : "doesn't actually authenticate at all, and allows anyone to query the server. "
- simple : "involves sending the password in plaintext"
- sasl (simple authentication & security layer) : "involves a secure challenge-repsonse authentication mechanism"
LDAP Bind operation : "A client authenticates to a directory server using the Bind operation."
Kerberos : "a network authentication protocol that's used to authenticate user identity, secure the transfer of user credentials, and more."

# Active directory
"Active Directory (AD) : The native directory service for Mic rosoft Windows"
Work in a similar way as OpenLDAP.
Tools for AD : Active directory Administrative Center (ADAC). 
Above a domain (hierarchiccally) is a forest. A Forest can have one or more domain. 
"The service that hosts copies of the Active Directory are called Domain controllers. 

"Flexible Single-Master Operations (FSMOs) in AD are used to prevent conflicting updates in cases where conflict resolution is inappropriate. By planning the management of FSMOs, you enhance the availability of your Active Directory deployment."

## Managing Active Directory Users and Groups
For PS command for new AD group : `New-ADGroup`

## GPO or Group Policiy Object
GPO is " a set of policies and preferences that can be applied to a group of objects in the directory."
Need to be link to work : " When you link a GPO, all of the computers or users under that domain, site, or OU will have that policy applied."
"A Group Policy Object can contain computer configuration, user configuration, or both."
Policies : "Setting that are reapplied every few minutes, and aren't meant to be changed even by the local administrators"
Group policy preferences : "Settings that, in many cases, are meant to be a template for settings."
"Many policies and preferences in GPOs are represented as values in the Windows Registry"
"Windows Registry : A hierarchical database of settings that Windows, and many Windows applications, use for storing configuration data".


## Group Policy Troubleshooting 
"One of the most common issue you might encounter is when a user isn't able to __login__ to their computer, or isn't able to __authenticate__ to the Active Directory domain."
"The SRC records that we're interested in are _ldap._tcp.dc._msdcs.DOMAIN.NAME, where DOMAIN.NAME is the DNS name of our domain".
PS : `Resolve-DNSName -Type SRC _ldap._tcp.dc._msdcs.DOMAIN`

UTC Time can cause authentification problem. 


"A common issue that you might have to troubleshoot is when a GPO-defined policy or preference fails to apply to a computer"
To force the update of the gpo : gpupdate/force/sync

Replication failure

Check for the $env:LOGONSERVER

## Stateful vs. stateless
Stateless : "state not needed to work"
Stateful : "state must be maintained to work"

# OpenLDAP
Lightweight directory access protocol.
Can work on Linux, MacOS and Windows. 
To install it : `sudo atp-get install slapd ldap-utils`
On my version of linux, it's said that the version now is `ldap-utils` without the slapd


# Data Recovery

"The process of trying to restore data after an unexpected event that results in data loss or corruption.

"When an unexpected event occurs, your main objective is to resume normal operations as soon as possible, while minimizing the disruption to business functions."

"The best way to be prepared for a data-loss event is to have a well-thought-out disaster plan and procedure in place."

## Types of Backup
### Data backup solution
- Full backup --> all include
- Differential backup --> only files that change are backup
- Regular incremental backups --> "when only the data that's changed in file since the last incremental backup is backed up"
- File compression for backup
  
### Data storage solution
**RAID** : Redundant Array of Independent Disks
"A method of taking multiple physical disks and combining them into one large virtual disk."
NOT A REPLACEMENT FOR BACKUP

## Disaster Recovery Plans
"A collection of documented procedures and plans on how to react and handle an emergency or disaster scenario, from the operational perspective"

- Preventive measures : "Any procedures or systems in place that will proactively minimize the impact of a disaster"
- Detection measures : "Meant to alert you and your team that a disaster has occurred that can impact operations"
- Corrective or recovery measures : "Those enacted after a disaster has occurred" 

### Designing a Disaster Recovery Plan
-Perform risk assessment : "Allows you to prioritize certain aspects of the organizations that are more at risk if there's an unforeseen event"
- Determine backup and recovery system 
- Determine Dectection & Alert Measure
- Determine detection & alert measures & Test Systems
- Determine recovery measures

## Post-mortem
"We create a post-mortem after an incident, an outage, or some event when something goes wrong, or at the end of a project to analyze how it went."

### Writing a post-mortem
- Brief summary
- Detailed Timeline
- Root Cause
- Resolution and recovery Efforts
- Actions to Avoid Same Scenario
- Optional : what went well (useful to justify the backup cost and effort)