├─ api/            ← Interface Adapters: Controller
│   ├─ routes/
│   ├─ deps.py
│   └─ schemas/             ← API DTO (Pydantic schemas) Presenter
├─ db/             ← Frameworks & Drivers
├─ repositories/   ← Interface Adapters: Gateway Implementation (DB adapter)
├─ services/       ← Use Case
│   ├─ interfaces/              ← Interface Adapters: Gateway interfaces (Protocols)
│       └─ event_publisher.py   
├─ domain/         ← Entities
├─ workers/        ← Interface Adapters: Controller
│   └─ kafka_consumer.py     
├─ integrations/   ← Interface Adapters: Gateway Implementation (external adapter)
│   └─ kafka_producer.py         
├─ core/
│   ├─ config.py        
│   ├─ logging.py
│   └─ security.py    

Enterprices Business Rules: Entities
Application Business Rules: Use Cases
Interface Adapters: Controllers, Gateways, Presenters
Frameworks and Drivers: DB, External Interfaces, UI, Web, Devices
