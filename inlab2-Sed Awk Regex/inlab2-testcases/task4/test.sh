vis_testcases=($(seq 1 1 2))
subparts=("D" "C" "B" "A")
tail_inp="_inp_vis_testcase"
tail_out="_out_vis_testcase"
file_dir="./testcases/vis/"
script_name="./q4.sh"
out_dir="./output/vis/"
out_ref="./testcases/vis/"
[[ -d $out_dir ]] || mkdir -p "$out_dir"
if [[ -s $script_name ]];
then
	echo ""
	for i in "${vis_testcases[@]}"
	do
		echo "Current testcase -> $file_dir$i$tail_inp"
		$script_name $file_dir$i$tail_inp > "$out_dir$i$tail_out"
		echo "Your Output file -> $out_dir$i$tail_out"
		   
		for j in "${subparts[@]}"
	   	do
		   echo "Part .$j"
		   echo "Sample Output file -> $out_ref$i$tail_out.$j"
		   diff $out_ref$i$tail_out.$j $out_dir$i$tail_out > result
			if [[ -s result ]];
			then
				echo "status -> failed";
			else
				echo "status -> passed"
				break;
			fi
			rm result
		
		   echo ""
		done	
		echo ""
	done
else
	echo "q4.sh missing"
fi

