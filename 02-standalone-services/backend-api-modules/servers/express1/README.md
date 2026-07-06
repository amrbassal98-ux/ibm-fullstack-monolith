# StoreAPI - Modular Express.js Monolith

A structured, clean-architecture Express.js server containing decoupled layers (models, routes, controllers) and separate frontend HTML views for all CRUD operations, styled with Bootstrap 5.

## Project Structure
Organized following distributed monolith / layered monolithic best practices:

```text
/home/bassal/coding/servers/express1/
├── package.json               # Dependencies and scripts
├── README.md                  # Project documentation
├── test-api.sh                # Integration script to test API endpoints
├── src/                       # Backend Source
│   ├── index.js               # Application Entrypoint (listens to port)
│   ├── app.js                 # App configuration & middleware wiring
│   ├── controllers/           # HTTP Request Handlers
│   │   └── product.controller.js
│   ├── models/                # Business Entity & Memory Store
│   │   └── product.model.js
│   └── routes/                # Endpoint Router mappings
│       └── product.routes.js
└── public/                    # Frontend client pages (static assets)
    ├── style.css              # Custom styling / Dark theme theme config
    ├── index.html             # Landing Page / Catalog Grid & Filter controls
    ├── create.html            # CRUD: Add Product Form
    ├── edit.html              # CRUD: Edit Product Form
    ├── detail.html            # CRUD: Read Single Product / Trigger Delete
    └── 404.html               # Not Found fallback Page
```

## Setup & Running

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Start the server**:
   ```bash
   npm start
   ```
   Or run in development mode (with file watcher):
   ```bash
   npm run dev
   ```

3. **Interact in your browser**:
   Navigate to http://localhost:3000 to interact with the catalog dashboard.
   - **Create**: Click the **"+ Add Product"** button in the header.
   - **Read**: View products directly on the dashboard or click **"View"** to see individual detail stats.
   - **Update**: Click **"Edit"** from either the homepage or details page to modify a product.
   - **Delete**: Click **"Delete Product"** from the product details page to trigger a confirmation modal.

4. **Verify APIs (CLI)**:
   Keep the server running and execute the automated script:
   ```bash
   ./test-api.sh
   ```
