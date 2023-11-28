#Copyright (c) 2023, Teemu Tallskog
#All rights reserved.
#
#This source code is licensed under the BSD-style license found in the
#LICENSE file in the root directory of this source tree. 

import os
import sys
from dockerless_fs.cmd_list import CmdList
from dockerless_fs.cmd_cd import CmdChangeDirectory
from dockerless_fs.cmd_cat import CmdConcatenate

class CommandHandler:
    def __init__(self, tar_handler):
        self.cmd_list = CmdList(tar_handler)
        self.cmd_cd = CmdChangeDirectory(tar_handler)
        self.cmd_cat = CmdConcatenate(tar_handler)
    
    def execute_cmd(self, cmd_opt, cmd):
        match cmd_opt:
            case "ls":
                self.cmd_list.execute_command(cmd)
            case "cd":
                self.cmd_cd.execute_command(cmd)
            case "cat":
                self.cmd_cat.execute_command(cmd)
            case "clear" | "cls":
                os.system('clear||cls')
            case "exit":
                sys.exit(0)
            case "help":
                print(f"dockerless-fs available commands:\n{'':-<34}\n- ls\n- cd\n- cat\n- clear | cls\n- help\n- exit")
            case default:
                print(f"Unrecognized command: {cmd_opt}")
            
                