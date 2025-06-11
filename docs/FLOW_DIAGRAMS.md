# 🔄 System Flow Diagrams

This document contains comprehensive flow diagrams showing how the Telegram Transparency Master Bot works.

## 📱 User Interaction Flow

```mermaid
flowchart TD
    A[User starts chat] --> B[/start command]
    B --> C[Welcome message with transparency options]
    
    C --> D{User action?}
    
    D -->|Send image directly| E[Use default 'full' mode]
    D -->|Send mode command| F[Parse mode command]
    D -->|Send /help| G[Show help message]
    D -->|Send /modes| H[Show all transparency modes]
    D -->|Send /settings| I[Show current settings]
    
    F --> J{Valid mode?}
    J -->|Yes| K[Update user settings]
    J -->|No| L[Show error message]
    
    K --> M[Confirm mode change]
    L --> D
    M --> N[Wait for image]
    
    E --> O[Process image]
    N --> P[Receive image]
    P --> Q[Validate image]
    
    Q --> R{Valid image?}
    R -->|No| S[Show validation error]
    R -->|Yes| T[Check rate limit]
    
    T --> U{Within limit?}
    U -->|No| V[Show rate limit error]
    U -->|Yes| W[Show processing message]
    
    W --> X[Apply transparency effect]
    X --> Y{Processing successful?}
    Y -->|No| Z[Show processing error]
    Y -->|Yes| AA[Send processed image]
    
    AA --> BB[Delete processing message]
    BB --> CC[Ready for next image]
    
    S --> D
    V --> D
    Z --> D
    CC --> D
    G --> D
    H --> D
    I --> D
    
    style A fill:#e1f5fe
    style C fill:#f3e5f5
    style O fill:#fff3e0
    style X fill:#e8f5e8
    style AA fill:#e8f5e8
```

## 🖼️ Image Processing Pipeline

```mermaid
flowchart LR
    A[Raw Image Bytes] --> B[Image Validation]
    B --> C{Valid Format & Size?}
    
    C -->|No| D[Return Error]
    C -->|Yes| E[Convert to PIL Image]
    
    E --> F[Load InSPyReNet Model]
    F --> G[Generate Mask]
    
    G --> H{Transparency Mode?}
    
    H -->|Full| I[Standard RGBA Output]
    H -->|Semi| J[Semi-transparent Background]
    H -->|Soft| K[Gaussian Blur Edges]
    H -->|Subject| L[Transparent Subject]
    H -->|Custom| M[Custom Opacity Level]
    
    I --> N[Apply Alpha Channel]
    J --> O[Create Background Alpha]
    K --> P[Blur Mask Edges]
    L --> Q[Invert Alpha Channel]
    M --> R[Calculate Opacity]
    
    O --> N
    P --> N
    Q --> N
    R --> N
    
    N --> S[Convert to PNG Bytes]
    S --> T[Return Processed Image]
    
    style A fill:#e3f2fd
    style G fill:#fff3e0
    style H fill:#f3e5f5
    style N fill:#e8f5e8
    style T fill:#e8f5e8
```

## 🏗️ System Architecture

```mermaid
graph TB
    subgraph "User Interface"
        A[Telegram Client]
        B[User Commands]
        C[Image Upload]
    end
    
    subgraph "Telegram Bot API"
        D[Bot Framework]
        E[Message Handlers]
        F[Command Processors]
    end
    
    subgraph "Application Layer"
        G[Bot Controller]
        H[User Settings Manager]
        I[Rate Limiter]
        J[Error Handler]
    end
    
    subgraph "Processing Layer"
        K[Image Processor]
        L[Transparency Engine]
        M[InSPyReNet Model]
        N[Effect Generators]
    end
    
    subgraph "Storage & Cache"
        O[User Settings]
        P[Model Cache]
        Q[Temporary Files]
    end
    
    subgraph "External Services"
        R[Telegram Servers]
        S[Model Repository]
        T[Hosting Platform]
    end
    
    A --> R
    R --> D
    B --> E
    C --> E
    
    E --> F
    F --> G
    
    G --> H
    G --> I
    G --> J
    
    G --> K
    K --> L
    L --> M
    L --> N
    
    H --> O
    M --> P
    K --> Q
    
    M --> S
    T --> G
    
    style A fill:#e1f5fe
    style M fill:#fff3e0
    style L fill:#f3e5f5
    style G fill:#e8f5e8
```

## 🎨 Transparency Modes Decision Tree

```mermaid
flowchart TD
    A[User Sends Image] --> B{Mode Selected?}
    
    B -->|No mode set| C[Use 'full' mode]
    B -->|Mode set| D{Which mode?}
    
    D -->|full| E[Complete Background Removal]
    D -->|semi| F[50% Background Transparency]
    D -->|soft| G[Gaussian Blur Edges]
    D -->|subject| H[Transparent Subject]
    D -->|custom| I[User-defined Opacity]
    
    C --> E
    
    E --> J[Generate mask with InSPyReNet]
    F --> K[Generate mask + 50% alpha]
    G --> L[Generate mask + blur filter]
    H --> M[Generate mask + invert alpha]
    I --> N[Generate mask + custom alpha]
    
    J --> O[Standard RGBA output]
    K --> P[Semi-transparent background]
    L --> Q[Feathered edges]
    M --> R[Translucent subject]
    N --> S[Custom transparency level]
    
    O --> T[Send to user]
    P --> T
    Q --> T
    R --> T
    S --> T
    
    T --> U[Ready for next image]
    
    style A fill:#e1f5fe
    style D fill:#f3e5f5
    style J fill:#fff3e0
    style K fill:#fff3e0
    style L fill:#fff3e0
    style M fill:#fff3e0
    style N fill:#fff3e0
    style T fill:#e8f5e8
```

## 🚀 Development and Deployment Flow

```mermaid
gitgraph
    commit id: "Initial Setup"
    commit id: "Core Bot Logic"
    commit id: "Transparency Features"
    
    branch develop
    checkout develop
    commit id: "Add Semi Mode"
    commit id: "Add Soft Edges"
    commit id: "Add Custom Opacity"
    
    checkout main
    merge develop
    commit id: "Release v1.0.0"
    
    branch feature/docker
    checkout feature/docker
    commit id: "Add Dockerfile"
    commit id: "Add Docker Compose"
    commit id: "Test Container"
    
    checkout main
    merge feature/docker
    commit id: "Release v1.1.0"
    
    branch hotfix/memory-leak
    checkout hotfix/memory-leak
    commit id: "Fix Memory Issue"
    
    checkout main
    merge hotfix/memory-leak
    commit id: "Release v1.1.1"
```

## ⚠️ Error Handling Flow

```mermaid
flowchart TD
    A[User Request] --> B[Validation Layer]
    
    B --> C{Valid Request?}
    C -->|No| D[Input Validation Error]
    C -->|Yes| E[Rate Limiting Check]
    
    E --> F{Within Limits?}
    F -->|No| G[Rate Limit Error]
    F -->|Yes| H[Image Processing]
    
    H --> I{Processing Success?}
    I -->|No| J[Processing Error]
    I -->|Yes| K[Send Result]
    
    D --> L[Log Error]
    G --> M[Log Rate Limit]
    J --> N[Log Processing Error]
    
    L --> O[Send User-Friendly Message]
    M --> P[Send Rate Limit Message]
    N --> Q[Send Processing Error Message]
    
    O --> R[Suggest Correction]
    P --> S[Suggest Wait Time]
    Q --> T[Suggest Retry]
    
    K --> U[Success Response]
    R --> V[Ready for Next Request]
    S --> V
    T --> V
    U --> V
    
    subgraph "Error Types"
        W[File Too Large]
        X[Invalid Format]
        Y[Network Timeout]
        Z[Model Loading Error]
        AA[Memory Error]
    end
    
    J --> W
    J --> X
    J --> Y
    J --> Z
    J --> AA
    
    style D fill:#ffebee
    style G fill:#fff3e0
    style J fill:#ffebee
    style K fill:#e8f5e8
    style U fill:#e8f5e8
```

## 📊 Flow Summary

### Key Components:

1. **User Interface Layer**: Telegram client interaction
2. **Bot Framework**: Message handling and command processing
3. **Application Logic**: User settings, rate limiting, error handling
4. **AI Processing**: InSPyReNet model and transparency effects
5. **Storage**: User preferences and model caching

### Transparency Modes:

- **Full**: Complete background removal (default)
- **Semi**: 50% transparent background
- **Soft**: Feathered edges with Gaussian blur
- **Subject**: Translucent subject with transparent background
- **Custom**: User-defined opacity levels

### Error Handling:

- Input validation for file size and format
- Rate limiting to prevent abuse
- Comprehensive error logging
- User-friendly error messages
- Automatic retry suggestions

### Development Workflow:

- Feature branches for new functionality
- Main branch for stable releases
- Hotfix branches for critical issues
- Automated CI/CD pipeline
- Docker containerization support
