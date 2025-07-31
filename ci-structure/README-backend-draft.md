# SkilledUp.Life Backend (Laravel)

> **Version 2 Backend** - Laravel API for SkilledUp.Life platform

## 🚀 Development Setup

### Prerequisites
- PHP 8.1+
- Composer
- Laravel CLI

### Quick Start
1. Install dependencies: `composer install`
2. Copy environment: `cp .env.example .env`
3. Generate key: `php artisan key:generate`
4. Run tests: `php artisan test`

### CI/CD Workflow
This project uses automated CI/CD for code quality:
- **PHPStan** - Static analysis and error detection
- **Laravel Pint** - Code formatting consistency
- **GitHub Actions** - Automated checks on every PR

### Before Submitting PRs
- [ ] Run `composer run lint` to check for code issues
- [ ] Run `composer run format` to ensure proper formatting
- [ ] Run `composer run test` to verify tests pass
- [ ] Fix any linting, formatting, or test errors locally
- [ ] CI will automatically check your code on PR submission

### Test Coverage
Track our test coverage progress: [Test Coverage Tracker](https://docs.google.com/spreadsheets/d/1q2xA4L0VjMm7GEi-NSbk-X55E4FXBHt9O2PLc0jlqhk/edit?gid=0#gid=0)

### IDE Setup
We recommend installing these VS Code extensions:
- PHP Intelephense
- Laravel Blade Snippets
- PHP Debug

## 📁 Project Structure

```
app/
├── Http/
│   ├── Controllers/    # API Controllers
│   ├── Middleware/     # Custom middleware
│   └── Requests/       # Form requests
├── Models/             # Eloquent models
├── Services/           # Business logic
└── Providers/          # Service providers

database/
├── migrations/         # Database migrations
├── seeders/           # Database seeders
└── factories/         # Model factories

tests/
├── Feature/           # Feature tests
└── Unit/              # Unit tests

routes/
├── api.php            # API routes
└── web.php            # Web routes
```

## 🛠️ Available Scripts

```bash
# Development
php artisan serve      # Start development server
php artisan migrate    # Run migrations
php artisan seed       # Run seeders

# Code Quality
composer run lint      # Run PHPStan
composer run format    # Check Laravel Pint formatting
composer run test      # Run tests

# Database
php artisan migrate:fresh --seed  # Reset database with seeders
php artisan db:seed               # Run seeders only
```

## 🔧 Configuration Files

- `phpstan.neon` - PHPStan configuration
- `.env.example` - Environment variables template
- `composer.json` - PHP dependencies and scripts

## 📚 Documentation

- [Laravel Documentation](https://laravel.com/docs)
- [PHPStan Documentation](https://phpstan.org/)
- [Laravel Pint Documentation](https://laravel.com/docs/pint)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run linting, formatting, and tests
5. Submit a pull request

## 📄 License

This project is part of SkilledUp.Life platform. 