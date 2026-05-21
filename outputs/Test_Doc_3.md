Third Edition

## Data Structures and Algorithm

Analysis in Java Mark  Allen Weiss Florida  International  University TM

## PEARSON

Boston Columbus Indianapolis New York San Francisco Upper Saddle River Amsterdam Cape Town Dubai London Madrid Milan Munich Paris Montreal Toronto Delhi Mexico City Sao Paulo Sydney Hong Kong Seoul Singapore Taipei Tokyo

Editorial Director: Marcia Horton Editor-in-Chief: Michael Hirsch Editorial Assistant: Emma Snider Director of Marketing: Patrice Jones Marketing Manager: Yezan Alayan Marketing Coordinator: Kathryn Ferranti Director of Production: Vince O'Brien Managing Editor: Jeff Holcomb Production Project Manager: Kayla Smith-Tarbox

Project Manager: Pat Brown Manufacturing Buyer: Pat Brown Art Director: Jayne Conte Cover Designer: Bruce Kenselaar Cover Photo: © Media Editor: Daniel Sandin Composition: Integra Printer/Binder: Courier Westford Text Font: Berkeley-Book

c De-Kay Dreamstime.com

Full-Service Project Management: Integra

Cover Printer: Lehigh-Phoenix Color/Hagerstown

Copyright c © 2012, 2007, 1999 Pearson Education, Inc., publishing as Addison-Wesley. All rights reserved. Printed in the United States of America. This publication is protected by Copyright, and permission should be obtained from the publisher prior to any prohibited reproduction, storage in a retrieval system, or transmission in any form or by any means, electronic, mechanical, photocopying, recording, or likewise. To obtain permission(s) to use material from this work, please submit a written request to Pearson Education, Inc., Permissions Department, One Lake Street, Upper Saddle River, New Jersey 07458, or you may fax your request to 201-236-3290.

Many of the designations by manufacturers and sellers to distinguish their products are claimed as trademarks. Where those designations appear in this book, and the publisher was aware of a trademark claim, the designations have been printed in initial caps or all caps.

## Library of Congress Cataloging-in-Publication Data

```
Weiss, Mark Allen. Data structures and algorithm analysis in Java / Mark Allen Weiss. - 3rd ed. p. cm. ISBN-13: 978-0-13-257627-7 (alk. paper) ISBN-10: 0-13-257627-9 (alk. paper) 1. Java (Computer program language) 2. Data structures (Computer science) 3. Computer algorithms. I. Title. QA76.73.J38W448 2012 005.1-dc23 2011035536
```

15 14 13 12 11-CRW-10 9 8 7 6 5 4 3 2 1

<!-- image -->

ISBN 10: 0-13-257627-9

## Sorting

In this chapter we discuss the problem of sorting an array of elements. To simplify matters, we will assume in our examples that the array contains only integers, although our code will once again allow more general objects. For most of this chapter, we will also assume that the entire sort can be done in main memory , so that the number of elements is relatively small (less than a few million). Sorts that cannot be performed in main memory and must be done on disk or tape are also quite important. This type of sorting, known as external sorting, will be discussed at the end of the chapter.

Our investigation of internal sorting will show that

- /a114 There are several easy algorithms to sort in O ( N 2 ), such as insertion sort.
- /a114 There is an algorithm, Shellsort, that is very simple to code, runs in o ( N 2 ), and is efficient in practice.
- /a114 There are slightly more complicated O ( N log N ) sorting algorithms.
- /a114 Any general-purpose sorting algorithm requires /Omega1 ( N log N ) comparisons.

The rest of this chapter will describe and analyze the various sorting algorithms. These algorithms contain interesting and important ideas for code optimization as well as algorithm design. Sorting is also an example where the analysis can be precisely performed. Be forewarned that where appropriate, we will do as much analysis as possible.

## 7.1 Preliminaries

The algorithms we describe will all be interchangeable. Each will be passed an array containing the elements; we assume all array positions contain data to be sorted. We will assume that N is the number of elements passed to our sorting routines.

The objects being sorted are of type Comparable , as described in Section 1.4. We thus use the compareTo method to place a consistent ordering on the input. Besides (reference) assignments, this is the only operation allowed on the input data. Sorting under these conditions is known as comparison-based sorting . The sorting algorithms are easily rewritten to use Comparator s, in the event that the default ordering is unavailable or unacceptable.

7

| Original    |   34 |   8 |   64 |   51 |   32 |   21 |   Positions Moved |
|-------------|------|-----|------|------|------|------|-------------------|
| After p = 1 |    8 |  34 |   64 |   51 |   32 |   21 |                 1 |
| After p = 2 |    8 |  34 |   64 |   51 |   32 |   21 |                 0 |
| After p = 3 |    8 |  34 |   51 |   64 |   32 |   21 |                 1 |
| After p = 4 |    8 |  32 |   34 |   51 |   64 |   21 |                 3 |
| After p 5   |    8 |  21 |   32 |   34 |   51 |   64 |                 4 |

=

Figure 7.1 Insertion sort after each pass

## 7.2 Insertion Sort

## 7.2.1 The Algorithm

One of the simplest sorting algorithms is the insertion sort . Insertion sort consists of N -1 passes . For pass p = 1 through N -1, insertion sort ensures that the elements in positions 0 through p are in sorted order. Insertion sort makes use of the fact that elements in positions 0 through p -1 are already known to be in sorted order. Figure 7.1 shows a sample array after each pass of insertion sort.

Figure 7.1 shows the general strategy . In pass p , we move the element in position p left until its correct place is found among the first p + 1 elements. The code in Figure 7.2 implements this strategy . Lines 12 through 15 implement that data movement without the explicit use of swaps. The element in position p is saved in tmp , and all larger elements (prior to position p ) are moved one spot to the right. Then tmp is placed in the correct spot. This is the same technique that was used in the implementation of binary heaps.

## 7.2.2 Analysis of Insertion Sort

Because of the nested loops, each of which can take N iterations, insertion sort is O ( N 2 ). Furthermore, this bound is tight, because input in reverse order can achieve this bound. A precise calculation shows that the number of tests in the inner loop in Figure 7.2 is at most p + 1 times for each value of p . Summing over all p gives a total of

<!-- formula-not-decoded -->

On the other hand, if the input is presorted, the running time is O ( N ), because the test in the inner for loop always fails immediately . Indeed, if the input is almost sorted (this term will be more rigorously defined in the next section), insertion sort will run quickly. Because of this wide variation, it is worth analyzing the average-case behavior of this algorithm. It turns out that the average case is /Theta1 ( N 2 ) for insertion sort, as well as for a variety of other sorting algorithms, as the next section shows.

```
1 / ** 2 * Simple insertion sort. 3 * @param a an array of Comparable items. 4 * / 5 public static <AnyType extends Comparable<? super AnyType>> 6 void insertionSort( AnyType [ ] a ) 7 { 8 int j; 9 10 for( int p = 1; p < a.length; p++ ) 11 { 12 AnyType tmp = a[ p ]; 13 for( j = p; j > 0 && tmp.compareTo( a[ j -1 ] ) < 0; j--) 14 a[ j ] = a[ j - 1 ]; 15 a[ j ] = tmp; 16 } 17 }
```

Figure 7.2 Insertion sort routine

## 7.3 A Lower Bound for Simple Sorting Algorithms

An inversion in an array of numbers is any ordered pair ( i , j ) having the property that i &lt; j but a [ i ] &gt; a [ j ]. In the example of the last section, the input list 34, 8, 64, 51, 32, 21 had nine inversions, namely (34, 8), (34, 32), (34, 21), (64, 51), (64, 32), (64, 21), (51, 32), (51, 21), and (32, 21). Notice that this is exactly the number of swaps that needed to be (implicitly) performed by insertion sort. This is always the case, because swapping two adjacent elements that are out of place removes exactly one inversion, and a sorted array has no inversions. Since there is O ( N ) other work involved in the algorithm, the running time of insertion sort is O ( I + N ), where I is the number of inversions in the original array . Thus, insertion sort runs in linear time if the number of inversions is O ( N ).

We can compute precise bounds on the average running time of insertion sort by computing the average number of inversions in a permutation. As usual, defining average is a difficult proposition. We will assume that there are no duplicate elements (if we allow duplicates, it is not even clear what the average number of duplicates is). Using this assumption, we can assume that the input is some permutation of the first N integers (since only relative ordering is important) and that all are equally likely . Under these assumptions, we have the following theorem:

## Theorem 7.1.

The average number of inversions in an array of N distinct elements is N ( N -1) / 4.

## Proof.

For any list, L , of elements, consider Lr , the list in reverse order. The reverse list of the example is 21, 32, 51, 64, 8, 34. Consider any pair of two elements in the list ( x , y ), with y &gt; x . Clearly , in exactly one of L and Lr this ordered pair represents an inversion. The total number of these pairs in a list L and its reverse Lr is N ( N -1) / 2. Thus, an average list has half this amount, or N ( N -1) / 4 inversions.

This theorem implies that insertion sort is quadratic on average. It also provides a very strong lower bound about any algorithm that only exchanges adjacent elements.

## Theorem 7.2.

Any algorithm that sorts by exchanging adjacent elements requires /Omega1 ( N 2 ) time on average.

## Proof.

The average number of inversions is initially N ( N -1) / 4 = /Omega1 ( N 2 ). Each swap removes only one inversion, so /Omega1 ( N 2 ) swaps are required.

This is an example of a lower-bound proof. It is valid not only for insertion sort, which performs adjacent exchanges implicitly , but also for other simple algorithms such as bubble sort and selection sort, which we will not describe here. In fact, it is valid over an entire class of sorting algorithms, including those undiscovered, that perform only adjacent exchanges. Because of this, this proof cannot be confirmed empirically . Although this lower-bound proof is rather simple, in general proving lower bounds is much more complicated than proving upper bounds and in some cases resembles magic.

This lower bound shows us that in order for a sorting algorithm to run in subquadratic, or o ( N 2 ), time, it must do comparisons and, in particular, exchanges between elements that are far apart. A sorting algorithm makes progress by eliminating inversions, and to run efficiently , it must eliminate more than just one inversion per exchange.

## 7.4 Shellsort

Shellsort, named after its inventor, Donald Shell, was one of the first algorithms to break the quadratic time barrier, although it was not until several years after its initial discovery that a subquadratic time bound was proven. As suggested in the previous section, it works by comparing elements that are distant; the distance between comparisons decreases as the algorithm runs until the last phase, in which adjacent elements are compared. For this reason, Shellsort is sometimes referred to as diminishing increment sort .

Shellsort uses a sequence, h 1, h 2, . . . , ht , called the increment sequence . Any increment sequence will do as long as h 1 = 1, but some choices are better than others (we will discuss that issue later). After a phase, using some increment hk , for every i , we have a [ i ] ≤ a [ i + hk ] (where this makes sense); all elements spaced hk apart are sorted. The file is then said to be hk -sorted . For example, Figure 7.3 shows an array after several phases of Shellsort. An important property of Shellsort (which we state without proof) is that an hk -sorted file that is then hk -1-sorted remains hk -sorted. If this were not the case, the

Figure 7.3 Shellsort after each pass, using { 1, 3, 5 } as the increment sequence

| Original     |   81 |   94 |   11 |   96 |   12 |   35 |   17 |   95 |   28 |   58 |   41 |   75 |   15 |
|--------------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| After 5-sort |   35 |   17 |   11 |   28 |   12 |   41 |   75 |   15 |   96 |   58 |   81 |   94 |   95 |
| After 3-sort |   28 |   12 |   11 |   35 |   15 |   41 |   58 |   17 |   94 |   75 |   81 |   96 |   95 |
| After 1-sort |   11 |   12 |   15 |   17 |   28 |   35 |   41 |   58 |   75 |   81 |   94 |   95 |   96 |

```
1 / ** 2 * Shellsort, using Shell's (poor) increments. 3 * @param a an array of Comparable items. 4 * / 5 public static <AnyType extends Comparable<? super AnyType>> 6 void shellsort( AnyType [ ] a ) 7 { 8 int j; 9 10 for( int gap = a.length / 2; gap > 0; gap /= 2 ) 11 for( int i = gap; i < a.length; i++ ) 12 { 13 AnyType tmp = a[ i ]; 14 for( j = i; j >= gap && 15 tmp.compareTo( a[ j -gap ] ) < 0; j -= gap ) 16 a[ j ] = a[ j -gap ]; 17 a[ j ] = tmp; 18 } 19 }
```

Figure 7.4 Shellsort routine using Shell's increments (better increments are possible)

algorithm would likely be of little value, since work done by early phases would be undone by later phases.

The general strategy to hk -sort is for each position, i , in hk , hk + 1, . . . , N -1, place the element in the correct spot among i , i -hk , i -2 hk , and so on. Although this does not affect the implementation, a careful examination shows that the action of an hk -sort is to perform an insertion sort on hk independent subarrays. This observation will be important when we analyze the running time of Shellsort.

A popular (but poor) choice for increment sequence is to use the sequence suggested by Shell: ht = ⌊ N / 2 ⌋ , and hk = ⌊ hk + 1 / 2 ⌋ (This is not the sequence used in the example in Figure 7.3). Figure 7.4 contains a method that implements Shellsort using this sequence. We shall see later that there are increment sequences that give a significant improvement in the algorithm's running time; even a minor change can drastically affect performance (Exercise 7.10).

The program in Figure 7.4 avoids the explicit use of swaps in the same manner as our implementation of insertion sort.

## 7.4.1 Worst-Case Analysis of Shellsort

Although Shellsort is simple to code, the analysis of its running time is quite another story . The running time of Shellsort depends on the choice of increment sequence, and the proofs can be rather involved. The average-case analysis of Shellsort is a long-standing open problem, except for the most trivial increment sequences. We will prove tight worst-case bounds for two particular increment sequences.

## Theorem 7.3.

The worst-case running time of Shellsort, using Shell's increments, is /Theta1 ( N 2 ).

## Proof.

The proof requires showing not only an upper bound on the worst-case running time but also showing that there exists some input that actually takes /Omega1 ( N 2 ) time to run. We prove the lower bound first, by constructing a bad case. First, we choose N to be a power of 2. This makes all the increments even, except for the last increment, which is 1. Now, we will give as input an array with the N / 2 largest numbers in the even positions and the N / 2 smallest numbers in the odd positions (for this proof, the first position is position 1). As all the increments except the last are even, when we come to the last pass, the N / 2 largest numbers are still all in even positions and the N / 2 smallest numbers are still all in odd positions. The i th smallest number ( i ≤ N / 2) is thus in position 2 i -1 before the beginning of the last pass. Restoring the ith element to its correct place requires moving it i -1 spaces in the array . Thus, to merely place the N / 2 smallest elements in the correct place requires at least ∑ N / 2 i = 1 i -1 = /Omega1 ( N 2 ) work. As an example, Figure 7.5 shows a bad (but not the worst) input when N = 16. The number of inversions remaining after the 2-sort is exactly 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28; thus, the last pass will take considerable time.

| Start        |   1 |   9 |   2 |   10 |   3 |   11 |   4 |   12 |   5 |   13 |   6 14 |    |   7 |   15 |   8 |   16 |
|--------------|-----|-----|-----|------|-----|------|-----|------|-----|------|--------|----|-----|------|-----|------|
| After 8-sort |   1 |   9 |   2 |   10 |   3 |   11 |   4 |   12 |   5 |   13 |      6 | 14 |   7 |   15 |   8 |   16 |
| After 4-sort |   1 |   9 |   2 |   10 |   3 |   11 |   4 |   12 |   5 |   13 |      6 | 14 |   7 |   15 |   8 |   16 |
| After 2-sort |   1 |   9 |   2 |   10 |   3 |   11 |   4 |   12 |   5 |   13 |      6 | 14 |   7 |   15 |   8 |   16 |
| After 1-sort |   1 |   2 |   3 |    4 |   5 |    6 |   7 |    8 |   9 |   10 |     11 | 12 |  13 |   14 |  15 |   16 |

To finish the proof, we show the upper bound of O ( N 2 ). As we have observed before, a pass with increment hk consists of hk insertion sorts of about N / hk elements. Since insertion sort is quadratic, the total cost of a pass is O ( hk ( N / hk ) 2 ) = O ( N 2 / hk ). Summing over all passes gives a total bound of O ( ∑ t i = 1 N 2 / hi ) = O ( N 2 ∑ t i = 1 1 / hi ). Because the increments form a geometric series with common ratio 2, and the largest term in the series is h 1 = 1, ∑ t i = 1 1 / hi &lt; 2. Thus we obtain a total bound of O ( N 2 ).

Figure 7.5 Bad case for Shellsort with Shell's increments (positions are numbered 1 to 16)

The problem with Shell's increments is that pairs of increments are not necessarily relatively prime, and thus the smaller increment can have little effect. Hibbard suggested a slightly different increment sequence, which gives better results in practice (and theoretically). His increments are of the form 1, 3, 7, . . . , 2 k -1. Although these increments are almost identical, the key difference is that consecutive increments have no common factors. We now analyze the worst-case running time of Shellsort for this increment sequence. The proof is rather complicated.

## Theorem 7.4.

The worst-case running time of Shellsort using Hibbard's increments is /Theta1 ( N 3 / 2 ).

## Proof.

We will prove only the upper bound and leave the proof of the lower bound as an exercise. The proof requires some well-known results from additive number theory. References to these results are provided at the end of the chapter.

For the upper bound, as before, we bound the running time of each pass and sum over all passes. For increments hk &gt; N 1 / 2 , we will use the bound O ( N 2 / hk ) from the previous theorem. Although this bound holds for the other increments, it is too large to be useful. Intuitively , we must take advantage of the fact that this increment sequence is special. What we need to show is that for any element a [ p ] in position p , when it is time to perform an hk -sort, there are only a few elements to the left of position p that are larger than a [ p ].

When we come to hk -sort the input array , we know that it has already been hk + 1and hk + 2-sorted. Prior to the hk -sort, consider elements in positions p and p -i , i ≤ p . If i is a multiple of hk + 1 or hk + 2, then clearly a [ p -i ] &lt; a [ p ]. We can say more, however. If i is expressible as a linear combination (in nonnegative integers) of hk + 1 and hk + 2, then a [ p -i ] &lt; a [ p ]. As an example, when we come to 3-sort, the file is already 7- and 15-sorted. 52 is expressible as a linear combination of 7 and 15, because 52 = 1 ∗ 7 + 3 ∗ 15. Thus, a [100] cannot be larger than a [152] because a [100] ≤ a [107] ≤ a [122] ≤ a [137] ≤ a [152].

Now, hk + 2 = 2 hk + 1 + 1, so hk + 1 and hk + 2 cannot share a common factor. In this case, it is possible to show that all integers that are at least as large as ( hk + 1 -1) ( hk + 2 -1) = 8 h 2 k + 4 hk can be expressed as a linear combination of hk + 1 and hk + 2 (see the reference at the end of the chapter).

This tells us that the body of the innermost for loop can be executed at most 8 hk + 4 = O ( hk ) times for each of the N -hk positions. This gives a bound of O ( Nhk ) per pass.

Using the fact that about half the increments satisfy hk &lt; √ N , and assuming that t is even, the total running time is then

<!-- formula-not-decoded -->

Because both sums are geometric series, and since ht / 2 = /Theta1 ( √ N ), this simplifies to

<!-- formula-not-decoded -->

The average-case running time of Shellsort, using Hibbard's increments, is thought to be O ( N 5 / 4 ), based on simulations, but nobody has been able to prove this. Pratt has shown that the /Theta1 ( N 3 / 2 ) bound applies to a wide range of increment sequences.

Sedgewick has proposed several increment sequences that give an O ( N 4 / 3 ) worstcase running time (also achievable). The average running time is conjectured to be O ( N 7 / 6 ) for these increment sequences. Empirical studies show that these sequences perform significantly better in practice than Hibbard's. The best of these is the sequence { 1, 5, 19, 41, 109, . . . } , in which the terms are either of the form 9 · 4 i -9 · 2 i + 1 or 4 i -3 · 2 i + 1. This is most easily implemented by placing these values in an array . This increment sequence is the best known in practice, although there is a lingering possibility that some increment sequence might exist that could give a significant improvement in the running time of Shellsort.

There are several other results on Shellsort that (generally) require difficult theorems from number theory and combinatorics and are mainly of theoretical interest. Shellsort is a fine example of a very simple algorithm with an extremely complex analysis.

The performance of Shellsort is quite acceptable in practice, even for N in the tens of thousands. The simplicity of the code makes it the algorithm of choice for sorting up to moderately large input.

## 7.5 Heapsort

As mentioned in Chapter 6, priority queues can be used to sort in O ( N log N ) time. The algorithm based on this idea is known as heapsort and gives the best Big-Oh running time we have seen so far.

Recall, from Chapter 6, that the basic strategy is to build a binary heap of N elements. This stage takes O ( N ) time. We then perform N deleteMin operations. The elements leave the heap smallest first, in sorted order. By recording these elements in a second array and then copying the array back, we sort N elements. Since each deleteMin takes O (log N ) time, the total running time is O ( N log N ).

The main problem with this algorithm is that it uses an extra array . Thus, the memory requirement is doubled. This could be a problem in some instances. Notice that the extra time spent copying the second array back to the first is only O ( N ), so that this is not likely to affect the running time significantly . The problem is space.

A clever way to avoid using a second array makes use of the fact that after each deleteMin , the heap shrinks by 1. Thus the cell that was last in the heap can be used to store the element that was just deleted. As an example, suppose we have a heap with six elements. The first deleteMin produces a 1. Now the heap has only five elements, so we can place a 1 in position 6. The next deleteMin produces a 2. Since the heap will now only have four elements, we can place a 2 in position 5.

Figure 7.6 ( Max ) heap after buildHeap phase

<!-- image -->

Using this strategy , after the last deleteMin the array will contain the elements in decreasing sorted order. If we want the elements in the more typical increasing sorted order, we can change the ordering property so that the parent has a larger key than the child. Thus we have a ( max )heap.

In our implementation, we will use a ( max )heap but avoid the actual ADT for the purposes of speed. As usual, everything is done in an array . The first step builds the heap in linear time. We then perform N -1 deleteMax es by swapping the last element in the heap with the first, decrementing the heap size, and percolating down. When the algorithm terminates, the array contains the elements in sorted order. For instance, consider the input sequence 31, 41, 59, 26, 53, 58, 97. The resulting heap is shown in Figure 7.6.

Figure 7.7 shows the heap that results after the first deleteMax . As the figures imply , the last element in the heap is 31; 97 has been placed in a part of the heap array that is technically no longer part of the heap. After 5 more deleteMax operations, the heap will actually have only one element, but the elements left in the heap array will be in sorted order.

The code to perform heapsort is given in Figure 7.8. The slight complication is that, unlike the binary heap, where the data begin at array index 1, the array for heapsort contains data in position 0. Thus the code is a little different from the binary heap code. The changes are minor.

## 7.5.1 Analysis of Heapsort

As we saw in Chapter 6, the first phase, which constitutes the building of the heap, uses less than 2 N comparisons. In the second phase, the i th deleteMax uses at most less than 2 ⌊ log ( N -i + 1) ⌋ comparisons, for a total of at most 2 N log N -O ( N ) comparisons (assuming N ≥ 2). Consequently, in the worst case, at most 2 N log N -O ( N ) comparisons are used by heapsort. Exercise 7.13 asks you to show that it is possible for all of the deleteMax operations to achieve their worst case simultaneously .

Figure 7.7 Heap after first deleteMax

<!-- image -->

Experiments have shown that the performance of heapsort is extremely consistent: On average it uses only slightly fewer comparisons than the worst-case bound suggests. For many years, nobody had been able to show nontrivial bounds on heapsort's average running time. The problem, it seems, is that successive deleteMax operations destroy the heap's randomness, making the probability arguments very complex. Eventually another approach proved successful.

## Theorem 7.5.

The average number of comparisons used to heapsort a random permutation of N distinct items is 2 N log N -O ( N log log N ).

## Proof.

The heap construction phase uses /Theta1 ( N ) comparisons on average, and so we only need to prove the bound for the second phase. We assume a permutation of { 1, 2, . . . , N } .

Let f ( N ) be the number of heaps of N items. One can show (Exercise 7.58) that f ( N ) &gt; ( N / (4 e )) N (where e = 2.71828 . . . ). We will show that only an exponentially small fraction of these heaps (in particular ( N / 16) N ) have a cost smaller than M = N (log N -log log N -4). When this is shown, it follows that the average value of MD is at least M minus a term that is o (1), and thus the average number of comparisons is at least 2 M . Consequently, our basic goal is to show that there are very few heaps that have small cost sequences.

Suppose the i th deleteMax pushes the root element down di levels. Then it uses 2 di comparisons. For heapsort on any input, there is a cost sequence D : d 1, d 2, . . . , dN that defines the cost of phase 2. That cost is given by MD = ∑ N i = 1 di ; the number of comparisons used is thus 2 MD .

```
1 / ** 2 * Internal method for heapsort. 3 * @param i the index of an item in the heap. 4 * @return the index of the left child. 5 * / 6 private static int leftChild( int i ) 7 { 8 return 2 * i + 1; 9 } 10 11 / ** 12 * Internal method for heapsort that is used in deleteMax and buildHeap. 13 * @param a an array of Comparable items. 14 * @int i the position from which to percolate down. 15 * @int n the logical size of the binary heap. 16 * / 17 private static <AnyType extends Comparable<? super AnyType>> 18 void percDown( AnyType [ ] a, int i, int n ) 19 { 20 int child; 21 AnyType tmp; 22 23 for( tmp = a[ i ]; leftChild( i ) < n; i = child ) 24 { 25 child = leftChild( i ); 26 if( child != n -1 && a[ child ].compareTo( a[ child + 1 ] ) < 0 ) 27 child++; 28 if( tmp.compareTo( a[ child ] ) < 0 ) 29 a[ i ] = a[ child ]; 30 else 31 break; 32 } 33 a[ i ] = tmp; 34 } 35 36 / ** 37 * Standard heapsort. 38 * @param a an array of Comparable items. 39 * / 40 public static <AnyType extends Comparable<? super AnyType>> 41 void heapsort( AnyType [ ] a ) 42 { 43 for( int i = a.length / 2 -1; i >= 0; i--) / * buildHeap * / 44 percDown( a, i, a.length ); 45 for( int i = a.length - 1; i > 0; i--) 46 { 47 swapReferences( a, 0, i ); / * deleteMax * / 48 percDown( a, 0, i ); 49 } 50 }
```

Figure 7.8 Heapsort

Because level di has at most 2 di nodes, there are 2 di possible places that the root element can go for any di . Consequently, for any sequence D , the number of distinct corresponding deleteMax sequences is at most

<!-- formula-not-decoded -->

A simple algebraic manipulation shows that for a given sequence D

<!-- formula-not-decoded -->

Because each di can assume any value between 1 and ⌊ log N ⌋ , there are at most (log N ) N possible sequences D . It follows that the number of distinct deleteMax sequences that require cost exactly equal to M is at most the number of cost sequences of total cost M times the number of deleteMax sequences for each of these cost sequences. A bound of (log N ) N 2 M follows immediately.

The total number of heaps with cost sequence less than M is at most

<!-- formula-not-decoded -->

If we choose M = N (log N -log log N -4), then the number of heaps that have cost sequence less than M is at most ( N / 16) N , and the theorem follows from our earlier comments.

Using a more complex argument, it can be shown that heapsort always uses at least N log N -O ( N ) comparisons, and that there are inputs that can achieve this bound. The average case analysis also can be improved to 2 N log N -O ( N ) comparisons (rather than the nonlinear second term in Theorem 7.5).

## 7.6 Mergesort

We now turn our attention to mergesort . Mergesort runs in O ( N log N ) worst-case running time, and the number of comparisons used is nearly optimal. It is a fine example of a recursive algorithm.

The fundamental operation in this algorithm is merging two sorted lists. Because the lists are sorted, this can be done in one pass through the input, if the output is put in a third list. The basic merging algorithm takes two input arrays A and B , an output array C , and three counters, Actr , Bctr , and Cctr , which are initially set to the beginning of their respective arrays. The smaller of A [ Actr ] and B [ Bctr ] is copied to the next entry in C , and the appropriate counters are advanced. When either input list is exhausted, the remainder of the other list is copied to C . An example of how the merge routine works is provided for the following input.

<!-- image -->

If the array A contains 1, 13, 24, 26, and B contains 2, 15, 27, 38, then the algorithm proceeds as follows: First, a comparison is done between 1 and 2. 1 is added to C , and then 13 and 2 are compared.

<!-- image -->

2 is added to C , and then 13 and 15 are compared.

<!-- image -->

13 is added to C , and then 24 and 15 are compared. This proceeds until 26 and 27 are compared.

<!-- image -->

26 is added to C , and the A array is exhausted.

<!-- image -->

The remainder of the B array is then copied to C .

<!-- image -->

The time to merge two sorted lists is clearly linear, because at most N -1 comparisons are made, where N is the total number of elements. To see this, note that every comparison adds an element to C , except the last comparison, which adds at least two.

The mergesort algorithm is therefore easy to describe. If N = 1, there is only one element to sort, and the answer is at hand. Otherwise, recursively mergesort the first half and the second half. This gives two sorted halves, which can then be merged together using the merging algorithm described above. For instance, to sort the eight-element array 24, 13, 26, 1, 2, 27, 38, 15, we recursively sort the first four and last four elements, obtaining 1, 13, 24, 26, 2, 15, 27, 38. Then we merge the two halves as above, obtaining the final list 1, 2, 13, 15, 24, 26, 27, 38. This algorithm is a classic divide-and-conquer strategy . The problem is divided into smaller problems and solved recursively. The conquering phase consists of patching together the answers. Divide-and-conquer is a very powerful use of recursion that we will see many times.

An implementation of mergesort is provided in Figure 7.9. The public mergeSort is just a driver for the private recursive method mergeSort .

The merge routine is subtle. If a temporary array is declared locally for each recursive call of merge , then there could be log N temporary arrays active at any point. A close examination shows that since merge is the last line of mergeSort , there only needs to be one temporary array active at any point, and that the temporary array can be created in the public mergeSort driver. Further, we can use any part of the temporary array; we will use the same portion as the input array a . This allows the improvement described at the end of this section. Figure 7.10 implements the merge routine.

## 7.6.1 Analysis of Mergesort

Mergesort is a classic example of the techniques used to analyze recursive routines: we have to write a recurrence relation for the running time. We will assume that N is a power of 2, so that we always split into even halves. For N = 1, the time to mergesort is constant, which we will denote by 1. Otherwise, the time to mergesort N numbers is equal to the time to do two recursive mergesorts of size N / 2, plus the time to merge, which is linear. The following equations say this exactly:

<!-- formula-not-decoded -->

This is a standard recurrence relation, which can be solved several ways. We will show two methods. The first idea is to divide the recurrence relation through by N . The reason for doing this will become apparent soon. This yields

<!-- formula-not-decoded -->

```
1 / ** 2 * Internal method that makes recursive calls. 3 * @param a an array of Comparable items. 4 * @param tmpArray an array to place the merged result. 5 * @param left the left-most index of the subarray. 6 * @param right the right-most index of the subarray. 7 * / 8 private static <AnyType extends Comparable<? super AnyType>> 9 void mergeSort( AnyType [ ] a, AnyType [ ] tmpArray, int left, int right ) 10 { 11 if( left < right ) 12 { 13 int center = ( left + right ) / 2; 14 mergeSort( a, tmpArray, left, center ); 15 mergeSort( a, tmpArray, center + 1, right ); 16 merge( a, tmpArray, left, center + 1, right ); 17 } 18 } 19 20 / ** 21 * Mergesort algorithm. 22 * @param a an array of Comparable items. 23 * / 24 public static <AnyType extends Comparable<? super AnyType>> 25 void mergeSort( AnyType [ ] a ) 26 { 27 AnyType [ ] tmpArray = (AnyType[]) new Comparable[ a.length ]; 28 29 mergeSort( a, tmpArray, 0, a.length -1 ); 30 }
```

Figure 7.9 Mergesort routines

This equation is valid for any N that is a power of 2, so we may also write

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and

```
1 / ** 2 * Internal method that merges two sorted halves of a subarray. 3 * @param a an array of Comparable items. 4 * @param tmpArray an array to place the merged result. 5 * @param leftPos the left-most index of the subarray. 6 * @param rightPos the index of the start of the second half. 7 * @param rightEnd the right-most index of the subarray. 8 * / 9 private static <AnyType extends Comparable<? super AnyType>> 10 void merge( AnyType [ ] a, AnyType [ ] tmpArray, 11 int leftPos, int rightPos, int rightEnd ) 12 { 13 int leftEnd = rightPos -1; 14 int tmpPos = leftPos; 15 int numElements = rightEnd -leftPos + 1; 16 17 // Main loop 18 while( leftPos <= leftEnd && rightPos <= rightEnd ) 19 if( a[ leftPos ].compareTo( a[ rightPos ] ) <= 0 ) 20 tmpArray[ tmpPos++ ] = a[ leftPos++ ]; 21 else 22 tmpArray[ tmpPos++ ] = a[ rightPos++ ]; 23 24 while( leftPos <= leftEnd ) // Copy rest of first half 25 tmpArray[ tmpPos++ ] = a[ leftPos++ ]; 26 27 while( rightPos <= rightEnd ) // Copy rest of right half 28 tmpArray[ tmpPos++ ] = a[ rightPos++ ]; 29 30 // Copy tmpArray back 31 for( int i = 0; i < numElements; i++, rightEnd--) 32 a[ rightEnd ] = tmpArray[ rightEnd ]; 33 }
```

Figure 7.10 merge routine

Now add up all the equations. This means that we add all of the terms on the left-hand side and set the result equal to the sum of all of the terms on the right-hand side. Observe that the term T ( N / 2) / ( N / 2) appears on both sides and thus cancels. In fact, virtually all the terms appear on both sides and cancel. This is called telescoping a sum. After everything is added, the final result is

<!-- formula-not-decoded -->

because all of the other terms cancel and there are log N equations, and so all the 1's at the end of these equations add up to log N . Multiplying through by N gives the final answer.

<!-- formula-not-decoded -->

Notice that if we did not divide through by N at the start of the solutions, the sum would not telescope. This is why it was necessary to divide through by N .

An alternative method is to substitute the recurrence relation continually on the righthand side. We have

<!-- formula-not-decoded -->

Since we can substitute N / 2 into the main equation,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Again, by substituting N / 4 into the main equation, we see that

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Continuing in this manner, we obtain

<!-- formula-not-decoded -->

we have

So we have

Using k = log N , we obtain

<!-- formula-not-decoded -->

The choice of which method to use is a matter of taste. The first method tends to produce scrap work that fits better on a standard, 8 1 / 2 × 11 sheet of paper, leading to fewer mathematical errors, but it requires a certain amount of experience to apply . The second method is more of a brute-force approach.

Recall that we have assumed N = 2 k . The analysis can be refined to handle cases when N is not a power of 2. The answer turns out to be almost identical (this is usually the case).

Although mergesort's running time is O ( N log N ), it has the significant problem that merging two sorted lists uses linear extra memory . 1 The additional work involved in copying to the temporary array and back, throughout the algorithm, slows the sort considerably . This copying can be avoided by judiciously switching the roles of a and tmpArray at alternate levels of the recursion. A variant of mergesort can also be implemented nonrecursively (Exercise 7.16).

1 It is theoretically possible to use less extra memory , but the resulting algorithm is complex and impractical.

The running time of mergesort, when compared with other O ( N log N ) alternatives, depends heavily on the relative costs of comparing elements and moving elements in the array (and the temporary array). These costs are language dependent.

For instance, in Java, when performing a generic sort (using a Comparator ), an element comparison can be expensive (because comparisons might not be easily inlined, and thus the overhead of dynamic dispatch could slow things down), but moving elements is cheap (because they are reference assignments, rather than copies of large objects). Mergesort uses the lowest number of comparisons of all the popular sorting algorithms, and thus is a good candidate for general-purpose sorting in Java. In fact, it is the algorithm used in the standard Java library for generic sorting.

On the other hand, in C++, in a generic sort, copying objects can be expensive if the objects are large, while comparing objects often is relatively cheap because of the ability of the compiler to aggressively perform inline optimization. In this scenario, it might be reasonable to have an algorithm use a few more comparisons, if we can also use significantly fewer data movements. Quicksort, which we discuss in the next section, achieves this tradeoff, and is the sorting routine commonly used in C++ libraries.

In Java, quicksort is also used as the standard library sort for primitive types. Here, the costs of comparisons and data moves are similar, so using significantly fewer data movements more than compensates for a few extra comparisons.

## 7.7 Quicksort

As its name implies, quicksort is a fast sorting algorithm in practice and is especially useful in C++, or for sorting primitive types in Java. Its average running time is O ( N log N ). It is very fast, mainly due to a very tight and highly optimized inner loop. It has O ( N 2 ) worst-case performance, but this can be made exponentially unlikely with a little effort. By combining quicksort with heapsort, we can achieve quicksort's fast running time on almost all inputs, with heapsort's O ( N log N ) worst-case running time. Exercise 7.27 describes this approach.

The quicksort algorithm is simple to understand and prove correct, although for many years it had the reputation of being an algorithm that could in theory be highly optimized but in practice was impossible to code correctly . Like mergesort, quicksort is a divide-andconquer recursive algorithm.

Let us begin with the following simple sorting algorithm to sort a list. Arbitrarily choose any item, and then form three groups: those smaller than the chosen item, those equal to the chosen item, and those larger than the chosen item. Recursively sort the first and third groups, and then concatenate the three groups. The result is guaranteed by the basic principles of recursion to be a sorted arrangement of the original list. A direct implementation of this algorithm is shown in Figure 7.11, and its performance, is generally speaking, quite respectable on most inputs. In fact, if the list contains large numbers of duplicates with relatively few distinct items, as is sometimes the case, then the performance is extremely good.

The algorithm we have described forms the basis of the quicksort. However, by making the extra lists, and doing so recursively , it is hard to see how we have improved upon