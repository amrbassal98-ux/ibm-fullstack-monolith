
import React, { useState, useEffect } from 'react';
import {useDispatch} from 'react-redux';
import {fetchCart} from './CartSlice';
import ProductList from './ProductList';
import './App.css';
import AboutUs from './AboutUs';

function App() {

  const dispatch = useDispatch();
  
  useEffect(() => {
    dispatch(fetchCart());
  }, [dispatch]);

  const [showProductList, setShowProductList] = useState(false);

  const handleGetStartedClick = () => {
    setShowProductList(true);
  };

  const handleHomeClick = () => {
    setShowProductList(false);
  };

 return (
  <div className="app-container">
    {/* 1. Show ONLY the Landing Page if showProductList is false */}
    {!showProductList ? (
      <div className="landing-page">
        <div className="background-image"></div>
        <div className="content">
          <div className="landing_content">
            <h1>Welcome To Paradise Nursery</h1>
            <div className="divider"></div>
            <p>Where Green Meets Serenity</p>
            <button className="get-started-button" onClick={handleGetStartedClick}>
              Get Started
            </button>
          </div>
          <div className="aboutus_container">
            <AboutUs />
          </div>
        </div>
      </div>
    ) : (
      /* 2. Show ONLY the Product List if showProductList is true */
      <div className="product-list-container">
        <ProductList onHomeClick={handleHomeClick} />
      </div>
    )}
  </div>
  );
}

export default App;
