#!/bin/bash

sed -i "/ENGINE/ s/mysql/$2/" $1

sed -i "/HOST/ s/mysql/$3/" $1

sed -i "71,90 s/student_list/$4/g" $1

sed -i "71,90 s/root/$5/g" $1

sed -i "71,90 s/0000/$6/g" $1