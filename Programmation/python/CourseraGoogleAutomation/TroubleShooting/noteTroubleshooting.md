# Troubleshooting Concepts
Troubleshooting : "The process of identifying, analyzing, and solving problems"
Debugging : "The process of identifying, analyzing and removing bugs in a system. "

Examples of tools : 
- tcpdump 
- wireshark
- strace
-ltrace : A library call tracer (https://www.man7.org/linux/man-pages/man1/ltrace.1.html)

Debuggers : 
"Let us follow the code line by line, inspect changes in variable assignments, interrupt the program when a specific condition is met, and more"

## Problem Solving Steps 
1. Getting information
    - Reproduction case : "A clear description of how and when the problem appears".
2. Finding the root cause
3. Performing the ncessary remediation. 
Important to document what we do while debugging. 

### Silently Crashing Application
strace "lets us look more deeply at what the program is doing. It will trace a system calls made by the program and tell us what the result of each of these calls was."
System calls : "calls that the programs running on our computer make to the running kernel". 
To see failure `strace -o failure.strace ./<program-name>`
Pipping with less : `strace ./script.py | less`

# Understanding the problems
Questions to ask to understand what didn't work :
"
- What were you trying to do?
- What steps did you follow?
- What was the expected results?
- What was the actual results?
"

## Reproduction case 
"A reproduction case is a way to verify if the problem is present or not"
"First step is to read the logs available to you"
On Linux : /var/log/syslog and read the file .xsession-errors
On MacOs /library/Logs
On Windows : Event viewer tool.
## Finding the Root Cause
Use creativity and research to find the cause. 
For memory error, we can use iotop, iostat and vmstat
And to solve it : ionice
For a service using to much network bandwith : iftop,
To solve it rsync or Trickle
## Dealing with Intermittent Issues
If possible, adding code to have more information. 
Heisenbug or the observer effect : "observing a phenomen alters the phenomenon."

# Binary Search a Problem
Faster, but need a sorted list. 

## Applying Binary Search in Troubleshooting
Bisecting the problem : each part of the problem we know is working can be put aside.

git let us use `bisect` that do that automaticaly. 

## Finding Invalid Data 
`cat contacts.csv | ./import.py --server test`

Important to put server. 

Using `wc` to count the number of files
`wc -l contacts.csv`

Searching invalid Data with head and tail
`head -50 contacts.csv | ./import.py --server test`
`less -50 contacts.csv | ./import.py --server test`
`head -50 contacts.csv | tail -25 | head -13 ./import.py --server test`

# Introduction to Slowness
## Why is my computer slow?
Monitoring are system to see where is the bottleneck component :
- On Linux : top
- MacOs : Activity Monitor
- Windows : Resource Monitor and Performance Monitor. 

## How Computers Use Resources
The data uses by a processes can be on the CPU/GPU, RAM,  Hard-driver or Network (from the quicker to slower)
Cache is a good way to fasten the speed of an app : if the data is on the network, we can cache it on the RAM (etc).

## Possible Causes of Slowness
Use the process of elimination (like with every other problem) : 
1. Looking for the simplest explanation. 
2. Bissecting the problem

Possibles causes
- When a file uses by a program become to big. 
    - Can be solve with logrotate
- Can look if the problem is for all users or just some (help fin the cause)
- If a program use a share-file system base on a network
- Malicious software

## Slow Web Server
If the loading page is slow, we can use the tool `ab` (Apache Benchmark) "to figure out how slow it is."

Priority in linux : lower the number, the higher the priority. 

To change the priority  : `nice` and `renice`

Example "for pid in $(pidof ffmpeg); do renice 19 #pid; done
To resolve the ffmpeg problem
`for pid in $(pidof ffmpeg); do while kill -CONT $pid: do sleep 1; done

## Monitoring tools
https://docs.microsoft.com/en-us/sysinternals/downloads/procmon 

http://www.brendangregg.com/linuxperf.html

http://brendangregg.com/usemethod.html

Activity Monitor in Mac:

Performance Monitor on Windows

https://www.digitalcitizen.life/how-use-resource-monitor-windows-7

https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer

https://en.wikipedia.org/wiki/Cache_(computing)

https://www.reddit.com/r/linux/comments/d7hx2c/why_nice_levels_are_a_placebo_and_have_been_for_a/

# Slow code
## Writing Efficient Code 
"We should always start by writing clear code that does what it should, and only try to make it faster if we realize that's not fast enough."
"Trying to optimize every second out of a script is probably not worth your time." 
__Good practice__ : 
- "Storing data that was already calculated"
- "Using the right data structures for the problem"
- "Reorganizing the code so that the computer can stay busy while waiting for information form slow source."

__Profiler__ : "A tool that measures the resources that our code is using, giving us a better understanding of what's going on."
For C, the profiler is gprof
For Python the profiler is cProfile 
For example, the "Cprofile module is used to count how many times functions are called, and how long they run."

Avoiding expensive action ("Those that can take a long time to complete")

## Using the Right Data Structures
Lists : "Sequences of elements. We can add, remove, or modify the elements in them, and we can iterate through the whole list to operate on each of the elements. "

Called : "Arraylist in Java, Vector in C++, Array in Ruby, Slice in Go"

Dictionaries : "Store key-value pairs. We add data by associating a value to a key, and then we retrieve a value by looking up a specific key."

Called : "HashMap in Java, Unordered Map in C++, Hash in Ruby, Map in Go". 
Advantage : really fast to find value with a key. 

"If you need to acess elements by position, or will always iterate through all the elements, use a list to store them."

"If we need to look up the elements using a key, we'll use a dictionary."

## Expensive Loops
"If you do an expensive operation inside a loop, you multiply the time it takes to do the expensive operation by the amount of times you repeat the loop."

"Make sure that the list of elements that you're iterating through is only as long as you really need it to be."

"Another thing to remember about loops is to break out of the loop once you've found what you were looking for"

## Keeping Local Results
"If we're parsing a large file and only keeping a few key pieces of information form it, we can create a cache to store only that information, or if we're getting some information over the network, we can keep a local copy of the file to avoid downloading it over and over again". 

## Slow Script with Expensive Loop
Three values of the `time` command :
- Real : "The amount of actual time that it took to execute the command. 
- User : "The time spent doing operations in the user space"
- Sys : "The time spent doing system-level operations. 

pprofile3 and kcachegrind to see the file generated. 
# When Slowness Problems Get Complex

## Parallelizing Operations
"Threads : Let us run parallel tasks inside a process"
In Python, we can do threading or  __Asyncio__ module. 
I/O bound, when the script is waiting for information. 
"A script is __CPU bound__ iy you're running operations in parallel using all available CPU time."


(From https://realpython.com/python-concurrency/)
- "Threading (or pre-emptive multitasking) : the operating system decides when to switch tasks external to Python. 
- Asyncio (cooperative multitasking) : the tasks decide when to give up control. 
- Multiprocessing : The processess all run at the same time on different processor"
## Slowly Growing in Complexity
The more a file is large, the more we need to adjust the medium to contain it. CSV> SQLLite > DataServer (for example)

## Using Threads to Make things Go Faster
Python script :
To run something in parallel we need : 
- "Executor : "The process that's in charge of distributing the work among the different workers."
- Futures module : "provides a couple of different executors; one for using threads and another for using processes."
```
from concurrent import futures


executor = futures.ThreadpoolExecutor()
for root, _, files in os.walk('images'):
    for basename in progress_bar(files):
        if not basename.endswith(".jpg");
            continue
        executor.submit(process_file, root, basename)
print("Waiting for all threads to finish.")
executor.shutdown()
```
To make process instead of thread :
```
from concurrent import futures


executor = futures.ProcessPoolExecutor()
for root, _, files in os.walk('images'):
    for basename in progress_bar(files):
        if not basename.endswith(".jpg");
            continue
        executor.submit(process_file, root, basename)
print("Waiting for all threads to finish.")
executor.shutdown()
```
## Worklabs
"rsync(remote sync) is a utility for efficiently transferring and synchronizing files between a computer and an external hard drive and across networked computers by comparing the modification time and size of files. One of the important features of rsync is that it works on the delta transfer algorithm, which means it'll only sync or copy the changes from the source to the destination instead of copying the whole file. This ultimately reduces the amount of data sent over the network."

```
/home/student-01-cd6edbe0c987/data#!/usr/bin/env_python
from multiprocessing import Pool
def run(task)
#do something with task here
    print("Handling {}".format(task))
    #Create a pool of specific number of CPUs
    p = Pool(len(tasks))
    #Start each task within the pool
    p.map(run, tasks)

```

# Why Programs Crash
## Systems That Crash
1. Reduce the scope
   1. Looking at the log
   2. Trying to make the bug again, on the computer where it's happen and another
2. Try if it's happen reliably ("Do all invoice generations fail?")
3. Look for the hardware (trying another computer)
   1. Look for the RAM
   2. Looking for overheating
   3. Look for the Graphic/audio card

## Understanding Crashing Applications
To see logs :
- Linux : Varlog or usrlog 
- MacOS : Console App 
  - System Log Folder: /var/log
  - System Log: /var/log/system.log
  - Mac Analytics Data: /var/log/DiagnosticMessages
  - System Application Logs: /Library/Logs
  - System Reports: /Library/Logs/DiagnosticReports
  - User Application Logs: ~/Library/Logs (in other words, /  
  - Users/NAME/Library/Logs)
  - User Reports: ~/Library/Logs/DiagnosticReports (in other words, /Users/NAME/Library/Logs/DiagnosticReports)
- Windows : Event Viewere

To get more information about a program : 
- Linux : strace
- MacOS : dtruss
  - To look at a a specific PID : `dtruss -p 1871`
- Windows : Process Monitor
  - Run then perfmon

"To find the root cause of a crashing application, we'll want to look at all available logs, figure out what changed, trace the system or library calls the program makes, and create the smallest possible reproduction case"

## What to do when you can't fix the program?
Wrapper : "A function or program that provides a compatibility layer between two functions or programs, so they can work well together"
Watchdog : "A process that checks whether a program is running, and, when it's not, starts the program again"

## Internal Server Error
Usually a 500 error on the browser
To look for log more information :
```
ssh webserver
date
cd /var/log/
ls -lt | head
```

Netstat to access "a  bunch of sockets that are restricted to route the administrator user on Linux" : `sudo netstat -nlp | grep :80`

"The /etc directory will contain the application folder that stores configuration files"

## Resources for Understanding Crashes
Worst crashes 
- Linux and MacOS : Kernel Panic
- Windows : Blue Screen of Death

# Code that Crashes
## Accessing Invalid Memory
"Accessing invalid memory means that the process tried to access a portion of the system's memory that wasn't assigned to it."

Pointers : "The variables that store memory addresses"

Can be a pointers problem, which are called segmentation faults or segfaults.

"""Common programming errors that lead to segmentation faults:
- Trying to access a list element outside of the valid range
- Trying to use a portion of memory after having given it back
- Trying to write more data than the requested portion of memory can hold
"""

In case of a seffault : "is to attach a debugger to the faulty program. This way when the program crashes, you'll get information about the function where the fault happened"

Undefined behavior : "The code is doing something that's not valid in the programming language"

Valgrind : "A very powerful tool that can tell us if the code is doing any invalid operations, no matter if it crashed or not"

Dr. Memory : "can assist in finding out if invalid operations are occuring in a program running on Windows or Linux"

## Unhandled Errors and Exceptions
Traceback : "Shows the lines of the different functions that were being executed when the problem happened"

In Python, the debugger is pdb.

Printf debugging : Written statement in the code with var value to look where the program generate error

Logging module (in Python) : " The logging module sets debug messages to show up when the code fails"

## Fixing Someone Else's Code
1. Reading the comments or adding comments if no comments
2. Reading the test associated with the code or write test if there is none
3. Locate the affected function

## Debugging a Segmentation Fault
Core files : "Store all the information related to the crash so that we, or someone else, can debug what's going on"
In linux : 
```
ulimit -c unlimited
ls -l core
gdb -c core example
(gdb) backtrace 
(gdb)up
(gdb)print i
```

## Debugging a Python Crash
Python Debugger : `pdb3 name_script.py` then `next` or `continue`


# Handling Bigger Incidents
## Crashes in Complex Systems
1. Look at the general system logs
2. If the problems start appearing at the same time as some change, trying to rollback can help.
3. If the error message is not helpful, we can "include what the request and the response were and why the response was invalid" (in the case of a server problem, writing similar report for other kind of problem)
4. Find if there is one server/machine/computer where the problem start or came from. Isolating it if it's the case

## Communication and Documentation During Incidents
Regular information to the users for the update and issues that are coming/happened. 
When an issue is fix, it's important to sum up what happen, why, when and how it's was fix and how we can prevent it from happening again

## Writing Effective Postmortems
Postmortems : "Documents that describe details of incidents to help us learn from our mistakes"
Shouldn't be a blame.
Should include :
"""
- What caused the issue
- What the impact of the issue was
- How it got diagnosed
- The short-term remediation you applied
- The long-term remediation you applied
"""

# Managing Resources
## Memory Leaks and How to Prevent Them
**Memory leaks** : "A chunk of memory that's no longer needed is not release"
**Garbage collector**: "In charge of freeing the memory that's no longer in use"
**Memory profiler** : To checkhow the memory is being used
    In C and C++ : Valgrind
    In Python : a bunch of tool : 

## Managing Disk Space
Used of disk space 
- Installed binaries and libraries
- Data stored by the applications
- Cached information
- Logs
- Temporary files
- Backups

Running out of space create bug and problems.

## Network Saturation
**Latency** : The delay between sending a byte of data from one point and receiving it on the other. 

**Bandwidth** : How much data can be sent or received in a second. 

** Trafic shapping ** : A way of marking a data packets sent over the network with different priorities to avoid huge chunks of data use all of the bandwidth.

## Dealing with Memory Leaks
**Scroll buffer** : Feature that lets us scroll up and see the things that we executed and their output. 

**Decorator** : Used in Python to add extra behavior to functions without having to modify the code.

# Managing Our Time
## Getting to the Important Tasks
**Technical dept** : The pending work that accumulates when we choose a quck-and-easy solution instad of applying a sustainable long-term one.

