public class WorkerApp {
    public static void main(String[] args) {
        System.out.println("🏭 Java Background Worker Started...");
        
        int count = 0;
        try {
            while (true) {
                count++;
                System.out.println("Processing event #" + count + " at " + new java.util.Date());
                Thread.sleep(5000); // Wait 5 seconds between "events"
            }
        } catch (InterruptedException e) {
            System.err.println("Worker interrupted! Shutting down...");
        }
    }
}
