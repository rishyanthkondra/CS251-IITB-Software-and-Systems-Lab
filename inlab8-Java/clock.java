import java.util.Date;

class Timer implements Runnable{
   private Thread t;
   private String threadName;
   Timer(){
     threadName = "demo";//time for which thread sleeps
   }
   public void run(){
        try{
            while(true){
                Date today =new Date();
                String[] now=today.toString().split("\\s+");
                System.out.println(now[3]);
                Thread.sleep(1000);
            }
        }
        catch(InterruptedException e){}
   }

   public void start(){
    if (t == null){
        t = new Thread(this,threadName);
        t.start();
    }
   }
}

class clock{
    public static void main(String[] args){
       Timer mytimer = new Timer();
       mytimer.start();
    }
}
