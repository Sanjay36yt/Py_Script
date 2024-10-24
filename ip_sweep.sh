#! /bin/bash


if [ "$1" == "" ]
then
echo "Enter the argument"
echo "Eg: (192.168.10)"

else
for ip in `seq 1 255`;do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":"&
done
fi