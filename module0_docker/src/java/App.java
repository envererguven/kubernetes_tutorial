public class App {
    public static void main(String[] args) {
        System.out.println("☕ Java Application Starting...");
        
        String user = System.getenv("APP_USER");
        if (user == null) {
            user = "Guest";
        }
        
        System.out.println("Hello, " + user + "!");
        System.out.println("Runtime Version: " + System.getProperty("java.version"));
        
        try {
            for (int i = 1; i <= 3; i++) {
                System.out.println("Processing block " + i + "...");
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
            System.err.println("Thread interrupted!");
        }
        
        System.out.println("✅ Java execution finished.");
    }
}
