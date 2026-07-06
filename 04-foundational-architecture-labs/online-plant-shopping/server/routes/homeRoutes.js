import express from 'express';
import path from 'path';
import {fileURLToPath} from 'url';

const router = express.Router();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

router.get('/', (req, res) => {
    const filePath = path.join(__dirname, 'home.html');
    res.sendFile(filePath);
});

router.get('/status', (req, res) => {
    res.json({
        status: "Online",
        architecture: process.arch,
        directory: __dirname
    });
});

export default router