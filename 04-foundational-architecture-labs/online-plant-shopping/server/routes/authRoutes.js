import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';
import express from 'express';


const router = express.Router();

router.post('/login', async (req, res) => {
    const { email, password } = req.body;
    
    // Logic: In a real app, we'd find the user in a DB.
    // For now, let's use your hardcoded "amr@test.com"
    if (email === "amr@test.com") {
        const isMatch = await bcrypt.compare(password, hashedAdminPassword); // Security check
        
        if (isMatch) {
            const token = jwt.sign({ id: 'user123' }, process.env.JWT_SECRET, { expiresIn: '1h' });
            return res.json({ token });
        }
    }
    res.status(401).json({ message: "Invalid Credentials" });
});

export default router;