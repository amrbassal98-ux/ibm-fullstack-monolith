import React from "react";
import { useState, useEffect } from "react";
import { useSelector} from "react-redux";

const SuperCoin = () => {
    const [superCoins, setSuperCoins] = useState(0);
    const cartItems = useSelector(state => state.cart.cartItems);
    const totalAmount = cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
    useEffect(() => {
        if (100 <= totalAmount < 200) {
            setSuperCoins(10);
        } else if (200 <= totalAmount < 300) {
            setSuperCoins(20);
        } else if (totalAmount >= 300) {
            setSuperCoins(30);
        } else {
            setSuperCoins(0);
        }
    }, [totalAmount]);

    return (
        <div style={{textAlign: "center"}}>
            <h2>Super Coins</h2>
            <p>You will earn {superCoins} super coins with this purchase</p>
        </div>
    )
}

export default SuperCoin