# ES6 Promises 🚀

## Description 📖

This project focuses on understanding and using ES6 Promises in JavaScript. You will learn how to handle asynchronous operations efficiently using `then`, `catch`, and `async/await`. By the end of this project, you should be able to explain and implement Promises in real-world applications.

## Learning Objectives 🎯

By completing this project, you will be able to:

-   Understand what Promises are and why they are useful 🤔
    
-   Use `then`, `resolve`, and `catch` methods correctly ✅
    
-   Utilize all Promise object methods 📜
    
-   Implement error handling with `try/catch` ⚠️
    
-   Work with the `await` operator ⏳
    
-   Use `async` functions effectively 💡
    

## Requirements ⚙️

-   All files must run on **Ubuntu 20.04 LTS** with **Node.js 20.x.x** and **npm 9.x.x**
    
-   Use **vi, vim, emacs, or Visual Studio Code** as editors
    
-   End all files with a new line
    
-   A `README.md` file at the root of the project is **mandatory**
    
-   Use `.js` as the file extension
    
-   Code will be tested with **Jest** using `npm run test`
    
-   Code will be linted using **ESLint**
    
-   All functions must be exported
    

## Setup 🛠️

### Install Node.js 20.x.x

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y

```

Verify the installation:

```bash
nodejs -v  # Should return v20.x.x
npm -v     # Should return 9.x.x

```

### Install Jest, Babel, and ESLint 🧪

In your project directory, run:

```bash
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli
npm install --save-dev eslint

```

## Project Files 📂

### `package.json`

Defines project dependencies and scripts.

### `babel.config.js`

Configures Babel for transpiling JavaScript.

### `utils.js`

Provides helper functions like `uploadPhoto` and `createUser`.

### `.eslintrc.js`

Configures ESLint for code linting and style enforcement.

## Usage 🚀

To run tests:

```bash
npm run test

```

To check for linting errors:

```bash
npm run lint

```

## License 📜

This project follows an open-source license.

----------

Enjoy coding with ES6 Promises! 🎉