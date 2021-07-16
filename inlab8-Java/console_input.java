import java.util.Scanner;

public class console_input{
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
    Scanner Reader = new Scanner(System.in);  // Create a Scanner object
    System.out.print("Enter first name: ");
    String firstName = Reader.next();
    System.out.print("Enter last name: "); // Read user input
    String lastName = Reader.next();
    printPalindrome(firstName);
    printPalindrome(lastName);
  }
}
