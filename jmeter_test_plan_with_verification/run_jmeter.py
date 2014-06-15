import xml.etree.ElementTree as ET
import subprocess

TEST_PLAN = 'test.jmx'
TEMP_TEST_PLAN = 'temp_' + TEST_PLAN
THREAD_GROUPS_TAGS = [ 
    'ThreadGroup', 
    'kg.apc.jmeter.threads.UltimateThreadGroup'
]
THREAD_GROUP = 'Verify'
JMETER_CALL = '/usr/local/jmeter/apache-jmeter-2.11/bin/jmeter -n -t %(test_plan)s -l result.jtl'

tree = ET.parse(TEST_PLAN)
for element in tree.iter():
    for thread_group_tag in THREAD_GROUPS_TAGS:
        if element.tag == thread_group_tag:
            enabled = (element.attrib['testname'] == THREAD_GROUP)
            element.attrib['enabled'] = str(enabled)

tree.write(TEMP_TEST_PLAN)
jmeter = JMETER_CALL % { 'test_plan': TEMP_TEST_PLAN }
subprocess.call(jmeter, shell=True)
