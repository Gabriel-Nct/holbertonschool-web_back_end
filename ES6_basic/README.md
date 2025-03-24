# ES6 Basics 🚀

  

Welcome to the **ES6 Basics** project! This repository contains exercises to help you master the fundamentals of ECMAScript 6 (ES2015). Through these tasks, you'll learn about modern JavaScript features and best practices. 💻✨

  

## Project Overview 📋

  

This project covers:

-  `const` vs `let` declarations 🆚

- Block scoping 🧱

- Arrow functions ➡️

- Default parameters ⚙️

- Rest and spread operators 🔄

- Template literals 📝

- Object property shorthand ✏️

- ES6 method properties 🛠️

- Iterators and loops 🔁

  

## Requirements ✅

  

- Ubuntu 20.04 LTS 🐧

- NodeJS 20.x.x and npm 9.x.x 📦

- ESLint for code quality check ✔️

- Jest for testing 🧪

  

## Setup 🛠️

  

1.  **Install NodeJS 20.x:**

```bash

curl -sL  https://deb.nodesource.com/setup_20.x  -o  nodesource_setup.sh

sudo bash  nodesource_setup.sh

sudo apt  install  nodejs  -y

```

  

3.  **Verify installation:**

```bash

node -v  # Should show v20.x.x

npm -v  # Should show 9.x.x

```

3.  **Install project dependencies:**

```bash

npm install  --save-dev  jest  babel-jest  @babel/core  @babel/preset-env  eslint

```

  

## Tasks List 📚

  

### Mandatory Tasks

  

1.  **[0-constants.js](https://0-constants.js)** - `const` vs `let` 🆚

🔹 Modify functions to use proper variable declarations

2.  **[1-block-scoped.js](https://1-block-scoped.js)** - Block scope 🧱

🔹 Fix variable hoisting issues

3.  **[2-arrow.js](https://2-arrow.js)** - Arrow functions ➡️

🔹 Convert standard function to arrow syntax

4.  **[3-default-parameter.js](https://3-default-parameter.js)** - Default parameters ⚙️

🔹 Condense function to one line using default values

5.  **[4-rest-parameter.js](https://4-rest-parameter.js)** - Rest parameters 🔄

🔹 Count arguments using rest syntax

6.  **[5-spread-operator.js](https://5-spread-operator.js)** - Spread operator 🔄

🔹 Concatenate arrays and string in one line

7.  **[6-string-interpolation.js](https://6-string-interpolation.js)** - Template literals 📝

🔹 Rewrite return statement using template literals

8.  **[7-getBudgetObject.js](https://7-getBudgetObject.js)** - Object shorthand ✏️

🔹 Simplify object property assignment

9.  **[8-getBudgetCurrentYear.js](https://8-getBudgetCurrentYear.js)** - Computed properties 🧮

🔹 Use ES6 computed property names

10.  **[9-getFullBudget.js](https://9-getFullBudget.js)** - Method properties 🛠️

🔹 Convert functions to ES6 method syntax

11.  **[10-loops.js](https://10-loops.js)** - For...of loops 🔁

🔹 Replace for-in with for-of loop

12.  **[11-createEmployeesObject.js](https://11-createEmployeesObject.js)** - Iterator 🏢

🔹 Create department employees object

13.  **[12-createReportObject.js](https://12-createReportObject.js)** - Report object 📊

🔹 Generate employee report with department count

  

## How to Run Tests 🧪

  

To execute the tests for any task, run:

```bash

npm run  dev <file-path>

# Example:

npm run  dev  0-main.js

```

  

## Learning Objectives 🎯

  

After completing this project, you'll understand:

  

- ES6 features and their benefits 🌟

- Differences between `const`, `let`, and `var` 🆚

- Modern JavaScript syntax and best practices 💎

- How to write cleaner, more efficient code ✨

  

Happy coding! 💻🚀
