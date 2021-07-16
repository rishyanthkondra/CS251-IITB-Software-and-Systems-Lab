import java.io.*;
import java.util.*;

public class FetchAndProcessFromDisk implements FetchAndProcess {
    private Map<String, String> data = new HashMap<String,String>();

    @Override
    public Map<String, String> exposeData() {
	return data;
    }

    @Override
    public void fetch(List<String> paths) {
	// Implement here
    	for(int i=0;i<paths.size();i++){
    		String fullpath = paths.get(i);
            String path = fullpath.substring(fullpath.lastIndexOf("/")+1);
            if(path.contains(".")){
                path = path.substring(0,path.indexOf("."));}
    		try(BufferedReader rdr = new BufferedReader(new FileReader(fullpath))) {
    			for(String name; (name = rdr.readLine()) != null; ){
                    if(!data.containsKey(path+"@"+name)){
    				    data.put(path+"@"+name,path);
                        //System.out.println(name+" "+path);
                    }
    			}
			} catch(IOException u){ 
            System.out.println(u); 
        	}
    	}
    }
}
//try Scanner instead of BufferReader 
/*
Import java.util.Scanner
for(int i=0;i<paths.size();i++){
            String path = paths.get(i),name;
            try(Scanner rdr = new Scanner(new File(path))) {
                while(rdr.hasNext()){
                    name = rdr.next();
                    if(!data.containsKey(name)){
                        data.put(name,path);
                        System.out.println(name+" "+path);}
                }
            } catch(IOException u){ 
            System.out.println(u); 
            }*/