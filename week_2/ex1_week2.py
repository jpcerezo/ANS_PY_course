#!/usr/bin/env python

'''

juampe@parnassus ~> python
Python 2.7.13 (default, Dec 18 2016, 05:35:35) 
[GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pysnmp
>>> import patamiko
>>> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named patamiko
import paramiko
>>> pysnmp.__version__
>>> '4.3.2'
paramiko.__version__
>>> '2.1.1'

KeyboardInterrupt
>>> 

'''

import mi_funcion

mi_funcion.mi_funcion()

'''
juampe@parnassus ~/G/A/week_2> ./ex1_week2.py 
Aloha, man...
juampe@parnassus ~/G/A/week_2> ls 
ex1_week2.py          mi_funcion.py         my_prog.py            subdir                test_jpc_telnet.py
ex2_week2.py          mi_funcion.pyc        snmp_lesson.py        test_course_telnet.py
juampe@parnassus ~/G/A/week_2> sl subdir/
fish: Unknown command 'sl'
juampe@parnassus ~/G/A/week_2> ls subdir/
my.pyc
juampe@parnassus ~/G/A/week_2> rm subdir/my.pyc 
juampe@parnassus ~/G/A/week_2> mv mi_funcion.py subdir/
juampe@parnassus ~/G/A/week_2> rm mi_funcion.pyc 
juampe@parnassus ~/G/A/week_2> ./ex1_week2.py 
Traceback (most recent call last):
  File "./ex1_week2.py", line 25, in <module>
    import mi_funcion
ImportError: No module named mi_funcion
juampe@parnassus ~/G/A/week_2> export PYTHONPATH='/Users/juampe/GITHUB/ANS_PY_course/week_2/subdir'
juampe@parnassus ~/G/A/week_2> ./ex1_week2.py 
Aloha, man...
uampe@parnassus ~/G/A/week_2> mkdir -p ~/GITHUB/ANS_PY_course/week_2/lib/python2.7/site-packages
juampe@parnassus ~/G/A/week_2> mv lib/python2.7/mi_funcion.py ~/GIT/ANS_PY_course/week_2/lib/python2.7/site-packages
mv: rename lib/python2.7/mi_funcion.py to /Users/juampe/GIT/ANS_PY_course/week_2/lib/python2.7/site-packages: No such file or directory
juampe@parnassus ~/G/A/week_2> ls ~/GIT/ANS_PY_course/week_2/lib/python2.7/site-packages
ls: /Users/juampe/GIT/ANS_PY_course/week_2/lib/python2.7/site-packages: No such file or directory
juampe@parnassus ~/G/A/week_2> mkdir ~/GIT/ANS_PY_course/week_2/lib/python2.7/site-packages
mkdir: /Users/juampe/GIT/ANS_PY_course/week_2/lib/python2.7: No such file or directory
juampe@parnassus ~/G/A/week_2> mkdir ~/GITHUB/ANS_PY_course/week_2/lib/python2.7/site-packages
mkdir: /Users/juampe/GITHUB/ANS_PY_course/week_2/lib/python2.7/site-packages: File exists
juampe@parnassus ~/G/A/week_2> mv lib/python2.7/mi_funcion.py ~/GITHUB/ANS_PY_course/week_2/lib/python2.7/site-packages
juampe@parnassus ~/G/A/week_2> env -u PYTHONPATH
Apple_PubSub_Socket_Render=/private/tmp/com.apple.launchd.4V4X9azCqp/Render
DISPLAY=/private/tmp/com.apple.launchd.OUPP9HiLHj/org.macosforge.xquartz:0
HOME=/Users/juampe
LANG=en_US.UTF-8
LANGUAGE=en_US.UTF-8
LC_ALL=en_US.UTF-8
LC_CTYPE=UTF-8
LOGNAME=juampe
PATH=/opt/local/bin:/opt/local/sbin:/opt/local/Library/Frameworks/Python.framework/Versions/Current/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/local/sbin:/opt/X11/bin:/usr/local/MacGPG2/bin
PWD=/Users/juampe/GITHUB/ANS_PY_course/week_2
SHELL=/bin/bash
SHLVL=1
SSH_AUTH_SOCK=/private/tmp/com.apple.launchd.BaBhxlOy37/Listeners
TERM=xterm
TERM_PROGRAM=Apple_Terminal
TERM_PROGRAM_VERSION=361
TERM_SESSION_CLASS_ID=AFB11676-14F0-4B28-8475-F434AE34F73D
TERM_SESSION_ID=E278FD73-7C68-4300-83DE-AF0D611D25F7
TMPDIR=/var/folders/lk/qx3gmg552tj5vpprgkbc2sb00000gp/T/
USER=juampe
XPC_FLAGS=0x0
XPC_SERVICE_NAME=0
__CF_USER_TEXT_ENCODING=0x1F6:0x0:0x0
__fish_bin_dir=/Volumes/SATA 1TB/Downloads/fish.app/Contents/Resources/base/bin
__fish_datadir=/Volumes/SATA 1TB/Downloads/fish.app/Contents/Resources/base/share/fish
__fish_help_dir=/usr/local/share/doc
__fish_sysconfdir=/Volumes/SATA 1TB/Downloads/fish.app/Contents/Resources/base/etc/fish
juampe@parnassus ~/G/A/week_2> 
juampe@parnassus ~/G/A/week_2> python
Python 2.7.13 (default, Dec 18 2016, 05:35:35) 
[GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> from pprint import pprint
>>> pprint(sys.path)
>>> ['',
 '/Users/juampe/GITHUB/ANS_PY_course/week_2',
 '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip',
 '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7',
 '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin',
 '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac',
 '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages',
 '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk',
 '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old',
 '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload',
 '/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages']
^D>>> 
juampe@parnassus ~/G/A/week_2> ./ex1_week2.py 
Aloha, man...
juampe@parnassus ~/G/A/week_2>
'''

