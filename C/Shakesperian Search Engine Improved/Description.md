# A Compleat Serch Engyne

**Due Thursday, May 10, at 11:59 PM**.

**You may work with a partner on this project**.

## Description

You've built the local Java version of the Shakespearean search engine. Now move it to the web!

Use the Spring Boot framework to create a search engine application with a web front end and Java back end.

- a user will type a query into a box on the front end and press a submit button

- this action triggers an `XMLHttpRequest` to the server, with the query as its parameter

- the server receives the query, performs a lookup in its index data structure, and returns the search results back to the front end

Note that you should construct the index **ONE TIME** when the server starts. Your query method must be `O(log N)` (if you're using a 
tree-based map) or `O(1)` (if you're using a hash map). Do not open or scan any files in the server's query method; use only the pre-built index.

## One New Feature

If you complete working engine with HTML front end and Spring back end, you'll receive 90 points. To get the last 10 points, you must
add one **one new significant feature** to the system.

You have broad freedom to pick your own feature, but here are a few ideas:

- the ability to filter the search based on some criterion

- the ability to control which fields are printed in the results

- the ability to search on multiple words and return only lines that contain all of the query words

Any of these would be awesome, but you can also come up with your own idea.

A good feature will require you to make at least small changes to both the front end and the back end of the system.


## Guidelines

I've given you a basic directory structure, the `mvnw` build tool, and its `pom.xml` file. You can use the code we developed in the labs
as a starting point.

- Always build your project using `./mvnw clean package`. Do not build anything using `javac`. You do not need to edit the `pom.xml` file.

- Run the project using `java -jar target/cms330-search-engine-0.1.0.jar`. Remember that the server sometimes takes a moment to start. 
If it seems to be taking a long time, kill it with `CTRL + c` and re-run the program.

- Check the status of your Maven builds. If it does not report `BUILD SUCCESS` scroll up and look for compiler errors.
