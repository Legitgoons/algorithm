import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int[] arr;
    static int[] sorted;
    static int cnt = 0;
    static int result = -1; // K값 달성하지 못할경우 -1
    static int K;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        K = sc.nextInt();
        arr = new int[N] ;

        for (int i = 0; i<N; i++) {
            arr[i] = sc.nextInt();
        }
        sorted = new int[N];
        mergeSort(0, arr.length - 1);
        System.out.println(result);
    }

    public static void mergeSort(int left, int right) {
        if (right <= left) return; // 정렬 완료시 반환

        int mid = (left + right) / 2; // 위치의 절반

        mergeSort(left, mid); // 좌측 나누기
        mergeSort(mid+1, right); // 우측 나누기

        merge(left, mid, right); // 결합
    }

    public static void merge(int left, int mid, int right) {
        int l = left; // 좌측 리스트들의 시작점
        int r = mid + 1; // 우측 리스트들의 시작점
        int idx = left; // 정렬된 데이터가 들어갈 인덱스
        while (l <= mid && r <= right) {
            /*
             * 왼쪽 부분리스트 l번째 원소가 오른쪽 부분리스트 r번째 원소보다 작거나 같을 경우 왼쪽의 l번째 원소를 새 배열에 넣고 l과 idx를 1 증가시킨다.
             */
            if (arr[l] <= arr[r]) { //좌측 리스트 l번째 원소가 우측 리스트 r번째 원소보다 작거나 같다면
                sorted[idx] = arr[l]; // 정렬용 배열에 넣어주고
                idx++; //인덱스와
                l++; // 좌측 리스트 타겟을 한칸씩 이동시킴
            }
            else { // 우측이 더 작을 경우
                sorted[idx] = arr[r];
                idx++;
                r++;
            }
        }
        if (l > mid) { // 좌측 부분 리스트가 모두 정렬용 배열에 들어갔다면
            while (r <= right) { // 우측 부분 리스트들도 모두 채워줌
                sorted[idx] = arr[r];
                idx++;
                r++;
            }
        }
        else { // 우측이 모두 들어갔다면
            while (l <= mid) {
                sorted[idx] = arr[l];
                idx++;
                l++;
            }
        }
        for(int i = left; i <= right; i++) {
            arr[i] = sorted[i];
            cnt++;
            if(cnt == K){
                result = arr[i];
                break;
            }
        }
    }
}
