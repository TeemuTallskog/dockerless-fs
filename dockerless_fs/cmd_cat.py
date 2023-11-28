#Copyright (c) 2023, Teemu Tallskog
#All rights reserved.
#
#This source code is licensed under the BSD-style license found in the
#LICENSE file in the root directory of this source tree. 

class CmdConcatenate:
    def __init__(self, tar_handler):
        self.tar_handler = tar_handler

    def execute_command(self, cmd):
        if cmd:
            node = None
            if cmd.startswith("/"):
                node = self.tar_handler.file_system.get_node_from_root(cmd)
            else:
                node = self.tar_handler.file_system.get_node_from_current(cmd)
            if node:
                if node.member and node.member.isreg():
                    try:
                        if node.content:
                            print(node.content.decode('utf-8'))
                        else:
                            print(f"'{node.member.name}' is not a readable file.")
                    except Exception as e:
                        print(f"Failed to read {node.member.name}: {e}")
                else:
                    print(f"'{node.member.name}' is not a readable file.")
                
                    