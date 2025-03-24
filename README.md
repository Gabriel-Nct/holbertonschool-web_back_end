# Holberton School Web Back-End 🚀

Welcome to the **Web Back-End** repository! This project focuses on server-side development, APIs, databases, and modern JavaScript (ES6) fundamentals.  

---

## What is Back-End Development? 🤖

Back-end development refers to the **server-side** of web applications. It handles:
- **Business logic** 🧠  
- **Database interactions** 🗃️  
- **API creation** 🌐  
- **Authentication** 🔒  
- **Performance optimization** ⚡  

Key technologies:  
- **Languages**: JavaScript (Node.js), Python, Ruby, PHP  
- **Frameworks**: Express, Django, Flask, Ruby on Rails  
- **Databases**: MySQL, MongoDB, PostgreSQL  
- **APIs**: REST, GraphQL  

---

## ES6 (ECMAScript 2015) Overview ✨

ES6 introduced major improvements to JavaScript, making it more powerful and readable. Key features:

### 1. **Variables** 🏷️  
- `let` and `const` (block-scoped) vs `var` (function-scoped).  
- Prefer `const` for constants, `let` for variables.  

### 2. **Arrow Functions** ➡️  
```javascript
const sum = (a, b) => a + b; // Shorter syntax!
```

### 3. **Template Literals** 📝

```javascript
console.log(`Hello, ${name}!`); // Embedded expressions
```

### 4. **Destructuring** 🧩
```javascript
const { firstName, age } = user; // Extract object properties
```

### 5. **Spread/Rest Operators** 🔄
```javascript
const combined = [...arr1, ...arr2]; // Spread
function logArgs(...args) { /* Rest */ }
```

### 6. **Classes & Modules** 🏗️
```javascript
class User { constructor(name) { this.name = name; } }
export default User; // Modules
```

### 7. **Promises & Async/Await** ⏳
```javascript
async function fetchData() {
  const data = await axios.get('/api');
}
```

----------

## Project Structure 📂

This repository includes:

-   **ES6 Basics**: Exercises on modern JavaScript (`const/let`, arrow functions, etc.).
    
-   **API Development**: Building RESTful services.
    
-   **Database Integration**: SQL/NoSQL interactions.
    
-   **Authentication**: JWT, OAuth.

## How to Use This Repo 🛠️

1.  **Clone the repository**:
    
   ```bash
   git clone https://github.com/your-username/holbertonschool-web_back_end.git
  ```
2.  **Install dependencies**:
    
   ``` bash
   pm install
   ``` 
3.  **Run exercises**:
    
   ``` bash
    npm test  # For Jest tests
   ```

## Resources 📚

-   [ES6 Features](https://es6-features.org)
    
-   [Node.js Docs](https://nodejs.org/en/docs/)
    
-   [Express Framework](https://expressjs.com)
    

----------

**Happy coding!** 💻🔥  
_"The back-end is where the magic happens."_ 🎩✨
