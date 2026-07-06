import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const fetchCart = createAsyncThunk(
  'cart/fetchCart',
  async () => {
    const response = await fetch('/api/cart');
    return response.json();
  }
);

export const syncAddToCart = createAsyncThunk(
  'cart/syncAddToCart',
  async (product) => {
    const response = await fetch('/api/cart/add', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      }, 
      body: JSON.stringify(product)
    });
    return response.json();
  }
);

export const syncUpdateQuantity = createAsyncThunk(
    'cart/syncUpdateQuantity',
    async ({ name, quantity }) => {
        const response = await fetch('/api/cart/update', {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, quantity })
        });
        return response.json();
    }
);


export const syncRemoveItem = createAsyncThunk(
    'cart/syncRemoveItem',
    async (name) => {
        const response = await fetch(`/api/cart/remove/${name}`, {
            method: 'DELETE'
        });
        return response.json();
    }
);

export const CartSlice = createSlice({
  name: 'cart',
  initialState: {
    items: [],
    status: 'idle',
  },
  reducers: {
    addItem: (state, action) => {
      const product = action.payload;
      const existingProduct = state.items.find((item) => product.name === item.name);
      if (!existingProduct) {
        product.quantity = 1;
        state.items.push(product);
      } else {
        existingProduct.quantity++;
      };
    
    },
    removeItem: (state, action) => {
      const product = action.payload;
      state.items = state.items.filter((item) => product !== item.name);
    },
    updateQuantity: (state, action) => {
      const product = action.payload;
      const productToUpdate = state.items.find((item) => item.name === product.name);
      if (productToUpdate) {
      productToUpdate.quantity = product.quantity;
      }
    },
  },
  extraReducers: (builder) => {
    builder
    .addCase(syncAddToCart.fulfilled, (state, action) => {
      state.items = action.payload.cart;
    })
    .addCase(syncRemoveItem.fulfilled, (state, action) => {
      state.items = action.payload.cart;
    })
    .addCase(syncUpdateQuantity.fulfilled, (state, action) => {
      state.items = action.payload.cart;
    })
    .addCase(fetchCart.fulfilled, (state, action) => {
    state.items = action.payload;
    });
  }
});

export const { addItem, removeItem, updateQuantity } = CartSlice.actions;

export default CartSlice.reducer;
