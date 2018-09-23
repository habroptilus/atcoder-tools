#!/bin/sh

# $1=course name(lower case)
# $2=round
# $3=prob

level_camel=`echo $1 | tr '[a-z]' '[A-Z]'`
level=`echo $1`
display_round=`printf %03d $2`
round=`echo $2`
prob=`echo $3`

# scraping sample cases if not exist
if [ ! -e $level_camel/$level$display_round/sample_$prob ];then
mkdir $level_camel/$level$display_round/sample_$prob;
python scrape_sample.py $level $round $prob ;
else
    echo "Sample cases are already created."
fi
