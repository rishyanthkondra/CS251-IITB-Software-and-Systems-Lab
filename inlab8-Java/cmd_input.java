import java.util.Scanner;

public class cmd_input{
  static void printPalindrome(String a){
    boolean palindrome = true;
    String b = a.toLowerCase();
    for(int i=0;i<(b.length()/2);i++){
     if(b.charAt(i)!=b.charAt(a.length()-1-i)){
	//System.out.println(b.charAt(i)+" "+b.charAt(b.length()-1-i));
	palindrome = false;
	break;}
    }
    if(palindrome){
    System.out.println(a+" is palindrome");}
  }
  public static void main(String[] args) {
        // check if length of args array is 
        // greater than 0 
        if (args.length == 2) { 
  	 for (String val:args) 
            printPalindrome(val); } 
        else
            System.out.println("Invalid Number of Arguments!"); 
    } 
}
