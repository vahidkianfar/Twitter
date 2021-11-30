This Project contains various features for Social Network Analysis on Twitter.

-Creating a recommendation graph:

	1. Open "grabData_for_Graph.py"
	2. Put your username on screen_name
	3. Don't touch credentials (the tokens are valid)
	<!--- please read the comments before proceeding to the next step--->
	<!---Step 4 running time depends on amout of friends! maybe it takes up to 20 hours to finish (limitations of twitter's API)-->
	<!---but you can change setting to speed-up the process, for example: Line 67, you can reduce the friends_count-->
	<!---for skiping this part, I put the folder, including all .json files, in my project-->
	4. Run the file and wait until it is finished. <!--- you can skip this step if you wish--->
	5. Open "Graph.py"
	6. Note: screen_name in both files should be the same
	7. Run the "Graph.py"
	8. "screen_name".png is the final graph.

-Analyzing Tweets:

1. Open "Project.ipynb" in Google Colab or Jupyter Notbook.
2. Enter Username <!---this project only work on usernames with ENGLISH Language-->
3. Upload "emotions.txt" on your directory <!---for custom sentiment analysis based on Lexicons-->
4. select "Run All" and wait until its finished.
5. it takes at least 45 minutes to run all cells.
