# Single Neuron

This trivial neuron example illustrates using gradiant descent to
learn a neural weight that will yield a goal of 0.8 when it sees an
input "somewhere near" 0.5. 

This silly example illustrates a single neuron configuring a weight
that will yield a stipulated goal.


## Log of Learning Run

```
1. Prediction 1010.0511078835278 using weight 1515.4766618252918. Seeking goal 0.8
2. Prediction 757.7383309126459 using weight 1137.0074963689688. Seeking goal 0.8
3. Prediction 568.5037481844844 using weight 853.1556222767265. Seeking goal 0.8
4. Prediction 426.57781113836324 using weight 640.2667167075449. Seeking goal 0.8
5. Prediction 320.13335835377245 using weight 480.6000375306587. Seeking goal 0.8
6. Prediction 240.30001876532936 using weight 360.85002814799407. Seeking goal 0.8
7. Prediction 180.42501407399703 using weight 271.03752111099556. Seeking goal 0.8
8. Prediction 135.51876055549778 using weight 203.6781408332467. Seeking goal 0.8
9. Prediction 101.83907041662334 using weight 153.158605624935. Seeking goal 0.8
10. Prediction 76.5793028124675 using weight 115.26895421870125. Seeking goal 0.8
11. Prediction 57.63447710935063 using weight 86.85171566402593. Seeking goal 0.8
12. Prediction 43.425857832012966 using weight 65.53878674801945. Seeking goal 0.8
13. Prediction 32.769393374009724 using weight 49.554090061014584. Seeking goal 0.8
14. Prediction 24.777045030507292 using weight 37.56556754576094. Seeking goal 0.8
15. Prediction 18.78278377288047 using weight 28.57417565932071. Seeking goal 0.8
16. Prediction 14.287087829660354 using weight 21.830631744490532. Seeking goal 0.8
17. Prediction 10.915315872245266 using weight 16.7729738083679. Seeking goal 0.8
18. Prediction 8.38648690418395 using weight 12.979730356275926. Seeking goal 0.8
19. Prediction 6.489865178137963 using weight 10.134797767206944. Seeking goal 0.8
20. Prediction 5.067398883603472 using weight 8.001098325405207. Seeking goal 0.8
21. Prediction 4.000549162702604 using weight 6.4008237440539055. Seeking goal 0.8
22. Prediction 3.2004118720269528 using weight 5.200617808040429. Seeking goal 0.8
23. Prediction 2.6003089040202143 using weight 4.300463356030321. Seeking goal 0.8
24. Prediction 2.1502316780151607 using weight 3.625347517022741. Seeking goal 0.8
25. Prediction 1.8126737585113706 using weight 3.119010637767056. Seeking goal 0.8
26. Prediction 1.559505318883528 using weight 2.739257978325292. Seeking goal 0.8
27. Prediction 1.369628989162646 using weight 2.4544434837439693. Seeking goal 0.8
28. Prediction 1.2272217418719846 using weight 2.240832612807977. Seeking goal 0.8
29. Prediction 1.1204163064039885 using weight 2.080624459605983. Seeking goal 0.8
30. Prediction 1.0403122298029914 using weight 1.9604683447044873. Seeking goal 0.8
31. Prediction 0.9802341723522436 using weight 1.8703512585283655. Seeking goal 0.8
32. Prediction 0.9351756292641827 using weight 1.802763443896274. Seeking goal 0.8
33. Prediction 0.901381721948137 using weight 1.7520725829222057. Seeking goal 0.8
34. Prediction 0.8760362914611028 using weight 1.7140544371916544. Seeking goal 0.8
35. Prediction 0.8570272185958272 using weight 1.6855408278937407. Seeking goal 0.8
36. Prediction 0.8427704139468704 using weight 1.6641556209203054. Seeking goal 0.8
37. Prediction 0.8320778104601527 using weight 1.6481167156902292. Seeking goal 0.8
38. Prediction 0.8240583578451146 using weight 1.636087536767672. Seeking goal 0.8
39. Prediction 0.818043768383836 using weight 1.6270656525757539. Seeking goal 0.8
40. Prediction 0.8135328262878769 using weight 1.6202992394318154. Seeking goal 0.8
41. Prediction 0.8101496197159077 using weight 1.6152244295738616. Seeking goal 0.8
42. Prediction 0.8076122147869308 using weight 1.6114183221803962. Seeking goal 0.8
43. Prediction 0.8057091610901981 using weight 1.6085637416352971. Seeking goal 0.8
44. Prediction 0.8042818708176486 using weight 1.606422806226473. Seeking goal 0.8
45. Prediction 0.8032114031132365 using weight 1.6048171046698547. Seeking goal 0.8
46. Prediction 0.8024085523349274 using weight 1.6036128285023912. Seeking goal 0.8
47. Prediction 0.8018064142511956 using weight 1.6027096213767935. Seeking goal 0.8
48. Prediction 0.8013548106883968 using weight 1.6020322160325953. Seeking goal 0.8
49. Prediction 0.8010161080162976 using weight 1.6015241620244465. Seeking goal 0.8
50. Prediction 0.8007620810122232 using weight 1.601143121518335. Seeking goal 0.8
51. Prediction 0.8005715607591675 using weight 1.6008573411387512. Seeking goal 0.8
52. Prediction 0.8004286705693756 using weight 1.6006430058540635. Seeking goal 0.8
53. Prediction 0.8003215029270317 using weight 1.6004822543905477. Seeking goal 0.8
54. Prediction 0.8002411271952738 using weight 1.6003616907929108. Seeking goal 0.8
55. Prediction 0.8001808453964554 using weight 1.6002712680946831. Seeking goal 0.8
56. Prediction 0.8001356340473416 using weight 1.6002034510710124. Seeking goal 0.8
57. Prediction 0.8001017255355062 using weight 1.6001525883032592. Seeking goal 0.8
58. Prediction 0.8000762941516296 using weight 1.6001144412274444. Seeking goal 0.8
59. Prediction 0.8000572206137222 using weight 1.6000858309205834. Seeking goal 0.8
60. Prediction 0.8000429154602917 using weight 1.6000643731904376. Seeking goal 0.8
61. Prediction 0.8000321865952188 using weight 1.6000482798928282. Seeking goal 0.8
62. Prediction 0.8000241399464141 using weight 1.600036209919621. Seeking goal 0.8
63. Prediction 0.8000181049598105 using weight 1.6000271574397158. Seeking goal 0.8
64. Prediction 0.8000135787198579 using weight 1.6000203680797869. Seeking goal 0.8
65. Prediction 0.8000101840398934 using weight 1.6000152760598403. Seeking goal 0.8
66. Prediction 0.8000076380299201 using weight 1.6000114570448802. Seeking goal 0.8
67. Prediction 0.8000057285224401 using weight 1.6000085927836603. Seeking goal 0.8
68. Prediction 0.8000042963918301 using weight 1.6000064445877453. Seeking goal 0.8
69. Prediction 0.8000032222938727 using weight 1.600004833440809. Seeking goal 0.8
70. Prediction 0.8000024167204045 using weight 1.600003625080607. Seeking goal 0.8
71. Prediction 0.8000018125403034 using weight 1.600002718810455. Seeking goal 0.8
72. Prediction 0.8000013594052275 using weight 1.6000020391078413. Seeking goal 0.8
73. Prediction 0.8000010195539207 using weight 1.6000015293308811. Seeking goal 0.8
74. Prediction 0.8000007646654406 using weight 1.600001146998161. Seeking goal 0.8
75. Prediction 0.8000005734990805 using weight 1.6000008602486209. Seeking goal 0.8
76. Prediction 0.8000004301243104 using weight 1.6000006451864657. Seeking goal 0.8
77. Prediction 0.8000003225932328 using weight 1.6000004838898492. Seeking goal 0.8
78. Prediction 0.8000002419449246 using weight 1.600000362917387. Seeking goal 0.8
79. Prediction 0.8000001814586934 using weight 1.6000002721880402. Seeking goal 0.8
80. Prediction 0.8000001360940201 using weight 1.6000002041410302. Seeking goal 0.8
81. Prediction 0.8000001020705151 using weight 1.6000001531057726. Seeking goal 0.8
82. Prediction 0.8000000765528863 using weight 1.6000001148293295. Seeking goal 0.8
83. Prediction 0.8000000574146647 using weight 1.6000000861219972. Seeking goal 0.8
84. Prediction 0.8000000430609986 using weight 1.600000064591498. Seeking goal 0.8
85. Prediction 0.800000032295749 using weight 1.6000000484436234. Seeking goal 0.8
86. Prediction 0.8000000242218117 using weight 1.6000000363327176. Seeking goal 0.8
87. Prediction 0.8000000181663588 using weight 1.6000000272495383. Seeking goal 0.8
88. Prediction 0.8000000136247691 using weight 1.6000000204371538. Seeking goal 0.8
89. Prediction 0.8000000102185769 using weight 1.6000000153278653. Seeking goal 0.8
90. Prediction 0.8000000076639326 using weight 1.600000011495899. Seeking goal 0.8
91. Prediction 0.8000000057479495 using weight 1.6000000086219242. Seeking goal 0.8
92. Prediction 0.8000000043109621 using weight 1.600000006466443. Seeking goal 0.8
93. Prediction 0.8000000032332215 using weight 1.6000000048498322. Seeking goal 0.8
94. Prediction 0.8000000024249161 using weight 1.600000003637374. Seeking goal 0.8
95. Prediction 0.800000001818687 using weight 1.6000000027280306. Seeking goal 0.8
96. Prediction 0.8000000013640153 using weight 1.600000002046023. Seeking goal 0.8
97. Prediction 0.8000000010230115 using weight 1.6000000015345173. Seeking goal 0.8
98. Prediction 0.8000000007672586 using weight 1.600000001150888. Seeking goal 0.8
99. Prediction 0.800000000575444 using weight 1.600000000863166. Seeking goal 0.8
100. Prediction 0.800000000431583 using weight 1.6000000006473747. Seeking goal 0.8
101. Prediction 0.8000000003236873 using weight 1.600000000485531. Seeking goal 0.8
102. Prediction 0.8000000002427655 using weight 1.6000000003641484. Seeking goal 0.8
103. Prediction 0.8000000001820742 using weight 1.6000000002731114. Seeking goal 0.8
104. Prediction 0.8000000001365557 using weight 1.6000000002048336. Seeking goal 0.8
105. Prediction 0.8000000001024168 using weight 1.6000000001536252. Seeking goal 0.8
106. Prediction 0.8000000000768126 using weight 1.600000000115219. Seeking goal 0.8
107. Prediction 0.8000000000576095 using weight 1.6000000000864143. Seeking goal 0.8
108. Prediction 0.8000000000432071 using weight 1.6000000000648107. Seeking goal 0.8
109. Prediction 0.8000000000324053 using weight 1.600000000048608. Seeking goal 0.8
110. Prediction 0.800000000024304 using weight 1.600000000036456. Seeking goal 0.8
111. Prediction 0.800000000018228 using weight 1.600000000027342. Seeking goal 0.8
112. Prediction 0.800000000013671 using weight 1.6000000000205066. Seeking goal 0.8
113. Prediction 0.8000000000102533 using weight 1.60000000001538. Seeking goal 0.8
114. Prediction 0.80000000000769 using weight 1.600000000011535. Seeking goal 0.8
115. Prediction 0.8000000000057675 using weight 1.6000000000086514. Seeking goal 0.8
116. Prediction 0.8000000000043257 using weight 1.6000000000064887. Seeking goal 0.8
117. Prediction 0.8000000000032443 using weight 1.6000000000048664. Seeking goal 0.8
118. Prediction 0.8000000000024332 using weight 1.6000000000036498. Seeking goal 0.8
119. Prediction 0.8000000000018249 using weight 1.6000000000027375. Seeking goal 0.8
120. Prediction 0.8000000000013687 using weight 1.6000000000020531. Seeking goal 0.8
121. Prediction 0.8000000000010266 using weight 1.6000000000015397. Seeking goal 0.8
122. Prediction 0.8000000000007699 using weight 1.6000000000011547. Seeking goal 0.8
123. Prediction 0.8000000000005774 using weight 1.600000000000866. Seeking goal 0.8
124. Prediction 0.800000000000433 using weight 1.6000000000006496. Seeking goal 0.8
125. Prediction 0.8000000000003248 using weight 1.6000000000004873. Seeking goal 0.8
126. Prediction 0.8000000000002436 using weight 1.6000000000003656. Seeking goal 0.8
Initial weight: 2020.1022157670557
Learned weight: 1.6000000000003656

Use it: request outputs as function of fuzzy neural inputs
1. Prediction 1.440000000000329 from input 0.9
2. Prediction 3.5200000000008047 from input 2.2
3. Prediction -16.000000000003656 from input -10.0
4. Prediction 0.7680000000001754 from input 0.48
5. Prediction 0.7760000000001773 from input 0.485
6. Prediction 0.7840000000001791 from input 0.49
7. Prediction 0.792000000000181 from input 0.495
8. Prediction 0.8000000000001828 from input 0.5
9. Prediction 0.8800000000002012 from input 0.55
10. Prediction 0.8160000000001865 from input 0.51
11. Prediction 0.8240000000001882 from input 0.515
```