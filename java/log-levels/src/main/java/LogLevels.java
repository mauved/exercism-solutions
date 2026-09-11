import java.lang.String;
import java.util.Locale;
import java.util.regex.Pattern;

public class LogLevels {
    public static String message(String logLine) {
        // Splits log lines based on closing bracket immediately succeeded by colon
        // That pattern shouldn't appear many times in a log line, right?
        return logLine.split("]:")[1].strip();
    }

    public static String logLevel(String logLine) {
        // Do the log splitting based on bracket and colon, but select the first token
        // Then remove all non-word characters, like say, opening brackets
        return logLine.split("]:")[0].strip().replaceAll("\\W","").toLowerCase();
    }

    public static String reformat(String logLine) {
        // Use preceding functions to reconstruct log line
        return message(logLine) + " (" + logLevel(logLine) + ")";
    }
}
