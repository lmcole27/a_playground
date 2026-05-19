
```mermaid
sequenceDiagram
	participant Client as Client Browser
	participant WS as /socket.io;
  participant Webhook as /api/webhook
  participant CreateChargeService as /api/create_charge
  participant Stripe as Stripe                        
    	
  Client->>+CreateChargeService: POST /api/create_charge
  CreateChargeService->>+Stripe: POST /charges
  CreateChargeService->>+WS: POST /socket.io {charge_status: pending}
  Client->>+WS: GET /socket.io
  Stripe->>+Webhook: POST /api/webhook {event: charge.succeeded}
  Webhook->>+WS: POST /socket.io {charge_status: succeeded}
  Client->>+WS: GET /socket.io
 ``` 
```mermaid  
gantt
  dateFormat  YYYY-MM-DD
  title Adding GANTT diagram to mermaid
  excludes weekdays 2014-01-10

  section A section
  Completed task            :done,    des1, 2014-01-06,2014-01-08
  Active task               :active,  des2, 2014-01-09, 3d
  Future task               :         des3, after des2, 5d
  Future task2               :         des4, after des3, 5d
```
