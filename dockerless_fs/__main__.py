#Copyright (c) 2023, Teemu Tallskog
#All rights reserved.
#
#This source code is licensed under the BSD-style license found in the
#LICENSE file in the root directory of this source tree. 

import readline
import sys
from dockerless_fs.tar_handler import TarHandler
from dockerless_fs.command_handler import CommandHandler

def main():
    if len(sys.argv) != 2:
        print("Please provide the path to a tarball.")
        sys.exit(1)

    tarball_path = sys.argv[1]
    tar_handler = TarHandler()
    tar_handler.process_manifest(tarball_path)
    command_handler = CommandHandler(tar_handler)
    try:
        while(True):
            input_cmd = input(f"\033[36m/{(tar_handler.file_system.current_node.member.name if tar_handler.file_system.current_node.member else '')}\033[0m$ ")
            cmd = input_cmd.split(" ", 1)
            if len(cmd) > 0:
                cmd_opt = cmd[0]
                cmd = cmd[1] if (len(cmd) > 1) else ""
                command_handler.execute_cmd(cmd_opt, cmd)
    except KeyboardInterrupt:
        sys.exit(0)
            
if __name__ == "__main__":
    main()
        

    