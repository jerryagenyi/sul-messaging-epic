

[**1\. Purpose	2**](#1.-purpose)

[**2\. Repository Structure	2**](#2.-repository-structure)

[2.1 Front-end	2](#2.1-front-end)

[2.2 Back-end	2](#2.2-back-end)

[2.2 Common	3](#2.2-common)

[**3\. Branching Strategy	3**](#3.-branching-strategy)

[3.1 Workflow	3](#3.1-workflow)

[3.2 Code flow	3](#3.2-code-flow)

[3.3 Rules	3](#3.3-rules)

[**4\. Commit Messages	4**](#4.-commit-messages)

[4.1 Examples:	4](#4.1-examples:)

[4.2 Types:	4](#4.2-types:)

[**5\. Pull Request Guidelines	5**](#5.-pull-request-guidelines)

[**6\. Code Reviews	5**](#6.-code-reviews)

[**7\. Version Control	5**](#7.-version-control)

[7.1 Semantic Versioning Format	5](#7.1-semantic-versioning-format)

[7.2 File Naming Conventions	6](#7.2-file-naming-conventions)

[7.3 Dependency Management	6](#7.3-dependency-management)

[**8\. Security Practices	7**](#8.-security-practices)

[**9\. Issue Management	7**](#9.-issue-management)

[**10\. Documentation Standards	7**](#10.-documentation-standards)

[**11\. Commits to Server(s)	7**](#11.-commits-to-server\(s\))

# 1\. Purpose {#1.-purpose}

This document outlines the rules, guidelines, and best practices for managing the GitHub repositories for our project. The front-end uses Vue 3 with Tailwind CSS, and the back-end uses PHP.

# 2\. Repository Structure {#2.-repository-structure}

## 2.1 Front-end {#2.1-front-end}

* **src/** \- Vue components, Tailwind styles, and Assets  
* **public/** \- Publicly accessible files  
* **tests/** \- Unit and integration tests  
* **Package.json** \- Project dependencies and scripts

## 2.2 Back-end {#2.2-back-end}

* **app/**  
* **routes/**  
* **databases/**  
* **tests/**  
* **bootstrap/**  
* **config/**  
* **public/**  
* **resources/**  
* **storage/**  
* **Composer.json**  
* **Package.json**

***Please visit the Github repo for the latest structure.***

## 2.2 Common {#2.2-common}

* **.github/** \- Github Actions workflow and templates  
* **README.md** \- Project overview and setup instructions  
* **.env** \- Environment variable template 

# 3\. Branching Strategy {#3.-branching-strategy}

## 3.1 Workflow {#3.1-workflow}

We follow the Gitflow Workflow. The following branches are used:

* **develop/** \- Contains code ready for the next release  
* **feature/** \- Used for developing new features *(e.g. feat/new-ui)*  
* **fix/** \- Used for fixing bugs in the development phase *(e.g. fix/volunteer-registration)*  
* **hotfix/** \- Used for fixing bugs in production *(e.g. hotfix/login-bug)*  
* **testing/** \- Contains production-read code for rigorous testing by QAs  
* **staging/** \- Prepare for a new production release, this branch is used for final testing *(UAT: User Acceptance Testing)*  
* **production/** \- Production release *(tagged with version number: v2.0.0)*

## 3.2 Code flow {#3.2-code-flow}

Process flow for development:

**\-\> feat/, fix/** merged to **develop/** after review and testing  
**\-\>** **develop/** to **testing/** for QA testing  
**\-\>** **testing/** to **staging/**: After successful testing for UAT   
**\-\>** **staging/** to **production/** *(tagged with version number: v2.0.0)*

## 3.3 Rules {#3.3-rules}

* Always branch off from **develop/** for features  
* Merge **feature/** branches into **develop/** only after code review  
* Ensure **main/** is protected with pull request requirements.

# 4\. Commit Messages {#4.-commit-messages}

Follow the Conventional Commit format:  
**\<type\>(\<scope\>): \<short description\>**

## 4.1 Examples: {#4.1-examples:}

* feat(ui): add dark mode toggle

* feat(auth): resolve login redirect issues

* docs(readme): update setup instructions

**Please note**: 

* *Use short descriptions*  
* *For branch names:*  
  * ***Do not** use spaces, colons or brackets*   
  * *Only forward slashes are allowed*  
  * Example: **feat/addProfilePicture**

## 4.2 Types: {#4.2-types:}

* **feat:** New feature  
* **fix:** Bug fix  
* **docs:** Documentation changes  
* **style:** Code style changes (non-functional)

*COMMENT: As we are using tailwind, a lot of times the styling will be done at the same time as the functionality development. It would be impractical to use two types*

* **refactor:** Code refactoring

*COMMENT: Most of the time, refactoring is done on the original branch*

* **test:** Adding or updating tests  
* **chore:** Miscellaneous tasks

# 5\. Pull Request Guidelines {#5.-pull-request-guidelines}

* Always create pull request for merging code  
* Assign at least one reviewer for code reviews  
* Add a clear description summarizing the changes  
* Link to relevant issue(s) in the PR description  
* Ensure all test pass before requesting a review  
* Use labels (e.g bug, review-ready, draft, documentation)

# 6\. Code Reviews {#6.-code-reviews}

Reviewers must:

* Check for adherence to coding standards  
* Ensure proper testing coverage  
* Suggest improvements or refactoring where necessary

The author must:

* Address all comments before merging  
* Re-request reviews after making changes

# 7\. Version Control {#7.-version-control}

This section refers to managing the progression of the project versions using semantic versioning (SemVer). It’s a standardised way to communicate the nature of changes in a release.

## 7.1 Semantic Versioning Format {#7.1-semantic-versioning-format}

MAJOR.MINOR.PATCH

* **MAJOR:** Increment this number when changes made are not compatible with the current functionality and might break the applications known flow to the existing users.    
  * Example: 1.0.0 → 2.0.0 (a breaking change is introduced)  
* **MINOR:** Increment this number when added features are backward-compatible, meaning existing functionality will continue to work as expected.   
  * Example: 1.1.2 → 1.2.0 (a new feature is added, like a new API endpoint)  
* **PATCH:** Increment this number for bug fixes or very small backward-compatible improvements, like resolving a typo or fixing a minor issue without affecting the existing functionality. 

  * Example: 1.1.0 → 1.1.1 (a minor bug fix is applied)

## 7.2 File Naming Conventions {#7.2-file-naming-conventions}

**Frontend:**

* Use PascalCase for components (e.g. UserCard.vue)  
* Use kebab-case for files (e.g. string-formatter.js, date-helper.js), folder names (utils/, data-services/)  
* Use camelCase for functions and variables (e.g. getUserData)

**Backend:** [asinsala@skilledup.life](mailto:asinsala@skilledup.life)

## 7.3 Dependency Management {#7.3-dependency-management}

**Frontend:**

* NPM for managing packages  
* \*\*\*Run npm audit regularly (can be discussed further with dev team)

**Backend:**

* NPM for managing packages

# 8\. Security Practices {#8.-security-practices}

* Store secrets in environment variable (never in code)  
* Regularly review and update dependencies (if need be)  
* Use .env files for configurations (never to be committed to repository)

# 9\. Issue Management {#9.-issue-management}

* Use GitHub Issues to track tasks and bugs  
* Apply appropriate labels  
  * Bug, enhancement, documentation, etc  
* Assign issue to team members

# 10\. Documentation Standards {#10.-documentation-standards}

* Maintain updated README.md file  
* Include detailed comments in code (where applicable)  
* Create CONTRIBUTING.md to guide external or incoming developers.

# 11\. Commits to Server(s) {#11.-commits-to-server(s)}

Initially, we will run V2 on a single production server with another for development. A staging server can be set up just to test the code before committing to production if needed for subsequent releases after V2.001.

