from jinja2 import Template

template = Template('''
hostname {{name}}
!
interface loopback 0
 ip add 10.1.{{num+1}}.1 255.255.255.255
!
interface gi0/{{interfaces.0.id}}
 ip add {{interfaces.0.ip}} 255.255.255.0
 description {{interfaces.0.desc}}
 cdp enable
 no shut
!
interface gi0/{{interfaces.1.id}}
 ip add {{interfaces.1.ip}} 255.255.255.0
 description {{interfaces.1.desc}}
 cdp enable
 no shut
!
router ospf 1
 network {{interfaces.0.ip}} 0.0.0.0 area 0
 network {{interfaces.1.ip}} 0.0.0.0 area 0
''')

router1 = {'name': 'R1', "num": 0, 
           'interfaces': [{"id": 1, "ip": "172.16.1.1", "desc": "connection to R2"},
                          {"id": 2, "ip": "172.17.1.1", "desc": "connection to R3"}]}

print(template.render(router1))