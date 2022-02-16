import json
import asyncio
from fastapi import FastAPI 
from aiokafka import AIOKafkaProducer
from settings import config
from api.entities.producer import ProducerMessage, ProducerResponse


app = FastAPI(title=config.PROJECT_NAME, 
              openapi_url="/api/openapi.json", docs_url="/api/docs")


loop = asyncio.get_event_loop()
aioproducer = AIOKafkaProducer(
    loop=loop, client_id=config.PROJECT_NAME, bootstrap_servers=config.KAFKA_INSTANCE
)

@app.on_event("startup")
async def startup_event():
    await aioproducer.start()


@app.on_event("shutdown")
async def shutdown_event():
    await aioproducer.stop()


@app.post("/producer/{topicname}")
async def kafka_produce(msg: ProducerMessage, topicname: str):
    await aioproducer.send(topicname, json.dumps(msg.dict()).encode("ascii"))
    response = ProducerResponse(
        name=msg.name, message_id=msg.message_id, topic=topicname
    )
    return response

