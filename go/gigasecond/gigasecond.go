package gigasecond

import "time"

const testVersion = 4

const Gigasecond = time.Duration(1e9 * time.Second)

func AddGigasecond(t time.Time) time.Time {
	return t.Add(Gigasecond)
}
