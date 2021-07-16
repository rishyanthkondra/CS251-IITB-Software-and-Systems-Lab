import java.net.*;
import java.io.*; 
import java.util.*;

public class MultiServer{
	static final Integer max_size=30000;
     
    public static void main(String[] args) throws IOException{
		Map<Integer,Integer> storing_map=new HashMap<Integer,Integer>();
        storing_map=java.util.Collections.synchronizedMap(storing_map);
		Integer portNumber=5000;

        try{java.util.concurrent.ExecutorService pool = java.util.concurrent.Executors.newFixedThreadPool(max_size);
		System.out.println("Listening on "+portNumber);
		ServerSocket serverSocket =
                new ServerSocket(portNumber);
		while(true){
			
			try {
            	Socket clientSocket=serverSocket.accept();       

            	// PrintWriter out1 =
             //   		new PrintWriter(clientSocket.getOutputStream(), true);
            	// BufferedReader in = new BufferedReader(
             //  		new InputStreamReader(clientSocket.getInputStream()));
            	// Runnable r1=new ClientHandler(clientSocket,in,out1,storing_map);
                Runnable r1=new ClientHandler(clientSocket,storing_map);
                pool.execute(r1);
            	// pool.shutdown();
        	}
        	catch(Exception e){
        		// clientSocket.close();
			}
		}
    }
    catch(Exception e){}
	}
}

class ClientHandler implements Runnable{
	// final BufferedReader in; 
 //    final PrintWriter out1; 
    final Socket clientSocket;
    final Map<Integer,Integer> storing_map;
     public ClientHandler(Socket clientSocket,Map<Integer,Integer> storing_map)  
     // public ClientHandler(Socket clientSocket, BufferedReader in, PrintWriter out1,Map<Integer,Integer> storing_map)  
    { 
        this.clientSocket = clientSocket; 

       // this.in = in; 
       // this.out1 = out1; 
        this.storing_map=storing_map;
    } 

	public void run(){
            try{
                PrintWriter out1 =
                    new PrintWriter(clientSocket.getOutputStream(), true);
                BufferedReader in = new BufferedReader(
                    new InputStreamReader(clientSocket.getInputStream()));
	String inputLine=in.readLine();
// inputLine=in.readLine();
// System.out.println("aev");
if(inputLine!=null){
        while (!((inputLine.equals("disconnect"))||(inputLine==null))) {
                // out.println(inputLine);
           if(inputLine==null){System.out.println("hi");}
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
                        else{out1.println(0);
                    System.out.println("READ "+number1+" "+0);}
                }
                // else if(arr_input[0].equals("disconnect")){
                //     try{clientSocket.close();
                //     }
                //     catch(IOException e){}
                //     System.out.println("DIS");
                // }
                inputLine=in.readLine();
                if(inputLine!=null){}
                    else{break;}
            }}
            if(inputLine!=null){
            if(inputLine.equals("disconnect")){
                System.out.println("DIS");
                
            }}
            //else if(inputLine==null){try{clientSocket.close();}
              //  catch(IOException e){}}
clientSocket.close();
        }
        catch(IOException e){}

	}
}

















