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

 


for file in `ls $level_camel/$level$display_round/sample_$prob | grep input*` ; do
    sample_index=`echo ${file:8:1}`
    python $level_camel/$level$display_round/$level$display_round$prob_camel.py < $level_camel/$level$display_round/sample_$prob/$file > $level_camel/$level$display_round/outputs_$prob/"output_${prob}_${sample_index}.txt"
done

echo "Starting Test..."
total=`ls $level_camel/$level$display_round/outputs_$prob | grep -c output*`


# test
passed_num=0

for file in `ls $level_camel/$level$display_round/outputs_$prob | grep output*` ; do
    sample_index=`echo ${file:9:1}`
    printf "[${sample_index}/${total}] "
    judge=`python compare.py $level_camel/$level$display_round/outputs_$prob/$file $level_camel/$level$display_round/sample_$prob/"answer_${prob}_${sample_index}.txt"`
    python compare.py $level_camel/$level$display_round/outputs_$prob/$file $level_camel/$level$display_round/sample_$prob/"answer_${prob}_${sample_index}.txt"
    if [ ${#judge} = 7 ];then
         passed_num=`expr $passed_num + 1`
    fi
done

if [ $passed_num -eq $total ];then
    echo "Passed all the tests!"
    python submit.py $level $round $prob ;
else
    echo "${passed_num}/${total} samples are passed."
fi
