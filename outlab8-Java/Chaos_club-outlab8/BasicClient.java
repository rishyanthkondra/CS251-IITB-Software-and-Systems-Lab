import java.net.*;
import java.io.*; 
import java.util.*;

public class BasicClient{
	public static void main(String[] args){
		Map<Integer,Integer> read_stor=new HashMap<Integer,Integer>();
		Integer delta_sum=0;
		// BufferedReader reader;
		try(BufferedReader reader= new BufferedReader(new FileReader(args[0]));){
		String line=reader.readLine();
		while (line!=null){ 
			String[] arr=line.split(" ");
				// System.out.println(arr[0]);
				if (arr[0].equals("connect") ){ 
					Integer portNumber=Integer.parseInt(arr[2]);
					try(Socket clientSocket = new Socket(arr[1],portNumber);
						 PrintWriter out =new PrintWriter(clientSocket.getOutputStream(), true);
            	BufferedReader in =new BufferedReader(
                    new InputStreamReader(clientSocket.getInputStream()));) 
                    {	System.out.println("OK");
						line=reader.readLine();
					while(line!=null){arr=line.split(" ");
						if(arr[0].equals("add")){
							out.println(line);
							String to_string=in.readLine();
							Integer val1=Integer.parseInt(arr[1]);
							Integer key_val=Integer.parseInt(to_string);
							if(read_stor.containsKey(val1)){
								read_stor.replace(val1,key_val);
							}
							else{read_stor.put(val1,key_val);}
							}
						else if(arr[0].equals("read")){
							out.println(line);
							Integer temp1=Integer.parseInt(arr[1]);
							String curr_weight=in.readLine();
							Integer weight_val=Integer.parseInt(curr_weight);
							// System.out.println(" "+weight_val);
							Integer delta;
							if(read_stor.containsKey(temp1)){
								delta=weight_val-read_stor.get(temp1);							}
							else{
								delta=weight_val;
								
							}

							delta_sum=delta_sum+delta;
							System.out.println(weight_val+" "+delta);}
						else if(arr[0].equals("sleep")){
				// System.out.println("time");
				Integer num=Integer.parseInt(arr[1]);
				try{Thread.sleep(num);}
				catch(InterruptedException e){}
			}

						else if(arr[0].equals("disconnect")){
							out.println(line);
							clientSocket.close();
							System.out.println("OK");
							break;
							}
							line=reader.readLine();
					}
				}
			catch(IOException e){
					System.out.println("No Server");
					System.exit(1);
				}
			}
			else if(arr[0].equals("sleep")){
				// System.out.println("time");
				Integer num=Integer.parseInt(arr[1]);
				try{Thread.sleep(num);}
				catch(InterruptedException e){}
			}
			if(line!=null){
				try{line=reader.readLine();}
			catch(IOException e){}
		}
			else{break;}
			}
		}
		catch(IOException e){}
		System.out.println(delta_sum);
		// catch(IOException e){
		// 	e.printStackTrace();
		// 	}
		}
	}
	// }

