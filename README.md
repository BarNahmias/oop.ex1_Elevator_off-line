###    oop.ex1_Elevator_off-line    

#     Off-line Algorithms for the Elevator                ![This is an image](https://upload.wikimedia.org/wikipedia/commons/3/34/Elevator_icon_arrows.svg)   

Bar-Nahmias & Oriya-Zadok 



## introduction:
- youtube : This site was built using [youtube Pages](https://pages.github.com/).
- web : This site was built using [Elevator Pages](https://studylib.net/doc/7878746/on-line-algorithms-versus-off-line-algorithms-for-the-ele).
- code : This site was built using [code Pages](https://pages.github.com/).

## Off-line --- On-line Algorithms for the Elevator:
Motivation: In most scheduling problems, if the problem were off-line, i.e. we know the arrival time of a request, then we can find the optimal schedule. But in reality this is not the case and we need to use some heuristics or strategies or on-line algorithms for scheduling.  The question is which strategy is better.[^1] 
[^1]:https://studylib.net/doc/7878746/on-line-algorithms-versus-off-line-algorithms-for-the-ele

## my Off-line Algorithm  -  Optimal response for requests:  
1. Set a division parameter according to time units 
- partition = (time of last call - time of first call) / amount of all the calls
-Sort the readings according to division parameter
2. Dividing the status of requests into two groups
- group A : up calls
- group B : down calls
3. Matching a request to an elevator
4. Order to the elevator 
- According to the request
5. Send
6. Repit

## Design: 


![image](https://user-images.githubusercontent.com/92825016/142480602-95f89818-dbb8-470d-b9a2-da760b64caa8.png)







![image](https://user-images.githubusercontent.com/92825016/142415318-cec28474-605a-4d53-8409-8bd0161590d1.png)


## unitest 
We will compare the results of off line to an online algorithm, due to the differences we made between the algorithms we would expect off line algorithm to give a more optimal result compared to the online algorithm





