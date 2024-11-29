import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class Solution {

    public void partOne() throws Exception {
        Integer horiz = 0;
        Integer depth = 0;
        File file = new File("d2-input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String line;
        String dir;
        String amount;
        while ((line = br.readLine()) != null) {
            line = line.trim();
            dir = line.split(" ")[0];
            amount = line.split(" ")[1];
            switch (dir) {
                case "forward":
                    horiz += Integer.parseInt(amount);
                    break;
                case "down":
                    depth += Integer.parseInt(amount);
                    break;
                case "up":
                    depth -= Integer.parseInt(amount);
                    break;
                default:
                    break;
            }
        }
        br.close();
        System.out.println("Part One: " + horiz * depth);
    }

    public void partTwo() throws Exception {
        Integer horiz = 0;
        Integer depth = 0;
        Integer aim = 0;
        File file = new File("d2-input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String line;
        String dir;
        String amount;
        while ((line = br.readLine()) != null) {
            line = line.trim();
            dir = line.split(" ")[0];
            amount = line.split(" ")[1];
            switch (dir) {
                case "forward":
                    horiz += Integer.parseInt(amount);
                    depth += aim * Integer.parseInt(amount);
                    break;
                case "down":
                    aim += Integer.parseInt(amount);
                    break;
                case "up":
                    aim -= Integer.parseInt(amount);
                    break;
                default:
                    break;
            }
        }
        br.close();
        System.out.println("Part Two: " + horiz * depth);
    }

    public static void main(String[] args) {
        Solution dayTwo = new Solution();
        try {
            dayTwo.partOne();
            dayTwo.partTwo();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

}
