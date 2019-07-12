class SpaceAge(object):
    canonical_orbital_period = 31557600
    orbital_period_multiplier = {
            "mercury": 0.2408467,
            "venus": 0.61519726,
            "earth": 1.0,
            "mars": 1.8808158,
            "jupiter": 11.862615,
            "saturn": 29.447498,
            "uranus": 84.016846,
            "neptune": 164.79132
        }

    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        age_factor = SpaceAge.canonical_orbital_period * \
            SpaceAge.orbital_period_multiplier["mercury"]

        return float(format(self.seconds / age_factor, '.2f'))

    def on_venus(self):
        age_factor = SpaceAge.canonical_orbital_period * \
            SpaceAge.orbital_period_multiplier["venus"]

        return float(format(self.seconds / age_factor, '.2f'))

    def on_earth(self):
        age_factor = SpaceAge.canonical_orbital_period * \
            SpaceAge.orbital_period_multiplier["earth"]

        return float(format(self.seconds / age_factor, '.2f'))

    def on_mars(self):
        age_factor = SpaceAge.canonical_orbital_period * \
            SpaceAge.orbital_period_multiplier["mars"]

        return float(format(self.seconds / age_factor, '.2f'))

    def on_jupiter(self):
        age_factor = SpaceAge.canonical_orbital_period * \
            SpaceAge.orbital_period_multiplier["jupiter"]

        return float(format(self.seconds / age_factor, '.2f'))

    def on_saturn(self):
        age_factor = SpaceAge.canonical_orbital_period * \
            SpaceAge.orbital_period_multiplier["saturn"]

        return float(format(self.seconds / age_factor, '.2f'))

    def on_uranus(self):
        age_factor = SpaceAge.canonical_orbital_period * \
            SpaceAge.orbital_period_multiplier["uranus"]

        return float(format(self.seconds / age_factor, '.2f'))

    def on_neptune(self):
        age_factor = SpaceAge.canonical_orbital_period * \
            SpaceAge.orbital_period_multiplier["neptune"]

        return float(format(self.seconds / age_factor, '.2f'))
