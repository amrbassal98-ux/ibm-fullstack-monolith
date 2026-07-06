import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {syncRemoveItem, syncUpdateQuantity} from './CartSlice';
import './CartItem.css';

const CartItem = ({ onContinueShopping }) => {
  const cart = useSelector(state => state.cart.items);
  const dispatch = useDispatch();

  // Calculate total amount for all products in the cart
  const calculateTotalAmount = () => {
    let total = 0;
    cart.forEach ((item) => {
      const quantity = item.quantity;
      const cost = parseFloat(item.cost.substring(1));
        total = total + (quantity * cost);
      })
    return total;
  };

  const handleContinueShopping = (e) => {
    onContinueShopping(e);
   
  };



  const handleIncrement = (item) => {
    dispatch(syncUpdateQuantity({name: item.name, quantity: item.quantity + 1}));
  };

  const handleDecrement = (item) => {
    if (item.quantity > 1) {
      dispatch(syncUpdateQuantity({name: item.name, quantity: item.quantity - 1}));
    } else {
      dispatch(syncRemoveItem(item.name));
    };
   
  };

  const handleRemove = (item) => {
    dispatch(syncRemoveItem(item.name));
  };

  // Calculate total cost based on quantity for an item
  const calculateTotalCost = (item) => {
    const itemCost = parseFloat(item.cost.substring(1));
    const itemTotal = itemCost * item.quantity;
    return itemTotal;
  };

  const handleCheckoutShopping = (e) => {
    alert("Functionality to be added for future reference");
  };

  return (
    <div className="cart-container">
      <h2 className='total-cart-amount'>Total Cart Amount: ${calculateTotalAmount()}</h2>
      {cart.map(item => (
          <div className="cart-item" key={item.name}>
            <img className="cart-item-image" src={item.image} alt={item.name} />
            <div className="cart-item-details">
              <div className="cart-item-name">{item.name}</div>
              <div className="cart-item-cost">{item.cost}</div>
              <div className="cart-item-quantity">
                <button className="cart-item-button cart-item-button-dec" onClick={() => handleDecrement(item)}>-</button>
                <span className="cart-item-quantity-value">{item.quantity}</span>
                <button className="cart-item-button cart-item-button-inc" onClick={() => handleIncrement(item)}>+</button>
              </div>
              <div className="cart-item-total">Total: ${calculateTotalCost(item)}</div>
              <button className="cart-item-delete" onClick={() => handleRemove(item)}>Delete</button>
            </div>
          </div>
      ))}
      <div className="continue-shopping-btn">
        <button className="get-started-button" onClick={(e) => handleContinueShopping(e)}>Continue Shopping</button>
        <br />
        <button className="get-started-button" onClick={(e) => handleCheckoutShopping(e)}>Checkout</button>
      </div>
    </div>
  );
};

export default CartItem;


