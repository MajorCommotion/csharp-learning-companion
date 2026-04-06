# C# / ASP.NET Learning Companion

🌍 **NOW MULTILINGUAL!** Interactive learning tool for C# and ASP.NET developers in **English** and **한국어 (Korean)**.

Perfect for WinForms developers transitioning to ASP.NET Core, junior developers learning fundamentals, and self-study.

## Features

✅ **Multilingual Support** 🌍 - English and Korean (한국어)  
✅ **8 Core Topics** - C# fundamentals to advanced ASP.NET Core  
✅ **Interactive Quizzes** - Test your knowledge with instant feedback  
✅ **Code Examples** - Real-world C# and ASP.NET snippets  
✅ **Practice Exercises** - Hands-on projects to build  
✅ **Progress Tracking** - Save your learning journey  
✅ **Personalized Recommendations** - Adaptive learning paths  
✅ **SOLID Principles** - Enterprise-grade best practices  
✅ **Zero Dependencies** - Pure Python, runs anywhere

## Supported Languages

- 🇺🇸 **English** - Full interface localization
- 🇰🇷 **한국어 (Korean)** - Complete Korean translation

_Technical content (code examples, quizzes) maintained in English for accuracy. Interface fully translated._  

---

## Topics Covered

### 1. C# Fundamentals
- Variables and Data Types
- Control Flow (if, switch, loops)
- Methods and Parameters
- Classes and Objects
- Properties vs Fields
- Nullable Reference Types

### 2. Object-Oriented Programming
- Encapsulation, Inheritance, Polymorphism
- Interfaces vs Abstract Classes
- SOLID Principles
- Design Patterns

### 3. Collections and LINQ
- List<T>, Dictionary, HashSet
- LINQ queries (Where, Select, OrderBy)
- Lambda Expressions
- IEnumerable vs IQueryable

### 4. Async/Await and Threading
- async and await keywords
- Task and Task<T>
- Async Best Practices
- ConfigureAwait

### 5. ASP.NET Core Fundamentals
- MVC Pattern
- Controllers and Actions
- Routing
- Dependency Injection
- Middleware Pipeline

### 6. Entity Framework Core
- DbContext and DbSet
- Code-First vs Database-First
- LINQ to Entities
- Migrations
- Performance Optimization

### 7. RESTful Web APIs
- REST Principles
- HTTP Verbs (GET, POST, PUT, DELETE)
- Model Binding and Validation
- JWT Authentication
- API Versioning

### 8. Best Practices & Patterns
- Repository Pattern
- Unit of Work Pattern
- Error Handling
- Logging (Serilog, NLog)
- Unit Testing

---

## Installation

```bash
# Clone repository
git clone https://github.com/lexcellent/csharp-learning-companion.git
cd csharp-learning-companion

# Make executable
chmod +x learn.py

# Run
./learn.py
```

No dependencies required! Pure Python 3.6+

---

## Quick Start

```bash
./learn.py
```

**Language Selection:**

On first run, the app defaults to English. Change language anytime from the main menu (option 7).

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

**메인 메뉴 (Korean):**
```
============================================================
C# / ASP.NET 학습 도우미
============================================================
진행 상황: 0개 주제 | 0개 퀴즈 | 0점
============================================================

1. 주제 둘러보기
2. 퀴즈 풀기
3. 코드 예제 보기
4. Practice Exercises
5. View Progress
6. Learning Path Recommendations
7. Exit
```

---

## Usage Examples

### Study a Topic
```
1. Browse Topics
→ Select "C# Fundamentals"
→ Review key concepts
→ Mark as completed (+10 points)
```

### Take a Quiz
```
2. Take a Quiz
→ Select "C# Fundamentals" quiz
→ Answer 3 questions
→ Get instant feedback
→ Pass with 70%+ to earn points
```

### View Code Examples
```
3. View Code Examples
→ Browse 15+ real-world examples
→ See SOLID principles in action
→ Learn ASP.NET Core patterns
```

---

## Sample Quiz Question

```
Question 1/3:
What is the difference between 'int' and 'Int32' in C#?

1. int is a keyword, Int32 is the .NET type (they're aliases)
2. int is 32-bit, Int32 is 64-bit
3. int is faster than Int32
4. There is no difference, both are deprecated

Your answer (1-4): 1

✅ Correct!
💡 Explanation: In C#, 'int' is a keyword that aliases System.Int32. 
They compile to the same IL code.
```

---

## Sample Code Example

**SOLID: Single Responsibility Principle**

```csharp
// ✅ GOOD: Separate concerns
public class UserService
{
    private readonly IEmailService _emailService;
    private readonly ILogger _logger;
    
    public UserService(IEmailService emailService, ILogger logger)
    {
        _emailService = emailService;
        _logger = logger;
    }
    
    public void CreateUser(User user)
    {
        // Create user logic
        _emailService.SendWelcomeEmail(user);
        _logger.LogActivity($"User {user.Email} created");
    }
}
```

---

## Progress Tracking

Your progress is automatically saved to `progress.json`:

```json
{
  "topics_completed": ["csharp_basics", "oop"],
  "quizzes_passed": ["csharp_basics"],
  "total_score": 45,
  "exercises_completed": 0,
  "last_activity": "2026-04-05T11:40:00",
  "started_date": "2026-04-05T11:40:00"
}
```

**Score System:**
- Complete a topic: +10 points
- Pass a quiz: +5 points per correct answer
- 70%+ required to pass

---

## Learning Paths

### Beginner Path
1. C# Fundamentals
2. Object-Oriented Programming
3. Collections and LINQ
4. ASP.NET Core Fundamentals

### Intermediate Path
1. Async/Await and Threading
2. ASP.NET Core Fundamentals
3. Entity Framework Core
4. RESTful Web APIs

### Advanced Path
1. Best Practices & Patterns
2. Advanced EF Core
3. Microservices Architecture
4. Real-world projects

---

## Practice Exercises

### Exercise 1: Create a Simple REST API
**Difficulty:** Beginner

**Tasks:**
- Create ProductsController with [ApiController]
- Implement GET /api/products
- Implement POST /api/products
- Add model validation
- Return proper HTTP status codes

### Exercise 2: Implement Repository Pattern
**Difficulty:** Intermediate

**Tasks:**
- Create IRepository<T> interface
- Implement GenericRepository<T>
- Add Unit of Work pattern
- Use dependency injection
- Write unit tests

### Exercise 3: Build Authentication System
**Difficulty:** Advanced

**Tasks:**
- Create User model and DbContext
- Implement registration endpoint
- Implement login with JWT
- Add [Authorize] attribute
- Refresh token mechanism

---

## For WinForms Developers

**Transitioning from WinForms to ASP.NET Core?**

### Key Differences
| WinForms | ASP.NET Core |
|----------|--------------|
| Event-driven (button clicks) | Request/Response (HTTP) |
| Stateful (form state) | Stateless (HTTP) |
| Windows-only | Cross-platform |
| ADO.NET | Entity Framework Core |
| Sync by default | Async by default |

### What Carries Over
✅ C# fundamentals  
✅ OOP principles  
✅ LINQ queries  
✅ Design patterns  

### New Concepts to Learn
🆕 Middleware pipeline  
🆕 Dependency injection  
🆕 RESTful APIs  
🆕 Async/await everywhere  
🆕 Configuration system  

---

## Additional Resources

**Official Documentation:**
- [Microsoft Learn](https://docs.microsoft.com/learn)
- [ASP.NET Core Docs](https://docs.microsoft.com/aspnet/core)
- [Entity Framework Core](https://docs.microsoft.com/ef/core)

**Recommended Books:**
- *C# 10 in a Nutshell* by Joseph Albahari
- *Pro ASP.NET Core 6* by Adam Freeman
- *Clean Code* by Robert C. Martin

**Online Courses:**
- Pluralsight C# Path
- Microsoft Learn Modules
- Udemy ASP.NET Core courses

---

## Use Cases

### 1. Self-Study
- Work through topics at your own pace
- Take quizzes to test understanding
- Review code examples for patterns

### 2. Interview Preparation
- Refresh C# fundamentals
- Practice SOLID principles
- Learn common interview questions

### 3. Team Training
- Onboard junior developers
- Standardize best practices
- Share code examples

### 4. Daily Practice
- Quick 15-minute sessions
- One topic per day
- Build consistent learning habits

---

## Roadmap

- [ ] Video tutorials integration
- [ ] More quizzes (50+ questions)
- [ ] Interactive code challenges
- [ ] Community-contributed examples
- [ ] Certificate generation
- [ ] Integration with GitHub (track commits)
- [ ] Real-time code execution
- [ ] Peer learning features

---

## Internationalization (i18n)

### Architecture

The app uses a **JSON-based i18n system** for easy translation:

```
csharp-learning-companion/
├── learn.py           # Main application (i18n-enabled)
├── i18n.py            # Translation engine
└── locales/
    ├── en.json        # English translations
    └── ko.json        # Korean translations
```

### Adding New Languages

1. **Create translation file:**
   ```bash
   cp locales/en.json locales/ja.json  # Japanese example
   ```

2. **Translate strings:**
   ```json
   {
     "app_title": "C# / ASP.NET 学習コンパニオン",
     "welcome": "C# / ASP.NET 学習コンパニオンへようこそ!",
     ...
   }
   ```

3. **Register language in `i18n.py`:**
   ```python
   SUPPORTED_LANGUAGES = {
       'en': 'English',
       'ko': '한국어 (Korean)',
       'ja': '日本語 (Japanese)'  # Add here
   }
   ```

4. **Test and submit PR!**

### Translation Guidelines

- **UI elements**: Fully translate (menus, prompts, feedback)
- **Technical content**: Keep in English for accuracy
  - Code examples
  - Quiz questions
  - Programming terms (MVC, LINQ, async/await)
- **Hybrid approach**: Korean UI + English technical terms works well

---

## Contributing

Contributions welcome! Add:
- **New languages** (Japanese, Spanish, Chinese, etc.)
- New topics
- Quiz questions
- Code examples
- Practice exercises

**Translation Contributors:**
- 🇰🇷 Korean: lexcellent

---

## License

MIT License

---

## Author

**lexcellent** - Enterprise WinForms developer learning ASP.NET Core

---

**Learn daily. Code confidently. Build better.** 🎓
