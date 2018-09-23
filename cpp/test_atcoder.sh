#!/bin/sh

# $1=course name(lower case)
# $2=round
# $3=prob

level_camel=`echo $1 | tr '[a-z]' '[A-Z]'`
level=`echo $1`
display_round=`printf %03d $2`
round=`echo $2`
prob=`echo $3`
prob_camel=`echo $3 | tr '[a-z]' '[A-Z]'`

# scraping sample cases if not exist
if [ ! -e $level_camel/$level$display_round/sample_$prob ];then
mkdir $level_camel/$level$display_round/sample_$prob;
python scrape_sample.py $level $round $prob ;
else
    echo "Sample cases are already created."
fi


# make outputs directory if not exists

if [ ! -e $level_camel/$level$display_round/outputs_$prob ];
then
mkdir $level_camel/$level$display_round/outputs_$prob
fi

# compile c++ code
g++ $level_camel/$level$display_round/$level$display_round$prob_camel.cpp --std=c++14 -o $level_camel/$level$display_round/$prob_camel.out

for file in `ls $level_camel/$level$display_round/sample_$prob | grep input*` ; do
    sample_index=`echo ${file:8:1}`
    $level_camel/$level$display_round/$prob_camel.out < $level_camel/$level$display_round/sample_$prob/$file > $level_camel/$level$display_round/outputs_$prob/"output_${prob}_${sample_index}.txt"
done

echo "Starting Test..."
total=`ls $level_camel/$level$display_round/outputs_$prob | grep -c output*`


# test
for file in `ls $level_camel/$level$display_round/outputs_$prob | grep output*` ; do
    sample_index=`echo ${file:9:1}`
    printf "[${sample_index}/${total}] "
    python compare.py $level_camel/$level$display_round/outputs_$prob/$file $level_camel/$level$display_round/sample_$prob/"answer_${prob}_${sample_index}.txt"
done

echo "Finished."