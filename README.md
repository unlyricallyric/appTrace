# Features and Highlights

- Connection Pool is used for extensibility and efficiency
- Batch Processing is used for better performance
- Extensible to support different type of database
- Flexibility in terms of querying the slowest records
- Customized PriorityQueue for better handling records set


[Optional] Parting Question:
'What are the pitfalls of the database schema described here? If you had full liberty to modify the database schema, 
what would you change and what is the expected impact?'

Pitfalls: data column

Since both the navigation_history and metadata can be incrementing, The data column can become extremely long and 
inefficient, while querying for the longest duration, we don't need to know anything yet about the data column, 
so having data column with large content makes each query unnecessarily expensive, would be necessary to extract 
the data column into a new table with id as foreign key.
