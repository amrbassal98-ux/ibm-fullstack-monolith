import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';
import productRoutes from './routes/product.routes.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();

// Body Parser Middleware
app.use(express.json());

// Serve Static Frontend Pages from public directory
app.use(express.static(path.join(__dirname, '../public')));

// API Routes
app.use('/api/products', productRoutes);

// Main endpoint to greet customers
app.get('/api/greet', (req, res) => {
  res.json({
    message: "Welcome, Valued Customer!",
    description: "Explore our premium inventory and developer-friendly REST endpoints below."
  });
});

// Fallback to serve 404.html for unknown HTML paths
app.use((req, res, next) => {
  if (req.accepts('html')) {
    res.status(404).sendFile(path.join(__dirname, '../public/404.html'));
  } else {
    const err = new Error("Endpoint not found");
    err.status = 404;
    next(err);
  }
});

// Global Error Handler
app.use((err, req, res, next) => {
  const status = err.status || 500;
  res.status(status).json({
    error: {
      message: err.message || "Internal Server Error",
      status
    }
  });
});

export default app;
