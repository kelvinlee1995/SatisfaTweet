import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;


public class CollectData {
    //Send request to API with JSON result
    public String getJSON() throws IOException {
        URL obj = new URL("https://api.twitter.com/2/tweets/search/recent?" +
                "query=WorldCup2022&max_results=100");
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        con.setRequestMethod("GET");
        con.setRequestProperty("Authorization", "Bearer AAAAAAAAAAAAAAAAAAAAALQwkQEAAAAA3S02B%2FgOTK3jAS3u4WBvRVbOeRk%3DIVZYv7G5NEoscTlZ2q0zUq34a4pYLGS4aWxOic14PAlzN00iT4");
        int responseCode = con.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) { // success
            BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();
            while ((inputLine = in.readLine()) != null) {response.append(inputLine);}
            in.close();
            return response.toString();
        } else {
            System.out.println("GET request did not work.");
        }
        return null;
    }

    //Create JSON file on the desktop with data with only "Text" field
    public void createJSON(String src) throws IOException {
        FileWriter file = new FileWriter("C:\\Users\\kelvi\\Desktop\\twitter.json");
        file.write(src);
        file.close();
    }

    public void createTextField(String src) throws IOException {
        FileWriter file = new FileWriter("C:\\Users\\kelvi\\Desktop\\textfield.txt");
        file.write(src);
        file.close();
    }

    public String jsonObject(String src) {
        JSONObject obj = new JSONObject(src);
        JSONArray arr = obj.getJSONArray("data");
        String arrString = null;
        for (int i = 0; i < arr.length(); i++){
            String text = arr.getJSONObject(i).getString("text");
            text.replace("\n", " ");
            arrString+=text;
        }
        return arrString;
    }
}
