# 📚 Pagination Project

## 📖 Description

Learn how to implement pagination techniques for datasets, including simple pagination, hypermedia pagination, and deletion-resilient pagination.

---

## 🎯 Learning Objectives

By the end of this project, you will be able to:

- 📄 Paginate a dataset using simple `page` and `page_size` parameters
- 🌐 Implement hypermedia pagination with metadata
- 🛡️ Design pagination that remains resilient to deletions

---

## 📚 Resources

Recommended reading and references:

- [REST API Design: Pagination](https://restfulapi.net/pagination/)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

---

## 🛠️ Requirements

- ✅ All code must run on **Ubuntu 20.04 LTS** with **Python 3.9**
- ✅ Files must end with a new line
- ✅ First line of all Python files: `#!/usr/bin/env python3`
- ✅ Follow **pycodestyle** (version 2.5.\*)
- ✅ Provide full **module** and **function documentation**
- ✅ Type annotations are mandatory
- ✅ A `README.md` at the root of the project is required

---

## 🗂️ Setup

Use the provided **Popular_Baby_Names.csv** dataset for all tasks.

---

## 📋 Tasks

### 0. Simple Helper Function

🔹 Create a function `index_range(page: int, page_size: int) -> Tuple[int, int]`  
🔹 Returns a tuple of start and end indexes for pagination.

> **Example:**
>
> ```
> index_range(1, 7) ➔ (0, 7)
> index_range(3, 15) ➔ (30, 45)
> ```

---

### 1. Simple Pagination

🔹 Create a `Server` class to paginate the dataset.  
🔹 Implement `get_page(page: int = 1, page_size: int = 10)`:

- Validate inputs with assertions
- Use `index_range` to select the correct slice
- Return an empty list if out of bounds

---

### 2. Hypermedia Pagination

🔹 Extend `Server` with a method `get_hyper(page: int = 1, page_size: int = 10) -> Dict`:

- `page_size`
- `page`
- `data`
- `next_page`
- `prev_page`
- `total_pages`

🔹 Reuse `get_page` internally!

---

### 3. Deletion-Resilient Hypermedia Pagination

🔹 Implement `get_hyper_index(index: int = None, page_size: int = 10) -> Dict`:

- Ensure pagination remains consistent even when dataset rows are deleted
- Return `index`, `next_index`, `page_size`, and `data`
- Use assertions to validate the index

---

## 🏛️ Repository Structure

```
holbertonschool-web_back_end/
└── pagination/
    ├── 0-simple_helper_function.py
    ├── 1-simple_pagination.py
    ├── 2-hypermedia_pagination.py
    ├── 3-hypermedia_del_pagination.py
    └── Popular_Baby_Names.csv
```

---

## 🤝 Contributing

Contributions are welcome!
