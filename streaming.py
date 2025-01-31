import faust

app = faust.App('example-app', broker='kafka://localhost:29092')

topic = app.topic('topic_status', value_type=str,value_serializer='raw')

@app.agent(topic)
async def process(stream):
    async for message in stream:
        print(f"Receives message {message}")
        
if __name__ == '__main__':
    app.main()