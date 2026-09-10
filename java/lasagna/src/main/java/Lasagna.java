public class Lasagna {
    // All lasagnas should be cooked for 40 minutes
    public static int expectedMinutesInOven() {
        return 40;
    }

    public int remainingMinutesInOven(int minutesInOven) {
        return expectedMinutesInOven() - minutesInOven;
    }

	// Each layer takes two minutes to prepare
    public int preparationTimeInMinutes(int layers) {
        return layers * 2;
    }

	// Time spent is calculated by adding the prep time and time lasagna has spent in oven
    public int totalTimeInMinutes(int layers, int minutesInOven) {
        return preparationTimeInMinutes(layers) + minutesInOven;
    }
}
