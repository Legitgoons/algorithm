import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int[] arr;
    static int[] sorted;
    static int cnt = 0;
    static int K;
    static boolean breaker = false;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] nk = br.readLine().split(" ");
        int N = Integer.parseInt(nk[0]);
        K = Integer.parseInt(nk[1]);

        arr = new int[N];
        String[] arrInput = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(arrInput[i]);
        }

        sorted = new int[N];
        mergeSort(0, arr.length - 1);

        StringBuilder sb = new StringBuilder();
        if (breaker == true) {
            sb.append(arr[0]);
            for (int i = 1; i < N; i++) {
                sb.append(" " + arr[i]);
            }
        } else {
            sb.append(-1);
        }
        System.out.println(sb);
    }

    public static void mergeSort(int left, int right) {
        if (right <= left)
            return;
        else if (breaker == true)
            return;

        int mid = (left + right) / 2;
        mergeSort(left, mid);
        mergeSort(mid + 1, right);
        merge(left, mid, right);
    }

    public static void merge(int left, int mid, int right) {
        int l = left;
        int r = mid + 1;
        int idx = left;

        while (l <= mid && r <= right) {
            if (arr[l] <= arr[r]) {
                sorted[idx] = arr[l];
                idx++;
                l++;
            } else {
                sorted[idx] = arr[r];
                idx++;
                r++;
            }
        }

        if (l > mid) {
            while (r <= right) {
                sorted[idx] = arr[r];
                idx++;
                r++;
            }
        } else {
            while (l <= mid) {
                sorted[idx] = arr[l];
                idx++;
                l++;
            }
        }

        for (int i = left; i <= right; i++) {
            if (cnt == K) {
                breaker = true;
                return;
            }
            arr[i] = sorted[i];
            cnt++;
        }
    }
}