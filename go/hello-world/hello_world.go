//
// Completed by Sofia Nieves
// Mon 30 May 15:26:37 UTC 2016
//
package hello

const testVersion = 2

// It's "Hello world"
func HelloWorld(name string) string {
	if name != "" {
		return "Hello, " + name + "!"
	}
	return "Hello, World!"
}
