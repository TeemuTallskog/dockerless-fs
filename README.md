# dockerless-fs
Explore Docker image filesystem without Docker!

## Usage
Download a docker image tarbarll, this can be done Dockerless with for ex. ```skopeo```  
Then:
```bash
python3 main.py /path/to/image.tar 
```
Then explore by providing a folder path as an input:
```bash
ls /
-----
bin/
boot/
dev/
etc/
home/
lib/
lib32/
lib64/
libx32/
media/
mnt/
opt/
proc/
root/
run/
sbin/
srv/
sys/
tmp/
usr/
var/
-----
ls /usr
-----
bin/
games/
include/
lib/
lib32/
lib64/
libexec/
libx32/
local/
sbin/
share/
src/
-----
```
