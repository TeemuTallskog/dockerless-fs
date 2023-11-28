#Copyright (c) 2023, Teemu Tallskog
#All rights reserved.
#
#This source code is licensed under the BSD-style license found in the
#LICENSE file in the root directory of this source tree. 

class CmdList:
    def __init__(self, tar_handler):
        self.handler = tar_handler
    
    def execute_command(self, cmd):
        if cmd and cmd.startswith("/"):
            self.print_leafs_under_root(cmd)
        else:
            self.print_leafs_under_current(cmd)   

    def print_leafs_under_root(self, root_path):
        node = self.handler.file_system.get_node_from_root(root_path)
        if node:
            for child in node.children:
                print(node.children[child])
        
    def print_leafs_under_current(self, root_path):
        node = self.handler.file_system.get_node_from_current(root_path)
        if node:
            for child in node.children:
                print(node.children[child])   