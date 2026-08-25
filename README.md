# erD ER 다이어그램

Mermaid로 작성한 스키마 문서입니다. 저장소 루트의 `README.md`로 GitHub 메인 화면에 표시되며, Mermaid 블록은 GitHub에서 렌더됩니다.

## 전체 ER (상세)

```mermaid
erDiagram
    USERS {
        uuid id PK
        varchar email UK
        varchar password_hash
        varchar name
        varchar provider
        varchar role
        int token_balance
        varchar status
        int login_fail_count
        timestamp locked_until
        timestamp withdrawn_at
        timestamp updated_at
    }

    USER_PROFILES {
        uuid user_id PK,FK
        varchar role_type
        varchar preferred_level
        varchar purpose
        boolean onboarding_completed
        int onboarding_step
        timestamp created_at
        timestamp updated_at
    }

    REFRESH_TOKENS {
        bigserial id PK
        uuid user_id FK
        varchar token
        varchar device_info
        varchar ip_address
        timestamp expire_at
        timestamp created_at
    }

    EMAIL_VERIFICATIONS {
        bigserial id PK
        uuid user_id FK
        varchar token
        boolean used
        timestamp expires_at
        timestamp created_at
    }

    PROJECTS {
        uuid id PK
        uuid owner_user_id FK
        varchar project_type
        uuid educator_project_id
        uuid learner_project_id
        varchar title
        varchar topic
        text description
        varchar target_level
        jsonb model_settings
        text tags
        boolean is_favorite
        varchar status
        timestamp created_at
        timestamp updated_at
    }

    OUTLINES {
        uuid id PK
        uuid project_id FK
        jsonb tree_structure
        int version
        varchar status
        timestamp confirmed_at
        timestamp created_at
        timestamp updated_at
    }

    OUTLINE_VERSIONS {
        bigserial id PK
        uuid outline_id FK
        int version
        jsonb snapshot
        uuid updated_by
        timestamp created_at
    }

    CHAT_MESSAGES {
        bigserial id PK
        uuid project_id FK
        varchar sender_type
        text message
        jsonb context_meta
        timestamp created_at
    }

    REFERENCES {
        uuid id PK
        uuid project_id FK
        varchar source_type
        varchar file_url
        text extracted_text
        varchar vector_status
        timestamp created_at
    }

    TEMPLATES {
        uuid id PK
        uuid owner_user_id FK
        varchar name
        jsonb outline_template
        boolean is_public
        timestamp created_at
    }

    SHARED_LINKS {
        uuid id PK
        uuid project_id FK
        varchar token
        timestamp expires_at
        int view_count
        boolean is_active
        timestamp created_at
    }

    CONTENTS {
        uuid id PK
        uuid project_id FK
        uuid created_by FK
        varchar project_type
        varchar type
        varchar title
        text body_markdown
        varchar file_url
        int token_used
        jsonb meta
        varchar status
        timestamp created_at
        timestamp updated_at
    }

    QUIZ_QUESTIONS {
        uuid id PK
        uuid content_id FK
        text question
        varchar question_type
        jsonb choices
        text answer
        text explanation
        int order_no
    }

    QUESTION_VERSIONS {
        bigserial id PK
        uuid question_id FK
        int version
        jsonb snapshot
        uuid updated_by
        timestamp created_at
    }

    FLASHCARDS {
        uuid id PK
        uuid content_id FK
        text front
        text back
        varchar difficulty
        int order_no
    }

    CARD_REVIEWS {
        bigserial id PK
        uuid flashcard_id FK
        uuid user_id FK
        int quality_score
        int interval_days
        int repetition
        float easiness_factor
        timestamp reviewed_at
    }

    ILLUSTRATIONS {
        uuid id PK
        uuid content_id FK
        varchar prompt
        varchar image_url
        varchar model_name
        varchar status
        timestamp created_at
    }

    NARRATIONS {
        uuid id PK
        uuid content_id FK
        varchar voice
        varchar audio_url
        int duration_sec
        varchar status
        timestamp created_at
    }

    AUDIO_FILES {
        uuid id PK
        uuid project_id FK
        uuid uploaded_by FK
        varchar file_url
        varchar stt_status
        text transcript
        timestamp created_at
    }

    SELF_ASSESSMENTS {
        uuid id PK
        uuid content_id FK
        uuid user_id FK
        int score
        text feedback
        timestamp submitted_at
    }

    TOKEN_TRANSACTIONS {
        bigserial id PK
        uuid user_id FK
        int amount
        varchar tx_type
        varchar reason
        bigint ref_id
        timestamp created_at
    }

    JOBS {
        uuid id PK
        uuid content_id FK
        uuid requested_by FK
        varchar queue_name
        varchar status
        int retry_count
        text error_message
        timestamp created_at
        timestamp updated_at
    }

    %% 관계
    USERS ||--|| USER_PROFILES : has
    USERS ||--o{ REFRESH_TOKENS : owns
    USERS ||--o{ EMAIL_VERIFICATIONS : verifies
    USERS ||--o{ PROJECTS : owns
    USERS ||--o{ CONTENTS : creates
    USERS ||--o{ TOKEN_TRANSACTIONS : has
    USERS ||--o{ CARD_REVIEWS : reviews
    USERS ||--o{ AUDIO_FILES : uploads
    USERS ||--o{ TEMPLATES : owns
    USERS ||--o{ JOBS : requests

    PROJECTS ||--|| OUTLINES : has_current
    OUTLINES ||--o{ OUTLINE_VERSIONS : versioned_as
    PROJECTS ||--o{ CHAT_MESSAGES : contains
    PROJECTS ||--o{ REFERENCES : contains
    PROJECTS ||--o{ SHARED_LINKS : shared_by
    PROJECTS ||--o{ CONTENTS : generates
    PROJECTS ||--o{ AUDIO_FILES : contains

    CONTENTS ||--o{ QUIZ_QUESTIONS : includes
    QUIZ_QUESTIONS ||--o{ QUESTION_VERSIONS : versioned_as
    CONTENTS ||--o{ FLASHCARDS : includes
    FLASHCARDS ||--o{ CARD_REVIEWS : reviewed_by
    CONTENTS ||--o{ ILLUSTRATIONS : includes
    CONTENTS ||--o{ NARRATIONS : includes
    CONTENTS ||--o{ SELF_ASSESSMENTS : assessed_by
    CONTENTS ||--o{ JOBS : processed_by
```

## 발표용 ER (PK·FK·핵심 필드)

상세 스키마는 위 블록 참고. 슬라이드·한눈에 보기용으로 관계와 대표 필드만 남김.

```mermaid
erDiagram
    USERS {
        uuid id PK
        varchar email UK
        varchar role
        varchar status
        int token_balance
    }

    USER_PROFILES {
        uuid user_id PK,FK
        varchar role_type
        boolean onboarding_completed
    }

    REFRESH_TOKENS {
        bigserial id PK
        uuid user_id FK
        timestamp expire_at
    }

    EMAIL_VERIFICATIONS {
        bigserial id PK
        uuid user_id FK
        boolean used
    }

    PROJECTS {
        uuid id PK
        uuid owner_user_id FK
        varchar project_type
        uuid educator_project_id
        uuid learner_project_id
        varchar title
        varchar status
    }

    OUTLINES {
        uuid id PK
        uuid project_id FK
        int version
        varchar status
    }

    OUTLINE_VERSIONS {
        bigserial id PK
        uuid outline_id FK
        int version
    }

    CHAT_MESSAGES {
        bigserial id PK
        uuid project_id FK
        varchar sender_type
    }

    REFERENCES {
        uuid id PK
        uuid project_id FK
        varchar vector_status
    }

    TEMPLATES {
        uuid id PK
        uuid owner_user_id FK
        boolean is_public
    }

    SHARED_LINKS {
        uuid id PK
        uuid project_id FK
        boolean is_active
    }

    CONTENTS {
        uuid id PK
        uuid project_id FK
        uuid created_by FK
        varchar type
        varchar status
    }

    QUIZ_QUESTIONS {
        uuid id PK
        uuid content_id FK
        varchar question_type
        int order_no
    }

    QUESTION_VERSIONS {
        bigserial id PK
        uuid question_id FK
        int version
    }

    FLASHCARDS {
        uuid id PK
        uuid content_id FK
        int order_no
    }

    CARD_REVIEWS {
        bigserial id PK
        uuid flashcard_id FK
        uuid user_id FK
    }

    ILLUSTRATIONS {
        uuid id PK
        uuid content_id FK
        varchar status
    }

    NARRATIONS {
        uuid id PK
        uuid content_id FK
        varchar status
    }

    AUDIO_FILES {
        uuid id PK
        uuid project_id FK
        uuid uploaded_by FK
        varchar stt_status
    }

    SELF_ASSESSMENTS {
        uuid id PK
        uuid content_id FK
        uuid user_id FK
        int score
    }

    TOKEN_TRANSACTIONS {
        bigserial id PK
        uuid user_id FK
        int amount
        varchar tx_type
    }

    JOBS {
        uuid id PK
        uuid content_id FK
        uuid requested_by FK
        varchar status
    }

    USERS ||--|| USER_PROFILES : has
    USERS ||--o{ REFRESH_TOKENS : owns
    USERS ||--o{ EMAIL_VERIFICATIONS : verifies
    USERS ||--o{ PROJECTS : owns
    USERS ||--o{ CONTENTS : creates
    USERS ||--o{ TOKEN_TRANSACTIONS : has
    USERS ||--o{ CARD_REVIEWS : reviews
    USERS ||--o{ AUDIO_FILES : uploads
    USERS ||--o{ TEMPLATES : owns
    USERS ||--o{ JOBS : requests

    PROJECTS ||--|| OUTLINES : has_current
    OUTLINES ||--o{ OUTLINE_VERSIONS : versioned_as
    PROJECTS ||--o{ CHAT_MESSAGES : contains
    PROJECTS ||--o{ REFERENCES : contains
    PROJECTS ||--o{ SHARED_LINKS : shared_by
    PROJECTS ||--o{ CONTENTS : generates
    PROJECTS ||--o{ AUDIO_FILES : contains

    CONTENTS ||--o{ QUIZ_QUESTIONS : includes
    QUIZ_QUESTIONS ||--o{ QUESTION_VERSIONS : versioned_as
    CONTENTS ||--o{ FLASHCARDS : includes
    FLASHCARDS ||--o{ CARD_REVIEWS : reviewed_by
    CONTENTS ||--o{ ILLUSTRATIONS : includes
    CONTENTS ||--o{ NARRATIONS : includes
    CONTENTS ||--o{ SELF_ASSESSMENTS : assessed_by
    CONTENTS ||--o{ JOBS : processed_by
```

## 브라우저에서 미리보기

1. **`preview/er-preview.html`** 파일을 더블클릭하거나, 브라우저로 드래그해서 엽니다. (인터넷이 있어야 Mermaid CDN을 불러옵니다.)
2. `README.md`의 Mermaid를 고친 뒤 미리보기를 다시 만들려면, 이 폴더에서 터미널로 `python gen_preview.py`를 실행합니다.

온라인에서만 보려면 [Mermaid Live Editor](https://mermaid.live)를 열고, README에서 **mermaid**로 시작하는 코드 블록 전체를 복사해 붙여 넣으면 됩니다.

## GitHub에 올리기 (처음 하는 경우)

### 1단계: GitHub에서 빈 저장소 만들기

1. [github.com](https://github.com)에 로그인합니다.
2. 오른쪽 위 **+** → **New repository**를 누릅니다.
3. **Repository name**에 영문 이름을 입력합니다 (예: `er-diagram`).
4. **Add a README file**은 **체크하지 않습니다**. (로컬에 이미 `README.md`가 있으면, 원격에 README를 같이 만들면 첫 push 때 충돌이 나기 쉽습니다.)
5. **Create repository**를 누릅니다.
6. 다음 화면에서 **HTTPS** 주소를 복사해 둡니다.  
   예: `https://github.com/내아이디/er-diagram.git`

### 2단계: PC에 Git 설치

1. [Git for Windows](https://git-scm.com/download/win)를 설치합니다.
2. 설치 옵션에서 **“Git from the command line and also from 3rd-party software”**를 고르면 PowerShell·Cursor 터미널에서 `git`을 쓰기 쉽습니다.
3. 설치 후 **터미널·Cursor를 모두 닫았다가 다시** 엽니다.

### 3단계: 프로젝트 폴더에서 Git 초기화 후 업로드

1. 터미널을 연 뒤 **`README.md`가 있는 폴더**로 이동합니다.

   예 (경로는 본인 PC에 맞게 수정):

   ```powershell
   Set-Location "D:\프로젝트폴더\erD-main\erD-main"
   ```

2. 아래를 **위에서부터 순서대로** 실행합니다. 마지막 줄의 주소는 **2단계에서 복사한 본인 저장소 주소**로 바꿉니다.

```bash
git init
git add README.md .gitignore preview gen_preview.py
git commit -m "docs: ER 다이어그램 및 미리보기"
git branch -M main
git remote add origin https://github.com/<GitHub아이디>/<저장소이름>.git
git push -u origin main
```

3. `git push` 할 때 GitHub **비밀번호**를 물으면, 보통 **비밀번호 대신 Personal Access Token**을 붙여 넣어야 합니다.  
   GitHub 웹 → **Settings** → **Developer settings** → **Personal access tokens**에서 토큰을 만들고, 터미널 비밀번호 입력란에 그 토큰을 넣습니다.  
   (또는 [GitHub CLI](https://cli.github.com/)로 `gh auth login` 한 뒤 push할 수도 있습니다.)

4. 브라우저에서 `https://github.com/<GitHub아이디>/<저장소이름>` 으로 들어가면 `README.md`가 메인에 보이고, Mermaid ER도 GitHub가 렌더링합니다.

### 자주 나는 일

- **저장소 만들 때 README를 넣어버린 경우**  
  첫 `push`가 거절될 수 있습니다. 처음이면 저장소를 지우고 **README 없이** 다시 만드는 것이 가장 단순합니다.
- **`fatal: not a git repository`**  
  `git init`을 안 했거나, `README.md`가 있는 폴더가 아닌 곳에서 명령을 실행한 경우입니다.

### 이미 다른 Git 프로젝트에 합칠 때

이 폴더의 파일을 그 프로젝트 안으로 복사한 뒤, 그 저장소에서 `git add` → `commit` → `push`하면 됩니다.
