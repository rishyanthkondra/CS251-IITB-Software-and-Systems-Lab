import java.io.*;
import java.net.*;
import java.util.*;
import java.util.stream.Stream;
import java.sql.*;

public class FetchAndProcessFromNetworkFast implements FetchAndProcess {
    private Map<String, String> data = new HashMap<String,String>() ;

    @Override
    public Map<String, String> exposeData() {
	return data;
    }

    @Override
    public void fetch(List<String> paths) {	
	// Implement here, just do it parallely!
        String []path = new String[paths.size()];
        paths.toArray(path);
        run(Arrays.stream(path).parallel());
    }

    public void run(Stream<String> stream){
        stream.forEach(s -> {
            try{
                URL url = new URL(s);
                URLConnection conn = url.openConnection();
                String name;
                try(Scanner rdr = new Scanner(new InputStreamReader(conn.getInputStream()))){ 
                    while(rdr.hasNext()){
                        name = rdr.next();
                        //name = name.trim();
                        //if(!name.equals("")){
                        if(!data.containsKey(s+"@"+name)){
                            data.put(s+"@"+name,s);
                            //System.out.println(name+" "+s);
                        }
                    }
                    rdr.close();
                } catch (IOException u){ 
                System.out.println(u); 
                }
            } catch (IOException e){
                throw new RuntimeException(e);
            }
        });
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
