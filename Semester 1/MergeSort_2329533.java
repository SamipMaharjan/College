import java.util.ArrayList;
import java.util.Scanner;
public class MergeSort_2329533 {
    // Taking input
    ArrayList <Integer> getInput(ArrayList <Integer> al) {
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter the total number of elements you want in your arraylist: ");
        int n = sc.nextInt();
        for(int i=1; i<=n; i++) {
            System.out.println("Enter your "+i+"th number:");
            al.add(sc.nextInt());
        }
        return al;


    }
    // Displaying the output
    void getOutput (ArrayList <Integer> al) {
        System.out.println("Before being sorted your sequence was: "+ al);
        sort(al, 0, al.size()-1);
        System.out.println("After being sorted the sequence is:" + al);
    }
    void merge(ArrayList <Integer> al, int beg, int mid, int end) {
        ArrayList <Integer> sortedArraylist= new ArrayList <Integer>();
        int i = mid + 1;
        int j = beg;
        while (i<=end && j<=mid) {
            if (al.get(j) < al.get(i)) {
                sortedArraylist.add(al.get(j));
                j++;
            }
            else {
                sortedArraylist.add(al.get(i));
                i++;
            }
        }

        for (int m = j; m <= mid; m++){
            sortedArraylist.add(al.get(m));
        }
        for (int m = 0; m < sortedArraylist.size(); m++){
            al.set(beg + m, sortedArraylist.get(m));
        }
    }

    void sort(ArrayList <Integer> al, int beg, int end) {
        if (beg >= end) {
            return;
        }

        int mid = (beg + end)/2;
        sort(al, beg, mid);
        sort(al, mid + 1, end);//Dividing the arrays recursively.
        merge(al, beg, mid, end);
    }
    public static void main(String[] args) {
        ArrayList <Integer> al = new ArrayList <Integer>();
        MergeSort_2329533 obj = new MergeSort_2329533();
        obj.getInput(al);
        obj.getOutput(al);
    }
}
