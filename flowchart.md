```mermaid
flowchart TD
    A[User] -->|Accesses| B[Web Browser]
    B -->|Requests| C[MyHealthApp Server]
    C -->|Routes| D[URL Dispatcher]

    subgraph Django Project
        D -->|Handles| E[Admin App]
        D -->|Handles| F[Appointments App]
        D -->|Handles| G[Patients App]
        D -->|Handles| H[Providers App]
    end

    E -->|Manages| E1[Admin Interface]
    E1 -->|CRUD Operations| E2[Admin Models]

    F -->|Manages| F1[Appointment Views]
    F1 -->|CRUD Operations| F2[Appointment Models]

    G -->|Manages| G1[Patient Views]
    G1 -->|CRUD Operations| G2[Patient Models]

    H -->|Manages| H1[Provider Views]
    H1 -->|CRUD Operations| H2[Provider Models]

    subgraph Database
        E2 -->|Stores| I[Database]
        F2 -->|Stores| I
        G2 -->|Stores| I
        H2 -->|Stores| I
    end
