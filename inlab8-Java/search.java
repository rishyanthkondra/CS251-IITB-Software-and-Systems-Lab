import java.util.*;

public class search{
    public static void main(String[] args) {
      	Vector vec = new Vector();
	int n = Integer.parseInt(args[0]),result = 0;
	for(int i=1;i<n+1;i++){
           vec.add(Integer.parseInt(args[i]));	
	}
	if(vec.contains(Integer.parseInt(args[n+1]))){
	   result = 1;
	}
	System.out.println(result);
    }
}
