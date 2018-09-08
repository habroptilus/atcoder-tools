#!/bin/sh

# $1=cource name(lower case)
# $2=number

make_files(){
    dir=`echo $1 | tr '[a-z]' '[A-Z]'`
    display_num=`printf %03d $2`
    if [ ! -e $dir ]; then mkdir $dir ; fi
    cd $dir
    if [ ! -e $1$display_num ];then
        mkdir $1$display_num
        cd $1$display_num
        touch input.txt
        if [[ $1 = "abc"  ]] ; then
            L=(A B C D)
        elif [[ $1 = "agc" ]]; then
            L=(A B C D E F)
        elif [[ $1 = "arc" ]]; then
            if [[ "$2" -gt 57 ]]; then
                L=(C D E F)
            else
                L=(A B C D)
            fi
        fi
        for var in ${L[@]}
        do
            touch "$1$display_num$var.cpp"
            echo "#include <bits/stdc++.h>\ntypedef long long ll;" > "$1$display_num$var.cpp"
        done
    fi
}
make_files $1 $2
