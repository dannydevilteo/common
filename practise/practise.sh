#!/bin/bash

MQ_DEV_SERVER=estmt@10.112.176.60
ssh ${MQ_DEV_SERVER} "mkdir -p /home/estmt/training"
ssh ${MQ_DEV_SERVER} "rm -f /home/estmt/training/FindFiles{1,2,3,4,5}"
ssh ${MQ_DEV_SERVER} "rm -f /home/estmt/training/ManiFile{1,2,3}"
ssh ${MQ_DEV_SERVER} "rm -f /home/estmt/training/DiffFile1"
ssh ${MQ_DEV_SERVER} "touch /home/estmt/training/FindFiles{1,2,3,4,5}"
ssh ${MQ_DEV_SERVER} "touch /home/estmt/training/ManiFile{1,2,3}"
ssh ${MQ_DEV_SERVER} "touch /home/estmt/training/DiffFile1"
ssh ${MQ_DEV_SERVER} "touch /home/estmt/training/myprogview1"
ssh ${MQ_DEV_SERVER} "touch /home/estmt/training/myprogviewErr1"
ssh ${MQ_DEV_SERVER} "touch /home/estmt/training/myprogview2"
ssh ${MQ_DEV_SERVER} "mkdir -p /home/estmt/training/prog"
scp textmodifier ${MQ_DEV_SERVER}":/home/estmt/training/textmodifier"
scp textmanipulator ${MQ_DEV_SERVER}":/home/estmt/training/textmanipulator"
scp myprog ${MQ_DEV_SERVER}":/home/estmt/training/prog/myprog"
scp adhocscripts.tar.gzip ${MQ_DEV_SERVER}":/home/estmt/training/adhocscripts.tar.gzip"
scp UnzipThisFile.zip ${MQ_DEV_SERVER}":/home/estmt/training/UnzipThisFile.zip"
scp infinite_loop.sh ${MQ_DEV_SERVER}":/home/estmt/training/infinite_loop.sh"
scp fast_job.sh ${MQ_DEV_SERVER}":/home/estmt/training/fast_job.sh"
ssh ${MQ_DEV_SERVER} "ssh ec2-user@10.198.104.139 mkdir -p /home/ec2-user/training"
ssh ${MQ_DEV_SERVER} "ssh ec2-user@10.198.104.139 sudo setfacl -m u:ec2-user:rwx /prd/estmt/mesa/staging"
ssh ${MQ_DEV_SERVER} "ssh ec2-user@10.198.104.139 touch /home/ec2-user/training/deleteme"
ssh ${MQ_DEV_SERVER} "ssh ec2-user@10.198.104.139 chmod 3777 /home/ec2-user/training/deleteme"
ssh ${MQ_DEV_SERVER} "ssh ec2-user@10.198.104.139 touch /home/ec2-user/training/deleteme_too"
ssh ${MQ_DEV_SERVER} "ssh ec2-user@10.198.104.139 sudo chattr +i /home/ec2-user/training/deleteme_too"
ssh ${MQ_DEV_SERVER} "scp /home/estmt/training/adhocscripts.tar.gzip ec2-user@10.198.104.139:/home/ec2-user/training/adhocscripts.tar.gzip"
ssh ${MQ_DEV_SERVER} "scp /home/estmt/training/UnzipThisFile.zip ec2-user@10.198.104.139:/home/ec2-user/training/UnzipThisFile.zip"
ssh ${MQ_DEV_SERVER} "scp /home/estmt/training/infinite_loop.sh ec2-user@10.198.104.139:/home/ec2-user/training/infinite_loop.sh"
ssh ${MQ_DEV_SERVER} "scp /home/estmt/training/fast_job.sh ec2-user@10.198.104.139:/home/ec2-user/training/fast_job.sh"
ssh ${MQ_DEV_SERVER} "ssh ec2-user@10.198.104.139 nohup sh /home/ec2-user/training/infinite_loop.sh" |
ssh ${MQ_DEV_SERVER} "ssh ec2-user@10.198.104.139 touch /prd/estmt/mesa/ZipMe.txt"
ssh ${MQ_DEV_SERVER} "mkdir -p /home/estmt/training/difference"
echo "abc" > DiffFile0
echo "abc" > DiffFile1
echo "abc" > DiffFile2
echo "abc" > DiffFile3
echo "abcd" > DiffFile4
echo "abc" > DiffFile5
echo "abc" > DiffFile6
echo "abc" > DiffFile7
echo "abc" > DiffFile8
echo "abc" > DiffFile9
scp DiffFile[0-9] ${MQ_DEV_SERVER}":/home/estmt/training/difference/"
ssh ${MQ_DEV_SERVER} "mkdir -p /home/estmt/training/permission"
ssh ${MQ_DEV_SERVER} "rm -f /home/estmt/training/permission/stickyfile{1,2,3,4,5}"
ssh ${MQ_DEV_SERVER} "touch /home/estmt/training/permission/stickyfile{1,2,3,4,5}"
ssh ${MQ_DEV_SERVER} "chmod 5644 /home/estmt/training/permission/stickyfile{1,3,5}"
ssh ${MQ_DEV_SERVER} "ssh ec2-user@10.198.104.139 touch /home/ec2-user/training/helloworld"
ssh ${MQ_DEV_SERVER} "ssh ec2-user@10.198.104.139 touch /home/ec2-user/training/everyhour"