import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class service {
	
	private static String readCSS() {
		try {
			BufferedReader br = new BufferedReader(new FileReader("src/template.css"));
			String line;
			String output = "";
			while ((line = br.readLine()) !=null) {
				output = output + line.replaceAll("\t", "");
			}
			br.close();
			return output;
		} catch (IOException e) {
			e.printStackTrace();
			return null;
		}
		
	}
	
	private static String substituteCSS(String css, String mainC, String accentC, String font) {
		css = css.replaceAll("_MAIN_COLOUR_", "#" + mainC);
		css = css.replaceAll("_ACCENT_COLOUR_", "#" + accentC);
		css = css.replaceAll("_FONT_FAMILY_", font);
		return css;
	}
	
	private static String verifyHex(String rawInput, String defaultValue) {
		try {
			Long.parseLong(rawInput,16);
			if (rawInput.length() <= 6) {
				return rawInput;
			} else {
				return defaultValue;
			}
		} catch (Exception e) {
			e.printStackTrace();
			return defaultValue;
		}
	}
	
	private static String verifyFont(String fontInput, String defaultValue) {
		if (fontInput.equals("serif")) {
			return "serif";
		} else if(fontInput.equals("sans-serif")) {
			return "sans-serif";
		} else if(fontInput.equals("monospace")) {
			return "monospace";
		} else {
			return defaultValue;
		}
	}
	
	public static void webServe(int port) throws IOException {
		ServerSocket server = new ServerSocket(port);
		while(true) {
			// server.accept() is blocking, so your code will stop here until a connection is made
			Socket userConn = server.accept();
			// Buffered Reader for handling the input stream from the user/client
			BufferedReader br = new BufferedReader(new InputStreamReader(userConn.getInputStream()), 1);
			String userin = "";
			String line;
			// Read from the buffer until the buffer is empty or the connection closes
			while ((line = br.readLine()) != null) {
				userin = userin + line;
	            if (line.isEmpty()) {
	                break;
	            }
	        }
			// Print out the input from the user/client
			String mainC = parseHeader("main", userin);
			String accentC = parseHeader("accent", userin);
			String font = parseHeader("font", userin);
			
			
			mainC = verifyHex(mainC, "FFFFFF");
			accentC = verifyHex(accentC, "FFFFFF");
			font = verifyFont(font, "monospace");
			
			System.out.println("font: " +font);
			System.out.println("main: " + mainC);
			System.out.println("accent: " + accentC);
			
			String css = readCSS();
			System.out.println(css);
			
			css = substituteCSS(css, mainC, accentC, font);
			System.out.println(css);
			
			// Writing our response message - note that the headers must end in \r\n\r\n
			// The message itself should come after the headers, and should end in \r\n
			String helloWorld = css + "\r\n";
			String response = "HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n" + helloWorld;
			// Write the HTTP message out to the output stream, back to the client/user
			userConn.getOutputStream().write(response.getBytes("UTF-8"));
			userConn.getOutputStream().flush();
			// Flush to make sure the data is sent, and then close the connection and the buffered reader
			userConn.close();
			br.close();
			server.setReuseAddress(true);
		}
	}
	
	public static String parseHeader(String variable, String rawInput) {
		String pattern = "GET /.*" + variable + "=(.*?)(?:&| HTTP)";
		Pattern regex = Pattern.compile(pattern);
		Matcher match = regex.matcher(rawInput);
		if(match.find()) {
			return match.group(1);
		} else {
			return null;
		}
	}
	
	public static void main(String[] args) throws IOException {
		// Begins the webserver on the specified port (Port 80 by default)
		webServe(80);
	}
	
}