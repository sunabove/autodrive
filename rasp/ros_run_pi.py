#coding: utf-8

import subprocess
from time import sleep

#print( "Hello" )

#proc    -> name/id of the process
#id = 1  -> search for pid
#id = 0  -> search for name (default)

def process_exists( proc ):
    ps = subprocess.Popen("ps -aux", shell=True, stdout=subprocess.PIPE) 
    output = ps.stdout.read()
    ps.stdout.close()
    ps.wait()

    output = str( output )

    for line in output.split("\n"):
        if line != None and proc in line : 
            return 1
        pass
    pass

    return 0
pass

if process_exists( "roscore" ) :
	print( "roscore is running already!" )
else :
    print( "roscore is not running." )
    if process_exists( "rosmaster" ) :
        cmd = "killall -9 rosmaster"
        print( cmd )
        subprocess.call([ cmd ])
    pass

    cmd = "roscore &"
    print( "running roscore" )
    import os
    os.system("roscore &")  

    while not process_exists( "roscore" ) :
        pass
        sleep( "5" )
    pass
pass

#print( "Good bye!" )
