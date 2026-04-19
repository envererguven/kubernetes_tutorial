public class ConfigApp {
    public static void main(String[] args) {
        System.out.println("⚙️ Java Config Reader Starting...");

        // 1. Read from Environment Variable
        String dbHost = System.getenv("DB_HOST");
        System.out.println("DATABASE HOST (from Env): " + (dbHost != null ? dbHost : "NOT SET"));

        // 2. Read from Mounted File
        try {
            java.nio.file.Path path = java.nio.file.Paths.get("/etc/config/app-settings.conf");
            if (java.nio.file.Files.exists(path)) {
                String content = java.nio.file.Files.readString(path);
                System.out.println("SETTINGS (from File): " + content.trim());
            } else {
                System.out.println("SETTINGS FILE NOT FOUND at /etc/config/app-settings.conf");
            }
        } catch (Exception e) {
            System.err.println("Error reading config file: " + e.getMessage());
        }
    }
}
