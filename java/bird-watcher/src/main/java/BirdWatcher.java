class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public static int[] getLastWeek() {
        int[] lastWeek = new int[] {0,2,5,3,7,8,4};
        return lastWeek;
    }

    public int getToday() {
        // The latest day is at the end of the array
        return birdsPerDay[birdsPerDay.length-1];
    }

    public void incrementTodaysCount() {
        birdsPerDay[birdsPerDay.length-1]++;
    }

    public boolean hasDayWithoutBirds() {
        // iterate over the array of bird visits and check the values
        for (int birds : birdsPerDay) {
            if (birds == 0)
                return true;
        }

        return false;
    }

    public int getCountForFirstDays(int numberOfDays) {
        int birdCount = 0;

        for (int day = 0; day < numberOfDays && day < birdsPerDay.length; day++) {
            birdCount += birdsPerDay[day];
        }
        return birdCount;
    }

    public int getBusyDays() {
        final int busyDayThreshold = 5;
        int busyDays = 0;

        for (int birds: birdsPerDay) {
            if (birds >= busyDayThreshold) {
                busyDays++;
            }
        }

        return busyDays;
    }
}
