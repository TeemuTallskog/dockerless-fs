# dockerless-fs
Explore Docker image filesystem without Docker!

## Install
````bash
pip install git+https://github.com/TeemuTallskog/dockerless-fs.git
# OR
git clone https://github.com/TeemuTallskog/dockerless-fs.git
cd dockerless-fs

pip install .
# Or run straight from
python3 dockerless_fs/__main__.py /path/to/image.tar
````
## Usage
Download a docker image tarbarll, this can be done Dockerless with for ex. [```skopeo``` ](https://github.com/containers/skopeo)  

Then:
```bash
dockerless-fs /path/to/image.tar 
```
Then explore explore the filesystem:
```shell
/$ help
dockerless-fs available commands:
----------------------------------
- ls
- cd
- cat
- clear | cls
- help
- exit
/$ cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=22.04
DISTRIB_CODENAME=jammy
DISTRIB_DESCRIPTION="Ubuntu 22.04.3 LTS"
/$ cd var/log
/var/log$ ls ..
backups/
cache/
lib/
local/
lock/
log/
mail/
opt/
run/
spool/
tmp/
/var/log$
```
### Available commands
Available commands are stripped down versions of ther regular counter parts.
- ls < path >  
list files - Siple way to list files in directories.  
doesn't provide additional arguments other than path.
- cd < path >  
Change directory - hop between directories.
- cat < path >  
concatenate - read file contents to output.
- clear | cls  
clear terminal
- help  
display available commands
- exit  
exit the program


# License
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)


