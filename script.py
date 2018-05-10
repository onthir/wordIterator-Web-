# script to add words to the database
import psycopg2


conn = psycopg2.connect("host='ec2-54-243-137-182.compute-1.amazonaws.com' dbname='d4di8681dvvgib' user='orpzbzxodbhyvi' password='19db2a8383cbca125757d30b4219260864e109ea4fce0d5978ccdf1ab38dee84'")
cur = conn.cursor()
with open("wordlist.txt") as file:
    data = file.readlines()
    x = 1
    for d in data:
        c = d.replace(" ", "")
        e = str(c.lower())
        # add to the database
        cur.execute("""insert into "dictionary" (word) VALUES (%s)""", (e,))
        conn.commit()
        x += 1

        print("Added " + str(d))