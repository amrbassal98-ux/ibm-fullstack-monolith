let products = [
  { id: 1, name: "Wireless Mechanical Keyboard", price: 89.99, category: "Electronics", stock: 15 },
  { id: 2, name: "Ergonomic Office Chair", price: 249.99, category: "Furniture", stock: 8 },
  { id: 3, name: "Smart Water Bottle", price: 39.99, category: "Accessories", stock: 25 },
  { id: 4, name: "Noise Cancelling Headphones", price: 199.99, category: "Electronics", stock: 12 },
  { id: 5, name: "Minimalist Leather Wallet", price: 45.00, category: "Accessories", stock: 50 }
];

let nextId = 6;

export const ProductModel = {
  findAll: ({ category, search }) => {
    let filtered = [...products];
    if (category) {
      filtered = filtered.filter(p => p.category.toLowerCase() === category.toLowerCase());
    }
    if (search) {
      filtered = filtered.filter(p => p.name.toLowerCase().includes(search.toLowerCase()));
    }
    return filtered;
  },

  findById: (id) => {
    return products.find(p => p.id === id);
  },

  create: ({ name, price, category, stock }) => {
    const newProduct = {
      id: nextId++,
      name: name.trim(),
      price: parseFloat(price),
      category: category.trim(),
      stock: parseInt(stock, 10)
    };
    products.push(newProduct);
    return newProduct;
  },

  update: (id, updates) => {
    const index = products.findIndex(p => p.id === id);
    if (index === -1) return null;

    const { name, price, category, stock } = updates;
    if (name !== undefined) products[index].name = name.trim();
    if (price !== undefined) products[index].price = parseFloat(price);
    if (category !== undefined) products[index].category = category.trim();
    if (stock !== undefined) products[index].stock = parseInt(stock, 10);

    return products[index];
  },

  delete: (id) => {
    const index = products.findIndex(p => p.id === id);
    if (index === -1) return null;
    return products.splice(index, 1)[0];
  }
};
