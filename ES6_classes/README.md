# ES6 Classes 🚀

## Description 📖

This project covers the fundamentals of ES6 classes in JavaScript. You will learn:

-   How to define and use classes.
    
-   How to add methods and static methods.
    
-   How to extend a class from another.
    
-   Metaprogramming and symbols.
    

## Learning Objectives 🎯

By the end of this project, you should be able to explain:

-   ✅ How to define a Class.
    
-   ✅ How to add methods to a Class.
    
-   ✅ Why and how to add static methods.
    
-   ✅ How to extend a Class.
    
-   ✅ Metaprogramming concepts using Symbols.
    

## Requirements 🛠️

-   Your code must run on **Ubuntu 20.04 LTS** with **Node.js 20.x.x** and **npm 9.x.x**.
    
-   Use one of the following editors: `vi`, `vim`, `emacs`, `Visual Studio Code`.
    
-   All files must end with a new line.
    
-   Your code must use the `.js` extension.
    
-   Testing will be done using `Jest` with `npm run test`.
    
-   Linting is done using `ESLint`.
    
-   Run `npm run full-test` to ensure all tests and linter checks pass.
    

## Setup 🏗️

### Install Node.js 20.x.x

```sh
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

Check installation:

```sh
nodejs -v  # Should return v20.x.x
npm -v     # Should return 9.x.x
```

### Install Dependencies 📦

Inside your project directory, run:

```sh
npm install --save-dev jest babel-jest @babel/core @babel/preset-env eslint
```

## Configuration ⚙️

### `package.json`

```json
{
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "dev": "npx babel-node",
    "test": "jest",
    "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
  },
  "devDependencies": {
    "@babel/core": "^7.6.0",
    "@babel/preset-env": "^7.6.0",
    "@babel/node": "^7.8.0",
    "eslint": "^6.8.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "jest": "^24.9.0"
  }
}
```

### `babel.config.js`

```js
module.exports = {
  presets: [
    ['@babel/preset-env', {
      targets: { node: 'current' },
    }],
  ],
};
```

### `.eslintrc.js`

```js
module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
    'plugin:jest/all',
  ],
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'max-classes-per-file': 'off',
    'no-underscore-dangle': 'off',
    'no-console': 'off',
  },
};
```

## Tasks ✅

### 0. **ClassRoom** 🏫

Create a class `ClassRoom` with:

-   A constructor that accepts `maxStudentsSize` (Number).
    
-   Store it in `_maxStudentsSize`.
    

### 1. **Initialize Rooms** 📚

Create a function `initializeRooms` that returns an array of 3 `ClassRoom` objects with sizes `19`, `20`, and `34`.

### 2. **Holberton Course** 📖

Create a class `HolbertonCourse` with:

-   Attributes: `name` (String), `length` (Number), `students` (array of Strings).
    
-   Implement getters and setters.
    

### 3. **Currency Class** 💰

Create a class `Currency` with:

-   Attributes: `code` (String), `name` (String).
    
-   Method `displayFullCurrency()` returning `name (code)`.
    

### 4. **Pricing** 💲

Create a class `Pricing` with:

-   Attributes: `amount` (Number), `currency` (Currency).
    
-   Method `displayFullPrice()` returning `amount currency_name (currency_code)`.
    
-   Static method `convertPrice(amount, conversionRate)` returning the converted amount.
    

### 5. **Building Class (Abstract)** 🏢

Create a class `Building` with:

-   Attribute: `sqft` (Number).
    
-   Abstract method `evacuationWarningMessage()` that must be implemented by any subclass.
    

### 6. **SkyHighBuilding** 🌆

Extend `Building` into `SkyHighBuilding` with:

-   Additional attribute: `floors` (Number).
    
-   Override `evacuationWarningMessage()` to return `Evacuate slowly the X floors`.
    

### 7. **Airport** ✈️

Create a class `Airport` with:

-   Attributes: `name` (String), `code` (String).
    
-   Default string representation should return the airport `code`.
    

### 8. **Holberton Class (Primitive Casting)** 🔢

Create `HolbertonClass` where:

-   Casting to `Number` returns `size`.
    
-   Casting to `String` returns `location`.
    

### 9. **Hoisting Fix** 🔄

Refactor code to fix class hoisting issues with `HolbertonClass` and `StudentHolberton`.

### 10. **Car Cloning** 🚗

Create a class `Car` with:

-   Attributes: `brand`, `motor`, `color`.
    
-   Method `cloneCar()` that returns a new `Car` object.
    

## Running Tests 🧪

Run the following command to test your implementation:

```sh
npm run test
```

To check linting issues:

```sh
npm run lint
```

## Author ✍️

-   **Johann Kerbrat**, Engineering Manager at Uber Works
    

## Repository 📂

-   **GitHub Repo:** [holbertonschool-web_back_end](https://github.com/holbertonschool-web_back_end)
    
-   **Directory:** `ES6_classes`
    

----------

🚀 Happy Coding! 🎉