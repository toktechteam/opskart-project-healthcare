```mermaid
flowchart TD
    subgraph subGraph0["Auto Scaling Group (I)"]
        direction TB
        G1["EC2 Instance 1"]
        G2["EC2 Instance 2"]
        G3["EC2 Instance N"]
    end
    A["User (Patient/Provider)"] -- Accesses via HTTP/HTTPS --> C["Web Browser or Mobile App"]
    C -- DNS Query --> J["Route 53 DNS"]
    J -- Resolves to --> H["Elastic Load Balancer"]
    H -- Distributes Traffic --> subGraph0
    G1 -- Runs --> D1["Django/PHP Application Instance"]
    G2 -- Runs --> D2["Django/PHP Application Instance"]
    G3 -- Runs --> D3["Django/PHP Application Instance"]
    D1 -- Reads/Writes Data --> E["RDS Database"]
    D2 -- Reads/Writes Data --> E
    D3 -- Reads/Writes Data --> E
    D1 -- Retrieves Static Content --> F["S3 Bucket"]
    D2 -- Retrieves Static Content --> F
    D3 -- Retrieves Static Content --> F
    F -- Cached by --> K["CloudFront CDN"]
    D1 -. Access Control .-> L["IAM Roles and Policies"]
    D2 -. Access Control .-> L
    D3 -. Access Control .-> L
    G1 -. Access Control .-> L
    G2 -. Access Control .-> L
    G3 -. Access Control .-> L
    E -. Access Control .-> L
    F -. Access Control .-> L
    D1 -- Generates Response --> G1
    D2 -- Generates Response --> G2
    D3 -- Generates Response --> G3
    G1 --> H
    G2 --> H
    G3 --> H
    H -- Returns Response --> C
    C -- Displays Content --> A
