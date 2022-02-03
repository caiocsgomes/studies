# shows date and time
date

# shows data about the partitions
df -h # human format
df -i # inodes

# creates links
ln file link # creates a hard link (link to inode)
ln -s file link # creates a symbolic link (link to the file), can be created to folder

# copy creating hard links
cp -rvl source dest

# show ocupation of each folder and file
du
du -hs # sumarize, show size of folder

# find files in directory
find folder -name filename 
find folder -type f -name foldername # search for folders
find folder -mtime -1 # search for files modified in the last day
find folder -amin -60 # search for files accessed in the last 60 minutes
find folder -cmin -60 # search for files created in the last 60 minutes

# show free memory
free
free --kilo
free --mega
free --kibi
free --mebi