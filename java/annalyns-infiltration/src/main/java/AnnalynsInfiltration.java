class AnnalynsInfiltration {
    public static boolean canFastAttack(boolean knightIsAwake) {
        // If the knight's not awake, Annalyn can perform a fast attack
        return !knightIsAwake;
    }

    public static boolean canSpy(boolean knightIsAwake, boolean archerIsAwake, boolean prisonerIsAwake) {
        // Spying only makes sense if any of party members are awake
        // Why spy on unconscious people?
        return knightIsAwake || archerIsAwake || prisonerIsAwake;
    }

    public static boolean canSignalPrisoner(boolean archerIsAwake, boolean prisonerIsAwake) {
        // The prisoner needs to be awake to be signaled
        // But the archer should not be awake, because they know how to read signals
        return prisonerIsAwake && !archerIsAwake;
    }

    public static boolean canFreePrisoner(boolean knightIsAwake, boolean archerIsAwake, boolean prisonerIsAwake, boolean petDogIsPresent) {
        // If Annalyn has her dog, then the prisoner can be rescued if the archer is asleep
        if (petDogIsPresent && !archerIsAwake) {
            return true;
        }
        // Otherwise, it just comes down to the party guards being asleep and the prisoner being awake
        else return prisonerIsAwake && !archerIsAwake && !knightIsAwake;
    }
}
