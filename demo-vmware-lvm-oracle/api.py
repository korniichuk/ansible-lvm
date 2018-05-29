#!/usr/bin/env python2

from bottle import post, request, run
from netifaces import AF_INET, ifaddresses

@post('/api/filesystem/increase')
def filesystem():
    """Increase filesystem.
    Automatically increase filesystem on Red Hat 7. Add new disk or
    modify existing in VMware vCenter (if applicable).
    Input:
        host -- Vmware vSpehre service to connect to (required | type: string),
        user -- user name to use (required | type: string),
        passwd -- password to use(required | type: string),
        vm_name -- name of the vm (required | type: string),
        disk_size -- disk size, in GB, to add to the VM
                     (not required | type: string | default: 16).

    """

    data = {}
    data["host"] = None
    data["user"] = None
    data["passwd"] =  None
    data["vm_name"] = None
    data["disk_size"] = '16'

    query = request.query
    for k, v in query.items():
        if k in data:
            data[k] = v
    if ((data["host"] == None) or (data["user"] == None) or
        (data["passwd"] == None) or (data["vm_name"] == None)):
        return 1
    extra_vars_str = ('host=%s user=%s passwd=%s vm_name=%s disk_size=%s' %
            (data["host"], data["user"], data["passwd"], data["vm_name"],
             data["disk_size"]))
    local("ansible-playbook /root/increase-filesystem.yml "
          "--extra-vars '%s'" % extra_vars_str)
    return 0

@post('/api/tablespace/increase')
def tablespace():
    """Increase tablespace.
    Automatically increase tablespace in Oracle DB. Increase file system on
    Red Hat 7, add new disk or modify existing in VMware vCenter
    (if applicable).
    Input:
        host -- Oracle database host (not required | type: string |
                default: localhost),
        db_name -- Oracle database service name to connect to
                   (required | type: string),
        user -- Oracle user name to connect to the database
                (required | type: string),
        passwd -- Oracle user password for 'user' (required | type: string),
        tablespace_name -- tablespace that should be managed
                           (required | type: string),
        free_mb -- minimum required size of tablespace free space. Not
                   increase tablespace, if value less than current available
                   tablespace free space (not required | type: string |
                   default: 32000),
        size -- size of the datafile (not required | type: string |
                default: 1G),
        next_size -- size of the next extent allocated (not required |
                    type: string | default: 1G),
        max_size -- maximum size of the datafile (not required | type: string |
                   default: UNLIMITED).

    """

    host = 'localhost'
    db_name = None
    user =  None
    passwd = None
    tablespace_name = None
    free_mb = '32000'
    size = '1G'
    next_size = '1G'
    max_size = 'UNLIMITED'

    query = request.query
    return 'tablespace'

host = ifaddresses('eth0')[AF_INET][0]['addr']
run(host=host, port=8000)
