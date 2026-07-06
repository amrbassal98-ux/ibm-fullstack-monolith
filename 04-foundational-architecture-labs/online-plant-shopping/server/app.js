import express from 'express'
import dotenv from 'dotenv';
import taskRoute from './routes/taskRoutes.js';
import authRoute from './routes/authRoutes.js';
import homeRoute from './routes/homeRoutes.js';
import cartRoute from './routes/cartRoutes.js';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.use('/', homeRoute);

app.use('/api/auth', authRoute);

app.use ('/api/cart', cartRoute);

app.use('/api/tasks', taskRoute);

app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});