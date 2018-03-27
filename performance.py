#!/usr/bin/env python
"""
Kenneth Vu

"""
import time
import subprocess
import os
import argparse


def sleep(num_of_seconds):
    """
    Delay time in seconds.

    Dependency:  build-in time

    Args:
            Number of seconds to be suspended.
    Return:
            None.
    """
    time.sleep(num_of_seconds)

def echo(msg):
    """
    Echo the message with timestamp to console.
    Args:
            msg   string of message to echo.
    Return:
            None.    
    """
    print "[{}]:[{}]".format(timestamp().msg)

def excecute(cmd, verbose=False):
    """
    Excecutes the command and return the result.

    Dependancy: build in subprocess.

    Args:
            cmd      Command string to execute.
            verbose  Default for command to be echoed to standard output.
    Return:
            output-string with the result when input cmd is executed.
    """

    if not verbose:
        echo(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output = p.communicate()[0]

    return output

def disk_with_write_catch(drives, catch_state="off"):
    """
    Turn on/off cache on drives used smartctl tool.
    Other smartctl for disk
        #smartctl --scan                 # Scan disks
        #smartctl -i /dev/sda            # Check if disk is SMART capable
        #smartctl -H /dev/sda            # Check overall disk SMART status
        #smartctl --test=short /dev/sda  # Selftest, short/long test
        #smartctl -a /dev/sda            # Print all SMART information
                                         # information, selftest, attribute
        #smartctl -A /dev/sda
        #smartctl -x /dev/sda
        #smartctl -l /dev/sda
    """
    for drive in drives:
        execute("smartcl -s wcache,{} {}".format(catch_state, drive.sd)
     
def write_to_log(text_info, file_name, console_n_log_timestamp=False):

    """
    Write test log to the file

    """
    with open(file_name, "a+") as fh:
        if console_n_log_timestamp:
        # print console timestamp and text_info
            print "[{}]: =======================\n".format(timestamp())
            print text_info
            fh.write "[{}]: =======================\n".format(timestamp()
            fh.write (text_info)
        else:
        # print text_info in log file
            echo(text_info)
            fh.write("[{}]:  {}\n".format(timestamp(), text_info)



def parse_args():
    """
    The input arguments are parsed     


    """    

    parser = argparse.ArgumentParser()
    parser.add_argument("chassis",
                         help="Support 'g6' for dual HBA, or 'g5' for single HBA"
                         type=str)
    parser.add_argument("node",
                         help="Support 'single' for single node, or 'dual' for dual node"
                         type=str)
    parser.add_argument("test",
                         help="support 'randread', 'randwrite', 'seqread', 'seqwrite', 'mixrand_n_seq' "
                         type=str)

    args = parser.parse_args()

    return args

"""---------------------------- main -----------------------------"""
if __name__ == "__main__":

    args = parse_args()
    chassis = args.chassis
    node    = args.node
    test    = args.test

    # Set log file path
    log_file = os.getcwd() + "/mnt/c/Users/Owner/Project/fnctest_{}".format(
                            time.strftime("%Y-%m-%d_%H-%M-%S"))

    # Check for invalid arguments
    try:
        if (chassis not in ["g6", "g5"]:
            raise ValueError
    except ValueError as e:
        print "Inputs error: chassis must be 'g6', or 'g5'."
        system.exit(1) 

    # Check for node
    try:
        if (chassis == "g6" and node not in ["single, "dual"]) or \
           (chassis == "g5" and node not in ["single", "dual"])"
           raise ValueError
    except ValueError as e:
        print "Input error: node must be 'single' or 'dual'."
        system.exit(1)
    else:
        if node == "single":
            test_process = SINGLE
        if node == "dual":
            test_process = PARALLEL

    # Check for test case 
