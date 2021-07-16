import java.io.*;
import java.net.*;
import java.util.*;
import java.sql.*;

public class FetchAndProcessFromNetwork implements FetchAndProcess {
    private Map<String, String> data = new HashMap<String,String>();

    @Override
    public Map<String, String> exposeData() {
	return data;
    }

    @Override
    public void fetch(List<String> paths){
	// Implement here
        for(int i=0;i<paths.size();i++){
            String path = paths.get(i);
            try{
                URL url = new URL(path);
                URLConnection conn = url.openConnection();
                String name;
                try(Scanner rdr = new Scanner(new InputStreamReader(conn.getInputStream()))){ 
                    while(rdr.hasNext()){
                        name = rdr.next();
                        //name = name.trim();
                        //if(!name.equals("")){
                        if(!data.containsKey(path+"@"+name)){
                            data.put(path+"@"+name,path);
                            //System.out.println(name+" "+path);
                        }
                    }
                    rdr.close();
                } catch (IOException u){ 
                System.out.println(u); 
                }
            } catch (IOException e){
                throw new RuntimeException(e);
            }
        }
    }

    @Override
    public List<String> process() {
	// Implement here
	// Can you make use of the default implementation here?
	// See https://dzone.com/articles/interface-default-methods-java
        Connection mydb = null;
        Statement curs = null;
        ResultSet rs = null;
        try {
            Class.forName("org.sqlite.JDBC");
            mydb = DriverManager.getConnection("jdbc:sqlite:"+DB_NAME);
            mydb.setAutoCommit(false);
            //System.out.println("Opened database successfully");
            curs = mydb.createStatement();
            curs.executeUpdate("CREATE TABLE if not exists "+TABLE_NAME+
                " (pokemon_name text,source_path text,UNIQUE(pokemon_name,source_path));");
            Map<String,String> insert = exposeData();
            for(Map.Entry m:insert.entrySet()){ 
                String name = m.getKey().toString(),pname,pvalue= m.getValue().toString();
                pname = name.substring(name.lastIndexOf("@")+1);
                //System.out.println(pname+" "+pvalue);
                try{
                    curs.executeUpdate("INSERT INTO "+TABLE_NAME+" VALUES(" 
                        +"'"+pname+"'"+", "+"'"+pvalue+"'"+" );");
                } catch (Exception e){
                    //System.out.println(e);
                    continue;
                }  
            }  
            rs = curs.executeQuery("SELECT pokemon_name FROM "+TABLE_NAME+
                " GROUP BY pokemon_name HAVING count(*)>1;");
            while(rs.next()){
                System.out.println(rs.getString("pokemon_name"));
            }
            curs.close();
            mydb.commit();
            mydb.close();
        } catch ( Exception e ) {
         System.err.println(e);
        }
        return null;
    }
}
