import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;

public class Solution {
    ArrayList<Integer> numbers = new ArrayList<Integer>();

    public void parseInput() throws Exception {
        File file = new File("d1-input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String line;
        while ((line = br.readLine()) != null)
            numbers.add(Integer.parseInt(line));
        br.close();
    }

    public void PartOne() {
        Integer numInc = 0;
        for (int i = 1; i < numbers.size(); i++) {
            if (numbers.get(i - 1) < numbers.get(i)) {
                numInc++;
            }
        }
        System.out.println("Part One: " + numInc);
    }

    public void PartTwo() {
        Integer numInc = 0;
        for (int i = 3; i < numbers.size(); i++) {
            Integer sum1 = numbers.get(i - 3) + numbers.get(i - 2) + numbers.get(i - 1);
            Integer sum2 = numbers.get(i - 2) + numbers.get(i - 1) + numbers.get(i);
            if (sum1 < sum2) {
                numInc++;
            }
        }
        System.out.println("Part Two: " + numInc);
    }

    public static void main(String[] args) {
        Solution dayOne = new Solution();
        try {
            dayOne.parseInput();
        } catch (Exception e) {
            e.printStackTrace();
        }
        dayOne.PartOne();
        dayOne.PartTwo();
    }
}
