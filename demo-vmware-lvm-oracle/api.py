#!/usr/bin/env python2
# Version: 0.1a5

import socket

from bottle import post, request, run
from fabric.api import local
from netifaces import AF_INET, ifaddresses

@post('/api/filesystem/increase')
def filesystem():
    """Increase file system.
    Automatically increase filesystem on Red Hat 7. Add new disk or
    modify existing in VMware (if applicable).
    Input:
        host -- linux hostname (not required | type: string |
                default: localhost)
        fs -- file system name (required | type: string),
        vmware -- Vmware vSpehre service to connect to (not required |
                  type: string),
        vmware_user -- user name to use (not required | type: string),
        vmware_passwd -- password to use(not required | type: string),
        disk_size -- disk size, in GB, to add to the VM
                     (not required | type: string | default: 16).

    """

    data = {}
    data['host'] = 'localhost'
    data['fs'] = None
    data['vmware'] = None
    data['vmware_user'] = None
    data['vmware_passwd'] =  None
    data['disk_size'] = '16'

    query = request.query
    for k, v in query.items():
        if k in data:
            data[k] = v
    if data['fs'] == None:
        return 1
    if data['host'] == 'localhost':
        data['host'] = socket.gethostname()
    extra_vars_str = 'host=%s fs=%s vmware=%s vmware_user=%s ' \
                     'vmware_passwd=%s disk_size=%s'
    extra_vars_str = extra_vars_str % (data['host'], data['fs'],
            data['vmware'], data['vmware_user'], data['vmware_passwd'],
            data['disk_size'])
    text = "ansible-playbook /root/increase-filesystem.yml " \
           "--extra-vars '%s'" % extra_vars_str
    blocks = text.split(" ")
    command = []
    for el in blocks:
        if 'None' not in el:
            command.append(el)
    command = " ".join(command)
    local(command)
    return 0

@post('/api/tablespace/increase')
def tablespace():
    """Increase tablespace.
    Automatically increase tablespace in Oracle DB. Increase file system on
    Red Hat 7, add new disk or modify existing in VMware (if applicable).
    Input:
        host -- Oracle database host (not required | type: string |
                default: localhost),
        db_name -- Oracle database service name to connect to
                   (required | type: string),
        tablespace_name -- tablespace that should be managed
                           (required | type: string),
        db_user -- Oracle user name to connect to the database
                (required | type: string),
        db_passwd -- Oracle user password for 'user' (required | type: string),
        free_mb -- minimum required size of tablespace free space. Not
                   increase tablespace, if value less than current available
                   tablespace free space (not required | type: string |
                   default: 32000),
        size -- size of the datafile (not required | type: string |
                default: 1G),
        next_size -- size of the next extent allocated (not required |
                    type: string | default: 1G),
        max_size -- maximum size of the datafile (not required | type: string |
                   default: UNLIMITED),
        fs -- file system name (required | type: string),
        vmware -- Vmware vSpehre service to connect to (not required |
                  type: string),
        user -- user name to use (not required | type: string),
        passwd -- password to use(not required | type: string),
        disk_size -- disk size, in GB, to add to the VM
                     (not required | type: string | default: 16).

    """

    data = {}
    data['host'] = 'localhost'
    data['db_name'] = None
    data['tablespace_name'] = None
    data['db_user'] =  None
    data['db_passwd'] = None
    data['free_mb'] = '32000'
    data['size'] = '1G'
    data['next_size'] = '1G'
    data['max_size'] = 'UNLIMITED'
    data['fs'] = None
    data['vmware'] = None
    data['vmware_user'] = None
    data['vmware_passwd'] =  None
    data['disk_size'] = '16'

    query = request.query
    for k, v in query.items():
        if k in data:
            data[k] = v
    if ((data['db_name'] == None) or (data['tablespace_name'] == None) or
        (data['db_user'] == None) or (data['db_passwd'] == None)):
        return 1
    if data['host'] == 'localhost':
        data['host'] = socket.gethostname()
    extra_vars_str = 'host=%s db_name=%s tablespace_name=%s db_user=%s ' \
                     'db_passwd=%s free_mb=%s size=%s next_size=%s ' \
                     'max_size=%s fs=%s vmware=%s vmware_user=%s ' \
                     'vmware_passwd=%s disk_size=%s'
    extra_vars_str = extra_vars_str % (data['host'], data['db_name'],
            data['tablespace_name'], data['db_user'], data['db_passwd'],
            data['free_mb'], data['size'], data['next_size'], data['max_size'],
            data['fs'], data['vmware'], data['vmware_user'],
            data['vmware_passwd'], data['disk_size'])
    text = "ansible-playbook /root/increase-tablespace.yml " \
           "--extra-vars '%s' --module-path ." % extra_vars_str
    blocks = text.split(" ")
    command = []
    for el in blocks:
        if 'None' not in el:
            command.append(el)
    command = " ".join(command)
    local(command)
    return 0

host = ifaddresses('eth0')[AF_INET][0]['addr']
run(host=host, port=8000)
