package clock

import "strconv"

const testVersion = 4

type Clock struct {
	hour, minute int
}

func New(hour, minute int) Clock {
	return Roll(Clock{hour, minute})
}

func TimeFormat(time int) string {
	// insert a '0' into the time string to make it double digit
	if time < 10 {
		return "0" + strconv.Itoa(time)
	}
	return strconv.Itoa(time)
}

func (self Clock) String() string {
	return TimeFormat(self.hour) + ":" + TimeFormat(self.minute)
}

func (self Clock) Add(minutes int) Clock {
	return Roll(Clock{self.hour, self.minute + minutes})
}

func Roll(self Clock) Clock {
	// roll over negative minutes
	if self.minute < 0 {
		self.hour += self.minute / 60 - 1
		self.minute = 60 + (self.minute % 60)
	}

	// roll over negative hours
	if self.hour < 0 {
		self.hour = 24 + (self.hour % 24)
	}

	// roll over hours and minutes
	if self.minute >= 60 || self.hour >= 24 {
		self.hour += self.minute / 60
		self.minute %= 60
		self.hour %= 24
	}
	return self
}
