# ES6 Data Manipulation 🚀

## Description 📖
This project focuses on data manipulation in JavaScript using ES6 features. You will work with arrays, typed arrays, sets, maps, and weak maps to perform various data transformations.

## Learning Objectives 🎯
By completing this project, you will be able to:
- Use `map`, `filter`, and `reduce` on arrays.
- Work with typed arrays.
- Utilize Set, Map, and WeakMap data structures.

## Requirements ✅
- All code will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Node.js 20.x.x** and **npm 9.x.x**.
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`.
- All files must end with a new line.
- A `README.md` file at the root of the project is mandatory.
- Code must use the `.js` extension.
- Tests will be executed using **Jest** (`npm run test`).
- Linting must pass using **ESLint**.
- To check all tests and linting, run `npm run full-test`.
- All functions must be exported.

---

## Setup 🔧
### Install Node.js 20.x.x:
```sh
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```
Verify installation:
```sh
nodejs -v   # Expected: v20.15.1
npm -v      # Expected: 10.7.0
```

### Install Dependencies:
```sh
npm install --save-dev jest babel-jest @babel/core @babel/preset-env eslint
```

Don't forget to run:
```sh
npm install
```
whenever `package.json` is modified.

---

## Tasks 📌

### 0️⃣ Basic List of Objects
- Implement `getListStudents()`: Returns an array of student objects with `id`, `firstName`, and `location`.

### 1️⃣ More Mapping
- Implement `getListStudentIds()`: Returns an array of student IDs using the `map` function.

### 2️⃣ Filter
- Implement `getStudentsByLocation()`: Returns students from a specified city using `filter`.

### 3️⃣ Reduce
- Implement `getStudentIdsSum()`: Returns the sum of student IDs using `reduce`.

### 4️⃣ Combine
- Implement `updateStudentGradeByCity()`: Updates student grades by city using `filter` and `map`.

### 5️⃣ Typed Arrays
- Implement `createInt8TypedArray()`: Returns an `ArrayBuffer` with an `Int8` value at a specified position.

### 6️⃣ Set Data Structure
- Implement `setFromArray()`: Converts an array into a `Set`.

### 7️⃣ More Set Data Structure
- Implement `hasValuesFromArray()`: Checks if all elements in an array exist in a `Set`.

### 8️⃣ Clean Set
- Implement `cleanSet()`: Returns a string of `Set` values that start with a specified string.

### 9️⃣ Map Data Structure
- Implement `groceriesList()`: Returns a `Map` of grocery items with their quantities.

### 🔟 More Map Data Structure
- Implement `updateUniqueItems()`: Updates all grocery items with an initial quantity of `1` to `100`.

---

## Repository 🏗️
- **GitHub Repository**: `holbertonschool-web_back_end`
- **Directory**: `ES6_data_manipulation`

Happy coding! 🎉

