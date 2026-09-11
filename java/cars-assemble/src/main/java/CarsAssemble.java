public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        final int carsPerSpeed = 221;

        double successRate = 0;   // Default failure rate is 100%

        if (speed > 0 && speed <= 4) {
            successRate = 1.0;
        }
        else if (speed > 4 && speed <= 8) {
            successRate = 0.9;
        }
        else if (speed == 9) {
            successRate = 0.8;
        }
        else if (speed == 10) {
            successRate = 0.77;
        }

        return speed * carsPerSpeed * successRate;
    }

    public int workingItemsPerMinute(int speed) {
        final int minutesPerHour = 60;
        return (int) productionRatePerHour(speed) / minutesPerHour;
    }
}
