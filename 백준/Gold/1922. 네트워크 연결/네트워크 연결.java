import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
    static int[] p; // 대표를 저장할 배열

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int V = sc.nextInt(); // V : 정점의 개수, 0부터 시작
        int E = sc.nextInt(); // E : 간선의 수

        int[][] edges = new int[E][3]; // 간선 정보 입력받아서 배열에 저장
        for (int i = 0; i < E; i++) {
            edges[i][0] = sc.nextInt();// 시작 정점
            edges[i][1] = sc.nextInt();// 끝 정점
            edges[i][2] = sc.nextInt();// 가중치
        }

        // 크루스칼 1단계 : 간선 오름차순 정렬
        Arrays.sort(edges, new Comparator<int[]>() {
            public int compare(int[] o1, int[] o2) {
                return o1[2] - o2[2];
            }
        });

        // 크루스칼 2단계 : 사이클이 발생하지 않는 V-1개의 간선 선택
        // make-set(자신을 대표로 초기화)
        p = new int[V+1];
        for (int i = 0; i < V+1; i++) {
            p[i] = i;
        }

        int ans = 0; // 최소비용
        int pick = 0; // 선택한 간선의 수

        for (int i = 0; i < E; i++) {
            int px = findset(edges[i][0]);
            int py = findset(edges[i][1]);

            if (px != py) { // 부모가 다르다면 = 사이클이 발생하지 않는다면
                union(px, py); // union으로 합쳐줌
                ans += edges[i][2];
                pick++;
            }
            if (pick == V-1) 
                break;
        }
        System.out.println(ans);
    }

    // path compression (Findset 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 조정)
    static int findset(int x) {
        if (x != p[x]) // x가 자신의 부모값이 아니라면
            p[x] = findset(p[x]); // 재귀로 부모값을 찾도록 함
        return p[x]; // 부모값을 찾았다면 return
    }

    static void union(int x, int y) { // 부모값이 작은쪽이 부모값이 큰쪽에 붙도록
        if (p[y] < p[x])
            p[y] = findset(x);
        else
            p[x] = findset(y);
    }
}