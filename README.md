This is the traveller salesman problem. My goal in this small project was to try an calculate what is the route with the minimum distance that allows a travelling salesman starting in Madrid, Spain to travel
through all the capital cities in Europe and back to Madrid, Spain.

tspfrommadrid
Initially, in the file tspfrommadrid I calculate the closest city to Madrid which is Andorra. The salesman will travel to this city and then Andorra is removed from the list of potential cities from which the salesman can
travel. The closest city to Andorra is then calculated and the salesman travellers to the next closest city. This is repeated until the salesman has travelled to all the capital cities in Europe. The salesman the returns home.
The chosen route and then the total distance to travel this route is returned by the program.

tspbeststartingcity
The program tspbeststartingcity runs a loop to repeat the program explained in tspfrommadrid, however each time it repeats the above program it changes the starting city. It does this for every city in europe. It then 
calculates the starting city from which the shortest route is create. The resulting city is reykjavik, Iceland. This process makes sense as the outputted route is a circle. This the salesman travelling from Madrid, Spain can start
in Madrid, but still travel the exact same route that was outputted by the program when the salesman starts in Reykjavik, Iceland.

tspfromiceland
This program is the same as tspfrommadrid, however it outputs the route and total distance travelled outputted from the program starting from Iceland i.e. the most efficient route. The sales man starting from Madrid would then
travel along the same route i.e. circle.
