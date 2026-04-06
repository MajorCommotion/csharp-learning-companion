# C# / ASP.NET 학습 도우미

🌍 **다국어 지원!** C#과 ASP.NET 개발자를 위한 대화형 학습 도구. **한국어**와 **English** 지원.

WinForms에서 ASP.NET Core로 전환하는 개발자, C# 기초를 배우는 주니어 개발자, 자기주도 학습에 완벽합니다.

## 기능

✅ **다국어 지원** 🌍 - 한국어와 영어  
✅ **8가지 핵심 주제** - C# 기초부터 고급 ASP.NET Core까지  
✅ **대화형 퀴즈** - 즉각적인 피드백으로 지식 테스트  
✅ **코드 예제** - 실전 C#과 ASP.NET 코드 스니펫  
✅ **연습 문제** - 실습 프로젝트  
✅ **진행 상황 추적** - 학습 여정 저장  
✅ **맞춤형 추천** - 적응형 학습 경로  
✅ **SOLID 원칙** - 엔터프라이즈급 모범 사례  
✅ **의존성 제로** - 순수 Python, 어디서나 실행

## 지원 언어

- 🇰🇷 **한국어** - 완전한 한국어 인터페이스
- 🇺🇸 **English** - 전체 영어 인터페이스

_기술 콘텐츠(코드 예제, 퀴즈)는 정확성을 위해 영어로 유지됩니다. 인터페이스는 완전히 번역되었습니다._

[다른 언어로 읽기: [English](README.md)]

---

## 다루는 주제

### 1. C# 기초
- 변수와 데이터 타입
- 제어 흐름 (if, switch, 반복문)
- 메서드와 매개변수
- 클래스와 객체
- 프로퍼티 vs 필드
- Nullable 참조 타입

### 2. 객체 지향 프로그래밍
- 캡슐화, 상속, 다형성
- 인터페이스 vs 추상 클래스
- SOLID 원칙
- 디자인 패턴

### 3. 컬렉션과 LINQ
- List<T>, Dictionary, HashSet
- LINQ 쿼리 (Where, Select, OrderBy)
- 람다 표현식
- IEnumerable vs IQueryable

### 4. 비동기 프로그래밍
- async와 await 키워드
- Task와 Task<T>
- 비동기 모범 사례
- ConfigureAwait

### 5. ASP.NET Core 기초
- MVC 패턴
- 컨트롤러와 액션
- 라우팅
- 의존성 주입
- 미들웨어 파이프라인

### 6. Entity Framework Core
- DbContext와 DbSet
- Code-First vs Database-First
- LINQ to Entities
- 마이그레이션
- 성능 최적화

### 7. RESTful Web API
- REST 원칙
- HTTP 동사 (GET, POST, PUT, DELETE)
- 모델 바인딩과 유효성 검사
- JWT 인증
- API 버전 관리

### 8. 모범 사례 및 패턴
- 리포지토리 패턴
- Unit of Work 패턴
- 에러 처리
- 로깅 (Serilog, NLog)
- 단위 테스트

---

## 설치

```bash
# 저장소 복제
git clone https://github.com/MajorCommotion/csharp-learning-companion.git
cd csharp-learning-companion

# 실행 권한 부여
chmod +x learn.py

# 실행
./learn.py
```

의존성 필요 없음! 순수 Python 3.6+

---

## 빠른 시작

```bash
./learn.py
```

**언어 선택:**

첫 실행 시 기본값은 영어입니다. 메인 메뉴의 옵션 7에서 언어를 변경할 수 있습니다.

**메인 메뉴 (한국어):**
```
============================================================
C# / ASP.NET 학습 도우미
============================================================
진행 상황: 0개 주제 | 0개 퀴즈 | 0점
============================================================

1. 주제 둘러보기
2. 퀴즈 풀기
3. 코드 예제 보기
4. 연습 문제
5. 진행 상황 보기
6. 학습 경로 추천
7. 언어 변경 🌍
8. 종료
```

**Main Menu (English):**
```
============================================================
C# / ASP.NET LEARNING COMPANION
============================================================
Progress: 0 topics | 0 quizzes | 0 points
============================================================

1. Browse Topics
2. Take a Quiz
3. View Code Examples
4. Practice Exercises
5. View Progress
6. Learning Path Recommendations
7. Change Language 🌍
8. Exit
```

---

## 사용 예시

### 1. 주제 학습
```bash
# 프로그램 실행
./learn.py

# 메뉴에서 "1" 선택 (주제 둘러보기)
# 관심 있는 주제 선택
# 주요 개념 읽기
# Enter 키로 완료 표시
```

### 2. 퀴즈 풀기
```bash
# 메뉴에서 "2" 선택 (퀴즈 풀기)
# 퀴즈 선택
# 질문에 답변 (1-4)
# 즉각적인 피드백과 설명 확인
# 70% 이상 득점 시 합격!
```

### 3. 코드 예제 보기
```bash
# 메뉴에서 "3" 선택 (코드 예제 보기)
# 예제 선택
# 실전 C# 코드와 설명 학습
```

---

## 학습 경로

### 초급 경로
1. C# 기초
2. 객체 지향 프로그래밍
3. 컬렉션과 LINQ
4. ASP.NET Core 기초

### 중급 경로
1. 비동기 프로그래밍
2. ASP.NET Core 기초
3. Entity Framework Core
4. RESTful Web API

### 고급 경로
1. 모범 사례 및 패턴
2. 고급 EF Core
3. 마이크로서비스 아키텍처
4. 실전 프로젝트

---

## 연습 문제

### 연습 문제 1: 간단한 REST API 만들기
**난이도:** 초급

**작업:**
- [ApiController]로 ProductsController 생성
- GET /api/products 구현
- POST /api/products 구현
- 모델 유효성 검사 추가
- 적절한 HTTP 상태 코드 반환

### 연습 문제 2: 리포지토리 패턴 구현
**난이도:** 중급

**작업:**
- IRepository<T> 인터페이스 생성
- GenericRepository<T> 구현
- Unit of Work 패턴 추가
- 의존성 주입 사용
- 단위 테스트 작성

### 연습 문제 3: 인증 시스템 구축
**난이도:** 고급

**작업:**
- User 모델과 DbContext 생성
- 회원가입 엔드포인트 구현
- JWT로 로그인 구현
- [Authorize] 속성 추가
- 리프레시 토큰 메커니즘

---

## WinForms 개발자를 위한 안내

**WinForms에서 ASP.NET Core로 전환하시나요?**

### 주요 차이점
| WinForms | ASP.NET Core |
|----------|--------------|
| 이벤트 기반 (버튼 클릭) | 요청/응답 (HTTP) |
| 상태 유지 (폼 상태) | 상태 비저장 (HTTP) |
| Windows 전용 | 크로스 플랫폼 |
| ADO.NET | Entity Framework Core |
| 기본적으로 동기 | 기본적으로 비동기 |

### 유지되는 것
✅ C# 기초  
✅ OOP 원칙  
✅ LINQ 쿼리  
✅ 디자인 패턴  

### 새로 배울 개념
🆕 미들웨어 파이프라인  
🆕 의존성 주입  
🆕 RESTful API  
🆕 async/await (모든 곳에서)  
🆕 구성 시스템  

---

## 추가 자료

**공식 문서:**
- [Microsoft Learn](https://docs.microsoft.com/learn)
- [ASP.NET Core 문서](https://docs.microsoft.com/aspnet/core)
- [Entity Framework Core](https://docs.microsoft.com/ef/core)

**추천 도서:**
- *C# 10 in a Nutshell* by Joseph Albahari
- *Pro ASP.NET Core 6* by Adam Freeman
- *Clean Code* by Robert C. Martin

**온라인 강좌:**
- Pluralsight C# 경로
- Microsoft Learn 모듈
- Udemy ASP.NET Core 강좌

---

## 사용 사례

### 1. 자기주도 학습
- 자신의 속도로 주제 학습
- 퀴즈로 이해도 테스트
- 코드 예제에서 패턴 학습

### 2. 면접 준비
- C# 기초 복습
- SOLID 원칙 연습
- 일반적인 면접 질문 학습

### 3. 팀 교육
- 주니어 개발자 온보딩
- 모범 사례 표준화
- 코드 예제 공유

### 4. 매일 연습
- 빠른 15분 세션
- 하루에 한 주제
- 일관된 학습 습관 형성

---

## 국제화 (i18n)

### 아키텍처

이 앱은 쉬운 번역을 위해 **JSON 기반 i18n 시스템**을 사용합니다:

```
csharp-learning-companion/
├── learn.py           # 메인 애플리케이션 (i18n 지원)
├── i18n.py            # 번역 엔진
└── locales/
    ├── en.json        # 영어 번역
    └── ko.json        # 한국어 번역
```

### 새 언어 추가

1. **번역 파일 생성:**
   ```bash
   cp locales/ko.json locales/ja.json  # 일본어 예시
   ```

2. **문자열 번역:**
   ```json
   {
     "app_title": "C# / ASP.NET 学習コンパニオン",
     "welcome": "C# / ASP.NET 学習コンパニオンへようこそ!",
     ...
   }
   ```

3. **`i18n.py`에 언어 등록:**
   ```python
   SUPPORTED_LANGUAGES = {
       'en': 'English',
       'ko': '한국어 (Korean)',
       'ja': '日本語 (Japanese)'  # 여기에 추가
   }
   ```

4. **테스트하고 PR 제출!**

### 번역 가이드라인

- **UI 요소**: 완전히 번역 (메뉴, 프롬프트, 피드백)
- **기술 콘텐츠**: 정확성을 위해 영어 유지
  - 코드 예제
  - 퀴즈 질문
  - 프로그래밍 용어 (MVC, LINQ, async/await)
- **하이브리드 접근**: 한국어 UI + 영어 기술 용어가 잘 작동함

---

## 로드맵

- [ ] 비디오 튜토리얼 통합
- [ ] 더 많은 퀴즈 (50개 이상의 질문)
- [ ] 대화형 코드 챌린지
- [ ] 커뮤니티 기여 예제
- [ ] 수료증 생성
- [ ] GitHub 통합 (커밋 추적)
- [ ] 실시간 코드 실행
- [ ] 피어 학습 기능

---

## 기여

기여를 환영합니다! 다음을 추가하세요:
- **새 언어** (일본어, 스페인어, 중국어 등)
- 새 주제
- 퀴즈 질문
- 코드 예제
- 연습 문제

**번역 기여자:**
- 🇰🇷 한국어: lexcellent

---

## 라이선스

MIT License - 자세한 내용은 [LICENSE](LICENSE) 참조

---

## 저자

**lexcellent**
- GitHub: [@MajorCommotion](https://github.com/MajorCommotion)
- Email: rj5al@pm.me

---

## 지원

문제가 있거나 제안 사항이 있으신가요?
- [GitHub Issues](https://github.com/MajorCommotion/csharp-learning-companion/issues) 열기
- Pull Request 제출

---

## 감사의 말

- Microsoft .NET 팀 (훌륭한 문서)
- C# 및 ASP.NET 커뮤니티
- 모든 기여자들

---

**즐거운 학습 되세요! 🎓**
