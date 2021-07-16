import java.util.*;
import java.sql.*;

public interface FetchAndProcess {
    static String DB_NAME = "pokemon.db";
    static String TABLE_NAME = "pokemon";

    /* The map populated by fetch */
    // public Map<String, String> data = new HashMap<String, String>();
    
    // no default implementation
    void fetch(List<String> paths);

    // no default implementation
    Map<String, String> exposeData();
    
    /* Provides a default implementation that does a lot of work:
     * 1. Create the `TABLE_NAME` table if it does not exist (along with a uniqueness constraint).
     * 2. Inserts data into the table, safely. ensuring no duplication.
     * 3. Returns the Connection (useful for the FetchAndProcessNetwork* classes)
     */
    default List<String> process() {
	// you can use exposeData() here.
        Connection mydb = null;
        Statement curs = null;
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
            curs.close();
            mydb.commit();
            mydb.close();
        } catch ( Exception e ) {
         System.err.println(e);
        }
      //System.out.println("Records created successfully");
      return null;
   }
}
