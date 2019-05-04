import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public static int solution(String S) throws ParseException{
    Map<String, List<Integer>> callToDuration = new HashMap<String, List<Integer>>();

        String[] parts = S.split("\\r?\\n|\\r");

        for(String s: parts) {
            String time_string = s.substring(0, s.indexOf(","));
            String phone_string = s.substring(s.indexOf(",") + 1, s.length());

            Date date = null;
            try {
                date = new SimpleDateFormat("hh:mm:ss").parse(time_string);
            } catch (ParseException e) {
                return 0;
            }
            int totalSeconds = date.getMinutes() * 60 + date.getSeconds();

            List<Integer> durationList = new ArrayList<Integer>();

            if(callToDuration.containsKey(phone_string)) {
                durationList = callToDuration.get(phone_string);
                durationList.add(totalSeconds);
            } else {
                durationList.add(totalSeconds);
                callToDuration.put(phone_string, durationList);
            }
        }


        Map<String, List<Integer>> finalMap = new TreeMap<String, List<Integer>>();

        for(Map.Entry<String, List<Integer>> e: callToDuration.entrySet()) {

            String phno = e.getKey();
            List<Integer> durations = e.getValue();

            List<Integer> trackValues = new ArrayList<Integer>();

            int totalDuration = 0;
            int bill = 0;

            for(int dur: durations) {
                totalDuration += dur;

                if(dur < 300) {
                    bill+= dur * 3;
            } else {
                    bill += (int)Math.ceil(Double.valueOf(dur)/60) * 150;
                }
            }

            trackValues.add(0,totalDuration);
            trackValues.add(1,bill);


            finalMap.put(phno, trackValues);
        }

        int maxDuration = 0;

        for(Map.Entry<String, List<Integer>> e: finalMap.entrySet()) {

            if (e.getValue().get(0) > maxDuration ) {
                maxDuration = e.getValue().get(0);
            }
        }

        boolean found = false;
        int totalBill = 0;

        for(Map.Entry<String, List<Integer>> e: finalMap.entrySet()) {

            List<Integer> trackvalues = e.getValue();

            if(trackvalues.get(0) == maxDuration && !found) {
                found = true;
                continue;
            }
            totalBill += trackvalues.get(1);
        }

        return totalBill;}
