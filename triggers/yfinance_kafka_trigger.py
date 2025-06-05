from findrum.interfaces import EventTrigger
from kafka import KafkaConsumer
import json
import pandas as pd

class KafkaEventListener(EventTrigger):
    def __init__(self, topic, bootstrap_servers='localhost:9092', group_id='findrum_listener'):
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.bootstrap_servers,
            group_id=self.group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='latest',
            enable_auto_commit=True
        )

    def start(self):
        for message in self.consumer:
            event_data = message.value
            df = pd.DataFrame([event_data])
            self.emit(df)