# Import any dependencies needed to execute sql queries
from sqlite3 import connect
from pathlib import Path
import pandas as pd
from .sql_execution import QueryMixin  # Import the mixin for query execution

# Define the database path
db_path = Path(__file__).parent / "employee_events.db"
# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
class QueryBase(QueryMixin):

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = ""

    # Define a `names` method that receives
    # no passed arguments
    def names(self):
        
        # Return an empty list
        return []


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self, entity_id):
        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        sql = f"""
            SELECT event_date, 
                   SUM(positive_events) AS total_positive_events, 
                   SUM(negative_events) AS total_negative_events
            FROM employee_events
            WHERE {self.name}_id = ?
            GROUP BY event_date
            ORDER BY event_date;
            """
        return self.pandas_query(sql, params = (entity_id,))
            
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    def notes(self, entity_id):

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        query = f"""
            SELECT note_date, note
            FROM notes
            where {self.name}_id = ?
            ORDER BY note_date;
            """
        return self.pandas_query(query, params = (entity_id,))

