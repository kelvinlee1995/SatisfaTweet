import java.io.IOException;
import java.net.MalformedURLException;
import org.json.*;


public class Main {
    public static void main(String[] args) throws IOException{
        CollectData data = new CollectData();
        //Données du GET
        String jsonData = data.sendGET();
        data.createJSON();
        data.jsonObject(jsonData);

    }
}