#!/usr/bin/env python3
"""
C# / ASP.NET Learning Companion (Internationalized)
Interactive learning tool for C# and ASP.NET developers.

NOW SUPPORTS MULTIPLE LANGUAGES! 🌍
- English
- 한국어 (Korean)

Perfect for:
- WinForms developers learning ASP.NET Core
- Junior developers learning C# fundamentals
- Self-study and skill assessment
- Korean-speaking developers

Author: lexcellent
License: MIT
Version: 2.0.0 (i18n)
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
import random

# Import i18n module
from i18n import get_i18n, t


@dataclass
class LearningProgress:
    """Track user's learning progress."""
    topics_completed: List[str]
    quizzes_passed: List[str]
    total_score: int
    exercises_completed: int
    last_activity: str
    started_date: str
    language: str = 'en'  # NEW: Store user's language preference
    
    def save(self, filepath: str = "progress.json"):
        """Save progress to file."""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(asdict(self), f, indent=2, ensure_ascii=False)
    
    @classmethod
    def load(cls, filepath: str = "progress.json"):
        """Load progress from file."""
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return cls(**data)
        return cls(
            topics_completed=[],
            quizzes_passed=[],
            total_score=0,
            exercises_completed=0,
            last_activity=datetime.now().isoformat(),
            started_date=datetime.now().isoformat(),
            language='en'
        )


class CSharpLearningCompanion:
    """Main learning companion class (internationalized)."""
    
    def __init__(self):
        """Initialize learning companion."""
        self.progress = LearningProgress.load()
        self.i18n = get_i18n()
        
        # Set language from saved progress
        self.i18n.set_language(self.progress.language)
        
        self.topics = self._load_topics()
        self.quizzes = self._load_quizzes()
        self.code_examples = self._load_code_examples()
    
    def _load_topics(self) -> Dict[str, Dict]:
        """Load learning topics (content remains in English for technical accuracy)."""
        return {
            "csharp_basics": {
                "subtopics": [
                    "Variables and Data Types",
                    "Control Flow (if, switch, loops)",
                    "Methods and Parameters",
                    "Classes and Objects",
                    "Properties and Fields",
                    "Constructors and Destructors"
                ]
            },
            "oop": {
                "subtopics": [
                    "Encapsulation",
                    "Inheritance",
                    "Polymorphism",
                    "Abstraction",
                    "Interfaces vs Abstract Classes",
                    "SOLID Principles"
                ]
            },
            "collections": {
                "subtopics": [
                    "List<T> and Arrays",
                    "Dictionary and HashSet",
                    "LINQ Basics (Where, Select, OrderBy)",
                    "Lambda Expressions",
                    "Deferred Execution",
                    "IEnumerable vs IQueryable"
                ]
            },
            "async": {
                "subtopics": [
                    "async and await keywords",
                    "Task and Task<T>",
                    "Async Best Practices",
                    "Thread Safety",
                    "ConfigureAwait",
                    "Parallel Programming"
                ]
            },
            "aspnet_core": {
                "subtopics": [
                    "MVC Pattern",
                    "Controllers and Actions",
                    "Routing",
                    "Dependency Injection",
                    "Middleware Pipeline",
                    "Configuration and Options"
                ]
            },
            "entity_framework": {
                "subtopics": [
                    "DbContext and DbSet",
                    "Code-First vs Database-First",
                    "LINQ to Entities",
                    "Migrations",
                    "Relationships (1:1, 1:N, N:N)",
                    "Performance Optimization"
                ]
            },
            "web_api": {
                "subtopics": [
                    "REST Principles",
                    "HTTP Verbs (GET, POST, PUT, DELETE)",
                    "Action Results",
                    "Model Binding and Validation",
                    "Authentication (JWT)",
                    "API Versioning"
                ]
            },
            "best_practices": {
                "subtopics": [
                    "Repository Pattern",
                    "Unit of Work Pattern",
                    "Dependency Injection",
                    "Error Handling",
                    "Logging (Serilog, NLog)",
                    "Unit Testing (xUnit, NUnit)"
                ]
            }
        }
    
    def _load_quizzes(self) -> Dict[str, List[Dict]]:
        """Load quiz questions (kept in English for technical accuracy)."""
        return {
            "csharp_basics": [
                {
                    "question": "What is the difference between 'int' and 'Int32' in C#?",
                    "options": [
                        "int is a keyword, Int32 is the .NET type (they're aliases)",
                        "int is 32-bit, Int32 is 64-bit",
                        "int is faster than Int32",
                        "There is no difference, both are deprecated"
                    ],
                    "correct": 0,
                    "explanation": "In C#, 'int' is a keyword that aliases System.Int32. They compile to the same IL code."
                },
                {
                    "question": "What does the 'sealed' keyword do when applied to a class?",
                    "options": [
                        "Makes the class thread-safe",
                        "Prevents the class from being inherited",
                        "Makes all methods in the class final",
                        "Encrypts the class data"
                    ],
                    "correct": 1,
                    "explanation": "The 'sealed' keyword prevents other classes from inheriting from it."
                },
                {
                    "question": "What is the output of: Console.WriteLine(5 / 2);",
                    "options": [
                        "2.5",
                        "2",
                        "3",
                        "Compiler error"
                    ],
                    "correct": 1,
                    "explanation": "Integer division truncates the decimal. Use 5.0 / 2 or (double)5 / 2 for 2.5."
                }
            ],
            "oop": [
                {
                    "question": "When should you use an interface instead of an abstract class?",
                    "options": [
                        "When you need to define behavior without implementation",
                        "When you want multiple inheritance",
                        "When classes are unrelated but share a contract",
                        "All of the above"
                    ],
                    "correct": 3,
                    "explanation": "Interfaces allow multiple inheritance, define contracts without implementation, and work across unrelated class hierarchies."
                },
                {
                    "question": "What is the 'virtual' keyword used for?",
                    "options": [
                        "Creating virtual machines",
                        "Allowing a method to be overridden in derived classes",
                        "Making a method run faster",
                        "Preventing a method from being called"
                    ],
                    "correct": 1,
                    "explanation": "'virtual' allows derived classes to override the method using the 'override' keyword."
                }
            ],
            "aspnet_core": [
                {
                    "question": "What is the role of the Startup.cs file in ASP.NET Core?",
                    "options": [
                        "Define database connection strings",
                        "Configure services and middleware pipeline",
                        "Define routing rules",
                        "Handle user authentication"
                    ],
                    "correct": 1,
                    "explanation": "Startup.cs configures dependency injection (ConfigureServices) and the middleware pipeline (Configure)."
                },
                {
                    "question": "What does [ApiController] attribute do in ASP.NET Core?",
                    "options": [
                        "Enables automatic model validation",
                        "Infers parameter binding sources",
                        "Returns 400 for invalid models",
                        "All of the above"
                    ],
                    "correct": 3,
                    "explanation": "[ApiController] enables API-specific behaviors: model validation, binding source inference, and problem details."
                }
            ],
            "entity_framework": [
                {
                    "question": "What does 'AsNoTracking()' do in EF Core?",
                    "options": [
                        "Disables change tracking for better read performance",
                        "Prevents database updates",
                        "Disables lazy loading",
                        "Removes tracking from the database"
                    ],
                    "correct": 0,
                    "explanation": "AsNoTracking() disables EF's change tracker, improving performance for read-only queries."
                },
                {
                    "question": "What is the difference between Include() and ThenInclude()?",
                    "options": [
                        "Include loads related data, ThenInclude loads nested related data",
                        "ThenInclude is faster",
                        "Include is for 1:1, ThenInclude for 1:N",
                        "No difference"
                    ],
                    "correct": 0,
                    "explanation": "Include() eagerly loads related entities. ThenInclude() loads entities related to the included entity."
                }
            ]
        }
    
    def _load_code_examples(self) -> Dict[str, List[Dict]]:
        """Load code examples (kept in English - code is universal)."""
        return {
            "csharp_basics": [
                {
                    "title": "Properties vs Fields",
                    "code": """// Field (direct variable access)
private string name;

// Property (encapsulated access)
public string Name 
{ 
    get { return name; } 
    set { name = value; } 
}

// Auto-property (C# 3.0+)
public string Email { get; set; }

// Property with validation
private int age;
public int Age 
{
    get { return age; }
    set 
    {
        if (value < 0 || value > 150)
            throw new ArgumentException("Invalid age");
        age = value;
    }
}""",
                    "explanation": "Properties provide encapsulation and validation. Use auto-properties when no logic is needed."
                },
                {
                    "title": "Nullable Reference Types (C# 8.0+)",
                    "code": """// Enable in .csproj: <Nullable>enable</Nullable>

// Non-nullable reference (default)
string name = "John";  // Cannot be null

// Nullable reference
string? middleName = null;  // Can be null

// Null-conditional operator
int? length = middleName?.Length;

// Null-coalescing operator
string display = middleName ?? "N/A";

// Null-forgiving operator (use carefully!)
string upper = middleName!.ToUpper();  // Assumes not null""",
                    "explanation": "Nullable reference types help catch null reference exceptions at compile time."
                }
            ],
            "oop": [
                {
                    "title": "SOLID: Single Responsibility Principle",
                    "code": """// ❌ BAD: Multiple responsibilities
public class UserService
{
    public void CreateUser(User user) { /* ... */ }
    public void SendWelcomeEmail(User user) { /* ... */ }
    public void LogActivity(string message) { /* ... */ }
}

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
}""",
                    "explanation": "Each class should have one reason to change. Separate concerns into focused classes."
                }
            ],
            "aspnet_core": [
                {
                    "title": "Dependency Injection in ASP.NET Core",
                    "code": """// 1. Define interface
public interface IProductService
{
    Task<List<Product>> GetAllAsync();
}

// 2. Implement service
public class ProductService : IProductService
{
    private readonly ApplicationDbContext _context;
    
    public ProductService(ApplicationDbContext context)
    {
        _context = context;
    }
    
    public async Task<List<Product>> GetAllAsync()
    {
        return await _context.Products.ToListAsync();
    }
}

// 3. Register in Program.cs (ASP.NET Core 6+)
builder.Services.AddScoped<IProductService, ProductService>();

// 4. Inject in controller
public class ProductsController : ControllerBase
{
    private readonly IProductService _productService;
    
    public ProductsController(IProductService productService)
    {
        _productService = productService;
    }
    
    [HttpGet]
    public async Task<IActionResult> GetAll()
    {
        var products = await _productService.GetAllAsync();
        return Ok(products);
    }
}""",
                    "explanation": "DI promotes loose coupling and testability. Use Scoped for per-request services, Singleton for app-lifetime, Transient for lightweight services."
                }
            ],
            "entity_framework": [
                {
                    "title": "EF Core: Efficient Queries",
                    "code": """// ❌ BAD: Loads all data into memory
var users = context.Users.ToList()
    .Where(u => u.Age > 18)
    .OrderBy(u => u.Name);

// ✅ GOOD: Filters in database
var users = context.Users
    .Where(u => u.Age > 18)
    .OrderBy(u => u.Name)
    .ToList();

// ✅ BETTER: Project to DTO (select only needed fields)
var userDtos = context.Users
    .Where(u => u.Age > 18)
    .Select(u => new UserDto 
    { 
        Id = u.Id, 
        Name = u.Name 
    })
    .ToList();

// ✅ BEST: Use AsNoTracking for read-only queries
var users = context.Users
    .AsNoTracking()
    .Where(u => u.Age > 18)
    .ToList();""",
                    "explanation": "Always filter in the database (before ToList). Use projections and AsNoTracking for performance."
                }
            ],
            "web_api": [
                {
                    "title": "RESTful API Best Practices",
                    "code": """[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    // GET api/products
    [HttpGet]
    public async Task<ActionResult<List<ProductDto>>> GetAll()
    {
        var products = await _service.GetAllAsync();
        return Ok(products);  // 200 OK
    }
    
    // GET api/products/5
    [HttpGet("{id}")]
    public async Task<ActionResult<ProductDto>> GetById(int id)
    {
        var product = await _service.GetByIdAsync(id);
        if (product == null)
            return NotFound();  // 404 Not Found
        return Ok(product);
    }
    
    // POST api/products
    [HttpPost]
    public async Task<ActionResult<ProductDto>> Create(CreateProductDto dto)
    {
        if (!ModelState.IsValid)
            return BadRequest(ModelState);  // 400 Bad Request
        
        var product = await _service.CreateAsync(dto);
        return CreatedAtAction(nameof(GetById), 
            new { id = product.Id }, product);  // 201 Created
    }
    
    // PUT api/products/5
    [HttpPut("{id}")]
    public async Task<IActionResult> Update(int id, UpdateProductDto dto)
    {
        var updated = await _service.UpdateAsync(id, dto);
        if (!updated)
            return NotFound();
        return NoContent();  // 204 No Content
    }
    
    // DELETE api/products/5
    [HttpDelete("{id}")]
    public async Task<IActionResult> Delete(int id)
    {
        var deleted = await _service.DeleteAsync(id);
        if (!deleted)
            return NotFound();
        return NoContent();
    }
}""",
                    "explanation": "Use proper HTTP verbs and status codes. Return ActionResult<T> for type safety."
                }
            ]
        }
    
    def show_menu(self):
        """Display main menu (localized)."""
        print("\n" + "="*60)
        print(t('app_title'))
        print("="*60)
        print(t('progress_summary', 
                topics=len(self.progress.topics_completed),
                quizzes=len(self.progress.quizzes_passed),
                score=self.progress.total_score))
        print("="*60)
        print(f"\n1. {t('menu.browse_topics')}")
        print(f"2. {t('menu.take_quiz')}")
        print(f"3. {t('menu.view_examples')}")
        print(f"4. {t('menu.practice')}")
        print(f"5. {t('menu.view_progress')}")
        print(f"6. {t('menu.recommendations')}")
        print(f"7. {t('menu.change_language')} 🌍")
        print(f"8. {t('menu.exit')}")
        print()
    
    def change_language(self):
        """Change interface language."""
        print("\n" + "="*60)
        print(t('language.select'))
        print("="*60)
        
        languages = self.i18n.list_languages()
        for idx, (code, name) in enumerate(languages.items(), 1):
            current = "✓" if code == self.i18n.current_language else " "
            print(f"{idx}. [{current}] {name} ({code})")
        
        choice = input(f"\n{t('prompts.enter_choice')} (1-{len(languages)}): ")
        
        if choice.isdigit() and 1 <= int(choice) <= len(languages):
            lang_code = list(languages.keys())[int(choice) - 1]
            self.i18n.set_language(lang_code)
            self.progress.language = lang_code
            self.progress.save()
            print(f"\n✅ {t('language.changed', lang=self.i18n.get_language_name())}")
            input(f"\n{t('prompts.press_enter')}")
    
    def browse_topics(self):
        """Browse available topics (localized)."""
        print("\n" + "="*60)
        print(t('headers.learning_topics'))
        print("="*60)
        
        for idx, (key, topic) in enumerate(self.topics.items(), 1):
            completed = "✅" if key in self.progress.topics_completed else "⬜"
            print(f"\n{idx}. {completed} {t(f'topics.{key}.title')}")
            print(f"   {t(f'topics.{key}.description')}")
            print(f"   Subtopics:")
            for subtopic in topic['subtopics']:
                print(f"     • {subtopic}")
        
        choice = input(f"\n{t('prompts.enter_topic')}: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.topics):
            topic_key = list(self.topics.keys())[int(choice) - 1]
            self.study_topic(topic_key)
    
    def study_topic(self, topic_key: str):
        """Study a specific topic."""
        topic = self.topics[topic_key]
        print("\n" + "="*60)
        print(f"{t('headers.learning_topics').replace('LEARNING TOPICS', 'STUDYING')}: {t(f'topics.{topic_key}.title')}")
        print("="*60)
        print(f"\n{t(f'topics.{topic_key}.description')}\n")
        
        print("Key Concepts:")
        for subtopic in topic['subtopics']:
            print(f"  • {subtopic}")
        
        if topic_key in self.code_examples:
            print(f"\nAvailable Code Examples: {len(self.code_examples[topic_key])}")
        
        input(f"\n{t('prompts.press_mark_complete')}")
        
        if topic_key not in self.progress.topics_completed:
            self.progress.topics_completed.append(topic_key)
            self.progress.total_score += 10
            self.progress.save()
            print(f"✅ {t('feedback.topic_completed')}")
    
    def take_quiz(self):
        """Take a quiz (localized interface, English questions)."""
        print("\n" + "="*60)
        print(t('headers.available_quizzes'))
        print("="*60)
        
        for idx, (key, questions) in enumerate(self.quizzes.items(), 1):
            passed = "✅" if key in self.progress.quizzes_passed else "⬜"
            topic_title = t(f'topics.{key}.title')
            print(f"{idx}. {passed} {topic_title} ({len(questions)} questions)")
        
        choice = input(f"\n{t('prompts.enter_quiz')}: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.quizzes):
            quiz_key = list(self.quizzes.keys())[int(choice) - 1]
            self.run_quiz(quiz_key)
    
    def run_quiz(self, quiz_key: str):
        """Run a specific quiz."""
        questions = self.quizzes[quiz_key]
        topic_title = t(f'topics.{quiz_key}.title')
        
        print("\n" + "="*60)
        print(f"QUIZ: {topic_title}")
        print("="*60)
        
        score = 0
        for idx, q in enumerate(questions, 1):
            print(f"\nQuestion {idx}/{len(questions)}:")
            print(q['question'])
            print()
            
            for opt_idx, option in enumerate(q['options']):
                print(f"{opt_idx + 1}. {option}")
            
            answer = input(f"\n{t('prompts.your_answer')}: ")
            
            if answer.isdigit() and int(answer) - 1 == q['correct']:
                print(f"✅ {t('feedback.correct')}")
                score += 1
            else:
                print(f"❌ {t('feedback.incorrect', answer=q['correct'] + 1)}")
            
            print(f"💡 {t('feedback.explanation')}: {q['explanation']}")
            input(f"\n{t('prompts.next_question')}")
        
        percentage = (score / len(questions)) * 100
        print("\n" + "="*60)
        print(t('headers.quiz_results'))
        print("="*60)
        print(f"{t('progress.score_label')}: {score}/{len(questions)} ({percentage:.0f}%)")
        
        if percentage >= 70:
            print(f"🎉 {t('feedback.passed')}")
            if quiz_key not in self.progress.quizzes_passed:
                self.progress.quizzes_passed.append(quiz_key)
                self.progress.total_score += score * 5
                self.progress.save()
                print(f"✅ {t('feedback.quiz_completed', points=score * 5)}")
        else:
            print(f"📚 {t('feedback.keep_studying')}")
    
    def view_code_examples(self):
        """View code examples."""
        print("\n" + "="*60)
        print(t('headers.code_examples'))
        print("="*60)
        
        all_examples = []
        for topic_key, examples in self.code_examples.items():
            topic_title = t(f'topics.{topic_key}.title')
            for example in examples:
                all_examples.append((topic_title, example))
        
        for idx, (topic, example) in enumerate(all_examples, 1):
            print(f"\n{idx}. [{topic}] {example['title']}")
        
        choice = input(f"\n{t('prompts.enter_example')}: ")
        if choice.isdigit() and 1 <= int(choice) <= len(all_examples):
            _, example = all_examples[int(choice) - 1]
            self.show_code_example(example)
    
    def show_code_example(self, example: Dict):
        """Display a code example."""
        print("\n" + "="*60)
        print(example['title'])
        print("="*60)
        print("\n" + example['code'])
        print("\n" + "-"*60)
        print("💡 " + example['explanation'])
        print("="*60)
        input(f"\n{t('prompts.press_enter')}")
    
    def practice_exercises(self):
        """Show practice exercises (localized)."""
        print("\n" + "="*60)
        print(t('headers.practice_exercises'))
        print("="*60)
        
        exercises_keys = ['simple_api', 'repository_pattern', 'authentication']
        exercises = []
        
        for key in exercises_keys:
            exercises.append({
                "title": t(f'exercises.{key}.title'),
                "description": t(f'exercises.{key}.description'),
                "difficulty": t(f'exercises.{key}.difficulty')
            })
        
        # Hard-coded tasks (kept in English for technical terms)
        tasks = [
            [
                "Create ProductsController with [ApiController]",
                "Implement GET /api/products",
                "Implement POST /api/products",
                "Add model validation with DataAnnotations",
                "Return proper HTTP status codes"
            ],
            [
                "Create IRepository<T> interface",
                "Implement GenericRepository<T>",
                "Add Unit of Work pattern",
                "Use dependency injection",
                "Write unit tests"
            ],
            [
                "Create User model and DbContext",
                "Implement registration endpoint",
                "Implement login with JWT",
                "Add [Authorize] attribute",
                "Refresh token mechanism"
            ]
        ]
        
        for idx, (exercise, task_list) in enumerate(zip(exercises, tasks), 1):
            print(f"\n{idx}. {exercise['title']} [{exercise['difficulty']}]")
            print(f"   {exercise['description']}")
            print("   Tasks:")
            for task in task_list:
                print(f"     ☐ {task}")
        
        input(f"\n{t('prompts.press_enter')}")
    
    def view_progress(self):
        """View learning progress (localized)."""
        print("\n" + "="*60)
        print(t('headers.your_progress'))
        print("="*60)
        
        started = datetime.fromisoformat(self.progress.started_date)
        days_learning = (datetime.now() - started).days
        
        print(f"\n📅 {t('progress.started')}: {started.strftime('%Y-%m-%d')}")
        print(f"⏱️  {t('progress.days_learning')}: {days_learning}")
        print(f"🎯 {t('progress.total_score')}: {self.progress.total_score} points")
        print(f"\n📚 {t('progress.topics_completed')}: {len(self.progress.topics_completed)}/{len(self.topics)}")
        
        for topic_key in self.progress.topics_completed:
            print(f"  ✅ {t(f'topics.{topic_key}.title')}")
        
        print(f"\n📝 {t('progress.quizzes_passed')}: {len(self.progress.quizzes_passed)}/{len(self.quizzes)}")
        
        for quiz_key in self.progress.quizzes_passed:
            print(f"  ✅ {t(f'topics.{quiz_key}.title')}")
        
        total_items = len(self.topics) + len(self.quizzes)
        completed_items = len(self.progress.topics_completed) + len(self.progress.quizzes_passed)
        completion = (completed_items / total_items) * 100 if total_items > 0 else 0
        
        print(f"\n📊 {t('progress.overall_completion')}: {completion:.0f}%")
        
        input(f"\n{t('prompts.press_enter')}")
    
    def learning_recommendations(self):
        """Provide personalized learning recommendations (localized)."""
        print("\n" + "="*60)
        print(t('headers.learning_path'))
        print("="*60)
        
        completed_topics = len(self.progress.topics_completed)
        
        if completed_topics == 0:
            print(f"\n🎯 {t('recommendations.beginner_path')}")
            print(f"\n{t('recommendations.start_with')}")
            print(f"1. {t('topics.csharp_basics.title')}")
            print(f"2. {t('topics.oop.title')}")
            print(f"3. {t('topics.collections.title')}")
            print(f"\n{t('recommendations.once_comfortable')}")
            print(f"4. {t('topics.aspnet_core.title')}")
        
        elif completed_topics < 4:
            print(f"\n🎯 {t('recommendations.intermediate_path')}")
            print(f"\n{t('recommendations.focus_on')}")
            print(f"1. {t('topics.async.title')}")
            print(f"2. {t('topics.aspnet_core.title')}")
            print(f"3. {t('topics.entity_framework.title')}")
        
        else:
            print(f"\n🎯 {t('recommendations.advanced_path')}")
            print(f"\n{t('recommendations.deepen_knowledge')}")
            print(f"1. {t('topics.web_api.title')}")
            print(f"2. {t('topics.best_practices.title')}")
            print("3. Advanced EF Core (performance tuning)")
            print(f"\n{t('recommendations.next_steps')}")
            print(f"• {t('recommendations.build_projects')}")
            print(f"• {t('recommendations.contribute_opensource')}")
            print(f"• {t('recommendations.learn_microservices')}")
        
        print(f"\n💡 {t('recommendations.additional_resources')}")
        print("• Microsoft Learn (docs.microsoft.com/learn)")
        print("• Pluralsight C# Path")
        print("• ASP.NET Core documentation")
        print("• Entity Framework Core tutorials")
        
        input(f"\n{t('prompts.press_enter')}")
    
    def run(self):
        """Main application loop."""
        print(f"\n🎓 {t('welcome')}")
        print(t('current_score', score=self.progress.total_score))
        
        while True:
            self.show_menu()
            choice = input(f"{t('prompts.enter_choice')} (1-8): ")
            
            if choice == '1':
                self.browse_topics()
            elif choice == '2':
                self.take_quiz()
            elif choice == '3':
                self.view_code_examples()
            elif choice == '4':
                self.practice_exercises()
            elif choice == '5':
                self.view_progress()
            elif choice == '6':
                self.learning_recommendations()
            elif choice == '7':
                self.change_language()
            elif choice == '8':
                self.progress.last_activity = datetime.now().isoformat()
                self.progress.save()
                print(f"\n✅ {t('feedback.progress_saved')}")
                break
            else:
                print(f"❌ {t('feedback.invalid_choice')}")


def main():
    """Main entry point."""
    try:
        companion = CSharpLearningCompanion()
        companion.run()
    except KeyboardInterrupt:
        print(f"\n\n✅ {t('feedback.goodbye')}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
