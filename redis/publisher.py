from RedisUtils import getRedisConnectionWithPool
import time,threading

def publisher(n,conn):
    time.sleep(1)
    for i in range(n):
        conn.publish('channel',i)
        time.sleep(1)

def run_pubsub(conn):
    threading.Thread(target=publisher,args=(3,conn,)).start()
    pubsub=conn.pubsub()
    pubsub.subscribe(['channel'])
    count=0
    for item in pubsub.listen():
        print(item)
        count+=1
        if count==4:
            pubsub.unsubscribe()
        if count==5:
            break    

if __name__ == "__main__":
    conn=getRedisConnectionWithPool()
    run_pubsub(conn)
