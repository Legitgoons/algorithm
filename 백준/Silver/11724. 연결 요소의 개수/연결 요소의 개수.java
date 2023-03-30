import java.util.*;

public class Main {
	static int[] parents; // 관계 담을 배열
	static int ans; // 연결 요소 개수

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt(); // 정점의 개수
		int M = sc.nextInt(); // 간선의 개수
		ans = 0;
		parents = new int[N + 1]; // 

		for (int i = 1; i < parents.length; i++) {
			parents[i] = i; // Make-Set을 해줌(노드의 대표값을 index번호로 초기화해줌)
		}

		for (int i = 0; i < M; i++) { // 관계 입력받음
			int a = sc.nextInt(); // 간선의 양 끝점 입력받음
			int b = sc.nextInt();
			union(a, b); // union 실행
		}

		for (int i = 1; i < parents.length; i++) {
			if (parents[i] == i) {
				ans++;
			}
		}
		System.out.println(ans);

	}

	private static void union(int a, int b) { // union으로 묶어주기
		a = find(a); // find로 대표자 찾아줌
		b = find(b);

		if (a != b) { // 둘의 대표자가 다르다면 = 사이클이 생기지 않는다면
			parents[a] = b; // a의 대표자를 b로 변경
		}
	}

	private static int find(int x) { // 대표자 찾기
		if (parents[x] == x) // 대표자가 자신이라면
			return x; //return
		return parents[x] = find(parents[x]); // 아니면 재귀함수로 대표자 찾아줌
	}
}