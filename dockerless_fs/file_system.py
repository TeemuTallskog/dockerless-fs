#Copyright (c) 2023, Teemu Tallskog
#All rights reserved.
#
#This source code is licensed under the BSD-style license found in the
#LICENSE file in the root directory of this source tree. 

class FileSystem: 
    class Node:
        def __init__(self, name, member=None, parent=None, content=None):
            self.is_file=False
            self.is_directory=False
            self.member = member
            if self.member:
                self.is_file = member.isfile()
                self.is_directory = member.isdir()
            self.name = name
            self.children = {}
            self.parent = parent
            self.content = content
        def __str__(self):
            if self.is_file:
                return self.name
            return f"{self.name}/"
    
    def __init__(self):
        self.root = self.Node("/")
        self.current_node = self.root

    def add_path(self, path, member=None, content=None):
        current_node = self.root
        components = path.split('/')[1:]

        for component in components:
            if component not in current_node.children:
                current_node.children[component] = self.Node(component, member, parent=current_node, content=content)
            current_node = current_node.children[component]
    
    def get_node_from_root(self, root_path):
        root_node = self.root
        components = root_path.split('/')[1:]
        for component in components:
            if component == "..":
                if root_node.parent:
                    root_node = root_node.parent
                else:
                    return None
            elif component in root_node.children:
                root_node = root_node.children[component]

        return root_node

    def get_node_from_current(self, path):
        current_node = self.current_node
        components = path.split('/')
        for component in components:
            if component == "..":
                if current_node.parent:
                    current_node = current_node.parent
                else:
                    return None
            elif component in current_node.children:
                current_node = current_node.children[component]
        return current_node
        