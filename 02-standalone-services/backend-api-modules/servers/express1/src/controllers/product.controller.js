import { ProductModel } from '../models/product.model.js';

export const ProductController = {
  getAll: (req, res) => {
    const { category, search } = req.query;
    const products = ProductModel.findAll({ category, search });
    res.json(products);
  },

  getById: (req, res, next) => {
    const id = parseInt(req.params.id, 10);
    const product = ProductModel.findById(id);
    if (!product) {
      const err = new Error(`Product with ID ${id} not found`);
      err.status = 404;
      return next(err);
    }
    res.json(product);
  },

  create: (req, res, next) => {
    const { name, price, category, stock } = req.body;

    if (!name || typeof name !== 'string' || name.trim() === '') {
      const err = new Error("Product 'name' is required and must be a non-empty string");
      err.status = 400;
      return next(err);
    }
    if (price === undefined || (typeof price !== 'number' && isNaN(price)) || price < 0) {
      const err = new Error("Product 'price' is required and must be a non-negative number");
      err.status = 400;
      return next(err);
    }
    if (!category || typeof category !== 'string' || category.trim() === '') {
      const err = new Error("Product 'category' is required and must be a non-empty string");
      err.status = 400;
      return next(err);
    }
    if (stock === undefined || (typeof stock !== 'number' && isNaN(stock)) || stock < 0) {
      const err = new Error("Product 'stock' is required and must be a non-negative integer");
      err.status = 400;
      return next(err);
    }

    const newProduct = ProductModel.create({ name, price, category, stock });
    res.status(201).json(newProduct);
  },

  update: (req, res, next) => {
    const id = parseInt(req.params.id, 10);
    const { name, price, category, stock } = req.body;

    // Optional fields validation if provided
    if (name !== undefined && (typeof name !== 'string' || name.trim() === '')) {
      const err = new Error("Product 'name' must be a non-empty string");
      err.status = 400;
      return next(err);
    }
    if (price !== undefined && ((typeof price !== 'number' && isNaN(price)) || price < 0)) {
      const err = new Error("Product 'price' must be a non-negative number");
      err.status = 400;
      return next(err);
    }
    if (category !== undefined && (typeof category !== 'string' || category.trim() === '')) {
      const err = new Error("Product 'category' must be a non-empty string");
      err.status = 400;
      return next(err);
    }
    if (stock !== undefined && ((typeof stock !== 'number' && isNaN(stock)) || stock < 0)) {
      const err = new Error("Product 'stock' must be a non-negative integer");
      err.status = 400;
      return next(err);
    }

    const updatedProduct = ProductModel.update(id, { name, price, category, stock });
    if (!updatedProduct) {
      const err = new Error(`Product with ID ${id} not found`);
      err.status = 404;
      return next(err);
    }
    res.json(updatedProduct);
  },

  delete: (req, res, next) => {
    const id = parseInt(req.params.id, 10);
    const deletedProduct = ProductModel.delete(id);
    if (!deletedProduct) {
      const err = new Error(`Product with ID ${id} not found`);
      err.status = 404;
      return next(err);
    }
    res.json({
      message: `Product '${deletedProduct.name}' (ID: ${id}) deleted successfully`,
      deletedProduct
    });
  }
};
