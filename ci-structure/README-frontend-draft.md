# SkilledUp.Life Frontend (Vue.js)

> **Version 2 Frontend** - Vue.js application for SkilledUp.Life platform

## 🚀 Development Setup

### Prerequisites
- Node.js 18+ 
- npm or yarn

### Quick Start
1. Install dependencies: `npm install`
2. Run linting: `npm run lint`
3. Check formatting: `npm run format`
4. Fix formatting: `npm run format:fix`

### CI/CD Workflow
This project uses automated CI/CD for code quality:
- **ESLint** - Code quality and error detection
- **Prettier** - Code formatting consistency
- **GitHub Actions** - Automated checks on every PR
- **Regression Testing** - Automated smoke tests to prevent breaking changes

### Before Submitting PRs
- [ ] Run `npm run lint` to check for code issues
- [ ] Run `npm run format` to ensure proper formatting
- [ ] Fix any linting or formatting errors locally
- [ ] CI will automatically check your code on PR submission

### Test Coverage
Track our test coverage progress: [Test Coverage Tracker](https://docs.google.com/spreadsheets/d/1q2xA4L0VjMm7GEi-NSbk-X55E4FXBHt9O2PLc0jlqhk/edit?gid=0#gid=0)

### IDE Setup
We recommend installing these VS Code extensions:
- ESLint
- Prettier
- Vue Language Features (Volar)

## 📁 Project Structure

```
├── .github/
│   └── workflows/     # GitHub Actions CI/CD workflows
├── .vscode/           # VS Code workspace settings
├── public/            # Static assets and index.html
│   ├── images/        # Static images
│   ├── LogoRectangle.svg
│   └── vite.svg
├── src/               # Source code
│   ├── api/           # API integration
│   ├── assets/        # Static assets (images, styles)
│   ├── components/    # Vue components
│   ├── composables/   # Vue composables
│   ├── constants/     # Application constants
│   ├── data/          # Data files
│   ├── helper/        # Helper functions
│   ├── layouts/       # Layout components
│   ├── pages/         # Page components
│   ├── routes/        # Route definitions
│   ├── store/         # State management
│   ├── styles/        # CSS/SCSS files
│   ├── tailwind-theme-objects/  # Tailwind theme objects
│   ├── ui-kit/        # UI component library
│   ├── utils/         # Utility functions
│   ├── App.vue        # Main app component
│   ├── main.js        # Application entry point
│   └── style.css      # Global styles
├── .gitignore         # Git ignore rules
├── .prettierrc.json   # Prettier configuration
├── index.html         # Main HTML template
├── package.json       # Dependencies and scripts
├── postcss.config.js  # PostCSS configuration
├── tailwind.config.js # Tailwind CSS configuration
└── vite.config.js     # Vite build configuration
```

## 🛠️ Available Scripts

```bash
# Development
npm run dev        # Start development server
npm run build      # Build for production

# Code Quality
npm run lint       # Run ESLint
npm run format     # Check Prettier formatting
npm run format:fix # Fix Prettier formatting

# Testing
npm run test       # Run Jest tests
npm run test:unit  # Run unit tests (if configured)
npm run test:e2e   # Run E2E tests (if configured)
npm run test:regression # Run regression tests (future)
```

## 🔧 Configuration Files

- `.eslintrc.js` - ESLint configuration
- `.prettierrc.json` - Prettier configuration
- `vite.config.js` - Vite build configuration
- `tailwind.config.js` - Tailwind CSS configuration
- `postcss.config.js` - PostCSS configuration

## 📚 Documentation

- [Vue.js Documentation](https://vuejs.org/)
- [Vite Documentation](https://vitejs.dev/)
- [ESLint Documentation](https://eslint.org/)
- [Prettier Documentation](https://prettier.io/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run linting and formatting checks
5. Submit a pull request

## 📄 License

This project is part of SkilledUp.Life platform. 