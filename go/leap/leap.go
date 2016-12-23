// completed by Sofia Nieves

package leap

// testVersion should match the targetTestVersion in the test file.
const testVersion = 2

//Rules of leap years:
//on every year that is evenly divisible by 4
//  except every year that is evenly divisible by 100
//    unless the year is also evenly divisible by 400
func IsLeapYear(yr int) bool {
	return (yr%4 == 0) && ((yr%100 != 0) || (yr%400 == 0))
}
