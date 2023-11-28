#Copyright (c) 2023, Teemu Tallskog
#All rights reserved.
#
#This source code is licensed under the BSD-style license found in the
#LICENSE file in the root directory of this source tree. 

class CmdChangeDirectory:
    def __init__(self, tar_handler):
        self.handler = tar_handler
    
    def execute_command(self, cmd):
        self._change_directory(cmd)
    
    def _change_directory(self, path):
        if not path:
            return
        elif path.startswith("/"):
            node = self.handler.file_system.get_node_from_root(path)
            if node:
                self.handler.file_system.current_node = node
        else:
            node = self.handler.file_system.get_node_from_current(path)
            if node:
                self.handler.file_system.current_node = node
        