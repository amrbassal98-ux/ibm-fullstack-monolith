import express from 'express';
const router = express.Router();

let serverCart = [];

router.get('/', (req, res) => {
    res.status(200).json(serverCart);
});

router.get('/clearcart', (req, res) => {
    serverCart = [];
    res.status(200).json({message: "Cart Cleared", cart: serverCart});
});

router.post('/add', (req, res) => {
    const product = req.body;
    const existing = serverCart.find(item => item.name === product.name);
    if (!existing) {
        serverCart.push({...product, quantity: 1});
    } else {
        existing.quantity++;
    }
    res.status(201).json({message: "Sync Successful", cart: serverCart});
});

router.patch('/update', (req, res) => {
    const { name, quantity } = req.body;
    const item = serverCart.find(i => i.name === name);
    
    if (item) {
        item.quantity = quantity;
        res.status(200).json({ message: "Quantity updated", cart: serverCart });
    } else {
        res.status(404).json({ message: "Item not found" });
    }
});


router.delete('/remove/:name', (req, res) => {
    const { name } = req.params;
    serverCart = serverCart.filter(item => item.name !== name);
    res.status(200).json({ message: "Item removed", cart: serverCart });
});

export default router;
