jarfile=$1
inputfile=$2
input_dir_hdfs=$3
output_dir_hdfs=$4
scripts_dir=$5

input_file_name=$(basename $inputfile)





# delete trailing slash if it exists
if [ "${input_dir_hdfs: -1}" = "/" ]
then
  input_dir_hdfs=${input_dir_hdfs%?}
fi

if [ "${output_dir_hdfs: -1}" = "/" ]
then
  output_dir_hdfs=${output_dir_hdfs%?}
fi





# create input directory if it does not exist
hdfs dfs -mkdir -p $input_dir_hdfs




# delete input file if it exists
hdfs dfs -rm -R -f "${input_dir_hdfs}/input.txt"
# copy input file to hdfs

hdfs dfs -put "./input.txt" $input_dir_hdfs




# delete output directory if it exists
hdfs dfs -rm -R -f $output_dir_hdfs



rm -rf ./output ./output_combined




# run mapreduce job

# hadoop jar $jarfile  -input "${input_dir_hdfs}/input.txt" -output $output_dir_hdfs -file "$(realpath ${scripts_dir})/mapper.py" -mapper "$(realpath ${scripts_dir})/mapper.py" -file "$(realpath ${scripts_dir})/reducer.py" -reducer "$(realpath ${scripts_dir})/reducer.py" 
hadoop jar $jarfile -archives test1.tar -D mapred.map.tasks=10 -input "${input_dir_hdfs}/input.txt" -output $output_dir_hdfs -file "$(realpath ${scripts_dir})/mapper.py" -mapper "test1.tar/test1/bin/python3 mapper.py" -file "$(realpath ${scripts_dir})/reducer.py" -reducer "test1.tar/test1/bin/python3 reducer.py" 

hdfs dfs -copyToLocal -f $output_dir_hdfs ./output

hdfs dfs -rm -R -f "${input_dir_hdfs}/input.txt" $output_dir_hdfs

# combine all contents of filed from ./output to a single file
cat ./output/part-* > ./output_combined.txt

