# Single Neuron

This trivial neuron example illustrates using gradiant descent to
learn a neural weight that will yield a goal of 0.8 when it sees an
input "somewhere near" 0.5. 

This stupid example illustrates a single neuron configuring a weight
that will yield a stipulated goal.


## Log of Learning Run

```
1. Prediction 988.8170586343342 using weight 1483.6255879515013. Seeking goal 0.8
2. Prediction 741.8127939757507 using weight 1113.119190963626. Seeking goal 0.8
3. Prediction 556.559595481813 using weight 835.2393932227194. Seeking goal 0.8
4. Prediction 417.6196966113597 using weight 626.8295449170396. Seeking goal 0.8
5. Prediction 313.4147724585198 using weight 470.52215868777967. Seeking goal 0.8
6. Prediction 235.26107934388983 using weight 353.2916190158347. Seeking goal 0.8
7. Prediction 176.64580950791736 using weight 265.36871426187605. Seeking goal 0.8
8. Prediction 132.68435713093803 using weight 199.42653569640703. Seeking goal 0.8
9. Prediction 99.71326784820351 using weight 149.96990177230526. Seeking goal 0.8
10. Prediction 74.98495088615263 using weight 112.87742632922894. Seeking goal 0.8
11. Prediction 56.43871316461447 using weight 85.0580697469217. Seeking goal 0.8
12. Prediction 42.52903487346085 using weight 64.19355231019128. Seeking goal 0.8
13. Prediction 32.09677615509564 using weight 48.54516423264346. Seeking goal 0.8
14. Prediction 24.27258211632173 using weight 36.80887317448259. Seeking goal 0.8
15. Prediction 18.404436587241296 using weight 28.006654880861944. Seeking goal 0.8
16. Prediction 14.003327440430972 using weight 21.40499116064646. Seeking goal 0.8
17. Prediction 10.70249558032323 using weight 16.453743370484844. Seeking goal 0.8
18. Prediction 8.226871685242422 using weight 12.740307527863633. Seeking goal 0.8
19. Prediction 6.370153763931817 using weight 9.955230645897725. Seeking goal 0.8
20. Prediction 4.977615322948862 using weight 7.866422984423293. Seeking goal 0.8
21. Prediction 3.9332114922116466 using weight 6.29981723831747. Seeking goal 0.8
22. Prediction 3.149908619158735 using weight 5.124862928738102. Seeking goal 0.8
23. Prediction 2.562431464369051 using weight 4.243647196553576. Seeking goal 0.8
24. Prediction 2.121823598276788 using weight 3.582735397415182. Seeking goal 0.8
25. Prediction 1.791367698707591 using weight 3.0870515480613867. Seeking goal 0.8
26. Prediction 1.5435257740306934 using weight 2.7152886610460403. Seeking goal 0.8
27. Prediction 1.3576443305230201 using weight 2.43646649578453. Seeking goal 0.8
28. Prediction 1.218233247892265 using weight 2.2273498718383977. Seeking goal 0.8
29. Prediction 1.1136749359191989 using weight 2.0705124038787983. Seeking goal 0.8
30. Prediction 1.0352562019393992 using weight 1.9528843029090988. Seeking goal 0.8
31. Prediction 0.9764421514545494 using weight 1.8646632271818242. Seeking goal 0.8
32. Prediction 0.9323316135909121 using weight 1.7984974203863682. Seeking goal 0.8
33. Prediction 0.8992487101931841 using weight 1.7488730652897762. Seeking goal 0.8
34. Prediction 0.8744365326448881 using weight 1.711654798967332. Seeking goal 0.8
35. Prediction 0.855827399483666 using weight 1.683741099225499. Seeking goal 0.8
36. Prediction 0.8418705496127495 using weight 1.6628058244191244. Seeking goal 0.8
37. Prediction 0.8314029122095622 using weight 1.6471043683143434. Seeking goal 0.8
38. Prediction 0.8235521841571717 using weight 1.6353282762357575. Seeking goal 0.8
39. Prediction 0.8176641381178787 using weight 1.626496207176818. Seeking goal 0.8
40. Prediction 0.813248103588409 using weight 1.6198721553826136. Seeking goal 0.8
41. Prediction 0.8099360776913068 using weight 1.6149041165369602. Seeking goal 0.8
42. Prediction 0.8074520582684801 using weight 1.6111780874027202. Seeking goal 0.8
43. Prediction 0.8055890437013601 using weight 1.6083835655520402. Seeking goal 0.8
44. Prediction 0.8041917827760201 using weight 1.6062876741640302. Seeking goal 0.8
45. Prediction 0.8031438370820151 using weight 1.6047157556230227. Seeking goal 0.8
46. Prediction 0.8023578778115114 using weight 1.603536816717267. Seeking goal 0.8
47. Prediction 0.8017684083586335 using weight 1.6026526125379503. Seeking goal 0.8
48. Prediction 0.8013263062689752 using weight 1.6019894594034627. Seeking goal 0.8
49. Prediction 0.8009947297017314 using weight 1.601492094552597. Seeking goal 0.8
50. Prediction 0.8007460472762985 using weight 1.6011190709144478. Seeking goal 0.8
51. Prediction 0.8005595354572239 using weight 1.600839303185836. Seeking goal 0.8
52. Prediction 0.800419651592918 using weight 1.600629477389377. Seeking goal 0.8
53. Prediction 0.8003147386946885 using weight 1.6004721080420328. Seeking goal 0.8
54. Prediction 0.8002360540210164 using weight 1.6003540810315247. Seeking goal 0.8
55. Prediction 0.8001770405157623 using weight 1.6002655607736436. Seeking goal 0.8
56. Prediction 0.8001327803868218 using weight 1.6001991705802328. Seeking goal 0.8
57. Prediction 0.8000995852901164 using weight 1.6001493779351745. Seeking goal 0.8
58. Prediction 0.8000746889675873 using weight 1.600112033451381. Seeking goal 0.8
59. Prediction 0.8000560167256905 using weight 1.6000840250885358. Seeking goal 0.8
60. Prediction 0.8000420125442679 using weight 1.6000630188164018. Seeking goal 0.8
61. Prediction 0.8000315094082009 using weight 1.6000472641123014. Seeking goal 0.8
62. Prediction 0.8000236320561507 using weight 1.600035448084226. Seeking goal 0.8
63. Prediction 0.800017724042113 using weight 1.6000265860631695. Seeking goal 0.8
64. Prediction 0.8000132930315847 using weight 1.600019939547377. Seeking goal 0.8
65. Prediction 0.8000099697736885 using weight 1.600014954660533. Seeking goal 0.8
66. Prediction 0.8000074773302664 using weight 1.6000112159953996. Seeking goal 0.8
67. Prediction 0.8000056079976998 using weight 1.6000084119965496. Seeking goal 0.8
68. Prediction 0.8000042059982748 using weight 1.6000063089974121. Seeking goal 0.8
69. Prediction 0.8000031544987061 using weight 1.6000047317480592. Seeking goal 0.8
70. Prediction 0.8000023658740296 using weight 1.6000035488110445. Seeking goal 0.8
71. Prediction 0.8000017744055222 using weight 1.6000026616082834. Seeking goal 0.8
72. Prediction 0.8000013308041417 using weight 1.6000019962062126. Seeking goal 0.8
73. Prediction 0.8000009981031063 using weight 1.6000014971546594. Seeking goal 0.8
74. Prediction 0.8000007485773297 using weight 1.6000011228659945. Seeking goal 0.8
75. Prediction 0.8000005614329972 using weight 1.600000842149496. Seeking goal 0.8
76. Prediction 0.800000421074748 using weight 1.600000631612122. Seeking goal 0.8
77. Prediction 0.800000315806061 using weight 1.6000004737090916. Seeking goal 0.8
78. Prediction 0.8000002368545458 using weight 1.6000003552818187. Seeking goal 0.8
79. Prediction 0.8000001776409094 using weight 1.6000002664613642. Seeking goal 0.8
80. Prediction 0.8000001332306821 using weight 1.6000001998460232. Seeking goal 0.8
81. Prediction 0.8000000999230116 using weight 1.6000001498845173. Seeking goal 0.8
82. Prediction 0.8000000749422587 using weight 1.600000112413388. Seeking goal 0.8
83. Prediction 0.800000056206694 using weight 1.600000084310041. Seeking goal 0.8
84. Prediction 0.8000000421550205 using weight 1.6000000632325309. Seeking goal 0.8
85. Prediction 0.8000000316162654 using weight 1.6000000474243983. Seeking goal 0.8
86. Prediction 0.8000000237121991 using weight 1.6000000355682986. Seeking goal 0.8
87. Prediction 0.8000000177841493 using weight 1.600000026676224. Seeking goal 0.8
88. Prediction 0.800000013338112 using weight 1.600000020007168. Seeking goal 0.8
89. Prediction 0.800000010003584 using weight 1.6000000150053761. Seeking goal 0.8
90. Prediction 0.8000000075026881 using weight 1.600000011254032. Seeking goal 0.8
91. Prediction 0.800000005627016 using weight 1.600000008440524. Seeking goal 0.8
92. Prediction 0.800000004220262 using weight 1.600000006330393. Seeking goal 0.8
93. Prediction 0.8000000031651965 using weight 1.6000000047477947. Seeking goal 0.8
94. Prediction 0.8000000023738973 using weight 1.600000003560846. Seeking goal 0.8
95. Prediction 0.800000001780423 using weight 1.6000000026706345. Seeking goal 0.8
96. Prediction 0.8000000013353172 using weight 1.6000000020029759. Seeking goal 0.8
97. Prediction 0.8000000010014879 using weight 1.600000001502232. Seeking goal 0.8
98. Prediction 0.800000000751116 using weight 1.600000001126674. Seeking goal 0.8
99. Prediction 0.800000000563337 using weight 1.6000000008450055. Seeking goal 0.8
100. Prediction 0.8000000004225027 using weight 1.600000000633754. Seeking goal 0.8
101. Prediction 0.800000000316877 using weight 1.6000000004753154. Seeking goal 0.8
102. Prediction 0.8000000002376577 using weight 1.6000000003564865. Seeking goal 0.8
103. Prediction 0.8000000001782432 using weight 1.6000000002673649. Seeking goal 0.8
104. Prediction 0.8000000001336824 using weight 1.6000000002005237. Seeking goal 0.8
105. Prediction 0.8000000001002618 using weight 1.6000000001503927. Seeking goal 0.8
106. Prediction 0.8000000000751963 using weight 1.6000000001127945. Seeking goal 0.8
107. Prediction 0.8000000000563973 using weight 1.600000000084596. Seeking goal 0.8
108. Prediction 0.800000000042298 using weight 1.6000000000634471. Seeking goal 0.8
109. Prediction 0.8000000000317236 using weight 1.6000000000475854. Seeking goal 0.8
110. Prediction 0.8000000000237927 using weight 1.600000000035689. Seeking goal 0.8
111. Prediction 0.8000000000178445 using weight 1.600000000026767. Seeking goal 0.8
112. Prediction 0.8000000000133834 using weight 1.6000000000200751. Seeking goal 0.8
113. Prediction 0.8000000000100376 using weight 1.6000000000150565. Seeking goal 0.8
114. Prediction 0.8000000000075282 using weight 1.6000000000112924. Seeking goal 0.8
115. Prediction 0.8000000000056462 using weight 1.6000000000084693. Seeking goal 0.8
116. Prediction 0.8000000000042347 using weight 1.600000000006352. Seeking goal 0.8
117. Prediction 0.800000000003176 using weight 1.6000000000047638. Seeking goal 0.8
118. Prediction 0.8000000000023819 using weight 1.6000000000035728. Seeking goal 0.8
119. Prediction 0.8000000000017864 using weight 1.6000000000026797. Seeking goal 0.8
120. Prediction 0.8000000000013399 using weight 1.6000000000020098. Seeking goal 0.8
121. Prediction 0.8000000000010049 using weight 1.6000000000015073. Seeking goal 0.8
122. Prediction 0.8000000000007537 using weight 1.6000000000011305. Seeking goal 0.8
123. Prediction 0.8000000000005653 using weight 1.6000000000008479. Seeking goal 0.8
124. Prediction 0.8000000000004239 using weight 1.600000000000636. Seeking goal 0.8
125. Prediction 0.800000000000318 using weight 1.600000000000477. Seeking goal 0.8
126. Prediction 0.8000000000002385 using weight 1.6000000000003578. Seeking goal 0.8
Initial weight: 1977.6341172686684
Learned weight: 1.6000000000003578

Use it: request outputs as function of fuzzy neural inputs
1. Prediction 0.7680000000001718 from input 0.48
2. Prediction 0.7760000000001736 from input 0.485
3. Prediction 0.7840000000001753 from input 0.49
4. Prediction 0.7920000000001771 from input 0.495
5. Prediction 0.8000000000001789 from input 0.5
6. Prediction 0.8800000000001968 from input 0.55
7. Prediction 0.8160000000001825 from input 0.51
8. Prediction 0.8240000000001843 from input 0.515
```