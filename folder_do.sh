#!/bin/bash
#遍历目录 执行命令
run_make()
{
        #如果该目录下存在Makefile
        if [ -f "Makefile" ];then
            echo ""
            echo ===================== FOUND ===================
            pwd;
            echo ===============================================
            make clean;
        fi
}

run_ls()
{
        pwd;

        #每目录 执行命令
        #ls -l |awk '{if($5 > 10485760){print $5}}'
        #ls -l |awk '{if($5 > 10485760){print "--",$9,$5}}'
        vcs --numcaps 12 --columns 4 --height 160 --autoaspect --anonymous   *
        echo ""
}

myfunc()
{
        cd $1;
        #run_make;
        run_ls;

        for x in $(ls .)
        do
                if [ -d "$x" ];then
                        myfunc $x;
                        cd ..
                fi
            
        done
}

p=.
if [ $1 ];then
    p=$1
fi
echo $p

myfunc $p
