#!/usr/bin/env python2

from bottle import post, request, run
from netifaces import AF_INET, ifaddresses

@post('/api/filesystem/increase')
def filesystem():
    """Increase filesystem.
    Automatically add new disk or modify existing (if applicable).
    Input:
        host -- Vmware vSpehre service to connect to (required | type:string),
        user -- user name to use (required | type:string),
        passwd -- password to use(required | type:string),
        vm_name -- name of the vm (required | type:string),
        disk_size -- disk size, in GB, to add to the VM
                     (required | type:string).

    """

    host = None
    user= None
    passwd =  None
    vm_name = None
    size = None

    query = request.query
    return 'filesystem'

@post('/api/tablespace/increase')
def tablespace():
    """Increase tablespace"""

    host = None

    query = request.query
    return 'tablespace'

host = ifaddresses('eth0')[AF_INET][0]['addr']
run(host=host, port=8000)
