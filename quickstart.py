
import duckdb
con = duckdb.connect()

results = con.execute("SELECT 42").fetchall()

# results_df = con.execute("SELECT 42").df()

print(results)
# print(results_df)