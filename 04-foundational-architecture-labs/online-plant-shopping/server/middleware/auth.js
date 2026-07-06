// server/middleware/auth.js
import jwt from 'jsonwebtoken';

export const protect = (req, res, next) => {
    const token = req.headers.authorization?.split(' ')[1];
    
    if (!token) return res.status(401).json({ message: "No Token, Access Denied" });

    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        req.user = decoded; // Attach user identity to the request
        next(); // Proceed to the route logic
    } catch (err) {
        res.status(401).json({ message: "Token Invalid" });
    }
};

export default authMiddleware;