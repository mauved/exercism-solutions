// Leap stub file
// completed by Sofia Nieves

// The package name is expected by the test program.
package leap

// testVersion should match the targetTestVersion in the test file.
const testVersion = 2

// It's good style to write a comment here documenting IsLeapYear.
func IsLeapYear(yr int) bool {
	return (yr%4 == 0) && ((yr%100 != 0) || (yr%400 == 0))
}
