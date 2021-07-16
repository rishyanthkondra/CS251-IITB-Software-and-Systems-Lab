vis_testcases=($(seq 1 1 3))
script_name="q1.sed"
tail_inp="_inp_vis_testcase"
tail_out="_out_vis_testcase"
file_dir="./testcases/vis/"
out_dir="./output/vis/"
out_ref="./testcases/vis/"
[[ -d $out_dir ]] || mkdir -p "$out_dir"
if [[ $script_name ]];
then
	echo ""
	for i in "${vis_testcases[@]}"
	do
		echo "Current testcase -> $file_dir$i$tail_inp"
		echo "Your Output file -> $out_dir$i$tail_out"
		echo "Sample Output file -> $out_ref$i$tail_out"
		sed -f $script_name $file_dir$i$tail_inp > $out_dir$i$tail_out
		diff $out_ref$i$tail_out $out_dir$i$tail_out > result

		if [[ -s result ]];
		then
			echo "status -> failed"
		else
			echo "status -> passed"
		fi
		rm result
		echo ""
	done
else
	echo "please create a script with name q1.sed"
fi