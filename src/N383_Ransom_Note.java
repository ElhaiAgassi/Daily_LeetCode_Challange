import java.util.HashMap;
import java.util.Map;

public class N383_Ransom_Note {
    public static boolean canConstruct(String ransomNote, String magazine) {
        int[] bucket = new int[128];
        for (Character c: magazine.toCharArray()){
            bucket[c]++;
        }
        for (Character c: ransomNote.toCharArray()){
            bucket[c]--;
            if (bucket[c]<0){
                return false;
            }
        }
        return true;
    }


    public static void main(String[] args) {
        System.out.println(canConstruct("aa","aab"));
    }
}
//Runtime: 9 ms, faster than 54.43% of Java online submissions for Ransom Note.
//Memory Usage: 46.3 MB, less than 50.16% of Java online submissions for Ransom Note.
