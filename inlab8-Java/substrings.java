import java.util.*; 
class substrings {
	public static void main(String[] args){
	String s = args[0];
	int reql = Integer.parseInt(args[1]);
	List<String> lis = new ArrayList<String>(s.length()-reql+1);
	for (int i=0; i< s.length()-reql+1; i+=1){
		lis.add(s.substring(i, i + reql));
	}
	for (int i=0; i < lis.size(); i++){
		System.out.println(lis.get(i));	}
	}
}
	
