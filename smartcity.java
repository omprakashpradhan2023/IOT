import java.util.Random;

public class Smartcity {
    public static void main(String[] args) {
        // Simulate sensor reading
        Random random = new Random();
        int vehicleCount = random.nextInt(101);  // 0 to 100 vehicles
        String location = "Junction A";

        // Display simulated data
        System.out.println("📍 Location: " + location);
        System.out.println("🚗 Vehicle Count: " + vehicleCount);

        // Analyze traffic and decide signal
        String command;
        if (vehicleCount > 70) {
            command = "Switch light to GREEN (Heavy traffic)";
        } else if (vehicleCount > 30) {
            command = "Switch light to YELLOW (Moderate traffic)";
        } else {
            command = "Keep light RED (Low traffic)";
        }

        // Output decision
        System.out.println("🚦 Decision: " + command);
    }
}
