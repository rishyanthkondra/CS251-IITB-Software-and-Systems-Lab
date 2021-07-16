// A Java program for a Server
import java.net.*;
import java.io.*; 
import java.util.*;

public class BasicServer {
    public static void main(String[] args) throws IOException {
        Map<Integer,Integer> storing_map= new HashMap<Integer,Integer>();

        // if (args.length != 1) {
        //     System.err.println("Usage: java BasicServer <port number>");
        //     System.exit(1);
        // }
        
        // int portNumber = Integer.parseInt(args[0]);
        int portNumber=5000;
        System.out.println("Listening on "+portNumber); 
        ServerSocket serverSocket =
                new ServerSocket(portNumber);
        while(true){
        try (
            

            Socket clientSocket = serverSocket.accept();       

            PrintWriter out1 =
               new PrintWriter(clientSocket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(
               new InputStreamReader(clientSocket.getInputStream()))) {
            String inputLine;
              
            while ((inputLine = in.readLine())!= null){
                // out.println(inputLine);
                String[] arr_input=inputLine.split(" ");
                if(arr_input[0].equals("add")){
                    Integer number1=Integer.parseInt(arr_input[1]);
                    if(storing_map.containsKey(number1)){
                        Integer temp=storing_map.get(number1);    
                        temp++;
                        storing_map.replace(number1,temp);
                    }
                    else{
                        storing_map.put(number1,1);
                    }
                     out1.println(storing_map.get(number1));
                    System.out.println("ADD "+number1);
                }
                else if (arr_input[0].equals("read")){
                    Integer number1=Integer.parseInt(arr_input[1]);
                    if(storing_map.containsKey(number1)){
                        // out1.println(0);
                        System.out.println("READ "+number1+" "+storing_map.get(number1));
                    // }
                    out1.println(storing_map.get(number1));}
                        else{System.out.println("READ "+number1+" "+0);
                            out1.println(0);
                    }
                }
                else if(arr_input[0].equals("disconnect")){
                   
                    System.out.println("DIS");
                     clientSocket.close();
                    in.close();
                    break;
                }
            }
        } 
        catch (IOException e) {
            // System.out.println("Exception caught when trying to listen on port "
            //     + portNumber + " or listening for a connection");
            // System.out.println(e.getMessage());
            // System.out.println("No Server");
        }
        }
    }
}
