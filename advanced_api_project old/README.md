## 📌 View Configuration & Behavior (Task Documentation)

This project uses **Django REST Framework Generic Views** to manage CRUD operations for the `Book` model.

| View Class       | Endpoint          | Purpose                     | Access |
|------------------|------------------|-----------------------------|--------|
| BookListView     | `/books/`         | List all books              | Public |
| BookDetailView   | `/books/<pk>/`    | Retrieve one book           | Public |
| BookCreateView   | `/books/`         | Create a new book           | Authenticated |
| BookUpdateView   | `/books/<pk>/`    | Update an existing book     | Authenticated |
| BookDeleteView   | `/books/<pk>/`    | Delete a book               | Authenticated |

### Permission Strategy

- **Public Read Access** → List & Detail Views
- **Restricted Write Access** → Create, Update, Delete (only for logged-in users)

### Custom Behavior

- `perform_create()` is overridden to allow future customization (logging, user binding, etc.).
- Comments are added directly in the view classes to explain usage and intent.
