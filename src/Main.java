import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException{
        CollectData data = new CollectData();
        //Données du GET
        String jsonData = data.getJSON();
        data.createJSON(jsonData);
        String textField = data.jsonObject(jsonData);
        data.createTextField(textField);
    }
}