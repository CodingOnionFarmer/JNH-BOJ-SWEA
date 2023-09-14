# [Platinum II] Sightseeing Cows - 6141 

[문제 링크](https://www.acmicpc.net/problem/6141) 

### 성능 요약

메모리: 184516 KB, 시간: 920 ms

### 분류

벨만–포드, 이분 탐색, 그래프 이론, 매개 변수 탐색

### 문제 설명

<p>Farmer John has decided to reward his cows for their hard work by taking them on a tour of the big city! The cows must decide how best to spend their free time.</p>

<p>Fortunately, they have a detailed city map showing the L (2 <= L <= 1000) major landmarks (conveniently numbered 1.. L) and the P (2 <= P <= 5000) unidirectional cow paths that join them. Farmer John will drive the cows to a starting landmark of their choice, from which they will walk along the cow paths to a series of other landmarks, ending back at their starting landmark where Farmer John will pick them up and take them back to the  farm. Because space in the city is at a premium, the cow paths are very narrow and so travel along each cow path is only allowed in one fixed direction.</p>

<p>While the cows may spend as much time as they like in the city, they do tend to get bored easily. Visiting each new landmark is fun, but walking between them takes time. The cows know the exact fun values F_i (1 <= F_i <= 1000) for each landmark i.</p>

<p>The cows also know about the cowpaths. Cowpath i connects landmark L1_i to L2_i (in the direction L1_i -> L2_i) and requires time T_i (1 <= T_i <= 1000) to traverse.</p>

<p>In order to have the best possible day off, the cows want to maximize the average fun value per unit time of their trip.  Of course, the landmarks are only fun the first time they are visited; the cows may pass through the landmark more than once, but they do not perceive its fun value again. Furthermore, Farmer John is making the cows visit at least two landmarks, so that they get some exercise during their day off.</p>

<p>Help the cows find the maximum fun value per unit time that they can achieve.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: L and P</li>
	<li>Lines 2..L+1: Line i+1 contains a single one integer: F_i</li>
	<li>Lines L+2..L+P+1: Line L+i+1 describes cow path i with three space-separated integers: L1_i, L2_i, and T_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single number given to two decimal places (do not perform explicit rounding), the maximum possible average fun per unit time, or 0 if the cows cannot plan any trip at all in accordance with the above rules.</li>
</ul>

<p> </p>

