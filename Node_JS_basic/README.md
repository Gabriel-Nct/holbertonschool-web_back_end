# NodeJS Basics

This project covers the foundational aspects of Node.js development, focusing on key concepts and practical implementations for building server-side applications.

## Learning Objectives

By the end of this project, you should be able to:

- Run JavaScript code using Node.js
- Use Node.js modules effectively
- Read files with specific Node.js modules
- Access command line arguments and environment variables using `process`
- Create simple HTTP servers using Node.js core modules
- Create HTTP servers with Express.js
- Implement advanced routing with Express.js
- Use ES6 features with Node.js via Babel
- Accelerate development with Nodemon

## Requirements

- Allowed editors: vi, vim, emacs, Visual Studio Code
- All files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 20.x.x)
- All files should end with a new line
- All code uses the `.js` extension
- Code will be tested using Jest and the command `npm run test`
- Code will be verified against lint using ESLint
- All functions/classes must be exported using: `module.exports = myFunction;`

## Installation

```bash
# Clone the repository
git clone [your-repo-link]
cd Node_JS_basic

# Install dependencies
npm install
```

## Project Structure

The project is organized into several tasks that progressively build your Node.js skills:

### Task 0: Basic JavaScript with Node.js
- File: `0-console.js`
- Create a function that prints a message to STDOUT

### Task 1: Using Process stdin
- File: `1-stdin.js`
- Create an interactive program that manages input/output through command line

### Task 2: Reading Files Synchronously
- File: `2-read_file.js`
- Implement a function to read and process CSV data synchronously

### Task 3: Reading Files Asynchronously
- File: `3-read_file_async.js`
- Implement an asynchronous function to read and process CSV data

### Task 4: Simple HTTP Server
- File: `4-http.js`
- Create a basic HTTP server using Node.js core modules

### Task 5: Advanced HTTP Server
- File: `5-http.js`
- Create a more complex HTTP server with different routes

### Task 6: Express HTTP Server
- File: `6-http_express.js`
- Create a simple HTTP server using Express.js

### Task 7: Advanced Express HTTP Server
- File: `7-http_express.js`
- Create a more complex HTTP server using Express.js with different routes

### Task 8: Organized Express Server
- Directory: `full_server/`
- Implement a complete server with proper structure using Express.js, routes, and controllers

## Testing

```bash
# Run tests
npm run test

# Run tests with coverage
npm run full-test
```

## Resources

- [Node.js Getting Started](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)
- [Process API Documentation](https://nodejs.org/api/process.html)
- [Child Process](https://nodejs.org/api/child_process.html)
- [Express Getting Started](https://expressjs.com/en/starter/installing.html)
- [Mocha Documentation](https://mochajs.org/)
- [Nodemon Documentation](https://github.com/remy/nodemon#nodemon)
